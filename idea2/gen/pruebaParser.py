# Generated from C:/Users/josen/PycharmProjects/pythonProject2/prueba.g4 by ANTLR 4.13.1
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
        4,1,14,70,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,4,0,20,8,0,11,0,12,0,21,1,1,1,1,1,1,1,1,1,
        1,1,2,5,2,30,8,2,10,2,12,2,33,9,2,1,3,1,3,1,3,1,3,1,3,3,3,40,8,3,
        1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,7,1,7,1,7,5,7,54,8,7,10,7,
        12,7,57,9,7,1,7,1,7,1,8,1,8,5,8,63,8,8,10,8,12,8,66,9,8,1,8,1,8,
        1,8,0,0,9,0,2,4,6,8,10,12,14,16,0,3,1,0,11,13,1,0,10,14,1,0,9,9,
        68,0,19,1,0,0,0,2,23,1,0,0,0,4,31,1,0,0,0,6,39,1,0,0,0,8,41,1,0,
        0,0,10,44,1,0,0,0,12,48,1,0,0,0,14,50,1,0,0,0,16,60,1,0,0,0,18,20,
        3,2,1,0,19,18,1,0,0,0,20,21,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,
        22,1,1,0,0,0,23,24,5,10,0,0,24,25,5,1,0,0,25,26,3,4,2,0,26,27,5,
        2,0,0,27,3,1,0,0,0,28,30,3,6,3,0,29,28,1,0,0,0,30,33,1,0,0,0,31,
        29,1,0,0,0,31,32,1,0,0,0,32,5,1,0,0,0,33,31,1,0,0,0,34,40,3,8,4,
        0,35,40,3,10,5,0,36,40,3,16,8,0,37,40,3,12,6,0,38,40,3,14,7,0,39,
        34,1,0,0,0,39,35,1,0,0,0,39,36,1,0,0,0,39,37,1,0,0,0,39,38,1,0,0,
        0,40,7,1,0,0,0,41,42,5,3,0,0,42,43,5,12,0,0,43,9,1,0,0,0,44,45,5,
        11,0,0,45,46,5,4,0,0,46,47,7,0,0,0,47,11,1,0,0,0,48,49,5,10,0,0,
        49,13,1,0,0,0,50,51,5,5,0,0,51,55,5,6,0,0,52,54,7,1,0,0,53,52,1,
        0,0,0,54,57,1,0,0,0,55,53,1,0,0,0,55,56,1,0,0,0,56,58,1,0,0,0,57,
        55,1,0,0,0,58,59,5,7,0,0,59,15,1,0,0,0,60,64,5,8,0,0,61,63,8,2,0,
        0,62,61,1,0,0,0,63,66,1,0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,65,67,
        1,0,0,0,66,64,1,0,0,0,67,68,5,8,0,0,68,17,1,0,0,0,5,21,31,39,55,
        64
    ]

class pruebaParser ( Parser ):

    grammarFileName = "prueba.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'|:'", "':|'", "'<w>'", "'='", "'(:)'", 
                     "'{'", "'}'", "'###'", "'#'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID_CAP", "ID_MIN", "STRING", 
                      "INT", "WS" ]

    RULE_prog = 0
    RULE_procedure = 1
    RULE_block = 2
    RULE_statement = 3
    RULE_writeStatement = 4
    RULE_variableAssignment = 5
    RULE_musicalNote = 6
    RULE_section = 7
    RULE_comment = 8

    ruleNames =  [ "prog", "procedure", "block", "statement", "writeStatement", 
                   "variableAssignment", "musicalNote", "section", "comment" ]

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
    ID_CAP=10
    ID_MIN=11
    STRING=12
    INT=13
    WS=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def procedure(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pruebaParser.ProcedureContext)
            else:
                return self.getTypedRuleContext(pruebaParser.ProcedureContext,i)


        def getRuleIndex(self):
            return pruebaParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = pruebaParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.procedure()
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==10):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProcedureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID_CAP(self):
            return self.getToken(pruebaParser.ID_CAP, 0)

        def block(self):
            return self.getTypedRuleContext(pruebaParser.BlockContext,0)


        def getRuleIndex(self):
            return pruebaParser.RULE_procedure

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProcedure" ):
                listener.enterProcedure(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProcedure" ):
                listener.exitProcedure(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcedure" ):
                return visitor.visitProcedure(self)
            else:
                return visitor.visitChildren(self)




    def procedure(self):

        localctx = pruebaParser.ProcedureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_procedure)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.match(pruebaParser.ID_CAP)
            self.state = 24
            self.match(pruebaParser.T__0)
            self.state = 25
            self.block()
            self.state = 26
            self.match(pruebaParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pruebaParser.StatementContext)
            else:
                return self.getTypedRuleContext(pruebaParser.StatementContext,i)


        def getRuleIndex(self):
            return pruebaParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = pruebaParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3368) != 0):
                self.state = 28
                self.statement()
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def writeStatement(self):
            return self.getTypedRuleContext(pruebaParser.WriteStatementContext,0)


        def variableAssignment(self):
            return self.getTypedRuleContext(pruebaParser.VariableAssignmentContext,0)


        def comment(self):
            return self.getTypedRuleContext(pruebaParser.CommentContext,0)


        def musicalNote(self):
            return self.getTypedRuleContext(pruebaParser.MusicalNoteContext,0)


        def section(self):
            return self.getTypedRuleContext(pruebaParser.SectionContext,0)


        def getRuleIndex(self):
            return pruebaParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = pruebaParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statement)
        try:
            self.state = 39
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.writeStatement()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                self.variableAssignment()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 36
                self.comment()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 37
                self.musicalNote()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 5)
                self.state = 38
                self.section()
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


    class WriteStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(pruebaParser.STRING, 0)

        def getRuleIndex(self):
            return pruebaParser.RULE_writeStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWriteStatement" ):
                listener.enterWriteStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWriteStatement" ):
                listener.exitWriteStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWriteStatement" ):
                return visitor.visitWriteStatement(self)
            else:
                return visitor.visitChildren(self)




    def writeStatement(self):

        localctx = pruebaParser.WriteStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_writeStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(pruebaParser.T__2)
            self.state = 42
            self.match(pruebaParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableAssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID_MIN(self, i:int=None):
            if i is None:
                return self.getTokens(pruebaParser.ID_MIN)
            else:
                return self.getToken(pruebaParser.ID_MIN, i)

        def STRING(self):
            return self.getToken(pruebaParser.STRING, 0)

        def INT(self):
            return self.getToken(pruebaParser.INT, 0)

        def getRuleIndex(self):
            return pruebaParser.RULE_variableAssignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableAssignment" ):
                listener.enterVariableAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableAssignment" ):
                listener.exitVariableAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableAssignment" ):
                return visitor.visitVariableAssignment(self)
            else:
                return visitor.visitChildren(self)




    def variableAssignment(self):

        localctx = pruebaParser.VariableAssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_variableAssignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(pruebaParser.ID_MIN)
            self.state = 45
            self.match(pruebaParser.T__3)
            self.state = 46
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14336) != 0)):
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


    class MusicalNoteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID_CAP(self):
            return self.getToken(pruebaParser.ID_CAP, 0)

        def getRuleIndex(self):
            return pruebaParser.RULE_musicalNote

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMusicalNote" ):
                listener.enterMusicalNote(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMusicalNote" ):
                listener.exitMusicalNote(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMusicalNote" ):
                return visitor.visitMusicalNote(self)
            else:
                return visitor.visitChildren(self)




    def musicalNote(self):

        localctx = pruebaParser.MusicalNoteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_musicalNote)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(pruebaParser.ID_CAP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID_CAP(self, i:int=None):
            if i is None:
                return self.getTokens(pruebaParser.ID_CAP)
            else:
                return self.getToken(pruebaParser.ID_CAP, i)

        def ID_MIN(self, i:int=None):
            if i is None:
                return self.getTokens(pruebaParser.ID_MIN)
            else:
                return self.getToken(pruebaParser.ID_MIN, i)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(pruebaParser.STRING)
            else:
                return self.getToken(pruebaParser.STRING, i)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(pruebaParser.INT)
            else:
                return self.getToken(pruebaParser.INT, i)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(pruebaParser.WS)
            else:
                return self.getToken(pruebaParser.WS, i)

        def getRuleIndex(self):
            return pruebaParser.RULE_section

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSection" ):
                listener.enterSection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSection" ):
                listener.exitSection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSection" ):
                return visitor.visitSection(self)
            else:
                return visitor.visitChildren(self)




    def section(self):

        localctx = pruebaParser.SectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_section)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(pruebaParser.T__4)
            self.state = 51
            self.match(pruebaParser.T__5)
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 31744) != 0):
                self.state = 52
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 31744) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 58
            self.match(pruebaParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return pruebaParser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComment" ):
                return visitor.visitComment(self)
            else:
                return visitor.visitChildren(self)




    def comment(self):

        localctx = pruebaParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_comment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(pruebaParser.T__7)
            self.state = 64
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 61
                    _la = self._input.LA(1)
                    if _la <= 0 or _la==9:
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 66
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 67
            self.match(pruebaParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





