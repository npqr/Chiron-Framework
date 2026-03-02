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
        4,1,41,237,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,1,0,1,0,1,0,1,1,5,1,63,8,1,10,1,12,1,66,9,1,
        1,2,4,2,69,8,2,11,2,12,2,70,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,3,3,85,8,3,1,4,1,4,1,4,1,5,1,5,3,5,92,8,5,1,6,1,6,1,
        6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,
        8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,
        11,1,11,1,11,1,12,1,12,1,13,1,13,1,14,1,14,1,15,1,15,1,15,1,15,3,
        15,140,8,15,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,5,16,150,8,16,
        10,16,12,16,153,9,16,1,17,1,17,1,17,3,17,158,8,17,1,17,1,17,1,18,
        1,18,1,18,5,18,165,8,18,10,18,12,18,168,9,18,1,19,1,19,1,19,1,19,
        1,19,1,19,1,19,1,19,1,19,1,19,3,19,180,8,19,1,19,1,19,1,19,1,19,
        1,19,1,19,1,19,1,19,5,19,190,8,19,10,19,12,19,193,9,19,1,20,1,20,
        1,21,1,21,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,
        1,23,1,23,1,23,3,23,213,8,23,1,23,1,23,1,23,1,23,5,23,219,8,23,10,
        23,12,23,222,9,23,1,24,1,24,1,25,1,25,1,26,1,26,1,27,1,27,3,27,232,
        8,27,1,28,1,28,1,28,1,28,0,2,38,46,29,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,0,7,1,0,12,
        15,1,0,16,17,1,0,24,25,1,0,22,23,1,0,27,32,1,0,33,34,1,0,36,37,235,
        0,58,1,0,0,0,2,64,1,0,0,0,4,68,1,0,0,0,6,84,1,0,0,0,8,86,1,0,0,0,
        10,91,1,0,0,0,12,93,1,0,0,0,14,99,1,0,0,0,16,109,1,0,0,0,18,115,
        1,0,0,0,20,122,1,0,0,0,22,126,1,0,0,0,24,129,1,0,0,0,26,131,1,0,
        0,0,28,133,1,0,0,0,30,135,1,0,0,0,32,146,1,0,0,0,34,154,1,0,0,0,
        36,161,1,0,0,0,38,179,1,0,0,0,40,194,1,0,0,0,42,196,1,0,0,0,44,198,
        1,0,0,0,46,212,1,0,0,0,48,223,1,0,0,0,50,225,1,0,0,0,52,227,1,0,
        0,0,54,229,1,0,0,0,56,233,1,0,0,0,58,59,3,2,1,0,59,60,5,0,0,1,60,
        1,1,0,0,0,61,63,3,6,3,0,62,61,1,0,0,0,63,66,1,0,0,0,64,62,1,0,0,
        0,64,65,1,0,0,0,65,3,1,0,0,0,66,64,1,0,0,0,67,69,3,6,3,0,68,67,1,
        0,0,0,69,70,1,0,0,0,70,68,1,0,0,0,70,71,1,0,0,0,71,5,1,0,0,0,72,
        85,3,20,10,0,73,85,3,10,5,0,74,85,3,16,8,0,75,85,3,22,11,0,76,85,
        3,26,13,0,77,85,3,18,9,0,78,85,3,28,14,0,79,85,3,30,15,0,80,85,3,
        34,17,0,81,85,3,8,4,0,82,85,3,54,27,0,83,85,3,56,28,0,84,72,1,0,
        0,0,84,73,1,0,0,0,84,74,1,0,0,0,84,75,1,0,0,0,84,76,1,0,0,0,84,77,
        1,0,0,0,84,78,1,0,0,0,84,79,1,0,0,0,84,80,1,0,0,0,84,81,1,0,0,0,
        84,82,1,0,0,0,84,83,1,0,0,0,85,7,1,0,0,0,86,87,5,1,0,0,87,88,3,46,
        23,0,88,9,1,0,0,0,89,92,3,12,6,0,90,92,3,14,7,0,91,89,1,0,0,0,91,
        90,1,0,0,0,92,11,1,0,0,0,93,94,5,2,0,0,94,95,3,46,23,0,95,96,5,3,
        0,0,96,97,3,4,2,0,97,98,5,4,0,0,98,13,1,0,0,0,99,100,5,2,0,0,100,
        101,3,46,23,0,101,102,5,3,0,0,102,103,3,4,2,0,103,104,5,4,0,0,104,
        105,5,5,0,0,105,106,5,3,0,0,106,107,3,4,2,0,107,108,5,4,0,0,108,
        15,1,0,0,0,109,110,5,6,0,0,110,111,3,52,26,0,111,112,5,3,0,0,112,
        113,3,4,2,0,113,114,5,4,0,0,114,17,1,0,0,0,115,116,5,7,0,0,116,117,
        5,8,0,0,117,118,3,38,19,0,118,119,5,9,0,0,119,120,3,38,19,0,120,
        121,5,10,0,0,121,19,1,0,0,0,122,123,5,37,0,0,123,124,5,11,0,0,124,
        125,3,38,19,0,125,21,1,0,0,0,126,127,3,24,12,0,127,128,3,38,19,0,
        128,23,1,0,0,0,129,130,7,0,0,0,130,25,1,0,0,0,131,132,7,1,0,0,132,
        27,1,0,0,0,133,134,5,18,0,0,134,29,1,0,0,0,135,136,5,19,0,0,136,
        137,5,38,0,0,137,139,5,8,0,0,138,140,3,32,16,0,139,138,1,0,0,0,139,
        140,1,0,0,0,140,141,1,0,0,0,141,142,5,10,0,0,142,143,5,3,0,0,143,
        144,3,2,1,0,144,145,5,4,0,0,145,31,1,0,0,0,146,151,5,37,0,0,147,
        148,5,9,0,0,148,150,5,37,0,0,149,147,1,0,0,0,150,153,1,0,0,0,151,
        149,1,0,0,0,151,152,1,0,0,0,152,33,1,0,0,0,153,151,1,0,0,0,154,155,
        5,38,0,0,155,157,5,8,0,0,156,158,3,36,18,0,157,156,1,0,0,0,157,158,
        1,0,0,0,158,159,1,0,0,0,159,160,5,10,0,0,160,35,1,0,0,0,161,166,
        3,38,19,0,162,163,5,9,0,0,163,165,3,38,19,0,164,162,1,0,0,0,165,
        168,1,0,0,0,166,164,1,0,0,0,166,167,1,0,0,0,167,37,1,0,0,0,168,166,
        1,0,0,0,169,170,6,19,-1,0,170,171,3,44,22,0,171,172,3,38,19,6,172,
        180,1,0,0,0,173,180,3,52,26,0,174,175,5,8,0,0,175,176,3,38,19,0,
        176,177,5,10,0,0,177,180,1,0,0,0,178,180,3,34,17,0,179,169,1,0,0,
        0,179,173,1,0,0,0,179,174,1,0,0,0,179,178,1,0,0,0,180,191,1,0,0,
        0,181,182,10,5,0,0,182,183,3,40,20,0,183,184,3,38,19,6,184,190,1,
        0,0,0,185,186,10,4,0,0,186,187,3,42,21,0,187,188,3,38,19,5,188,190,
        1,0,0,0,189,181,1,0,0,0,189,185,1,0,0,0,190,193,1,0,0,0,191,189,
        1,0,0,0,191,192,1,0,0,0,192,39,1,0,0,0,193,191,1,0,0,0,194,195,7,
        2,0,0,195,41,1,0,0,0,196,197,7,3,0,0,197,43,1,0,0,0,198,199,5,23,
        0,0,199,45,1,0,0,0,200,201,6,23,-1,0,201,202,5,35,0,0,202,213,3,
        46,23,5,203,204,3,38,19,0,204,205,3,48,24,0,205,206,3,38,19,0,206,
        213,1,0,0,0,207,213,5,26,0,0,208,209,5,8,0,0,209,210,3,46,23,0,210,
        211,5,10,0,0,211,213,1,0,0,0,212,200,1,0,0,0,212,203,1,0,0,0,212,
        207,1,0,0,0,212,208,1,0,0,0,213,220,1,0,0,0,214,215,10,3,0,0,215,
        216,3,50,25,0,216,217,3,46,23,4,217,219,1,0,0,0,218,214,1,0,0,0,
        219,222,1,0,0,0,220,218,1,0,0,0,220,221,1,0,0,0,221,47,1,0,0,0,222,
        220,1,0,0,0,223,224,7,4,0,0,224,49,1,0,0,0,225,226,7,5,0,0,226,51,
        1,0,0,0,227,228,7,6,0,0,228,53,1,0,0,0,229,231,5,20,0,0,230,232,
        3,38,19,0,231,230,1,0,0,0,231,232,1,0,0,0,232,55,1,0,0,0,233,234,
        5,21,0,0,234,235,3,38,19,0,235,57,1,0,0,0,14,64,70,84,91,139,151,
        157,166,179,189,191,212,220,231
    ]

class tlangParser ( Parser ):

    grammarFileName = "tlang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'assert'", "'if'", "'['", "']'", "'else'", 
                     "'repeat'", "'goto'", "'('", "','", "')'", "'='", "'forward'", 
                     "'backward'", "'left'", "'right'", "'penup'", "'pendown'", 
                     "'pause'", "'to'", "'return'", "'print'", "'+'", "'-'", 
                     "'*'", "'/'", "'pendown?'", "'<'", "'>'", "'=='", "'!='", 
                     "'<='", "'>='", "'&&'", "'||'", "'!'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "PLUS", "MINUS", "MUL", 
                      "DIV", "PENCOND", "LT", "GT", "EQ", "NEQ", "LTE", 
                      "GTE", "AND", "OR", "NOT", "NUM", "VAR", "NAME", "Whitespace", 
                      "COMMENT", "MULTILINE_COMMENT" ]

    RULE_start = 0
    RULE_instruction_list = 1
    RULE_strict_ilist = 2
    RULE_instruction = 3
    RULE_assertCommand = 4
    RULE_conditional = 5
    RULE_ifConditional = 6
    RULE_ifElseConditional = 7
    RULE_loop = 8
    RULE_gotoCommand = 9
    RULE_assignment = 10
    RULE_moveCommand = 11
    RULE_moveOp = 12
    RULE_penCommand = 13
    RULE_pauseCommand = 14
    RULE_procedureDeclaration = 15
    RULE_paramList = 16
    RULE_procedureCall = 17
    RULE_argList = 18
    RULE_expression = 19
    RULE_multiplicative = 20
    RULE_additive = 21
    RULE_unaryArithOp = 22
    RULE_condition = 23
    RULE_binCondOp = 24
    RULE_logicOp = 25
    RULE_value = 26
    RULE_returnCommand = 27
    RULE_printCommand = 28

    ruleNames =  [ "start", "instruction_list", "strict_ilist", "instruction", 
                   "assertCommand", "conditional", "ifConditional", "ifElseConditional", 
                   "loop", "gotoCommand", "assignment", "moveCommand", "moveOp", 
                   "penCommand", "pauseCommand", "procedureDeclaration", 
                   "paramList", "procedureCall", "argList", "expression", 
                   "multiplicative", "additive", "unaryArithOp", "condition", 
                   "binCondOp", "logicOp", "value", "returnCommand", "printCommand" ]

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
    PLUS=22
    MINUS=23
    MUL=24
    DIV=25
    PENCOND=26
    LT=27
    GT=28
    EQ=29
    NEQ=30
    LTE=31
    GTE=32
    AND=33
    OR=34
    NOT=35
    NUM=36
    VAR=37
    NAME=38
    Whitespace=39
    COMMENT=40
    MULTILINE_COMMENT=41

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
            self.state = 58
            self.instruction_list()
            self.state = 59
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
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 412321050822) != 0):
                self.state = 61
                self.instruction()
                self.state = 66
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
            self.state = 68 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 67
                self.instruction()
                self.state = 70 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 412321050822) != 0)):
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
            self.state = 84
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.assignment()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.conditional()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 74
                self.loop()
                pass
            elif token in [12, 13, 14, 15]:
                self.enterOuterAlt(localctx, 4)
                self.state = 75
                self.moveCommand()
                pass
            elif token in [16, 17]:
                self.enterOuterAlt(localctx, 5)
                self.state = 76
                self.penCommand()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 6)
                self.state = 77
                self.gotoCommand()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 7)
                self.state = 78
                self.pauseCommand()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 8)
                self.state = 79
                self.procedureDeclaration()
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 9)
                self.state = 80
                self.procedureCall()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 10)
                self.state = 81
                self.assertCommand()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 11)
                self.state = 82
                self.returnCommand()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 12)
                self.state = 83
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


    class AssertCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(tlangParser.ConditionContext,0)


        def getRuleIndex(self):
            return tlangParser.RULE_assertCommand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssertCommand" ):
                return visitor.visitAssertCommand(self)
            else:
                return visitor.visitChildren(self)




    def assertCommand(self):

        localctx = tlangParser.AssertCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assertCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(tlangParser.T__0)
            self.state = 87
            self.condition(0)
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
        self.enterRule(localctx, 10, self.RULE_conditional)
        try:
            self.state = 91
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.ifConditional()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
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

        def condition(self):
            return self.getTypedRuleContext(tlangParser.ConditionContext,0)


        def strict_ilist(self):
            return self.getTypedRuleContext(tlangParser.Strict_ilistContext,0)


        def getRuleIndex(self):
            return tlangParser.RULE_ifConditional

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfConditional" ):
                return visitor.visitIfConditional(self)
            else:
                return visitor.visitChildren(self)




    def ifConditional(self):

        localctx = tlangParser.IfConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_ifConditional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(tlangParser.T__1)
            self.state = 94
            self.condition(0)
            self.state = 95
            self.match(tlangParser.T__2)
            self.state = 96
            self.strict_ilist()
            self.state = 97
            self.match(tlangParser.T__3)
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

        def condition(self):
            return self.getTypedRuleContext(tlangParser.ConditionContext,0)


        def strict_ilist(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tlangParser.Strict_ilistContext)
            else:
                return self.getTypedRuleContext(tlangParser.Strict_ilistContext,i)


        def getRuleIndex(self):
            return tlangParser.RULE_ifElseConditional

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfElseConditional" ):
                return visitor.visitIfElseConditional(self)
            else:
                return visitor.visitChildren(self)




    def ifElseConditional(self):

        localctx = tlangParser.IfElseConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_ifElseConditional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(tlangParser.T__1)
            self.state = 100
            self.condition(0)
            self.state = 101
            self.match(tlangParser.T__2)
            self.state = 102
            self.strict_ilist()
            self.state = 103
            self.match(tlangParser.T__3)
            self.state = 104
            self.match(tlangParser.T__4)
            self.state = 105
            self.match(tlangParser.T__2)
            self.state = 106
            self.strict_ilist()
            self.state = 107
            self.match(tlangParser.T__3)
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
        self.enterRule(localctx, 16, self.RULE_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(tlangParser.T__5)
            self.state = 110
            self.value()
            self.state = 111
            self.match(tlangParser.T__2)
            self.state = 112
            self.strict_ilist()
            self.state = 113
            self.match(tlangParser.T__3)
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
        self.enterRule(localctx, 18, self.RULE_gotoCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(tlangParser.T__6)
            self.state = 116
            self.match(tlangParser.T__7)
            self.state = 117
            self.expression(0)
            self.state = 118
            self.match(tlangParser.T__8)
            self.state = 119
            self.expression(0)
            self.state = 120
            self.match(tlangParser.T__9)
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
        self.enterRule(localctx, 20, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(tlangParser.VAR)
            self.state = 123
            self.match(tlangParser.T__10)
            self.state = 124
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
        self.enterRule(localctx, 22, self.RULE_moveCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.moveOp()
            self.state = 127
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
        self.enterRule(localctx, 24, self.RULE_moveOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 61440) != 0)):
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
        self.enterRule(localctx, 26, self.RULE_penCommand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            _la = self._input.LA(1)
            if not(_la==16 or _la==17):
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
        self.enterRule(localctx, 28, self.RULE_pauseCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(tlangParser.T__17)
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
        self.enterRule(localctx, 30, self.RULE_procedureDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(tlangParser.T__18)
            self.state = 136
            self.match(tlangParser.NAME)
            self.state = 137
            self.match(tlangParser.T__7)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 138
                self.paramList()


            self.state = 141
            self.match(tlangParser.T__9)
            self.state = 142
            self.match(tlangParser.T__2)
            self.state = 143
            self.instruction_list()
            self.state = 144
            self.match(tlangParser.T__3)
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
        self.enterRule(localctx, 32, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(tlangParser.VAR)
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 147
                self.match(tlangParser.T__8)
                self.state = 148
                self.match(tlangParser.VAR)
                self.state = 153
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
        self.enterRule(localctx, 34, self.RULE_procedureCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(tlangParser.NAME)
            self.state = 155
            self.match(tlangParser.T__7)
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 481044726016) != 0):
                self.state = 156
                self.argList()


            self.state = 159
            self.match(tlangParser.T__9)
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
        self.enterRule(localctx, 36, self.RULE_argList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.expression(0)
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 162
                self.match(tlangParser.T__8)
                self.state = 163
                self.expression(0)
                self.state = 168
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
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                localctx = tlangParser.UnaryExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 170
                self.unaryArithOp()
                self.state = 171
                self.expression(6)
                pass
            elif token in [36, 37]:
                localctx = tlangParser.ValueExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 173
                self.value()
                pass
            elif token in [8]:
                localctx = tlangParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 174
                self.match(tlangParser.T__7)
                self.state = 175
                self.expression(0)
                self.state = 176
                self.match(tlangParser.T__9)
                pass
            elif token in [38]:
                localctx = tlangParser.ProcedureCallExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 178
                self.procedureCall()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 191
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 189
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = tlangParser.MulExprContext(self, tlangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 181
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 182
                        self.multiplicative()
                        self.state = 183
                        self.expression(6)
                        pass

                    elif la_ == 2:
                        localctx = tlangParser.AddExprContext(self, tlangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 185
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 186
                        self.additive()
                        self.state = 187
                        self.expression(5)
                        pass

             
                self.state = 193
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

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
        self.enterRule(localctx, 40, self.RULE_multiplicative)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
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
        self.enterRule(localctx, 42, self.RULE_additive)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            _la = self._input.LA(1)
            if not(_la==22 or _la==23):
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
        self.enterRule(localctx, 44, self.RULE_unaryArithOp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
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
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_condition, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 201
                self.match(tlangParser.NOT)
                self.state = 202
                self.condition(5)
                pass

            elif la_ == 2:
                self.state = 203
                self.expression(0)
                self.state = 204
                self.binCondOp()
                self.state = 205
                self.expression(0)
                pass

            elif la_ == 3:
                self.state = 207
                self.match(tlangParser.PENCOND)
                pass

            elif la_ == 4:
                self.state = 208
                self.match(tlangParser.T__7)
                self.state = 209
                self.condition(0)
                self.state = 210
                self.match(tlangParser.T__9)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 220
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = tlangParser.ConditionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_condition)
                    self.state = 214
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 215
                    self.logicOp()
                    self.state = 216
                    self.condition(4) 
                self.state = 222
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

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
        self.enterRule(localctx, 48, self.RULE_binCondOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8455716864) != 0)):
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
        self.enterRule(localctx, 50, self.RULE_logicOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            _la = self._input.LA(1)
            if not(_la==33 or _la==34):
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
        self.enterRule(localctx, 52, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            _la = self._input.LA(1)
            if not(_la==36 or _la==37):
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
        self.enterRule(localctx, 54, self.RULE_returnCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(tlangParser.T__19)
            self.state = 231
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 230
                self.expression(0)


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
        self.enterRule(localctx, 56, self.RULE_printCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(tlangParser.T__20)
            self.state = 234
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
        self._predicates[19] = self.expression_sempred
        self._predicates[23] = self.condition_sempred
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
         




