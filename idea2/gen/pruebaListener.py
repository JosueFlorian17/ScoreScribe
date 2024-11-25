# Generated from C:/Users/josen/PycharmProjects/pythonProject2/prueba.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .pruebaParser import pruebaParser
else:
    from pruebaParser import pruebaParser

# This class defines a complete listener for a parse tree produced by pruebaParser.
class pruebaListener(ParseTreeListener):

    # Enter a parse tree produced by pruebaParser#prog.
    def enterProg(self, ctx:pruebaParser.ProgContext):
        pass

    # Exit a parse tree produced by pruebaParser#prog.
    def exitProg(self, ctx:pruebaParser.ProgContext):
        pass


    # Enter a parse tree produced by pruebaParser#procedure.
    def enterProcedure(self, ctx:pruebaParser.ProcedureContext):
        pass

    # Exit a parse tree produced by pruebaParser#procedure.
    def exitProcedure(self, ctx:pruebaParser.ProcedureContext):
        pass


    # Enter a parse tree produced by pruebaParser#block.
    def enterBlock(self, ctx:pruebaParser.BlockContext):
        pass

    # Exit a parse tree produced by pruebaParser#block.
    def exitBlock(self, ctx:pruebaParser.BlockContext):
        pass


    # Enter a parse tree produced by pruebaParser#statement.
    def enterStatement(self, ctx:pruebaParser.StatementContext):
        pass

    # Exit a parse tree produced by pruebaParser#statement.
    def exitStatement(self, ctx:pruebaParser.StatementContext):
        pass


    # Enter a parse tree produced by pruebaParser#writeStatement.
    def enterWriteStatement(self, ctx:pruebaParser.WriteStatementContext):
        pass

    # Exit a parse tree produced by pruebaParser#writeStatement.
    def exitWriteStatement(self, ctx:pruebaParser.WriteStatementContext):
        pass


    # Enter a parse tree produced by pruebaParser#variableAssignment.
    def enterVariableAssignment(self, ctx:pruebaParser.VariableAssignmentContext):
        pass

    # Exit a parse tree produced by pruebaParser#variableAssignment.
    def exitVariableAssignment(self, ctx:pruebaParser.VariableAssignmentContext):
        pass


    # Enter a parse tree produced by pruebaParser#musicalNote.
    def enterMusicalNote(self, ctx:pruebaParser.MusicalNoteContext):
        pass

    # Exit a parse tree produced by pruebaParser#musicalNote.
    def exitMusicalNote(self, ctx:pruebaParser.MusicalNoteContext):
        pass


    # Enter a parse tree produced by pruebaParser#section.
    def enterSection(self, ctx:pruebaParser.SectionContext):
        pass

    # Exit a parse tree produced by pruebaParser#section.
    def exitSection(self, ctx:pruebaParser.SectionContext):
        pass


    # Enter a parse tree produced by pruebaParser#comment.
    def enterComment(self, ctx:pruebaParser.CommentContext):
        pass

    # Exit a parse tree produced by pruebaParser#comment.
    def exitComment(self, ctx:pruebaParser.CommentContext):
        pass



del pruebaParser