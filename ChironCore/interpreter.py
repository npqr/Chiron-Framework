from ChironAST import ChironAST
from ChironHooks import Chironhooks
import turtle

Release = "Chiron v5.3"


def addContext(s):
    return str(s).strip().replace(":", "self.prg.")


class Interpreter:
    # Turtle program should not contain variable with names "ir", "pc", "t_screen"
    ir = None
    pc = None
    t_screen = None
    trtl = None

    def __init__(self, irHandler, params):
        self.ir = irHandler.ir
        self.cfg = irHandler.cfg
        self.pc = 0
        self.t_screen = turtle.getscreen()
        self.trtl = turtle.Turtle()
        self.trtl.shape("turtle")
        self.trtl.color("blue", "yellow")
        self.trtl.fillcolor("green")
        self.trtl.begin_fill()
        self.trtl.pensize(4)
        self.trtl.speed(1) # TODO: Make it user friendly

        if params is not None:
            self.args = params
        else:
            self.args = None

        turtle.title(Release)
        turtle.bgcolor("white")
        turtle.hideturtle()

    def handleAssignment(self, stmt,tgt):
        raise NotImplementedError('Assignments are not handled!')

    def handleCondition(self, stmt, tgt):
        raise NotImplementedError('Conditions are not handled!')

    def handleMove(self, stmt, tgt):
        raise NotImplementedError('Moves are not handled!')

    def handlePen(self, stmt, tgt):
        raise NotImplementedError('Pens are not handled!')

    def handleGotoCommand(self, stmt, tgt):
        raise NotImplementedError('Gotos are not handled!')

    def handleNoOpCommand(self, stmt, tgt):
        raise NotImplementedError('No-Ops are not handled!')

    def handlePauseCommand(self, stmt, tgt):
        raise NotImplementedError('No-Ops are not handled!')

    def sanityCheck(self, irInstr):
        stmt, tgt = irInstr
        # if not a condition command, rel. jump can't be anything but 1
        if not isinstance(stmt, ChironAST.ConditionCommand):
            if tgt != 1:
                raise ValueError("Improper relative jump for non-conditional instruction", str(stmt), tgt)
    
    def interpret(self):
        pass

    def initProgramContext(self, params):
        pass

class ProgramContext:
    pass

class ProcedureReturn(Exception):
    def __init__(self, value):
        self.value = value

# TODO: move to a different file
class ConcreteInterpreter(Interpreter):
    # Ref: https://realpython.com/beginners-guide-python-turtle
    cond_eval = None # used as a temporary variable within the embedded program interpreter
    prg = None

    def __init__(self, irHandler, params):
        super().__init__(irHandler, params)
        self.prg = ProgramContext()
        # Hooks Object:
        if self.args is not None and self.args.hooks:
            self.chironhook = Chironhooks.ConcreteChironHooks()
        self.pc = 0

        # initialize call stack with global program context
        self.call_stack = [self.prg]

    def interpret(self):
        print("Program counter : ", self.pc)
        stmt, tgt = self.ir[self.pc]
        print(stmt, stmt.__class__.__name__, tgt)

        self.sanityCheck(self.ir[self.pc])

        if isinstance(stmt, ChironAST.AssignmentCommand):
            ntgt = self.handleAssignment(stmt, tgt)
        elif isinstance(stmt, ChironAST.ConditionCommand):
            ntgt = self.handleCondition(stmt, tgt)
        elif isinstance(stmt, ChironAST.MoveCommand):
            ntgt = self.handleMove(stmt, tgt)
        elif isinstance(stmt, ChironAST.PenCommand):
            ntgt = self.handlePen(stmt, tgt)
        elif isinstance(stmt, ChironAST.GotoCommand):
            ntgt = self.handleGotoCommand(stmt, tgt)
        elif isinstance(stmt, ChironAST.NoOpCommand):
            ntgt = self.handleNoOpCommand(stmt, tgt)
        elif isinstance(stmt, ChironAST.ProcedureDeclaration):
            ntgt = self.handleProcedureDeclaration(stmt, tgt)
        elif isinstance(stmt, ChironAST.ProcedureCall):
            ntgt = self.handleProcedureCall(stmt, tgt)
        elif isinstance(stmt, ChironAST.PrintCommand):
            ntgt = self.handlePrintCommand(stmt, tgt)
        else:
            raise NotImplementedError("Unknown instruction: %s, %s."%(type(stmt), stmt))

        # TODO: handle statement
        self.pc += ntgt

        if self.pc >= len(self.ir):
            # This is the ending of the interpreter.
            self.trtl.write("End, Press ESC", font=("Arial", 15, "bold"))
            if self.args is not None and self.args.hooks:
                self.chironhook.ChironEndHook(self)
            return True
        else:
            return False
    
    def initProgramContext(self, params):
        # This is the starting of the interpreter at setup stage.
        if self.args is not None and self.args.hooks:
            self.chironhook.ChironStartHook(self)
        self.trtl.write("Start", font=("Arial", 15, "bold"))
        for key,val in params.items():
            var = key.replace(":","")
            exec("setattr(self.prg,\"%s\",%s)" % (var, val))
    
    # modified Assignment handler to evaluate RHS expr
    def handleAssignment(self, stmt, tgt):
        print("  Assignment Statement")
        lhs = str(stmt.lvar).replace(":", "")
        # evaluate RHS expression in current frame
        val = self._eval_in_frame(stmt.rexpr, self.prg)
        setattr(self.prg, lhs, val)
        return 1

    def handleCondition(self, stmt, tgt):
        print("  Branch Instruction")
        condstr = addContext(stmt)
        exec("self.cond_eval = %s" % (condstr))
        return 1 if self.cond_eval else tgt

    def handleMove(self, stmt, tgt):
        print("  MoveCommand")
        exec("self.trtl.%s(%s)" % (stmt.direction,addContext(stmt.expr)))
        return 1

    def handleNoOpCommand(self, stmt, tgt):
        print("  No-Op Command")
        return 1

    def handlePen(self, stmt, tgt):
        print("  PenCommand")
        exec("self.trtl.%s()"%(stmt.status))
        return 1

    def handleGotoCommand(self, stmt, tgt):
        print(" GotoCommand")
        xcor = addContext(stmt.xcor)
        ycor = addContext(stmt.ycor)
        exec("self.trtl.goto(%s, %s)" % (xcor, ycor))
        return 1

    def handleProcedureDeclaration(self, stmt, tgt):
        print(" Procedure Declaration")
        setattr(self.prg, stmt.name, stmt)
        return 1

    def _eval_in_frame(self, expr, frame):
        if isinstance(expr, ChironAST.ProcedureCallExpr):
            arg_vals = []
            for a in expr.args:
                arg_vals.append(self._eval_in_frame(a, frame))
            return self._call_procedure_and_get_return(expr.name, arg_vals)

        expr_str = str(expr).strip().replace(":", "frame.")
        local = {"frame": frame}
        try:
            exec("__val = %s" % expr_str, {}, local)
            return local["__val"]
        except Exception as e:
            raise RuntimeError("Expression evaluation failed: %s (%s)" % (expr_str, e))

    def _execute_ast_instr(self, instr):
        if isinstance(instr, ChironAST.AssignmentCommand):
            return self.handleAssignment(instr, 1)
        if isinstance(instr, ChironAST.ConditionCommand):
            return self.handleCondition(instr, 1)
        if isinstance(instr, ChironAST.MoveCommand):
            return self.handleMove(instr, 1)
        if isinstance(instr, ChironAST.PenCommand):
            return self.handlePen(instr, 1)
        if isinstance(instr, ChironAST.GotoCommand):
            return self.handleGotoCommand(instr, 1)
        if isinstance(instr, ChironAST.NoOpCommand):
            return self.handleNoOpCommand(instr, 1)
        if isinstance(instr, ChironAST.PauseCommand):
            return self.handlePauseCommand(instr, 1)
        if isinstance(instr, ChironAST.ProcedureCall): 
            return self.handleProcedureCall(instr, 1)       # do we need to add handler for procedureCallExpr?
        if isinstance(instr, ChironAST.ReturnCommand):
            if instr.expr is None:
                val = None
            else:
                val = self._eval_in_frame(instr.expr, self.prg)
            raise ProcedureReturn(val)
        if isinstance(instr, ChironAST.PrintCommand):
            return self.handlePrintCommand(instr, 1)
        raise NotImplementedError(
            "Procedure body contains unsupported instruction: %s" % type(instr)
        )

    def handlePrintCommand(self, stmt, tgt):
        # print("  PrintCommand")
        value = self._eval_in_frame(stmt.expr, self.prg)
        print("[%s] : %s" % (stmt.expr, value))
        return 1

    # helper: call a procedure and return its value
    def _call_procedure_and_get_return(self, proc_name, arg_vals):
        print(" Procedure Call (expr): %s" % proc_name)

        # lookup proc in global frame
        global_frame = self.call_stack[0]
        if not hasattr(global_frame, proc_name):
            raise NameError("Undefined procedure: %s" % proc_name)
        proc = getattr(global_frame, proc_name)

        # create new frame and bind parameters
        new_frame = ProgramContext()
        for i, pname in enumerate(proc.params):
            bare = pname.replace(":", "")
            val = arg_vals[i] if i < len(arg_vals) else None
            setattr(new_frame, bare, val)

        # push new frame and execute body, catching ProcedureReturn
        self.call_stack.append(new_frame)
        prev_prg = self.prg
        self.prg = new_frame
        ret_val = None
        try:
            for instr in proc.body:
                try:
                    self._execute_ast_instr(instr)
                except ProcedureReturn as r:
                    ret_val = r.value
                    # stop executing body on return
                    break
        finally:
            self.call_stack.pop()
            self.prg = prev_prg
        return ret_val

    def handleProcedureCall(self, stmt, tgt):
        print(" Procedure Call: %s" % stmt.name)
        # For statement-level calls, evaluate args then call helper and ignore return value
        caller_frame = self.call_stack[-1]
        arg_vals = [self._eval_in_frame(a, caller_frame) for a in stmt.args]
        _ = self._call_procedure_and_get_return(stmt.name, arg_vals)
        return 1
