# Generated from C:/Users/Florian/Downloads/InterpreteILP/InterpreteILP/algoritmia.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .algoritmiaParser import algoritmiaParser
else:
    from algoritmiaParser import algoritmiaParser

# This class defines a complete generic visitor for a parse tree produced by algoritmiaParser.

class algoritmiaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by algoritmiaParser#programa.
    def visitPrograma(self, ctx:algoritmiaParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by algoritmiaParser#procedimiento.
    def visitProcedimiento(self, ctx:algoritmiaParser.ProcedimientoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by algoritmiaParser#bloque.
    def visitBloque(self, ctx:algoritmiaParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by algoritmiaParser#instruccion.
    def visitInstruccion(self, ctx:algoritmiaParser.InstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by algoritmiaParser#reproduccion.
    def visitReproduccion(self, ctx:algoritmiaParser.ReproduccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by algoritmiaParser#lectura.
    def visitLectura(self, ctx:algoritmiaParser.LecturaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by algoritmiaParser#asignacion.
    def visitAsignacion(self, ctx:algoritmiaParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by algoritmiaParser#lista.
    def visitLista(self, ctx:algoritmiaParser.ListaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by algoritmiaParser#escritura.
    def visitEscritura(self, ctx:algoritmiaParser.EscrituraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by algoritmiaParser#condicional.
    def visitCondicional(self, ctx:algoritmiaParser.CondicionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by algoritmiaParser#while.
    def visitWhile(self, ctx:algoritmiaParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by algoritmiaParser#invocacion.
    def visitInvocacion(self, ctx:algoritmiaParser.InvocacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by algoritmiaParser#comparator.
    def visitComparator(self, ctx:algoritmiaParser.ComparatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by algoritmiaParser#adicionLista.
    def visitAdicionLista(self, ctx:algoritmiaParser.AdicionListaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by algoritmiaParser#eliminacionLista.
    def visitEliminacionLista(self, ctx:algoritmiaParser.EliminacionListaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by algoritmiaParser#expresion.
    def visitExpresion(self, ctx:algoritmiaParser.ExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by algoritmiaParser#termino.
    def visitTermino(self, ctx:algoritmiaParser.TerminoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by algoritmiaParser#factor.
    def visitFactor(self, ctx:algoritmiaParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by algoritmiaParser#comentario.
    def visitComentario(self, ctx:algoritmiaParser.ComentarioContext):
        return self.visitChildren(ctx)



del algoritmiaParser