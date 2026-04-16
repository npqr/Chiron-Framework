#!/usr/bin/python3
# -*- coding: utf-8 -*-
# ChironLang Abstract Syntax Tree Builder

import os
import sys
sys.path.insert(0, os.path.join("..", "turtparse"))

from turtparse.tlangParser import tlangParser
from turtparse.tlangVisitor import tlangVisitor

from ChironAST import ChironAST


class astGenPass(tlangVisitor):

    def __init__(self):
        self.repeatInstrCount = 0 # keeps count for no of 'repeat' instructions

    def visitStart(self, ctx:tlangParser.StartContext):
        stmtList = self.visit(ctx.instruction_list())
        return stmtList

    def visitInstruction_list(self, ctx:tlangParser.Instruction_listContext):
        instrList = []
        for instr in ctx.instruction():
            instrList.extend(self.visit(instr))

        return instrList

    def visitStrict_ilist(self, ctx:tlangParser.Strict_ilistContext):
	# TODO: code refactoring. visitInstruction_list and visitStrict_ilist have same body
        instrList = []
        for instr in ctx.instruction():
            visvalue = self.visit(instr)
            instrList.extend(visvalue)

        return instrList


    def visitAssignment(self, ctx:tlangParser.AssignmentContext):
        lval = ChironAST.Var(ctx.VAR().getText())
        lval.lineno = ctx.start.line
        rval = self.visit(ctx.expression())
        node = ChironAST.AssignmentCommand(lval, rval)
        node.lineno = ctx.start.line  # Set line number
        return [(node, 1)]

    def visitIfConditional(self, ctx:tlangParser.IfConditionalContext):
        cond_ctx = ctx.condition() if ctx.condition() is not None else ctx.expression()
        condObj = ChironAST.ConditionCommand(self.visit(cond_ctx))
        condObj.lineno = ctx.start.line  # Set line number
        thenInstrList = self.visit(ctx.strict_ilist())
        return [(condObj, len(thenInstrList) + 1)] + thenInstrList

    def visitIfElseConditional(self, ctx:tlangParser.IfElseConditionalContext):
        cond_ctx = ctx.condition() if ctx.condition() is not None else ctx.expression()
        condObj = ChironAST.ConditionCommand(self.visit(cond_ctx))
        condObj.lineno = ctx.start.line

        thenInstrList = self.visit(ctx.strict_ilist(0))
        elseInstrList = self.visit(ctx.strict_ilist(1))

        jumpOverElseBlockNode = ChironAST.ConditionCommand(ChironAST.BoolFalse())
        jumpOverElseBlockNode.lineno = ctx.start.line
        jumpOverElseBlock = [(jumpOverElseBlockNode, len(elseInstrList) + 1)]

        return ([(condObj, len(thenInstrList) + 2)] + thenInstrList + jumpOverElseBlock + elseInstrList)

    def visitGotoCommand(self, ctx:tlangParser.GotoCommandContext):
        xcor = self.visit(ctx.expression(0))
        ycor = self.visit(ctx.expression(1))
        node = ChironAST.GotoCommand(xcor, ycor)
        node.lineno = ctx.start.line
        return [(node, 1)]

    def visitUnaryExpr(self,ctx:tlangParser.UnaryExprContext):
        expr1 = self.visit(ctx.expression())
        node = None
        if ctx.unaryArithOp().MINUS():
            node = ChironAST.UMinus(expr1)
        else:
            node = self.visitChildren(ctx)
        node.lineno = ctx.start.line
        return node

    def visitAddExpr(self, ctx:tlangParser.AddExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        node = None
        if ctx.additive().PLUS():
            node = ChironAST.Sum(left, right)
        elif ctx.additive().MINUS():
            node = ChironAST.Diff(left, right)
        node.lineno = ctx.start.line
        return node

    def visitMulExpr(self, ctx:tlangParser.MulExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        node = None
        if ctx.multiplicative().MUL():
            node = ChironAST.Mult(left, right)
        elif ctx.multiplicative().DIV():
            node = ChironAST.Div(left, right)
        node.lineno = ctx.start.line
        return node

    def visitParenExpr(self, ctx:tlangParser.ParenExprContext):
        return self.visit(ctx.expression())

    def visitCondition(self, ctx:tlangParser.ConditionContext):
        node = None
        if ctx.PENCOND():
            node = ChironAST.PenStatus()
        elif ctx.NOT():
            expr1 = self.visit(ctx.condition(0))
            node = ChironAST.NOT(expr1)
        elif ctx.logicOp():
            expr1 = self.visit(ctx.condition(0))
            expr2 = self.visit(ctx.condition(1))
            logicOpCtx = ctx.logicOp()
            if logicOpCtx.AND():
                node = ChironAST.AND(expr1, expr2)
            elif logicOpCtx.OR():
                node = ChironAST.OR(expr1, expr2)
        elif ctx.binCondOp():
            expr1 = self.visit(ctx.expression(0))
            expr2 = self.visit(ctx.expression(1))
            binOpCtx = ctx.binCondOp()
            if binOpCtx.LT():
                node = ChironAST.LT(expr1, expr2)
            elif binOpCtx.GT():
                node = ChironAST.GT(expr1, expr2)
            elif binOpCtx.EQ():
                node = ChironAST.EQ(expr1, expr2)
            elif binOpCtx.NEQ():
                node = ChironAST.NEQ(expr1, expr2)
            elif binOpCtx.LTE():
                node = ChironAST.LTE(expr1, expr2)
            elif binOpCtx.GTE():
                node = ChironAST.GTE(expr1, expr2)
        elif ctx.condition():
            node = self.visit(ctx.condition(0))
        else:
            node = self.visitChildren(ctx)
        node.lineno = ctx.start.line
        return node

    def visitValue(self, ctx:tlangParser.ValueContext):
        node = None
        if ctx.NUM():
            node = ChironAST.Num(ctx.NUM().getText())
        elif ctx.VAR():
            node = ChironAST.Var(ctx.VAR().getText())
        node.lineno = ctx.start.line
        return node

    def visitLoop(self, ctx:tlangParser.LoopContext):
        self.repeatInstrCount += 1
        repeatNum = self.visit(ctx.value())
        line = ctx.start.line

        counterVar = ChironAST.Var(":__rep_counter_" + str(self.repeatInstrCount))
        counterVar.lineno = line

        counterVarInitInstr = ChironAST.AssignmentCommand(counterVar, repeatNum)
        counterVarInitInstr.lineno = line

        constZero = ChironAST.Num(0)
        constOne = ChironAST.Num(1)

        loopCond = ChironAST.ConditionCommand(ChironAST.GT(counterVar, constZero))
        loopCond.lineno = line

        counterVarDecrInstr = ChironAST.AssignmentCommand(counterVar, ChironAST.Diff(counterVar, constOne))
        counterVarDecrInstr.lineno = line

        thenInstrList = []
        for instr in ctx.strict_ilist().instruction():
            thenInstrList.extend(self.visit(instr))

        boolFalse = ChironAST.ConditionCommand(ChironAST.BoolFalse())
        boolFalse.lineno = line

        return ([(counterVarInitInstr, 1), (loopCond, len(thenInstrList) + 3)] + thenInstrList + [(counterVarDecrInstr, 1), (boolFalse, -len(thenInstrList) - 2)])

    def visitMoveCommand(self, ctx:tlangParser.MoveCommandContext):
        mvcommand = ctx.moveOp().getText()
        mvexpr = self.visit(ctx.expression())
        node = ChironAST.MoveCommand(mvcommand, mvexpr)
        node.lineno = ctx.start.line
        return [(node, 1)]

    def visitPenCommand(self, ctx:tlangParser.PenCommandContext):
        node = ChironAST.PenCommand(ctx.getText())
        node.lineno = ctx.start.line
        return [(node, 1)]

    def visitPrintCommand(self, ctx:tlangParser.PrintCommandContext):
        expr = self.visit(ctx.expression())
        node = ChironAST.PrintCommand(expr)
        node.lineno = ctx.start.line
        return [(node, 1)]

    def visitReturnCommand(self, ctx:tlangParser.ReturnCommandContext):
        expr = None
        if ctx.expression():
            expr = self.visit(ctx.expression())
        node = ChironAST.ReturnCommand(expr)
        node.lineno = ctx.start.line
        return [(node, 1)]

    def visitProcedureDeclaration(self, ctx:tlangParser.ProcedureDeclarationContext):
        name = ctx.NAME().getText()
        params = []
        if ctx.paramList():
            for v in ctx.paramList().VAR():
                params.append(v.getText())

        body_instrs = self.visit(ctx.instruction_list())
        node = ChironAST.ProcedureDeclaration(name, params, body_instrs)
        node.lineno = ctx.start.line
        return [(node, 1)]

    def visitProcedureCall(self, ctx:tlangParser.ProcedureCallContext):
        name = ctx.NAME().getText()
        args = []
        if ctx.argList():
            for expr in ctx.argList().expression():
                args.append(self.visit(expr))
        node = ChironAST.ProcedureCall(name, args)
        node.lineno = ctx.start.line
        return [(node, 1)]

    def visitAssertCommand(self, ctx:tlangParser.AssertCommandContext):
        test_ctx = ctx.condition() if ctx.condition() is not None else ctx.expression()
        cond = self.visit(test_ctx)
        node = ChironAST.AssertCommand(cond)
        node.lineno = ctx.start.line
        return [(node, 1)]

    def visitProcedureCallExpr(self, ctx:tlangParser.ProcedureCallExprContext):
        name = ctx.procedureCall().NAME().getText()
        args = []
        if ctx.procedureCall().argList():
            for expr in ctx.procedureCall().argList().expression():
                args.append(self.visit(expr))
        node = ChironAST.ProcedureCallExpr(name, args)
        node.lineno = ctx.start.line
        return node

    def visitGlobalDecl(self, ctx:tlangParser.GlobalDeclContext):
        varname = ctx.VAR().getText()
        node = ChironAST.GlobalDecl(varname)
        node.lineno = ctx.start.line
        return [(node, 1)]