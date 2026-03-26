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
class Stack:
    def __init__(self, sz):
        self.sp = 0
        self.stack = [None] * sz
    def push(self, val):
        self.stack[self.sp] = val
        self.sp += 1
        print(self.stack)

        if self.sp > len(self.stack):
            raise OverflowError("Stack overflow")
    def pop(self):
        if self.sp <= 0:
            raise OverflowError("Stack underflow")
        self.sp -= 1
        return self.stack[self.sp]

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

        MAX_STACK_SIZE = 10000

        # initialize call stack with global program context
        # self.call_stack = [self.prg]
        # self.arg_stack = []

        self.stack = Stack(MAX_STACK_SIZE)
        self.tregs = [None] * 20
        self.funs = irHandler.funs
        self.rbp = 0
        print(self.funs)

    def interpret(self):
        print("Program counter : ", self.pc)
        stmt, tgt = self.ir[self.pc]
        print("CURR PC : ", self.pc, stmt, stmt.__class__.__name__, tgt)
        # print("STACK : ", self.stack.stack)
        print("RBP : ", self.rbp)
        print("RET_VAL : ", self.ret_val)

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
        # elif isinstance(stmt, ChironAST.ProcedureCall): # wont reach here now since now we have CallN
        #     ntgt = self.handleProcedureCall(stmt, tgt)
        elif isinstance(stmt, ChironAST.PrintCommand):
            ntgt = self.handlePrintCommand(stmt, tgt)
        elif isinstance(stmt, ChironAST.AssertCommand):
            ntgt = self.handleAssertCommand(stmt, tgt)
        elif isinstance(stmt, ChironAST.Label):
            ntgt = self.pc + 1
        elif isinstance(stmt, ChironAST.ReturnCommand):
            ntgt = self.handleReturnCommand(stmt, tgt)
        elif isinstance(stmt, ChironAST.ParamCommand):
            ntgt = self.handleParamCommand(stmt, tgt)
        elif isinstance(stmt, ChironAST.CallN):
            ntgt = self.handleCallN(stmt, tgt, self.pc)
        elif isinstance(stmt, ChironAST.StackAlloc):
            ntgt = self.handleStackAlloc(stmt, tgt)
        elif isinstance(stmt, ChironAST.StackDealloc):
            ntgt = self.handleStackDealloc(stmt, tgt)
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

    # TODO: handle turtle graphics states too
    def get_operand_value(self, node):
        print("  Evaluating operand/expression: ", node, type(node))
        # evaluate literals
        if isinstance(node, ChironAST.Num):
            return node.val
        if isinstance(node, ChironAST.BoolTrue):
            return True
        if isinstance(node, ChironAST.BoolFalse):
            return False

        # variables (global frame or stack frame)
        if isinstance(node, ChironAST.Var):
            varname = node.varname.replace(":", "")
            if self.rbp < 2:
                if hasattr(self.prg, varname):
                    return getattr(self.prg, varname)
                raise NameError("Undefined variable: %s" % varname)
            
            ret_pc = self.stack.stack[self.rbp - 2]

            if ret_pc <= 0 or ret_pc > len(self.ir):
                if hasattr(self.prg, varname):
                    return getattr(self.prg, varname)
                raise NameError("Undefined variable: %s (invalid return address)" % varname)

            instr = self.ir[ret_pc - 1][0]
            proc_name = getattr(instr, "proc_name", None)
            offsets = self.funs[proc_name].get("offsets", {})
            if varname not in offsets:
                # variable not a local of the procedure -> check global frame
                if hasattr(self.prg, varname):
                    return getattr(self.prg, varname)
                raise NameError("Undefined variable: %s" % varname)

            offset = offsets[varname]
            idx = self.rbp + offset
            # ensure index is within the current allocated stack region
            if idx < 0 or idx >= len(self.stack.stack):
                raise IndexError("STACK ACCESS VIOLATION: RBP=%s, offset=%s, idx=%s, sp=%s" % (self.rbp, offset, idx, self.stack.sp))

            return self.stack.stack[idx]
        
        # return value
        if isinstance(node, ChironAST.RetVal):
            return self.ret_val

        # pen status
        if isinstance(node, ChironAST.PenStatus):
            return self.trtl.isdown()

        # unary ops
        if isinstance(node, ChironAST.UMinus):
            return -self.get_operand_value(node.expr)
        if isinstance(node, ChironAST.NOT):
            return not bool(self.get_operand_value(node.expr))

        # binary arithmetic / comparison / logical ops
        if isinstance(node, (ChironAST.Sum, ChironAST.Diff, ChironAST.Mult, ChironAST.Div,
                             ChironAST.LT, ChironAST.GT, ChironAST.LTE, ChironAST.GTE,
                             ChironAST.EQ, ChironAST.NEQ, ChironAST.AND, ChironAST.OR,
                             ChironAST.BinArithOp, ChironAST.BinCondOp)):
            left = self.get_operand_value(node.lexpr)
            right = self.get_operand_value(node.rexpr)

            print(f"  Evaluating binary operation: {node.__class__.__name__} with left={left} and right={right}")

            if isinstance(node, ChironAST.Sum):   return left + right
            if isinstance(node, ChironAST.Diff):  return left - right
            if isinstance(node, ChironAST.Mult):  return left * right
            if isinstance(node, ChironAST.Div):   return left // right
            if isinstance(node, ChironAST.LT):    return left < right
            if isinstance(node, ChironAST.GT):    return left > right
            if isinstance(node, ChironAST.LTE):   return left <= right
            if isinstance(node, ChironAST.GTE):   return left >= right
            if isinstance(node, ChironAST.EQ):    return left == right
            if isinstance(node, ChironAST.NEQ):   return left != right
            if isinstance(node, ChironAST.AND):   return bool(left) and bool(right)
            if isinstance(node, ChironAST.OR):    return bool(left) or bool(right)
            
            raise RuntimeError("Unsupported binary operator type: %s" % type(node))

        # won't reach here now since now we have CallN

        # # procedure call as expression (evaluate args, delegate to helper if available)
        # if isinstance(node, ChironAST.ProcedureCallExpr):
        #     arg_vals = [self.get_operand_value(a) for a in node.args]
        #     if hasattr(self, "_call_procedure_and_get_return"):
        #         return self._call_procedure_and_get_return(node.name, arg_vals)
        #     raise NotImplementedError("Procedure call expressions not supported in this interpreter state")
        
        if not node:
            return None

        raise RuntimeError("Unsupported operand/expression type: %s" % type(node))
            
    def handleAssignment(self, stmt, tgt):
        """
        Processes x = <expr>. In 3AC, <expr> is guaranteed to be 
        a single operation or a leaf value.
        """
        lhs_name = stmt.lvar.varname.replace(":", "")
        rhs = stmt.rexpr
        final_val = None
        offset = None

        print("RHS of assignment is: ", rhs, type(rhs))
        final_val = self.get_operand_value(rhs)

        if(self.rbp == 0):
            setattr(self.prg, lhs_name, final_val)
            print(f"  Assigned variable {lhs_name} = {final_val} in global frame {self.prg.__dict__}")
        else:
            # if lhs_name.startswith("__treg"):
            #     reg_idx = int(lhs_name[6:])
            #     self.tregs[reg_idx] = final_val
            # else:
            # print("RCCBP : ", self.rbp)
            ret_pc = self.stack.stack[self.rbp - 2]
            proc_name = self.ir[ret_pc - 1][0].proc_name
            print(lhs_name)
            print(self.funs[proc_name])                
            offset = self.funs[proc_name]["offsets"][lhs_name]
            self.stack.stack[self.rbp + offset] = final_val

        print(f"  Assigned variable {lhs_name} = {final_val} in frame with RBP {self.rbp}, offset {offset}")
        return tgt

    def handleCondition(self, stmt, tgt, pc):
        print("  Branch Instruction")
        self.cond_eval = self.get_operand_value(stmt.cond)
        return pc + 1 if self.cond_eval else tgt

    def handleMove(self, stmt, tgt):
        print("  MoveCommand")
        val = self.get_operand_value(stmt.expr)
        exec("self.trtl.%s(%s)" % (stmt.direction, val))
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
        xcor = self.get_operand_value(stmt.xcor)
        ycor = self.get_operand_value(stmt.ycor)
        self.trtl.goto(xcor, ycor)    
        return tgt

    def handleProcedureDeclaration(self, stmt, tgt):
        # print(" Procedure Declaration")
        # disallow redeclaration of existing procedures/variables in global frame
        # if hasattr(self.prg, stmt.name):
        #     raise NameError("Name conflict: %s is already defined in global scope" % stmt.name)
        # setattr(self.prg, stmt.name, self.pc + 1)
        # print("  Stored procedure %s at IR index %s in frame %s" % (stmt.name, self.pc, self.prg.__dict__))
        return tgt

    def handleStackAlloc(self, stmt, tgt):
        self.stack.sp += stmt.size
        return tgt
    
    def handleStackDealloc(self, stmt, tgt):
        self.stack.sp -= stmt.size
        return tgt

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
        # value = self._eval_in_frame(stmt.expr, self.prg)
        value = self.get_operand_value(stmt.expr)
        print("[#######] [%s] : %s" % (stmt.expr, value))
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
        proc, pc = self.ir[proc - 1]
        caller_addr = self.pc + 1
        # print("  should return to ", caller_addr)

        self.pc = pc + 1
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
        # start_pc = self.pc
        # end_pc = self.pc + len(proc.body) if proc.body else self.pc + 1
        # try:
        #     while self.pc >= start_pc and self.pc < end_pc:
        #         # print("CURR PC : ", self.pc)
        #         self.interpret()

        # has encountered a return
        # finally:
        #     self.call_stack.pop()
        #     self.prg = prev_prg
        # return self.ret_val
        return None

    def handleProcedureCall(self, stmt, tgt):
        print(" Procedure Call: %s" % stmt.name)
        print("TGT : ", tgt)
        # For statement-level calls, evaluate args then call helper and ignore return value
        caller_frame = self.call_stack[-1]
        arg_vals = [self._eval_in_frame(a, caller_frame) for a in stmt.args]
        self._call_procedure_and_get_return(stmt.name, arg_vals)
        return tgt

    def handleCallN(self, stmt, tgt, pc):
        proc_name = stmt.proc_name
        arg_count = stmt.arg_count
        
        entry = self.funs[stmt.proc_name]["entry"]
        # print("  Found procedure declaration:", entry)

        proc, pc = self.ir[entry - 1]
        caller_addr = self.pc + 1

        self.stack.push(caller_addr) # push pc
        self.stack.push(self.rbp) # push bp
        self.rbp = self.stack.sp # update bp to new frame
        self.stack.sp += len(self.funs[proc_name]["offsets"])
        entry += 1
        # print("  should return to ", caller_addr)
        # print("jump to procedure body at pc ", entry)
        return entry

    def handleAssertCommand(self, stmt, tgt):
        # evaluate the assert condition in current frame; if false, raise AssertionError
        # cond_val = self._eval_in_frame(stmt.cond, self.call_stack[-1])
        print(type(stmt.cond))
        cond_val = self.get_operand_value(stmt.cond)
        print(f"  Assert condition {stmt.cond} evaluated to: {cond_val}")
        if not bool(cond_val) and cond_val is not None:
            raise AssertionError("Assertion failed: %s" % (stmt.cond,))
        return tgt

    def handleReturnCommand(self, stmt, tgt):
        self.stack.sp = self.rbp # reset stack pointer to current frame base
        old_rbp = self.stack.pop() # restore caller's base pointer
        caller_addr = self.stack.pop() # get caller's return address
        self.ret_val = self.get_operand_value(stmt.expr)
        self.rbp = old_rbp
        print("new rbp : ", self.rbp, "new caller_addr : ", caller_addr, "ret_val : ", self.ret_val, "stack sp : ", self.stack.sp)
        return caller_addr

    def handleParamCommand(self, stmt, tgt):
        # push the value of the parameter onto the argument stack
        param = stmt.param
        param_val = self.get_operand_value(param)
        self.stack.push(param_val)
        print("  Pushed param value onto arg stack: ", param_val)
        return tgt
