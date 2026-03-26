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

MAX_STACK_SIZE = 10000

# TODO: move to a different file
class Regs:
    def __init__(self, stack):
        self._stack = stack
        self.pc = 0
        self.ret_val = None
        self.bp = 0

    @property
    def sp(self):
        return self._stack.sp

    @sp.setter
    def sp(self, val):
        self._stack.sp = val

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

        self.stack = Stack(MAX_STACK_SIZE)
        self.regs = Regs(self.stack)
        self.sym_tab = irHandler.funs

    def interpret(self):
        print("Program counter : ", self.regs.pc)
        stmt, tgt = self.ir[self.regs.pc]
        print("CURR PC : ", self.regs.pc, stmt, stmt.__class__.__name__, tgt)
        # print("STACK : ", self.stack.stack)
        print("RBP : ", self.regs.bp)
        print("RET_VAL : ", self.regs.ret_val)

        self.sanityCheck(self.ir[self.regs.pc])

        if isinstance(stmt, ChironAST.AssignmentCommand):
            ntgt = self.handleAssignment(stmt, tgt)
        elif isinstance(stmt, ChironAST.ConditionCommand):
            ntgt = self.handleCondition(stmt, tgt, self.regs.pc)
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
        elif isinstance(stmt, ChironAST.PrintCommand):
            ntgt = self.handlePrintCommand(stmt, tgt)
        elif isinstance(stmt, ChironAST.AssertCommand):
            ntgt = self.handleAssertCommand(stmt, tgt)
        elif isinstance(stmt, ChironAST.Label):
            ntgt = self.regs.pc + 1
        elif isinstance(stmt, ChironAST.ReturnCommand):
            ntgt = self.handleReturnCommand(stmt, tgt)
        elif isinstance(stmt, ChironAST.ParamCommand):
            ntgt = self.handleParamCommand(stmt, tgt)
        elif isinstance(stmt, ChironAST.CallN):
            ntgt = self.handleCallN(stmt, tgt, self.regs.pc)
        elif isinstance(stmt, ChironAST.StackAlloc):
            ntgt = self.handleStackAlloc(stmt, tgt)
        elif isinstance(stmt, ChironAST.StackDealloc):
            ntgt = self.handleStackDealloc(stmt, tgt)
        else:
            raise NotImplementedError("Unknown instruction: %s, %s."%(type(stmt), stmt))

        # TODO: handle statement
        self.regs.pc = ntgt
        # print("NEXT PC : ", self.regs.pc)

        if self.regs.pc >= len(self.ir):
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
            if self.regs.bp < 2:
                if hasattr(self.prg, varname):
                    return getattr(self.prg, varname)
                raise NameError("Undefined variable: %s" % varname)
            
            ret_pc = self.stack.stack[self.regs.bp - 2]

            if ret_pc <= 0 or ret_pc > len(self.ir):
                if hasattr(self.prg, varname):
                    return getattr(self.prg, varname)
                raise NameError("Undefined variable: %s (invalid return address)" % varname)

            instr = self.ir[ret_pc - 1][0]
            proc_name = getattr(instr, "proc_name", None)
            offsets = self.sym_tab[proc_name].get("offsets", {})
            if varname not in offsets:
                # variable not a local of the procedure -> check global frame
                if hasattr(self.prg, varname):
                    return getattr(self.prg, varname)
                raise NameError("Undefined variable: %s" % varname)

            offset = offsets[varname]
            idx = self.regs.bp + offset
            # ensure index is within the current allocated stack region
            if idx < 0 or idx >= len(self.stack.stack):
                raise IndexError("STACK ACCESS VIOLATION: RBP=%s, offset=%s, idx=%s, sp=%s" % (self.regs.bp, offset, idx, self.stack.sp))

            return self.stack.stack[idx]
        
        # return value
        if isinstance(node, ChironAST.RetVal):
            return self.regs.ret_val

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

        if(self.regs.bp == 0):
            setattr(self.prg, lhs_name, final_val)
            # print(f"  Assigned variable {lhs_name} = {final_val} in global frame {self.prg.__dict__}")
        else:
            ret_pc = self.stack.stack[self.regs.bp - 2]
            proc_name = self.ir[ret_pc - 1][0].proc_name
            # print(self.sym_tab[proc_name])                
            offset = self.sym_tab[proc_name]["offsets"][lhs_name]
            self.stack.stack[self.regs.bp + offset] = final_val

        # print(f"  Assigned variable {lhs_name} = {final_val} in frame with RBP {self.regs.bp}, offset {offset}")
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
        return tgt

    def handleStackAlloc(self, stmt, tgt):
        self.regs.sp += stmt.size
        return tgt
    
    def handleStackDealloc(self, stmt, tgt):
        self.regs.sp -= stmt.size
        return tgt
   
    def handlePrintCommand(self, stmt, tgt):
        value = self.get_operand_value(stmt.expr)
        print("[#######] [%s] : %s" % (stmt.expr, value))
        return tgt

    def handleCallN(self, stmt, tgt, pc):
        proc_name = stmt.proc_name        
        entry = self.sym_tab[stmt.proc_name]["entry"]
        caller_addr = self.regs.pc + 1
        self.stack.push(caller_addr) # push pc
        self.stack.push(self.regs.bp) # push bp
        self.regs.bp = self.stack.sp # update bp to new frame
        self.regs.sp += len(self.sym_tab[proc_name]["offsets"])
        entry += 1
        return entry

    def handleAssertCommand(self, stmt, tgt):
        cond_val = self.get_operand_value(stmt.cond)
        # print(f"  Assert condition {stmt.cond} evaluated to: {cond_val}")
        if not bool(cond_val) and cond_val is not None:
            raise AssertionError("Assertion failed: %s" % (stmt.cond,))
        return tgt

    def handleReturnCommand(self, stmt, tgt):
        self.stack.sp = self.regs.bp # reset stack pointer to current frame base
        old_rbp = self.stack.pop() # restore caller's base pointer
        caller_addr = self.stack.pop() # get caller's return address
        self.regs.ret_val = self.get_operand_value(stmt.expr)
        self.regs.bp = old_rbp
        # print("new rbp : ", self.regs.bp, "new caller_addr : ", caller_addr, "ret_val : ", self.regs.ret_val, "stack sp : ", self.stack.sp)
        return caller_addr

    def handleParamCommand(self, stmt, tgt):
        # push the value of the parameter onto the argument stack
        param = stmt.param
        param_val = self.get_operand_value(param)
        self.stack.push(param_val)
        # print("  Pushed param value onto arg stack: ", param_val)
        return tgt
