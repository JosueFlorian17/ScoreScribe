# Generated from C:/Users/josen/PycharmProjects/pythonProject2/prueba.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .pruebaParser import pruebaParser
else:
    from pruebaParser import pruebaParser

# This class defines a complete generic visitor for a parse tree produced by pruebaParser.

class pruebaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by pruebaParser#prog.
    def visitProg(self, ctx:pruebaParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#procedure.
    def visitProcedure(self, ctx:pruebaParser.ProcedureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#block.
    def visitBlock(self, ctx:pruebaParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#statement.
    def visitStatement(self, ctx:pruebaParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#writeStatement.
    def visitWriteStatement(self, ctx:pruebaParser.WriteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#variableAssignment.
    def visitVariableAssignment(self, ctx:pruebaParser.VariableAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#musicalNote.
    def visitMusicalNote(self, ctx:pruebaParser.MusicalNoteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#section.
    def visitSection(self, ctx:pruebaParser.SectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pruebaParser#comment.
    def visitComment(self, ctx:pruebaParser.CommentContext):
        return self.visitChildren(ctx)



del pruebaParser