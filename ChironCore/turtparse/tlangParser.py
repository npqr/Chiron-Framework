# Generated from turtparse/tlang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,43,252,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,1,0,1,0,1,0,1,1,5,1,65,8,1,10,1,12,
        1,68,9,1,1,2,4,2,71,8,2,11,2,12,2,72,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,3,3,88,8,3,1,4,1,4,1,4,1,5,1,5,1,5,3,5,96,
        8,5,1,6,1,6,3,6,100,8,6,1,7,1,7,1,7,3,7,105,8,7,1,7,1,7,1,7,1,7,
        1,8,1,8,1,8,3,8,114,8,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,
        1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,
        1,11,1,12,1,12,1,12,1,13,1,13,1,14,1,14,1,15,1,15,1,16,1,16,1,16,
        1,16,3,16,154,8,16,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,5,17,
        164,8,17,10,17,12,17,167,9,17,1,18,1,18,1,18,3,18,172,8,18,1,18,
        1,18,1,19,1,19,1,19,5,19,179,8,19,10,19,12,19,182,9,19,1,20,1,20,
        1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,3,20,194,8,20,1,20,1,20,
        1,20,1,20,1,20,1,20,1,20,1,20,5,20,204,8,20,10,20,12,20,207,9,20,
        1,21,1,21,1,22,1,22,1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,
        1,24,1,24,1,24,1,24,1,24,3,24,227,8,24,1,24,1,24,1,24,1,24,5,24,
        233,8,24,10,24,12,24,236,9,24,1,25,1,25,1,26,1,26,1,27,1,27,1,28,
        1,28,1,28,3,28,247,8,28,1,29,1,29,1,29,1,29,0,2,40,48,30,0,2,4,6,
        8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,
        52,54,56,58,0,7,1,0,13,16,1,0,17,18,1,0,26,27,1,0,24,25,1,0,29,34,
        1,0,35,36,1,0,38,39,253,0,60,1,0,0,0,2,66,1,0,0,0,4,70,1,0,0,0,6,
        87,1,0,0,0,8,89,1,0,0,0,10,92,1,0,0,0,12,99,1,0,0,0,14,101,1,0,0,
        0,16,110,1,0,0,0,18,123,1,0,0,0,20,129,1,0,0,0,22,136,1,0,0,0,24,
        140,1,0,0,0,26,143,1,0,0,0,28,145,1,0,0,0,30,147,1,0,0,0,32,149,
        1,0,0,0,34,160,1,0,0,0,36,168,1,0,0,0,38,175,1,0,0,0,40,193,1,0,
        0,0,42,208,1,0,0,0,44,210,1,0,0,0,46,212,1,0,0,0,48,226,1,0,0,0,
        50,237,1,0,0,0,52,239,1,0,0,0,54,241,1,0,0,0,56,243,1,0,0,0,58,248,
        1,0,0,0,60,61,3,2,1,0,61,62,5,0,0,1,62,1,1,0,0,0,63,65,3,6,3,0,64,
        63,1,0,0,0,65,68,1,0,0,0,66,64,1,0,0,0,66,67,1,0,0,0,67,3,1,0,0,
        0,68,66,1,0,0,0,69,71,3,6,3,0,70,69,1,0,0,0,71,72,1,0,0,0,72,70,
        1,0,0,0,72,73,1,0,0,0,73,5,1,0,0,0,74,88,3,8,4,0,75,88,3,22,11,0,
        76,88,3,12,6,0,77,88,3,18,9,0,78,88,3,24,12,0,79,88,3,28,14,0,80,
        88,3,20,10,0,81,88,3,30,15,0,82,88,3,32,16,0,83,88,3,36,18,0,84,
        88,3,10,5,0,85,88,3,56,28,0,86,88,3,58,29,0,87,74,1,0,0,0,87,75,
        1,0,0,0,87,76,1,0,0,0,87,77,1,0,0,0,87,78,1,0,0,0,87,79,1,0,0,0,
        87,80,1,0,0,0,87,81,1,0,0,0,87,82,1,0,0,0,87,83,1,0,0,0,87,84,1,
        0,0,0,87,85,1,0,0,0,87,86,1,0,0,0,88,7,1,0,0,0,89,90,5,1,0,0,90,
        91,5,39,0,0,91,9,1,0,0,0,92,95,5,2,0,0,93,96,3,48,24,0,94,96,3,40,
        20,0,95,93,1,0,0,0,95,94,1,0,0,0,96,11,1,0,0,0,97,100,3,14,7,0,98,
        100,3,16,8,0,99,97,1,0,0,0,99,98,1,0,0,0,100,13,1,0,0,0,101,104,
        5,3,0,0,102,105,3,48,24,0,103,105,3,40,20,0,104,102,1,0,0,0,104,
        103,1,0,0,0,105,106,1,0,0,0,106,107,5,4,0,0,107,108,3,4,2,0,108,
        109,5,5,0,0,109,15,1,0,0,0,110,113,5,3,0,0,111,114,3,48,24,0,112,
        114,3,40,20,0,113,111,1,0,0,0,113,112,1,0,0,0,114,115,1,0,0,0,115,
        116,5,4,0,0,116,117,3,4,2,0,117,118,5,5,0,0,118,119,5,6,0,0,119,
        120,5,4,0,0,120,121,3,4,2,0,121,122,5,5,0,0,122,17,1,0,0,0,123,124,
        5,7,0,0,124,125,3,54,27,0,125,126,5,4,0,0,126,127,3,4,2,0,127,128,
        5,5,0,0,128,19,1,0,0,0,129,130,5,8,0,0,130,131,5,9,0,0,131,132,3,
        40,20,0,132,133,5,10,0,0,133,134,3,40,20,0,134,135,5,11,0,0,135,
        21,1,0,0,0,136,137,5,39,0,0,137,138,5,12,0,0,138,139,3,40,20,0,139,
        23,1,0,0,0,140,141,3,26,13,0,141,142,3,40,20,0,142,25,1,0,0,0,143,
        144,7,0,0,0,144,27,1,0,0,0,145,146,7,1,0,0,146,29,1,0,0,0,147,148,
        5,19,0,0,148,31,1,0,0,0,149,150,5,20,0,0,150,151,5,40,0,0,151,153,
        5,9,0,0,152,154,3,34,17,0,153,152,1,0,0,0,153,154,1,0,0,0,154,155,
        1,0,0,0,155,156,5,11,0,0,156,157,5,4,0,0,157,158,3,2,1,0,158,159,
        5,5,0,0,159,33,1,0,0,0,160,165,5,39,0,0,161,162,5,10,0,0,162,164,
        5,39,0,0,163,161,1,0,0,0,164,167,1,0,0,0,165,163,1,0,0,0,165,166,
        1,0,0,0,166,35,1,0,0,0,167,165,1,0,0,0,168,169,5,40,0,0,169,171,
        5,9,0,0,170,172,3,38,19,0,171,170,1,0,0,0,171,172,1,0,0,0,172,173,
        1,0,0,0,173,174,5,11,0,0,174,37,1,0,0,0,175,180,3,40,20,0,176,177,
        5,10,0,0,177,179,3,40,20,0,178,176,1,0,0,0,179,182,1,0,0,0,180,178,
        1,0,0,0,180,181,1,0,0,0,181,39,1,0,0,0,182,180,1,0,0,0,183,184,6,
        20,-1,0,184,185,3,46,23,0,185,186,3,40,20,6,186,194,1,0,0,0,187,
        194,3,54,27,0,188,194,3,36,18,0,189,190,5,9,0,0,190,191,3,40,20,
        0,191,192,5,11,0,0,192,194,1,0,0,0,193,183,1,0,0,0,193,187,1,0,0,
        0,193,188,1,0,0,0,193,189,1,0,0,0,194,205,1,0,0,0,195,196,10,5,0,
        0,196,197,3,42,21,0,197,198,3,40,20,6,198,204,1,0,0,0,199,200,10,
        4,0,0,200,201,3,44,22,0,201,202,3,40,20,5,202,204,1,0,0,0,203,195,
        1,0,0,0,203,199,1,0,0,0,204,207,1,0,0,0,205,203,1,0,0,0,205,206,
        1,0,0,0,206,41,1,0,0,0,207,205,1,0,0,0,208,209,7,2,0,0,209,43,1,
        0,0,0,210,211,7,3,0,0,211,45,1,0,0,0,212,213,5,25,0,0,213,47,1,0,
        0,0,214,215,6,24,-1,0,215,216,5,37,0,0,216,227,3,48,24,5,217,218,
        3,40,20,0,218,219,3,50,25,0,219,220,3,40,20,0,220,227,1,0,0,0,221,
        227,5,28,0,0,222,223,5,9,0,0,223,224,3,48,24,0,224,225,5,11,0,0,
        225,227,1,0,0,0,226,214,1,0,0,0,226,217,1,0,0,0,226,221,1,0,0,0,
        226,222,1,0,0,0,227,234,1,0,0,0,228,229,10,3,0,0,229,230,3,52,26,
        0,230,231,3,48,24,4,231,233,1,0,0,0,232,228,1,0,0,0,233,236,1,0,
        0,0,234,232,1,0,0,0,234,235,1,0,0,0,235,49,1,0,0,0,236,234,1,0,0,
        0,237,238,7,4,0,0,238,51,1,0,0,0,239,240,7,5,0,0,240,53,1,0,0,0,
        241,242,7,6,0,0,242,55,1,0,0,0,243,246,5,21,0,0,244,247,5,22,0,0,
        245,247,3,40,20,0,246,244,1,0,0,0,246,245,1,0,0,0,247,57,1,0,0,0,
        248,249,5,23,0,0,249,250,3,40,20,0,250,59,1,0,0,0,17,66,72,87,95,
        99,104,113,153,165,171,180,193,203,205,226,234,246
    ]

class tlangParser ( Parser ):

    grammarFileName = "tlang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'global'", "'assert'", "'if'", "'['", 
                     "']'", "'else'", "'repeat'", "'goto'", "'('", "','", 
                     "')'", "'='", "'forward'", "'backward'", "'left'", 
                     "'right'", "'penup'", "'pendown'", "'pause'", "'to'", 
                     "'return '", "'void'", "'print'", "'+'", "'-'", "'*'", 
                     "'/'", "'pendown?'", "'<'", "'>'", "'=='", "'!='", 
                     "'<='", "'>='", "'&&'", "'||'", "'!'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "PLUS", "MINUS", "MUL", "DIV", "PENCOND", "LT", "GT", 
                      "EQ", "NEQ", "LTE", "GTE", "AND", "OR", "NOT", "NUM", 
                      "VAR", "NAME", "Whitespace", "COMMENT", "MULTILINE_COMMENT" ]

    RULE_start = 0
    RULE_instruction_list = 1
    RULE_strict_ilist = 2
    RULE_instruction = 3
    RULE_globalDecl = 4
    RULE_assertCommand = 5
    RULE_conditional = 6
    RULE_ifConditional = 7
    RULE_ifElseConditional = 8
    RULE_loop = 9
    RULE_gotoCommand = 10
    RULE_assignment = 11
    RULE_moveCommand = 12
    RULE_moveOp = 13
    RULE_penCommand = 14
    RULE_pauseCommand = 15
    RULE_procedureDeclaration = 16
    RULE_paramList = 17
    RULE_procedureCall = 18
    RULE_argList = 19
    RULE_expression = 20
    RULE_multiplicative = 21
    RULE_additive = 22
    RULE_unaryArithOp = 23
    RULE_condition = 24
    RULE_binCondOp = 25
    RULE_logicOp = 26
    RULE_value = 27
    RULE_returnCommand = 28
    RULE_printCommand = 29

    ruleNames =  [ "start", "instruction_list", "strict_ilist", "instruction", 
                   "globalDecl", "assertCommand", "conditional", "ifConditional", 
                   "ifElseConditional", "loop", "gotoCommand", "assignment", 
                   "moveCommand", "moveOp", "penCommand", "pauseCommand", 
                   "procedureDeclaration", "paramList", "procedureCall", 
                   "argList", "expression", "multiplicative", "additive", 
                   "unaryArithOp", "condition", "binCondOp", "logicOp", 
                   "value", "returnCommand", "printCommand" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    PLUS=24
    MINUS=25
    MUL=26
    DIV=27
    PENCOND=28
    LT=29
    GT=30
    EQ=31
    NEQ=32
    LTE=33
    GTE=34
    AND=35
    OR=36
    NOT=37
    NUM=38
    VAR=39
    NAME=40
    Whitespace=41
    COMMENT=42
    MULTILINE_COMMENT=43

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruction_list(self):
            return self.getTypedRuleContext(tlangParser.Instruction_listContext,0)


        def EOF(self):
            return self.getToken(tlangParser.EOF, 0)

        def getRuleIndex(self):
            return tlangParser.RULE_start

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = tlangParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.instruction_list()
            self.state = 61
            self.match(tlangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instruction_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tlangParser.InstructionContext)
            else:
                return self.getTypedRuleContext(tlangParser.InstructionContext,i)


        def getRuleIndex(self):
            return tlangParser.RULE_instruction_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruction_list" ):
                return visitor.visitInstruction_list(self)
            else:
                return visitor.visitChildren(self)




    def instruction_list(self):

        localctx = tlangParser.Instruction_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instruction_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1649280016782) != 0):
                self.state = 63
                self.instruction()
                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Strict_ilistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tlangParser.InstructionContext)
            else:
                return self.getTypedRuleContext(tlangParser.InstructionContext,i)


        def getRuleIndex(self):
            return tlangParser.RULE_strict_ilist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStrict_ilist" ):
                return visitor.visitStrict_ilist(self)
            else:
                return visitor.visitChildren(self)




    def strict_ilist(self):

        localctx = tlangParser.Strict_ilistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_strict_ilist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 69
                self.instruction()
                self.state = 72 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1649280016782) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def globalDecl(self):
            return self.getTypedRuleContext(tlangParser.GlobalDeclContext,0)


        def assignment(self):
            return self.getTypedRuleContext(tlangParser.AssignmentContext,0)


        def conditional(self):
            return self.getTypedRuleContext(tlangParser.ConditionalContext,0)


        def loop(self):
            return self.getTypedRuleContext(tlangParser.LoopContext,0)


        def moveCommand(self):
            return self.getTypedRuleContext(tlangParser.MoveCommandContext,0)


        def penCommand(self):
            return self.getTypedRuleContext(tlangParser.PenCommandContext,0)


        def gotoCommand(self):
            return self.getTypedRuleContext(tlangParser.GotoCommandContext,0)


        def pauseCommand(self):
            return self.getTypedRuleContext(tlangParser.PauseCommandContext,0)


        def procedureDeclaration(self):
            return self.getTypedRuleContext(tlangParser.ProcedureDeclarationContext,0)


        def procedureCall(self):
            return self.getTypedRuleContext(tlangParser.ProcedureCallContext,0)


        def assertCommand(self):
            return self.getTypedRuleContext(tlangParser.AssertCommandContext,0)


        def returnCommand(self):
            return self.getTypedRuleContext(tlangParser.ReturnCommandContext,0)


        def printCommand(self):
            return self.getTypedRuleContext(tlangParser.PrintCommandContext,0)


        def getRuleIndex(self):
            return tlangParser.RULE_instruction

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruction" ):
                return visitor.visitInstruction(self)
            else:
                return visitor.visitChildren(self)




    def instruction(self):

        localctx = tlangParser.InstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_instruction)
        try:
            self.state = 87
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.globalDecl()
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                self.assignment()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 76
                self.conditional()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 4)
                self.state = 77
                self.loop()
                pass
            elif token in [13, 14, 15, 16]:
                self.enterOuterAlt(localctx, 5)
                self.state = 78
                self.moveCommand()
                pass
            elif token in [17, 18]:
                self.enterOuterAlt(localctx, 6)
                self.state = 79
                self.penCommand()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 7)
                self.state = 80
                self.gotoCommand()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 8)
                self.state = 81
                self.pauseCommand()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 9)
                self.state = 82
                self.procedureDeclaration()
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 10)
                self.state = 83
                self.procedureCall()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 11)
                self.state = 84
                self.assertCommand()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 12)
                self.state = 85
                self.returnCommand()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 13)
                self.state = 86
                self.printCommand()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GlobalDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(tlangParser.VAR, 0)

        def getRuleIndex(self):
            return tlangParser.RULE_globalDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGlobalDecl" ):
                return visitor.visitGlobalDecl(self)
            else:
                return visitor.visitChildren(self)




    def globalDecl(self):

        localctx = tlangParser.GlobalDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_globalDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(tlangParser.T__0)
            self.state = 90
            self.match(tlangParser.VAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssertCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(tlangParser.ConditionContext,0)


        def expression(self):
            return self.getTypedRuleContext(tlangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return tlangParser.RULE_assertCommand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssertCommand" ):
                return visitor.visitAssertCommand(self)
            else:
                return visitor.visitChildren(self)




    def assertCommand(self):

        localctx = tlangParser.AssertCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assertCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(tlangParser.T__1)
            self.state = 95
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 93
                self.condition(0)
                pass

            elif la_ == 2:
                self.state = 94
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifConditional(self):
            return self.getTypedRuleContext(tlangParser.IfConditionalContext,0)


        def ifElseConditional(self):
            return self.getTypedRuleContext(tlangParser.IfElseConditionalContext,0)


        def getRuleIndex(self):
            return tlangParser.RULE_conditional

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditional" ):
                return visitor.visitConditional(self)
            else:
                return visitor.visitChildren(self)




    def conditional(self):

        localctx = tlangParser.ConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_conditional)
        try:
            self.state = 99
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 97
                self.ifConditional()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 98
                self.ifElseConditional()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfConditionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def strict_ilist(self):
            return self.getTypedRuleContext(tlangParser.Strict_ilistContext,0)


        def condition(self):
            return self.getTypedRuleContext(tlangParser.ConditionContext,0)


        def expression(self):
            return self.getTypedRuleContext(tlangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return tlangParser.RULE_ifConditional

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfConditional" ):
                return visitor.visitIfConditional(self)
            else:
                return visitor.visitChildren(self)




    def ifConditional(self):

        localctx = tlangParser.IfConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_ifConditional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(tlangParser.T__2)
            self.state = 104
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 102
                self.condition(0)
                pass

            elif la_ == 2:
                self.state = 103
                self.expression(0)
                pass


            self.state = 106
            self.match(tlangParser.T__3)
            self.state = 107
            self.strict_ilist()
            self.state = 108
            self.match(tlangParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfElseConditionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def strict_ilist(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tlangParser.Strict_ilistContext)
            else:
                return self.getTypedRuleContext(tlangParser.Strict_ilistContext,i)


        def condition(self):
            return self.getTypedRuleContext(tlangParser.ConditionContext,0)


        def expression(self):
            return self.getTypedRuleContext(tlangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return tlangParser.RULE_ifElseConditional

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfElseConditional" ):
                return visitor.visitIfElseConditional(self)
            else:
                return visitor.visitChildren(self)




    def ifElseConditional(self):

        localctx = tlangParser.IfElseConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_ifElseConditional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(tlangParser.T__2)
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 111
                self.condition(0)
                pass

            elif la_ == 2:
                self.state = 112
                self.expression(0)
                pass


            self.state = 115
            self.match(tlangParser.T__3)
            self.state = 116
            self.strict_ilist()
            self.state = 117
            self.match(tlangParser.T__4)
            self.state = 118
            self.match(tlangParser.T__5)
            self.state = 119
            self.match(tlangParser.T__3)
            self.state = 120
            self.strict_ilist()
            self.state = 121
            self.match(tlangParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(tlangParser.ValueContext,0)


        def strict_ilist(self):
            return self.getTypedRuleContext(tlangParser.Strict_ilistContext,0)


        def getRuleIndex(self):
            return tlangParser.RULE_loop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop" ):
                return visitor.visitLoop(self)
            else:
                return visitor.visitChildren(self)




    def loop(self):

        localctx = tlangParser.LoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(tlangParser.T__6)
            self.state = 124
            self.value()
            self.state = 125
            self.match(tlangParser.T__3)
            self.state = 126
            self.strict_ilist()
            self.state = 127
            self.match(tlangParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GotoCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tlangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(tlangParser.ExpressionContext,i)


        def getRuleIndex(self):
            return tlangParser.RULE_gotoCommand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGotoCommand" ):
                return visitor.visitGotoCommand(self)
            else:
                return visitor.visitChildren(self)




    def gotoCommand(self):

        localctx = tlangParser.GotoCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_gotoCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(tlangParser.T__7)
            self.state = 130
            self.match(tlangParser.T__8)
            self.state = 131
            self.expression(0)
            self.state = 132
            self.match(tlangParser.T__9)
            self.state = 133
            self.expression(0)
            self.state = 134
            self.match(tlangParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(tlangParser.VAR, 0)

        def expression(self):
            return self.getTypedRuleContext(tlangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return tlangParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = tlangParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(tlangParser.VAR)
            self.state = 137
            self.match(tlangParser.T__11)
            self.state = 138
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MoveCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def moveOp(self):
            return self.getTypedRuleContext(tlangParser.MoveOpContext,0)


        def expression(self):
            return self.getTypedRuleContext(tlangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return tlangParser.RULE_moveCommand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMoveCommand" ):
                return visitor.visitMoveCommand(self)
            else:
                return visitor.visitChildren(self)




    def moveCommand(self):

        localctx = tlangParser.MoveCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_moveCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.moveOp()
            self.state = 141
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MoveOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return tlangParser.RULE_moveOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMoveOp" ):
                return visitor.visitMoveOp(self)
            else:
                return visitor.visitChildren(self)




    def moveOp(self):

        localctx = tlangParser.MoveOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_moveOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 122880) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PenCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return tlangParser.RULE_penCommand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPenCommand" ):
                return visitor.visitPenCommand(self)
            else:
                return visitor.visitChildren(self)




    def penCommand(self):

        localctx = tlangParser.PenCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_penCommand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            _la = self._input.LA(1)
            if not(_la==17 or _la==18):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PauseCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return tlangParser.RULE_pauseCommand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPauseCommand" ):
                return visitor.visitPauseCommand(self)
            else:
                return visitor.visitChildren(self)




    def pauseCommand(self):

        localctx = tlangParser.PauseCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_pauseCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(tlangParser.T__18)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProcedureDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(tlangParser.NAME, 0)

        def instruction_list(self):
            return self.getTypedRuleContext(tlangParser.Instruction_listContext,0)


        def paramList(self):
            return self.getTypedRuleContext(tlangParser.ParamListContext,0)


        def getRuleIndex(self):
            return tlangParser.RULE_procedureDeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcedureDeclaration" ):
                return visitor.visitProcedureDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def procedureDeclaration(self):

        localctx = tlangParser.ProcedureDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_procedureDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(tlangParser.T__19)
            self.state = 150
            self.match(tlangParser.NAME)
            self.state = 151
            self.match(tlangParser.T__8)
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 152
                self.paramList()


            self.state = 155
            self.match(tlangParser.T__10)
            self.state = 156
            self.match(tlangParser.T__3)
            self.state = 157
            self.instruction_list()
            self.state = 158
            self.match(tlangParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self, i:int=None):
            if i is None:
                return self.getTokens(tlangParser.VAR)
            else:
                return self.getToken(tlangParser.VAR, i)

        def getRuleIndex(self):
            return tlangParser.RULE_paramList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = tlangParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(tlangParser.VAR)
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 161
                self.match(tlangParser.T__9)
                self.state = 162
                self.match(tlangParser.VAR)
                self.state = 167
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProcedureCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(tlangParser.NAME, 0)

        def argList(self):
            return self.getTypedRuleContext(tlangParser.ArgListContext,0)


        def getRuleIndex(self):
            return tlangParser.RULE_procedureCall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcedureCall" ):
                return visitor.visitProcedureCall(self)
            else:
                return visitor.visitChildren(self)




    def procedureCall(self):

        localctx = tlangParser.ProcedureCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_procedureCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(tlangParser.NAME)
            self.state = 169
            self.match(tlangParser.T__8)
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1924178903552) != 0):
                self.state = 170
                self.argList()


            self.state = 173
            self.match(tlangParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tlangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(tlangParser.ExpressionContext,i)


        def getRuleIndex(self):
            return tlangParser.RULE_argList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgList" ):
                return visitor.visitArgList(self)
            else:
                return visitor.visitChildren(self)




    def argList(self):

        localctx = tlangParser.ArgListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_argList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.expression(0)
            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 176
                self.match(tlangParser.T__9)
                self.state = 177
                self.expression(0)
                self.state = 182
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return tlangParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ProcedureCallExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a tlangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def procedureCall(self):
            return self.getTypedRuleContext(tlangParser.ProcedureCallContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcedureCallExpr" ):
                return visitor.visitProcedureCallExpr(self)
            else:
                return visitor.visitChildren(self)


    class UnaryExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a tlangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def unaryArithOp(self):
            return self.getTypedRuleContext(tlangParser.UnaryArithOpContext,0)

        def expression(self):
            return self.getTypedRuleContext(tlangParser.ExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpr" ):
                return visitor.visitUnaryExpr(self)
            else:
                return visitor.visitChildren(self)


    class ValueExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a tlangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def value(self):
            return self.getTypedRuleContext(tlangParser.ValueContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValueExpr" ):
                return visitor.visitValueExpr(self)
            else:
                return visitor.visitChildren(self)


    class AddExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a tlangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tlangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(tlangParser.ExpressionContext,i)

        def additive(self):
            return self.getTypedRuleContext(tlangParser.AdditiveContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddExpr" ):
                return visitor.visitAddExpr(self)
            else:
                return visitor.visitChildren(self)


    class MulExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a tlangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tlangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(tlangParser.ExpressionContext,i)

        def multiplicative(self):
            return self.getTypedRuleContext(tlangParser.MultiplicativeContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulExpr" ):
                return visitor.visitMulExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a tlangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(tlangParser.ExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = tlangParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                localctx = tlangParser.UnaryExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 184
                self.unaryArithOp()
                self.state = 185
                self.expression(6)
                pass
            elif token in [38, 39]:
                localctx = tlangParser.ValueExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 187
                self.value()
                pass
            elif token in [40]:
                localctx = tlangParser.ProcedureCallExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 188
                self.procedureCall()
                pass
            elif token in [9]:
                localctx = tlangParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 189
                self.match(tlangParser.T__8)
                self.state = 190
                self.expression(0)
                self.state = 191
                self.match(tlangParser.T__10)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 205
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 203
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        localctx = tlangParser.MulExprContext(self, tlangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 195
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 196
                        self.multiplicative()
                        self.state = 197
                        self.expression(6)
                        pass

                    elif la_ == 2:
                        localctx = tlangParser.AddExprContext(self, tlangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 199
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 200
                        self.additive()
                        self.state = 201
                        self.expression(5)
                        pass

             
                self.state = 207
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MultiplicativeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MUL(self):
            return self.getToken(tlangParser.MUL, 0)

        def DIV(self):
            return self.getToken(tlangParser.DIV, 0)

        def getRuleIndex(self):
            return tlangParser.RULE_multiplicative

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicative" ):
                return visitor.visitMultiplicative(self)
            else:
                return visitor.visitChildren(self)




    def multiplicative(self):

        localctx = tlangParser.MultiplicativeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_multiplicative)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            _la = self._input.LA(1)
            if not(_la==26 or _la==27):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(tlangParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(tlangParser.MINUS, 0)

        def getRuleIndex(self):
            return tlangParser.RULE_additive

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditive" ):
                return visitor.visitAdditive(self)
            else:
                return visitor.visitChildren(self)




    def additive(self):

        localctx = tlangParser.AdditiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_additive)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            _la = self._input.LA(1)
            if not(_la==24 or _la==25):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryArithOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(tlangParser.MINUS, 0)

        def getRuleIndex(self):
            return tlangParser.RULE_unaryArithOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryArithOp" ):
                return visitor.visitUnaryArithOp(self)
            else:
                return visitor.visitChildren(self)




    def unaryArithOp(self):

        localctx = tlangParser.UnaryArithOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_unaryArithOp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(tlangParser.MINUS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(tlangParser.NOT, 0)

        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tlangParser.ConditionContext)
            else:
                return self.getTypedRuleContext(tlangParser.ConditionContext,i)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tlangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(tlangParser.ExpressionContext,i)


        def binCondOp(self):
            return self.getTypedRuleContext(tlangParser.BinCondOpContext,0)


        def PENCOND(self):
            return self.getToken(tlangParser.PENCOND, 0)

        def logicOp(self):
            return self.getTypedRuleContext(tlangParser.LogicOpContext,0)


        def getRuleIndex(self):
            return tlangParser.RULE_condition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)



    def condition(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = tlangParser.ConditionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_condition, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 215
                self.match(tlangParser.NOT)
                self.state = 216
                self.condition(5)
                pass

            elif la_ == 2:
                self.state = 217
                self.expression(0)
                self.state = 218
                self.binCondOp()
                self.state = 219
                self.expression(0)
                pass

            elif la_ == 3:
                self.state = 221
                self.match(tlangParser.PENCOND)
                pass

            elif la_ == 4:
                self.state = 222
                self.match(tlangParser.T__8)
                self.state = 223
                self.condition(0)
                self.state = 224
                self.match(tlangParser.T__10)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 234
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = tlangParser.ConditionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_condition)
                    self.state = 228
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 229
                    self.logicOp()
                    self.state = 230
                    self.condition(4) 
                self.state = 236
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class BinCondOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(tlangParser.EQ, 0)

        def NEQ(self):
            return self.getToken(tlangParser.NEQ, 0)

        def LT(self):
            return self.getToken(tlangParser.LT, 0)

        def GT(self):
            return self.getToken(tlangParser.GT, 0)

        def LTE(self):
            return self.getToken(tlangParser.LTE, 0)

        def GTE(self):
            return self.getToken(tlangParser.GTE, 0)

        def getRuleIndex(self):
            return tlangParser.RULE_binCondOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinCondOp" ):
                return visitor.visitBinCondOp(self)
            else:
                return visitor.visitChildren(self)




    def binCondOp(self):

        localctx = tlangParser.BinCondOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_binCondOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 33822867456) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(tlangParser.AND, 0)

        def OR(self):
            return self.getToken(tlangParser.OR, 0)

        def getRuleIndex(self):
            return tlangParser.RULE_logicOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicOp" ):
                return visitor.visitLogicOp(self)
            else:
                return visitor.visitChildren(self)




    def logicOp(self):

        localctx = tlangParser.LogicOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_logicOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            _la = self._input.LA(1)
            if not(_la==35 or _la==36):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(tlangParser.NUM, 0)

        def VAR(self):
            return self.getToken(tlangParser.VAR, 0)

        def getRuleIndex(self):
            return tlangParser.RULE_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = tlangParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            _la = self._input.LA(1)
            if not(_la==38 or _la==39):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(tlangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return tlangParser.RULE_returnCommand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnCommand" ):
                return visitor.visitReturnCommand(self)
            else:
                return visitor.visitChildren(self)




    def returnCommand(self):

        localctx = tlangParser.ReturnCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_returnCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(tlangParser.T__20)
            self.state = 246
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.state = 244
                self.match(tlangParser.T__21)
                pass
            elif token in [9, 25, 38, 39, 40]:
                self.state = 245
                self.expression(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(tlangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return tlangParser.RULE_printCommand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintCommand" ):
                return visitor.visitPrintCommand(self)
            else:
                return visitor.visitChildren(self)




    def printCommand(self):

        localctx = tlangParser.PrintCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_printCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(tlangParser.T__22)
            self.state = 249
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[20] = self.expression_sempred
        self._predicates[24] = self.condition_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

    def condition_sempred(self, localctx:ConditionContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         




