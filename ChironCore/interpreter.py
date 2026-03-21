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

    def handleAssertCommand(self, stmt, tgt):
        raise NotImplementedError('Asserts are not handled!')

    def sanityCheck(self, irInstr):
        stmt, tgt = irInstr
        # if not a condition command, rel. jump can't be anything but 1
        # if not isinstance(stmt, ChironAST.ConditionCommand) and not isinstance(stmt, ChironAST.ProcedureDeclaration):
        #     if tgt != 1:
        #         raise ValueError("Improper relative jump for non-conditional instruction", str(stmt), tgt)
    
    def interpret(self):
        pass

    def initProgramContext(self, params):
        pass

class ProgramContext:
    pass

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
        self.ret_val = None

        # initialize call stack with global program context
        self.call_stack = [self.prg]

    def interpret(self):
        print("Program counter : ", self.pc)
        stmt, tgt = self.ir[self.pc]
        print("CURR PC : ", self.pc, stmt, stmt.__class__.__name__, tgt)

        self.sanityCheck(self.ir[self.pc])

        if isinstance(stmt, ChironAST.AssignmentCommand):
            ntgt = self.handleAssignment(stmt, tgt)
        elif isinstance(stmt, ChironAST.ConditionCommand):
            ntgt = self.handleCondition(stmt, tgt, self.pc)
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
        elif isinstance(stmt, ChironAST.AssertCommand):
            ntgt = self.handleAssertCommand(stmt, tgt)
        elif isinstance(stmt, ChironAST.Label):
            ntgt = self.pc + 1
        elif isinstance(stmt, ChironAST.ReturnCommand):
            ntgt = self.handleReturnCommand(stmt, tgt)
        else:
            raise NotImplementedError("Unknown instruction: %s, %s."%(type(stmt), stmt))

        # TODO: handle statement
        self.pc = ntgt
        # print("NEXT PC : ", self.pc)

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
        # print("  Evaluating RHS expression for assignment to variable %s: %s" % (lhs, stmt.rexpr))
        val = self._eval_in_frame(stmt.rexpr, self.prg)
        # print("FINALLY RETURNED!!!!", val)
        # print("Setting variable %s to value %s in current frame" % (lhs, val))
        setattr(self.prg, lhs, val)
        return tgt

    def handleCondition(self, stmt, tgt, pc):
        print("  Branch Instruction")
        self.cond_eval = self._eval_in_frame(stmt.cond, self.prg)
        return pc + 1 if self.cond_eval else tgt

    def handleMove(self, stmt, tgt):
        print("  MoveCommand")
        exec("self.trtl.%s(%s)" % (stmt.direction,addContext(stmt.expr)))
        return tgt

    def handleNoOpCommand(self, stmt, tgt):
        print("  No-Op Command")
        return tgt

    def handlePen(self, stmt, tgt):
        print("  PenCommand")
        exec("self.trtl.%s()"%(stmt.status))
        return tgt

    def handleGotoCommand(self, stmt, tgt):
        print(" GotoCommand")
        xcor = addContext(stmt.xcor)
        ycor = addContext(stmt.ycor)
        exec("self.trtl.goto(%s, %s)" % (xcor, ycor))
        return tgt

    def handleProcedureDeclaration(self, stmt, tgt):
        print(" Procedure Declaration")
        # disallow redeclaration of existing procedures/variables in global frame
        if hasattr(self.prg, stmt.name):
            raise NameError("Name conflict: %s is already defined in global scope" % stmt.name)
        setattr(self.prg, stmt.name, self.pc)
        print("  Stored procedure %s at IR index %s in frame %s" % (stmt.name, self.pc, self.prg.__dict__))
        return tgt + len(stmt.body)

    # recursive expr evaluating instead of exec'ing raw strings
    def _eval_in_frame(self, expr, frame):
        print("CURR FRAME : ", frame.__dict__)
        print("  Evaluating expression: ", expr, type(expr))
        def eval_expr(e):
            if isinstance(e, ChironAST.Num):
                return e.val

            if isinstance(e, ChironAST.Var):
                name = e.varname.replace(":", "")
                if hasattr(frame, name):
                    return getattr(frame, name)
                # fall back to global frame if available
                if self.call_stack and hasattr(self.call_stack[0], name):
                    return getattr(self.call_stack[0], name)
                raise NameError("Undefined variable: %s" % e.varname)

            if isinstance(e, ChironAST.ProcedureCallExpr):
                arg_vals = [self._eval_in_frame(a, frame) for a in e.args]
                return self._call_procedure_and_get_return(e.name, arg_vals)

            if isinstance(e, ChironAST.UMinus):
                return -eval_expr(e.expr)

            if isinstance(e, ChironAST.Sum):
                return eval_expr(e.lexpr) + eval_expr(e.rexpr)
            if isinstance(e, ChironAST.Diff):
                return eval_expr(e.lexpr) - eval_expr(e.rexpr)
            if isinstance(e, ChironAST.Mult):
                return eval_expr(e.lexpr) * eval_expr(e.rexpr)
            if isinstance(e, ChironAST.Div):
                return eval_expr(e.lexpr) // eval_expr(e.rexpr) # integer division

            if isinstance(e, ChironAST.AND):
                return bool(eval_expr(e.lexpr)) and bool(eval_expr(e.rexpr))
            if isinstance(e, ChironAST.OR):
                return bool(eval_expr(e.lexpr)) or bool(eval_expr(e.rexpr))
            if isinstance(e, ChironAST.NOT):
                return not bool(eval_expr(e.expr))

            if isinstance(e, ChironAST.LT):
                return eval_expr(e.lexpr) < eval_expr(e.rexpr)
            if isinstance(e, ChironAST.GT):
                return eval_expr(e.lexpr) > eval_expr(e.rexpr)
            if isinstance(e, ChironAST.LTE):
                return eval_expr(e.lexpr) <= eval_expr(e.rexpr)
            if isinstance(e, ChironAST.GTE):
                return eval_expr(e.lexpr) >= eval_expr(e.rexpr)
            if isinstance(e, ChironAST.EQ):
                return eval_expr(e.lexpr) == eval_expr(e.rexpr)
            if isinstance(e, ChironAST.NEQ):
                return eval_expr(e.lexpr) != eval_expr(e.rexpr)

            if isinstance(e, ChironAST.BoolFalse):
                return False

            raise RuntimeError("Expression evaluation failed: Unsupported expression type %s" % type(e))

        return eval_expr(expr)

    def _execute_ast_instr(self, instr, pc):
        # instr may be either an AST node, or a (node, offset) tuple coming
        # from flattened procedure bodies. Normalize to (stmt, tgt).
        stmt, tgt = instr
        # print("CURR PC : ", pc, stmt, stmt.__class__.__name__, tgt)

        if isinstance(stmt, ChironAST.AssignmentCommand):
            return self.handleAssignment(stmt, tgt)
        if isinstance(stmt, ChironAST.ConditionCommand):
            return self.handleCondition(stmt, tgt, self.pc)
        if isinstance(stmt, ChironAST.MoveCommand):
            return self.handleMove(stmt, tgt)
        if isinstance(stmt, ChironAST.PenCommand):
            return self.handlePen(stmt, tgt)
        if isinstance(stmt, ChironAST.GotoCommand):
            return self.handleGotoCommand(stmt, tgt)
        if isinstance(stmt, ChironAST.NoOpCommand):
            return self.handleNoOpCommand(stmt, tgt)
        if isinstance(stmt, ChironAST.PauseCommand):
            return self.handlePauseCommand(stmt, tgt)
        if isinstance(stmt, ChironAST.ProcedureCall):
            return self.handleProcedureCall(stmt, tgt, pc)
        if isinstance(stmt, ChironAST.ReturnCommand):
            if stmt.expr is None:
                self.ret_val = None
            else:
                self.ret_val = self._eval_in_frame(stmt.expr, self.prg)
            return self.prg.caller_addr
        if isinstance(stmt, ChironAST.PrintCommand):
            return self.handlePrintCommand(stmt, tgt)
        if isinstance(stmt, ChironAST.AssertCommand):
            return self.handleAssertCommand(stmt, tgt)
        raise NotImplementedError(
            "Procedure body contains unsupported instruction: %s" % type(stmt)
        )

    def handlePrintCommand(self, stmt, tgt):
        # print("  PrintCommand")
        value = self._eval_in_frame(stmt.expr, self.prg)
        print("[%s] : %s" % (stmt.expr, value))
        return tgt

    # helper: call a procedure and return its value
    def _call_procedure_and_get_return(self, proc_name, arg_vals):
        print(" Procedure Call (expr): %s" % proc_name)

        # lookup proc in global frame
        global_frame = self.call_stack[0]
        if not hasattr(global_frame, proc_name):
            raise NameError("Undefined procedure: %s" % proc_name)
        proc = getattr(global_frame, proc_name)
        # print("  Found procedure declaration:", proc)
        proc, pc = self.ir[proc]
        caller_addr = self.pc + 1
        # print("  should return to ", caller_addr)

        self.pc = pc
        # create new frame and bind parameters
        new_frame = ProgramContext()
        for i, pname in enumerate(proc.params):
            bare = pname.replace(":", "")
            val = arg_vals[i] if i < len(arg_vals) else None
            setattr(new_frame, bare, val)

        self.call_stack.append(new_frame)

        prev_prg = self.prg
        self.prg = new_frame
        self.prg.caller_addr = caller_addr
        start_pc = self.pc
        end_pc = self.pc + len(proc.body) if proc.body else self.pc + 1
        try:
            while self.pc >= start_pc and self.pc < end_pc:
                # print("CURR PC : ", self.pc)
                self.interpret()

        # has encountered a return
        finally:
            self.call_stack.pop()
            self.prg = prev_prg
        return self.ret_val

    def handleProcedureCall(self, stmt, tgt):
        print(" Procedure Call: %s" % stmt.name)
        print("TGT : ", tgt)
        # For statement-level calls, evaluate args then call helper and ignore return value
        caller_frame = self.call_stack[-1]
        arg_vals = [self._eval_in_frame(a, caller_frame) for a in stmt.args]
        self._call_procedure_and_get_return(stmt.name, arg_vals)
        return tgt

    def handleAssertCommand(self, stmt, tgt):
        # evaluate the assert condition in current frame; if false, raise AssertionError
        cond_val = self._eval_in_frame(stmt.cond, self.call_stack[-1])
        if not bool(cond_val):
            raise AssertionError("Assertion failed: %s" % (stmt.cond,))
        return tgt

    def handleReturnCommand(self, stmt, tgt):
        if stmt.expr is None:
            self.ret_val = None
        else:
            self.ret_val = self._eval_in_frame(stmt.expr, self.prg)
            
        return self.prg.caller_addr