#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Abstract syntax tree for ChironLang

class AST(object):
    pass


# --Instruction Classes-----------------------------------------------

class Instruction(AST):
    pass


class AssignmentCommand(Instruction):
    def __init__(self, leftvar, rexpr):
        self.lvar = leftvar
        self.rexpr = rexpr

    def __str__(self):
        return self.lvar.__str__() + " = " + self.rexpr.__str__()


class ConditionCommand(Instruction):
    def __init__(self, condition):
        self.cond = condition

    def __str__(self):
        return "jump if false => " + self.cond.__str__()

# Not Implemented Yet.
class AssertCommand(Instruction):
    def __init__(self, condition):
        self.cond = condition

    def __str__(self):
        return "assert " + self.cond.__str__()

class MoveCommand(Instruction):
    def __init__(self, motion, expr):
        self.direction = motion
        self.expr = expr

    def __str__(self):
        return self.direction + " " + self.expr.__str__()


class PenCommand(Instruction):
    def __init__(self, penstat):
        self.status = penstat

    def __str__(self):
        return self.status

class GotoCommand(Instruction):
    def __init__(self, x, y):
        self.xcor = x
        self.ycor = y

    def __str__(self):
        return "goto " + str(self.xcor) + " " + str(self.ycor)

class NoOpCommand(Instruction):
    def __init__(self):
        pass

    def __str__(self):
        return "NOP"

class PauseCommand(Instruction):
    def __init__(self):
        pass

    def __str__(self):
        return "pause"

class PrintCommand(Instruction):
    def __init__(self, expr):
        self.expr = expr

    def __str__(self):
        return f"print {self.expr}"

class ReturnCommand(Instruction):
    def __init__(self, expr=None):
        self.expr = expr

    def __str__(self):
        if self.expr is None:
            return "return"
        return "return " + str(self.expr)

class Expression(AST):
    pass


# --Arithmetic Expressions--------------------------------------------

class ArithExpr(Expression):
    pass


class BinArithOp(ArithExpr):
    def __init__(self, expr1, expr2, opsymbol):
        self.lexpr = expr1
        self.rexpr = expr2
        self.symbol = opsymbol

    def __str__(self):
        return "(" + self.lexpr.__str__() + " " + self.symbol + " " + self.rexpr.__str__() + ")"


class UnaryArithOp(ArithExpr):
    def __init__(self, expr1, opsymbol):
        self.expr = expr1
        self.symbol = opsymbol

    def __str__(self):
        return self.symbol + self.expr.__str__()


class UMinus(UnaryArithOp):
    def __init__(self, lexpr):
        super().__init__(lexpr, "-")


class Sum(BinArithOp):
    def __init__(self, lexpr, rexpr):
        super().__init__(lexpr, rexpr, "+")


class Diff(BinArithOp):
    def __init__(self, lexpr, rexpr):
        super().__init__(lexpr, rexpr, "-")


class Mult(BinArithOp):
    def __init__(self, lexpr, rexpr):
        super().__init__(lexpr, rexpr, "*")

class Div(BinArithOp):
    def __init__(self, lexpr, rexpr):
        super().__init__(lexpr, rexpr, "/")


# --Boolean Expressions-----------------------------------------------

class BoolExpr(Expression):
    pass


class BinCondOp(BoolExpr):
    def __init__(self, expr1, expr2, opsymbol):
        self.lexpr = expr1
        self.rexpr = expr2
        self.symbol = opsymbol

    def __str__(self):
        return "(" + self.lexpr.__str__() + ' ' + self.symbol + ' ' + self.rexpr.__str__() + ")"


class AND(BinCondOp):
    def __init__(self, expr1, expr2):
        super().__init__(expr1, expr2, "and")

class OR(BinCondOp):
    def __init__(self, expr1, expr2):
        super().__init__(expr1, expr2, "or")


class LT(BinCondOp):
    def __init__(self, expr1, expr2):
        super().__init__(expr1, expr2, "<")


class GT(BinCondOp):
    def __init__(self, expr1, expr2):
        super().__init__(expr1, expr2, ">")


class LTE(BinCondOp):
    def __init__(self, expr1, expr2):
        super().__init__(expr1, expr2, "<=")


class GTE(BinCondOp):
    def __init__(self, expr1, expr2):
        super().__init__(expr1, expr2, ">=")


class EQ(BinCondOp):
    def __init__(self, expr1, expr2):
        super().__init__(expr1, expr2, "==")


class NEQ(BinCondOp):
    def __init__(self, expr1, expr2):
        super().__init__(expr1, expr2, "!=")


class NOT(BoolExpr):
    def __init__(self, uexpr):
        self.expr = uexpr
        self.symbol = "not"

    def __str__(self):
        return self.symbol + self.expr.__str__()


class PenStatus(BoolExpr):
    def __init__(self):
        pass

    def __str__(self):
        return "pendown?"


class BoolTrue(BoolExpr):
    def __init__(self):
        pass

    def __str__(self):
        return "True"


class BoolFalse(BoolExpr):
    def __init__(self):
        pass

    def __str__(self):
        return "False"


class Value(Expression):
    pass


class Num(Value):
    def __init__(self, v):
        self.val = int(v)

    def __str__(self):
        return str(self.val)


class Var(Value):
    def __init__(self, vname):
        self.varname = vname

    def __str__(self):
        return self.varname
    

# Procedure / call instruction nodes
class ProcedureDeclaration(Instruction):
    def __init__(self, name, params, body):
        # params: list of VAR token strings (e.g. [':x', ':y'])
        # body: list of AST Instruction nodes (e.g. [AssignmentCommand(...), GotoCommand(...), ...])
        self.name = name
        self.params = params if params is not None else []
        self.body = body if body is not None else []

    def __str__(self):
        params_s = ", ".join(self.params)
        header = f"to {self.name}({params_s})"

        return header
        # if not self.body:
        #     body_s = "    pass"
        # else:
        #     lines = []
        #     for idx, item in enumerate(self.body):
        #         if isinstance(item, tuple) and len(item) == 2:
        #             stmt, tgt = item
        #             lines.append("\t[SL" + str(idx) + "] " + str(stmt) + " [[" + str(tgt) + "]]")
        #         else:
        #             lines.append("\t[SL" + str(idx) + "] " + str(item))
        #     body_s = "\n".join(lines)
        # return header + "\n" + body_s + "\n\tend"


class ProcedureCall(Instruction):
    def __init__(self, name, args):
        # args: list of Expression AST nodes
        self.name = name
        self.args = args if args is not None else []

    def __str__(self):
        args_s = ", ".join([str(a) for a in self.args])
        return "call @" + self.name + "(" + args_s + ")"

class ProcedureCallExpr(Expression):
    def __init__(self, name, args):
        self.name = name
        self.args = args if args is not None else []

    def __str__(self):
        args_s = ", ".join([str(a) for a in self.args])
        return "call @" + self.name + "(" + args_s + ")"

class Label(Instruction):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "label " + self.name
    
class ParamCommand(Instruction):
    def __init__(self, param):
        self.param = param

    def __str__(self):
        return "param " + str(self.param)
    
class CallN(Instruction):
    def __init__(self, proc_name, arg_count):
        self.proc_name = proc_name
        self.arg_count = arg_count

    def __str__(self):
        return f"call @{self.proc_name}, {self.arg_count}"
    
class RetVal(Expression):
    def __init__(self):
        pass

    def __str__(self):
        return "ret_val"
    
class StackAlloc(Instruction):
    def __init__(self, size):
        self.size = size

    def __str__(self):
        return f"stack_alloc {self.size}"
class StackDealloc(Instruction):
    def __init__(self, size):
        self.size = size

    def __str__(self):
        return f"stack_dealloc {self.size}"
    
# class ReadFromArgStack(Instruction):
#     def __init__(self, idx):
#         self.idx = idx

#     def __str__(self):
#         return f"read_arg_stack {self.idx}"
    