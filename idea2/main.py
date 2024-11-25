from antlr4 import *
from gen.pruebaLexer import pruebaLexer
from gen.pruebaParser import pruebaParser
from gen.pruebaVisitor import pruebaVisitor


class MyLanguageVisitor(pruebaVisitor):
    def visitWriteStatement(self, ctx):
        # Imprimir el texto de la cadena dentro de <w>
        print(ctx.STRING().getText().strip('"'))
        return None  # No devolver nada, solo realizar la acción

    def visitVariableAssignment(self, ctx):
        # Asegurarnos de que el identificador es el primero de la lista
        var_name = ctx.ID_MIN()[0].getText()  # Accedemos al primer identificador
        value = ctx.STRING() if ctx.STRING() else ctx.INT()

        # Mostrar el valor de la asignación
        print(f"Asigna la variable {var_name} con valor {value.getText()}")
        return None

    def visitMusicalNote(self, ctx):
        # Imprimir la nota musical
        print(f"Nota musical: {ctx.ID_CAP().getText()}")
        return None


def main():
    # Aquí puedes cargar el código desde un archivo o directamente desde una cadena
    code = '''Main |:
        <w> "Hello Algoritmia"
        a = "Nota inicial"
        A C D
        ### Este es un comentario ###
        (:){A B C}
    :|'''

    # Crear un stream de entrada de la cadena de código
    input_stream = InputStream(code)

    # Crear el lexer y el parser
    lexer = pruebaLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = pruebaParser(token_stream)

    # Parsear el código a partir de la regla 'prog' (tu regla principal)
    tree = parser.prog()

    # Crear el visitante y recorrer el árbol de análisis
    visitor = MyLanguageVisitor()
    visitor.visit(tree)


if __name__ == '__main__':
    main()