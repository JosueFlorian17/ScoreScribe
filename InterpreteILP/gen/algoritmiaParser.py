# Generated from C:/Users/Florian/Downloads/InterpreteILP/InterpreteILP/algoritmia.g4 by ANTLR 4.13.1
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
        4,1,35,200,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,1,0,5,0,41,
        8,0,10,0,12,0,44,9,0,1,0,1,0,1,1,1,1,5,1,50,8,1,10,1,12,1,53,9,1,
        1,1,1,1,1,1,1,1,1,2,5,2,60,8,2,10,2,12,2,63,9,2,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,76,8,3,1,4,1,4,1,4,3,4,81,8,4,1,
        5,1,5,1,5,1,6,1,6,1,6,1,6,3,6,90,8,6,1,7,1,7,1,7,3,7,95,8,7,1,7,
        5,7,98,8,7,10,7,12,7,101,9,7,3,7,103,8,7,1,7,1,7,1,8,1,8,1,8,1,8,
        5,8,111,8,8,10,8,12,8,114,9,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,3,9,128,8,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,11,1,11,5,11,140,8,11,10,11,12,11,143,9,11,1,12,1,12,1,13,1,13,
        1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,5,15,160,
        8,15,10,15,12,15,163,9,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,3,15,
        172,8,15,1,16,1,16,1,16,5,16,177,8,16,10,16,12,16,180,9,16,1,17,
        1,17,1,17,1,17,1,17,1,17,1,17,3,17,189,8,17,1,18,1,18,5,18,193,8,
        18,10,18,12,18,196,9,18,1,18,1,18,1,18,0,0,19,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,36,0,4,1,0,12,17,1,0,22,23,1,0,25,
        27,1,0,24,24,212,0,42,1,0,0,0,2,47,1,0,0,0,4,61,1,0,0,0,6,75,1,0,
        0,0,8,77,1,0,0,0,10,82,1,0,0,0,12,85,1,0,0,0,14,91,1,0,0,0,16,106,
        1,0,0,0,18,115,1,0,0,0,20,129,1,0,0,0,22,137,1,0,0,0,24,144,1,0,
        0,0,26,146,1,0,0,0,28,150,1,0,0,0,30,171,1,0,0,0,32,173,1,0,0,0,
        34,188,1,0,0,0,36,190,1,0,0,0,38,41,3,2,1,0,39,41,3,36,18,0,40,38,
        1,0,0,0,40,39,1,0,0,0,41,44,1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,0,
        43,45,1,0,0,0,44,42,1,0,0,0,45,46,5,0,0,1,46,1,1,0,0,0,47,51,5,31,
        0,0,48,50,5,32,0,0,49,48,1,0,0,0,50,53,1,0,0,0,51,49,1,0,0,0,51,
        52,1,0,0,0,52,54,1,0,0,0,53,51,1,0,0,0,54,55,5,1,0,0,55,56,3,4,2,
        0,56,57,5,2,0,0,57,3,1,0,0,0,58,60,3,6,3,0,59,58,1,0,0,0,60,63,1,
        0,0,0,61,59,1,0,0,0,61,62,1,0,0,0,62,5,1,0,0,0,63,61,1,0,0,0,64,
        76,3,10,5,0,65,76,3,12,6,0,66,76,3,16,8,0,67,76,3,18,9,0,68,76,3,
        20,10,0,69,76,3,22,11,0,70,76,3,8,4,0,71,76,3,30,15,0,72,76,3,26,
        13,0,73,76,3,28,14,0,74,76,3,36,18,0,75,64,1,0,0,0,75,65,1,0,0,0,
        75,66,1,0,0,0,75,67,1,0,0,0,75,68,1,0,0,0,75,69,1,0,0,0,75,70,1,
        0,0,0,75,71,1,0,0,0,75,72,1,0,0,0,75,73,1,0,0,0,75,74,1,0,0,0,76,
        7,1,0,0,0,77,80,5,3,0,0,78,81,3,30,15,0,79,81,3,14,7,0,80,78,1,0,
        0,0,80,79,1,0,0,0,81,9,1,0,0,0,82,83,5,4,0,0,83,84,5,32,0,0,84,11,
        1,0,0,0,85,86,5,32,0,0,86,89,5,5,0,0,87,90,3,30,15,0,88,90,3,14,
        7,0,89,87,1,0,0,0,89,88,1,0,0,0,90,13,1,0,0,0,91,102,5,6,0,0,92,
        99,3,30,15,0,93,95,5,35,0,0,94,93,1,0,0,0,94,95,1,0,0,0,95,96,1,
        0,0,0,96,98,3,30,15,0,97,94,1,0,0,0,98,101,1,0,0,0,99,97,1,0,0,0,
        99,100,1,0,0,0,100,103,1,0,0,0,101,99,1,0,0,0,102,92,1,0,0,0,102,
        103,1,0,0,0,103,104,1,0,0,0,104,105,5,7,0,0,105,15,1,0,0,0,106,112,
        5,8,0,0,107,111,3,30,15,0,108,111,5,33,0,0,109,111,5,32,0,0,110,
        107,1,0,0,0,110,108,1,0,0,0,110,109,1,0,0,0,111,114,1,0,0,0,112,
        110,1,0,0,0,112,113,1,0,0,0,113,17,1,0,0,0,114,112,1,0,0,0,115,116,
        5,9,0,0,116,117,3,30,15,0,117,118,3,24,12,0,118,119,3,30,15,0,119,
        120,5,1,0,0,120,121,3,4,2,0,121,127,5,2,0,0,122,123,5,10,0,0,123,
        124,5,1,0,0,124,125,3,4,2,0,125,126,5,2,0,0,126,128,1,0,0,0,127,
        122,1,0,0,0,127,128,1,0,0,0,128,19,1,0,0,0,129,130,5,11,0,0,130,
        131,3,30,15,0,131,132,3,24,12,0,132,133,3,30,15,0,133,134,5,1,0,
        0,134,135,3,4,2,0,135,136,5,2,0,0,136,21,1,0,0,0,137,141,5,31,0,
        0,138,140,5,32,0,0,139,138,1,0,0,0,140,143,1,0,0,0,141,139,1,0,0,
        0,141,142,1,0,0,0,142,23,1,0,0,0,143,141,1,0,0,0,144,145,7,0,0,0,
        145,25,1,0,0,0,146,147,5,32,0,0,147,148,5,18,0,0,148,149,3,30,15,
        0,149,27,1,0,0,0,150,151,5,19,0,0,151,152,5,32,0,0,152,153,5,20,
        0,0,153,154,3,30,15,0,154,155,5,21,0,0,155,29,1,0,0,0,156,161,3,
        32,16,0,157,158,7,1,0,0,158,160,3,32,16,0,159,157,1,0,0,0,160,163,
        1,0,0,0,161,159,1,0,0,0,161,162,1,0,0,0,162,172,1,0,0,0,163,161,
        1,0,0,0,164,165,5,24,0,0,165,172,5,32,0,0,166,167,5,32,0,0,167,168,
        5,20,0,0,168,169,3,30,15,0,169,170,5,21,0,0,170,172,1,0,0,0,171,
        156,1,0,0,0,171,164,1,0,0,0,171,166,1,0,0,0,172,31,1,0,0,0,173,178,
        3,34,17,0,174,175,7,2,0,0,175,177,3,34,17,0,176,174,1,0,0,0,177,
        180,1,0,0,0,178,176,1,0,0,0,178,179,1,0,0,0,179,33,1,0,0,0,180,178,
        1,0,0,0,181,189,5,32,0,0,182,189,5,31,0,0,183,189,5,34,0,0,184,185,
        5,28,0,0,185,186,3,30,15,0,186,187,5,29,0,0,187,189,1,0,0,0,188,
        181,1,0,0,0,188,182,1,0,0,0,188,183,1,0,0,0,188,184,1,0,0,0,189,
        35,1,0,0,0,190,194,5,30,0,0,191,193,8,3,0,0,192,191,1,0,0,0,193,
        196,1,0,0,0,194,192,1,0,0,0,194,195,1,0,0,0,195,197,1,0,0,0,196,
        194,1,0,0,0,197,198,5,30,0,0,198,37,1,0,0,0,19,40,42,51,61,75,80,
        89,94,99,102,110,112,127,141,161,171,178,188,194
    ]

class algoritmiaParser ( Parser ):

    grammarFileName = "algoritmia.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'|:'", "':|'", "'(:)'", "'<?>'", "'<-'", 
                     "'{'", "'}'", "'<w>'", "'if'", "'else'", "'while'", 
                     "'='", "'<'", "'>'", "'<='", "'>='", "'/='", "'<<'", 
                     "'8<'", "'['", "']'", "'+'", "'-'", "'#'", "'*'", "'/'", 
                     "'%'", "'('", "')'", "'###'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID_CAP", "ID_MIN", 
                      "STRING", "INT", "WS" ]

    RULE_programa = 0
    RULE_procedimiento = 1
    RULE_bloque = 2
    RULE_instruccion = 3
    RULE_reproduccion = 4
    RULE_lectura = 5
    RULE_asignacion = 6
    RULE_lista = 7
    RULE_escritura = 8
    RULE_condicional = 9
    RULE_while = 10
    RULE_invocacion = 11
    RULE_comparator = 12
    RULE_adicionLista = 13
    RULE_eliminacionLista = 14
    RULE_expresion = 15
    RULE_termino = 16
    RULE_factor = 17
    RULE_comentario = 18

    ruleNames =  [ "programa", "procedimiento", "bloque", "instruccion", 
                   "reproduccion", "lectura", "asignacion", "lista", "escritura", 
                   "condicional", "while", "invocacion", "comparator", "adicionLista", 
                   "eliminacionLista", "expresion", "termino", "factor", 
                   "comentario" ]

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
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    ID_CAP=31
    ID_MIN=32
    STRING=33
    INT=34
    WS=35

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(algoritmiaParser.EOF, 0)

        def procedimiento(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(algoritmiaParser.ProcedimientoContext)
            else:
                return self.getTypedRuleContext(algoritmiaParser.ProcedimientoContext,i)


        def comentario(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(algoritmiaParser.ComentarioContext)
            else:
                return self.getTypedRuleContext(algoritmiaParser.ComentarioContext,i)


        def getRuleIndex(self):
            return algoritmiaParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = algoritmiaParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30 or _la==31:
                self.state = 40
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [31]:
                    self.state = 38
                    self.procedimiento()
                    pass
                elif token in [30]:
                    self.state = 39
                    self.comentario()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 45
            self.match(algoritmiaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProcedimientoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID_CAP(self):
            return self.getToken(algoritmiaParser.ID_CAP, 0)

        def bloque(self):
            return self.getTypedRuleContext(algoritmiaParser.BloqueContext,0)


        def ID_MIN(self, i:int=None):
            if i is None:
                return self.getTokens(algoritmiaParser.ID_MIN)
            else:
                return self.getToken(algoritmiaParser.ID_MIN, i)

        def getRuleIndex(self):
            return algoritmiaParser.RULE_procedimiento

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProcedimiento" ):
                listener.enterProcedimiento(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProcedimiento" ):
                listener.exitProcedimiento(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcedimiento" ):
                return visitor.visitProcedimiento(self)
            else:
                return visitor.visitChildren(self)




    def procedimiento(self):

        localctx = algoritmiaParser.ProcedimientoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_procedimiento)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(algoritmiaParser.ID_CAP)
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==32:
                self.state = 48
                self.match(algoritmiaParser.ID_MIN)
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 54
            self.match(algoritmiaParser.T__0)
            self.state = 55
            self.bloque()
            self.state = 56
            self.match(algoritmiaParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BloqueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruccion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(algoritmiaParser.InstruccionContext)
            else:
                return self.getTypedRuleContext(algoritmiaParser.InstruccionContext,i)


        def getRuleIndex(self):
            return algoritmiaParser.RULE_bloque

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloque" ):
                listener.enterBloque(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloque" ):
                listener.exitBloque(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloque" ):
                return visitor.visitBloque(self)
            else:
                return visitor.visitChildren(self)




    def bloque(self):

        localctx = algoritmiaParser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_bloque)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 24981801752) != 0):
                self.state = 58
                self.instruccion()
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lectura(self):
            return self.getTypedRuleContext(algoritmiaParser.LecturaContext,0)


        def asignacion(self):
            return self.getTypedRuleContext(algoritmiaParser.AsignacionContext,0)


        def escritura(self):
            return self.getTypedRuleContext(algoritmiaParser.EscrituraContext,0)


        def condicional(self):
            return self.getTypedRuleContext(algoritmiaParser.CondicionalContext,0)


        def while_(self):
            return self.getTypedRuleContext(algoritmiaParser.WhileContext,0)


        def invocacion(self):
            return self.getTypedRuleContext(algoritmiaParser.InvocacionContext,0)


        def reproduccion(self):
            return self.getTypedRuleContext(algoritmiaParser.ReproduccionContext,0)


        def expresion(self):
            return self.getTypedRuleContext(algoritmiaParser.ExpresionContext,0)


        def adicionLista(self):
            return self.getTypedRuleContext(algoritmiaParser.AdicionListaContext,0)


        def eliminacionLista(self):
            return self.getTypedRuleContext(algoritmiaParser.EliminacionListaContext,0)


        def comentario(self):
            return self.getTypedRuleContext(algoritmiaParser.ComentarioContext,0)


        def getRuleIndex(self):
            return algoritmiaParser.RULE_instruccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruccion" ):
                listener.enterInstruccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruccion" ):
                listener.exitInstruccion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccion" ):
                return visitor.visitInstruccion(self)
            else:
                return visitor.visitChildren(self)




    def instruccion(self):

        localctx = algoritmiaParser.InstruccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_instruccion)
        try:
            self.state = 75
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.lectura()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.asignacion()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 66
                self.escritura()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 67
                self.condicional()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 68
                self.while_()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 69
                self.invocacion()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 70
                self.reproduccion()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 71
                self.expresion()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 72
                self.adicionLista()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 73
                self.eliminacionLista()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 74
                self.comentario()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReproduccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(algoritmiaParser.ExpresionContext,0)


        def lista(self):
            return self.getTypedRuleContext(algoritmiaParser.ListaContext,0)


        def getRuleIndex(self):
            return algoritmiaParser.RULE_reproduccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReproduccion" ):
                listener.enterReproduccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReproduccion" ):
                listener.exitReproduccion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReproduccion" ):
                return visitor.visitReproduccion(self)
            else:
                return visitor.visitChildren(self)




    def reproduccion(self):

        localctx = algoritmiaParser.ReproduccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_reproduccion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(algoritmiaParser.T__2)
            self.state = 80
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24, 28, 31, 32, 34]:
                self.state = 78
                self.expresion()
                pass
            elif token in [6]:
                self.state = 79
                self.lista()
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


    class LecturaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID_MIN(self):
            return self.getToken(algoritmiaParser.ID_MIN, 0)

        def getRuleIndex(self):
            return algoritmiaParser.RULE_lectura

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLectura" ):
                listener.enterLectura(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLectura" ):
                listener.exitLectura(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLectura" ):
                return visitor.visitLectura(self)
            else:
                return visitor.visitChildren(self)




    def lectura(self):

        localctx = algoritmiaParser.LecturaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_lectura)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(algoritmiaParser.T__3)
            self.state = 83
            self.match(algoritmiaParser.ID_MIN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID_MIN(self):
            return self.getToken(algoritmiaParser.ID_MIN, 0)

        def expresion(self):
            return self.getTypedRuleContext(algoritmiaParser.ExpresionContext,0)


        def lista(self):
            return self.getTypedRuleContext(algoritmiaParser.ListaContext,0)


        def getRuleIndex(self):
            return algoritmiaParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def asignacion(self):

        localctx = algoritmiaParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(algoritmiaParser.ID_MIN)
            self.state = 86
            self.match(algoritmiaParser.T__4)
            self.state = 89
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24, 28, 31, 32, 34]:
                self.state = 87
                self.expresion()
                pass
            elif token in [6]:
                self.state = 88
                self.lista()
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


    class ListaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(algoritmiaParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(algoritmiaParser.ExpresionContext,i)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(algoritmiaParser.WS)
            else:
                return self.getToken(algoritmiaParser.WS, i)

        def getRuleIndex(self):
            return algoritmiaParser.RULE_lista

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLista" ):
                listener.enterLista(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLista" ):
                listener.exitLista(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLista" ):
                return visitor.visitLista(self)
            else:
                return visitor.visitChildren(self)




    def lista(self):

        localctx = algoritmiaParser.ListaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_lista)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(algoritmiaParser.T__5)
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 23907532800) != 0):
                self.state = 92
                self.expresion()
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 58267271168) != 0):
                    self.state = 94
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==35:
                        self.state = 93
                        self.match(algoritmiaParser.WS)


                    self.state = 96
                    self.expresion()
                    self.state = 101
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 104
            self.match(algoritmiaParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EscrituraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(algoritmiaParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(algoritmiaParser.ExpresionContext,i)


        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(algoritmiaParser.STRING)
            else:
                return self.getToken(algoritmiaParser.STRING, i)

        def ID_MIN(self, i:int=None):
            if i is None:
                return self.getTokens(algoritmiaParser.ID_MIN)
            else:
                return self.getToken(algoritmiaParser.ID_MIN, i)

        def getRuleIndex(self):
            return algoritmiaParser.RULE_escritura

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEscritura" ):
                listener.enterEscritura(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEscritura" ):
                listener.exitEscritura(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEscritura" ):
                return visitor.visitEscritura(self)
            else:
                return visitor.visitChildren(self)




    def escritura(self):

        localctx = algoritmiaParser.EscrituraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_escritura)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(algoritmiaParser.T__7)
            self.state = 112
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 110
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        self.state = 107
                        self.expresion()
                        pass

                    elif la_ == 2:
                        self.state = 108
                        self.match(algoritmiaParser.STRING)
                        pass

                    elif la_ == 3:
                        self.state = 109
                        self.match(algoritmiaParser.ID_MIN)
                        pass

             
                self.state = 114
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(algoritmiaParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(algoritmiaParser.ExpresionContext,i)


        def comparator(self):
            return self.getTypedRuleContext(algoritmiaParser.ComparatorContext,0)


        def bloque(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(algoritmiaParser.BloqueContext)
            else:
                return self.getTypedRuleContext(algoritmiaParser.BloqueContext,i)


        def getRuleIndex(self):
            return algoritmiaParser.RULE_condicional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicional" ):
                listener.enterCondicional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicional" ):
                listener.exitCondicional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicional" ):
                return visitor.visitCondicional(self)
            else:
                return visitor.visitChildren(self)




    def condicional(self):

        localctx = algoritmiaParser.CondicionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_condicional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(algoritmiaParser.T__8)
            self.state = 116
            self.expresion()
            self.state = 117
            self.comparator()
            self.state = 118
            self.expresion()
            self.state = 119
            self.match(algoritmiaParser.T__0)
            self.state = 120
            self.bloque()
            self.state = 121
            self.match(algoritmiaParser.T__1)
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 122
                self.match(algoritmiaParser.T__9)
                self.state = 123
                self.match(algoritmiaParser.T__0)
                self.state = 124
                self.bloque()
                self.state = 125
                self.match(algoritmiaParser.T__1)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(algoritmiaParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(algoritmiaParser.ExpresionContext,i)


        def comparator(self):
            return self.getTypedRuleContext(algoritmiaParser.ComparatorContext,0)


        def bloque(self):
            return self.getTypedRuleContext(algoritmiaParser.BloqueContext,0)


        def getRuleIndex(self):
            return algoritmiaParser.RULE_while

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile" ):
                listener.enterWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile" ):
                listener.exitWhile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile" ):
                return visitor.visitWhile(self)
            else:
                return visitor.visitChildren(self)




    def while_(self):

        localctx = algoritmiaParser.WhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_while)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(algoritmiaParser.T__10)
            self.state = 130
            self.expresion()
            self.state = 131
            self.comparator()
            self.state = 132
            self.expresion()
            self.state = 133
            self.match(algoritmiaParser.T__0)
            self.state = 134
            self.bloque()
            self.state = 135
            self.match(algoritmiaParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InvocacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID_CAP(self):
            return self.getToken(algoritmiaParser.ID_CAP, 0)

        def ID_MIN(self, i:int=None):
            if i is None:
                return self.getTokens(algoritmiaParser.ID_MIN)
            else:
                return self.getToken(algoritmiaParser.ID_MIN, i)

        def getRuleIndex(self):
            return algoritmiaParser.RULE_invocacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInvocacion" ):
                listener.enterInvocacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInvocacion" ):
                listener.exitInvocacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInvocacion" ):
                return visitor.visitInvocacion(self)
            else:
                return visitor.visitChildren(self)




    def invocacion(self):

        localctx = algoritmiaParser.InvocacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_invocacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(algoritmiaParser.ID_CAP)
            self.state = 141
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 138
                    self.match(algoritmiaParser.ID_MIN) 
                self.state = 143
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return algoritmiaParser.RULE_comparator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparator" ):
                listener.enterComparator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparator" ):
                listener.exitComparator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparator" ):
                return visitor.visitComparator(self)
            else:
                return visitor.visitChildren(self)




    def comparator(self):

        localctx = algoritmiaParser.ComparatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_comparator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 258048) != 0)):
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


    class AdicionListaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID_MIN(self):
            return self.getToken(algoritmiaParser.ID_MIN, 0)

        def expresion(self):
            return self.getTypedRuleContext(algoritmiaParser.ExpresionContext,0)


        def getRuleIndex(self):
            return algoritmiaParser.RULE_adicionLista

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdicionLista" ):
                listener.enterAdicionLista(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdicionLista" ):
                listener.exitAdicionLista(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdicionLista" ):
                return visitor.visitAdicionLista(self)
            else:
                return visitor.visitChildren(self)




    def adicionLista(self):

        localctx = algoritmiaParser.AdicionListaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_adicionLista)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(algoritmiaParser.ID_MIN)
            self.state = 147
            self.match(algoritmiaParser.T__17)
            self.state = 148
            self.expresion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EliminacionListaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID_MIN(self):
            return self.getToken(algoritmiaParser.ID_MIN, 0)

        def expresion(self):
            return self.getTypedRuleContext(algoritmiaParser.ExpresionContext,0)


        def getRuleIndex(self):
            return algoritmiaParser.RULE_eliminacionLista

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEliminacionLista" ):
                listener.enterEliminacionLista(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEliminacionLista" ):
                listener.exitEliminacionLista(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEliminacionLista" ):
                return visitor.visitEliminacionLista(self)
            else:
                return visitor.visitChildren(self)




    def eliminacionLista(self):

        localctx = algoritmiaParser.EliminacionListaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_eliminacionLista)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(algoritmiaParser.T__18)
            self.state = 151
            self.match(algoritmiaParser.ID_MIN)
            self.state = 152
            self.match(algoritmiaParser.T__19)
            self.state = 153
            self.expresion()
            self.state = 154
            self.match(algoritmiaParser.T__20)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termino(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(algoritmiaParser.TerminoContext)
            else:
                return self.getTypedRuleContext(algoritmiaParser.TerminoContext,i)


        def ID_MIN(self):
            return self.getToken(algoritmiaParser.ID_MIN, 0)

        def expresion(self):
            return self.getTypedRuleContext(algoritmiaParser.ExpresionContext,0)


        def getRuleIndex(self):
            return algoritmiaParser.RULE_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion" ):
                listener.enterExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion" ):
                listener.exitExpresion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresion" ):
                return visitor.visitExpresion(self)
            else:
                return visitor.visitChildren(self)




    def expresion(self):

        localctx = algoritmiaParser.ExpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expresion)
        self._la = 0 # Token type
        try:
            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.termino()
                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==22 or _la==23:
                    self.state = 157
                    _la = self._input.LA(1)
                    if not(_la==22 or _la==23):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 158
                    self.termino()
                    self.state = 163
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                self.match(algoritmiaParser.T__23)
                self.state = 165
                self.match(algoritmiaParser.ID_MIN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 166
                self.match(algoritmiaParser.ID_MIN)
                self.state = 167
                self.match(algoritmiaParser.T__19)
                self.state = 168
                self.expresion()
                self.state = 169
                self.match(algoritmiaParser.T__20)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TerminoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(algoritmiaParser.FactorContext)
            else:
                return self.getTypedRuleContext(algoritmiaParser.FactorContext,i)


        def getRuleIndex(self):
            return algoritmiaParser.RULE_termino

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermino" ):
                listener.enterTermino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermino" ):
                listener.exitTermino(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermino" ):
                return visitor.visitTermino(self)
            else:
                return visitor.visitChildren(self)




    def termino(self):

        localctx = algoritmiaParser.TerminoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_termino)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.factor()
            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 234881024) != 0):
                self.state = 174
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 234881024) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 175
                self.factor()
                self.state = 180
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID_MIN(self):
            return self.getToken(algoritmiaParser.ID_MIN, 0)

        def ID_CAP(self):
            return self.getToken(algoritmiaParser.ID_CAP, 0)

        def INT(self):
            return self.getToken(algoritmiaParser.INT, 0)

        def expresion(self):
            return self.getTypedRuleContext(algoritmiaParser.ExpresionContext,0)


        def getRuleIndex(self):
            return algoritmiaParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = algoritmiaParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_factor)
        try:
            self.state = 188
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.match(algoritmiaParser.ID_MIN)
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 182
                self.match(algoritmiaParser.ID_CAP)
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 3)
                self.state = 183
                self.match(algoritmiaParser.INT)
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 4)
                self.state = 184
                self.match(algoritmiaParser.T__27)
                self.state = 185
                self.expresion()
                self.state = 186
                self.match(algoritmiaParser.T__28)
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


    class ComentarioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return algoritmiaParser.RULE_comentario

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComentario" ):
                listener.enterComentario(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComentario" ):
                listener.exitComentario(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComentario" ):
                return visitor.visitComentario(self)
            else:
                return visitor.visitChildren(self)




    def comentario(self):

        localctx = algoritmiaParser.ComentarioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_comentario)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(algoritmiaParser.T__29)
            self.state = 194
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 191
                    _la = self._input.LA(1)
                    if _la <= 0 or _la==24:
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 196
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

            self.state = 197
            self.match(algoritmiaParser.T__29)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





