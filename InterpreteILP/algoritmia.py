import sys
from antlr4 import *
from gen.algoritmiaLexer import algoritmiaLexer
from gen.algoritmiaParser import algoritmiaParser
from gen.algoritmiaVisitor import algoritmiaVisitor
import os
from converter import create_lilypond_file

class AlgoritmiaInterpreter(algoritmiaVisitor):
    def __init__(self):
        self.variables = {}
        self.procedures = {}  # Diccionario para almacenar los procedimientos definidos

        self.notas = {
            'A0': 0, 'B0': 1, 'C1': 2, 'D1': 3, 'E1': 4, 'F1': 5, 'G1': 6,
            'A1': 7, 'B1': 8, 'C2': 9, 'D2': 10, 'E2': 11, 'F2': 12, 'G2': 13,
            'A2': 14, 'B2': 15, 'C3': 16, 'D3': 17, 'E3': 18, 'F3': 19, 'G3': 20,
            'A3': 21, 'B3': 22, 'C': 23, 'D': 24, 'E': 25, 'F': 26, 'G': 27,
            'A': 28, 'B': 29, 'C5': 30, 'D5': 31, 'E5': 32, 'F5': 33, 'G5': 34,
            'A5': 35, 'B5': 36, 'C6': 37, 'D6': 38, 'E6': 39, 'F6': 40, 'G6': 41,
            'A6': 42, 'B6': 43, 'C7': 44, 'D7': 45, 'E7': 46, 'F7': 47, 'G7': 48,
            'A7': 49, 'B7': 50, 'C8': 51
        }

        # Partitura para almacenar las notas
        self.partitura = {}

    def visitLectura(self, ctx):
        # Leer el valor de la entrada estándar y almacenarlo en la variable
        var_name = ctx.ID_MIN().getText()  # Obtener el nombre de la variable
        value = int(input(f"Enter an integer for {var_name}: "))  # Leer el valor desde el usuario
        self.variables[var_name] = value  # Almacenar el valor en la variable
        print(f"Value for {var_name}: {value}")  # Imprimir el valor almacenado para verificar

    def convertir_numero_a_nota(self, numero):
        notas = {
            0: 'A0', 1: 'B0', 2: 'C1', 3: 'D1', 4: 'E1', 5: 'F1', 6: 'G1',
            7: 'A1', 8: 'B1', 9: 'C2', 10: 'D2', 11: 'E2', 12: 'F2', 13: 'G2',
            14: 'A2', 15: 'B2', 16: 'C3', 17: 'D3', 18: 'E3', 19: 'F3', 20: 'G3',
            21: 'A3', 22: 'B3', 23: 'C', 24: 'D', 25: 'E', 26: 'F', 27: 'G',
            28: 'A', 29: 'B', 30: 'C5', 31: 'D5', 32: 'E5', 33: 'F5', 34: 'G5',
            35: 'A5', 36: 'B5', 37: 'C6', 38: 'D6', 39: 'E6', 40: 'F6', 41: 'G6',
            42: 'A6', 43: 'B6', 44: 'C7', 45: 'D7', 46: 'E7', 47: 'F7', 48: 'G7',
            49: 'A7', 50: 'B7', 51: 'C8'
        }
        return notas.get(numero, "Nota no válida")

    def visitReproduccion(self, ctx):
        # Lista para almacenar las notas que se reproducen
        notas_reproducidas = []
        # Si el contexto tiene una lista, la procesamos
        if ctx.lista():
            lista_de_notas = self.visit(ctx.lista())  # Evaluamos la lista explícita
            for nota in lista_de_notas:
                self.reproducir_nota(nota, notas_reproducidas)  # Reproducimos cada nota de la lista
        else:
            # Si no es una lista explícita, debemos verificar si es una variable
            nota_o_variable = self.visit(
                ctx.expresion())  # Obtenemos el valor de la expresión (puede ser variable o valor)

            # Verificamos si la expresión es una variable que contiene una lista
            if isinstance(nota_o_variable, list):  # Si es una lista, la procesamos
                for nota in nota_o_variable:
                    self.reproducir_nota(nota, notas_reproducidas)  # Reproducimos cada nota de la lista
            else:
                self.reproducir_nota(nota_o_variable, notas_reproducidas)  # Si no es lista, reproducimos la nota individual

        self.mostrar_partitura(notas_reproducidas)

    def reproducir_nota(self, nota, notas_reproducidas):
        # Verificamos si es un número, lo convertimos a una nota
        if isinstance(nota, int):  # Si es un número, lo convertimos a la nota correspondiente
            if 0 <= nota <= 51:  # Verificamos que esté en el rango válido
                nota = self.convertir_numero_a_nota(nota)
            else:
                raise ValueError("La nota numérica no es válida.")

        # Verificamos que la nota sea válida
        if nota in self.notas:
            notas_reproducidas.append(nota)
            print(f"Reproduciendo: {nota}")  # Aquí, reproduciríamos la nota
        else:
            raise ValueError("Solo se pueden reproducir notas musicales.")

    def mostrar_partitura(self, notas_reproducidas):
        # Mostramos todas las notas reproducidas en un solo mensaje
        notas_str = " ".join(notas_reproducidas)  # Convertir las notas a una cadena de texto
        print(f"Partitura final: {{{notas_str}}}")
        self.generar_partitura_final(notas_reproducidas)

    def visitAsignacion(self, ctx):
        # Obtener el nombre de la variable de la parte izquierda de la asignación
        var_name = ctx.ID_MIN().getText()

        # Evaluar si estamos asignando una lista
        if ctx.lista():
            # Si es una lista, evaluamos los elementos
            lista_valores = self.visit(ctx.lista())
            self.variables[var_name] = lista_valores
            print(f"Assigned {lista_valores} to {var_name}")  # Imprimir para verificar la asignación
        else:
            # Si no es una lista, evaluamos la expresión
            right_value = self.visit(ctx.expresion())

            # Si la expresión es una nota, la buscamos en el diccionario de notas
            if isinstance(right_value, str) and right_value in self.notas:
                right_value = self.notas[right_value]  # Obtener el valor numérico de la nota

            # Almacenar el valor de la expresión en la variable
            self.variables[var_name] = right_value
            print(f"Assigned {right_value} to {var_name}")  # Imprimir para verificar la asignación

    def visitLista(self, ctx):
        # Evaluar los elementos de la lista
        lista_valores = []
        for expr in ctx.expresion():
            valor = self.visit(expr)
            lista_valores.append(valor)
        return lista_valores

    def visitEscritura(self, ctx: algoritmiaParser.EscrituraContext):
        output = []  # Lista para almacenar los elementos a imprimir

        # Iteramos sobre los hijos del contexto de la instrucción de escritura
        for child in ctx.getChildren():
            if isinstance(child, algoritmiaParser.ExpresionContext):  # Si es una expresión
                result = self.visit(child)  # Evaluamos la expresión
                output.append(str(result))  # Convertimos el resultado a texto y lo agregamos
            elif isinstance(child, TerminalNode) and child.symbol.type == algoritmiaParser.STRING:  # Si es una cadena de texto
                output.append(child.getText().strip('"'))  # Extraemos el texto y lo agregamos al output
            elif isinstance(child, TerminalNode) and child.symbol.type == algoritmiaParser.ID_MIN:  # Si es una variable
                var_name = child.getText()  # Obtenemos el nombre de la variable
                output.append(str(self.variables.get(var_name, "Undefined")))  # Agregamos su valor o "Undefined" si no existe

        # Imprimimos todo en una sola línea, separados por espacios
        print(" ".join(output))

    def evaluar_condicion(self, operador, izq, der):
        # Evaluamos el operador de comparación
        if operador == '=':  # Igual
            return izq == der
        elif operador == '<':  # Menor que
            return izq < der
        elif operador == '>':  # Mayor que
            return izq > der
        elif operador == '<=':  # Menor o igual
            return izq <= der
        elif operador == '>=':  # Mayor o igual
            return izq >= der
        elif operador == '/=':  # Diferente (!=)
            return izq != der
        else:
            raise ValueError(f"Operador desconocido: {operador}")

    def visitCondicional(self, ctx: algoritmiaParser.CondicionalContext):
        # Obtenemos el operador de comparación
        operador = ctx.comparator().getText()

        # Evaluamos la condición
        condicion_izq = self.visit(ctx.expresion(0))  # Lado izquierdo de la condición
        condicion_der = self.visit(ctx.expresion(1))  # Lado derecho de la condición

        if self.evaluar_condicion(operador, condicion_izq, condicion_der):
            print(f"Condición {condicion_izq} {operador} {condicion_der} -> Ejecutando bloque")
            # Ejecutar el bloque del if
            self.visit(ctx.bloque(0))
        elif len(ctx.bloque()) > 1:  # Solo hay bloque del else si hay un "else"
            print(f"Condición {condicion_izq} {operador} {condicion_der} -> Ejecutando bloque else")
            # Ejecutar el bloque del else
            self.visit(ctx.bloque(1))

    def visitWhile(self, ctx: algoritmiaParser.WhileContext):
        # Obtenemos el operador de comparación
        operador = ctx.comparator().getText()

        while True:
            # Evaluamos la condición del while
            condicion_izq = self.visit(ctx.expresion(0))  # Lado izquierdo de la condición
            condicion_der = self.visit(ctx.expresion(1))  # Lado derecho de la condición

            if self.evaluar_condicion(operador, condicion_izq, condicion_der):
                print(f"Condición {condicion_izq} {operador} {condicion_der} -> Ejecutando bloque")
                # Ejecutar el bloque dentro del while
                self.visit(ctx.bloque())
            else:
                print(f"Condición {condicion_izq} {operador} {condicion_der} -> Salir del while")
                break  # Si la condición es falsa, salimos del bucle

    # Función para manejar la operación de agregar un elemento a la lista
    def visitAdicionLista(self, ctx):
        var_name = ctx.ID_MIN().getText()  # Obtener el nombre de la lista
        element = self.visit(ctx.expresion())  # Evaluar el elemento que se quiere agregar

        # Verificar si la variable es una lista
        if var_name in self.variables and isinstance(self.variables[var_name], list):
            self.variables[var_name].append(element)  # Añadir el elemento a la lista
            print(f"Elemento {element} añadido a la lista {var_name}.")
        else:
            print(f"Error: {var_name} no es una lista o no está definida correctamente.")

    # Función para manejar la operación de eliminar el i-ésimo elemento de la lista
    def visitEliminacionLista(self, ctx):
        # Obtener el nombre de la lista y la expresión que representa el índice
        var_name = ctx.ID_MIN().getText()
        index = self.visit(ctx.expresion())  # Evaluar la expresión del índice

        # Verificar si la variable es una lista
        if var_name in self.variables and isinstance(self.variables[var_name], list):
            lista = self.variables[var_name]
            # Verificar que el índice esté en el rango válido
            if 1 <= index <= len(lista):
                # Convertir el índice a índice basado en 0
                del lista[index - 1]  # Eliminar el elemento en la posición dada
                print(f"Elemento en la posición {index} de la lista {var_name} ha sido eliminado.")
            else:
                print(f"Error: Índice {index} fuera del rango válido de la lista {var_name}.")
        else:
            print(f"Error: {var_name} no es una lista o no está definida correctamente.")

    def visitExpresion(self, ctx):
        if ctx.getChildCount() == 2 and ctx.getChild(0).getText() == "#":
            var_name = ctx.ID_MIN().getText()
            if var_name in self.variables and isinstance(self.variables[var_name], list):
                print(f"El tamaño de la lista {var_name} es: {len(self.variables[var_name])}")
                return len(self.variables[var_name])  # Devolver la longitud de la lista
            else:
                print(f"Error: {var_name} no es una lista o no está definida correctamente.")
                return 0  # O retornar un valor por defecto en caso de error

        # Verificar si es una consulta de índice (v[i])
        if ctx.getChildCount() == 4 and ctx.getChild(1).getText() == '[':
            var_name = ctx.ID_MIN().getText()  # Obtener el nombre de la variable
            index = self.visit(ctx.expresion())  # Obtener el índice entre corchetes

            if var_name in self.variables and isinstance(self.variables[var_name], list):
                # Verificar si el índice es válido (1 ≤ i ≤ #v)
                if 1 <= index <= len(self.variables[var_name]):
                    element = self.variables[var_name][index - 1]  # Consultar el i-ésimo elemento (ajustado a índice 0)
                    print(f"El {index}-ésimo elemento de la lista {var_name} es: {element}")
                    return element
                else:
                    print(f"Error: El índice {index} está fuera del rango de la lista {var_name}.")
                    return None
            else:
                print(f"Error: {var_name} no es una lista o no está definida correctamente.")
                return None

        # Si no es una consulta de índice, evaluamos la expresión estándar
        if ctx.getChildCount() == 1:
            return self.visit(ctx.termino(0))  # Si solo hay un término, lo evaluamos directamente
        else:
            left_value = self.visit(ctx.termino(0))
            for i in range(1, len(ctx.termino())):
                right_value = self.visit(ctx.termino(i))
                if ctx.getChild(2 * i - 1).getText() == '+':
                    left_value += right_value
                elif ctx.getChild(2 * i - 1).getText() == '-':
                    left_value -= right_value
            return left_value

    def visitTermino(self, ctx):
        # Evaluar el término (factor * factor o factor / factor)
        left_value = self.visit(ctx.factor(0))
        for i in range(1, len(ctx.factor())):
            right_value = self.visit(ctx.factor(i))
            if ctx.getChild(2 * i - 1).getText() == '*':
                left_value *= right_value
            elif ctx.getChild(2 * i - 1).getText() == '/':
                left_value /= right_value
            elif ctx.getChild(2 * i - 1).getText() == '%':
                left_value %= right_value
        return left_value

    def visitFactor(self, ctx):
        # Evaluar el factor (puede ser una variable, un número entero o una expresión entre paréntesis)
        if ctx.ID_MIN():
            # Si es un identificador de variable, devolvemos su valor
            return self.variables.get(ctx.ID_MIN().getText(), 0)
        elif ctx.ID_CAP():
            # Si es una nota musical (como A4, B3, etc.), buscamos su valor numérico
            return self.notas.get(ctx.ID_CAP().getText(), 0)
        elif ctx.INT():
            # Si es un número entero, lo devolvemos como un valor
            return int(ctx.INT().getText())
        elif ctx.expresion():
            # Si es una expresión entre paréntesis, evaluamos la expresión interna
            return self.visit(ctx.expresion())

    def visitPrograma(self, ctx):
        # Visitar todos los procedimientos en el programa
        for procedimiento in ctx.procedimiento():
            self.visit(procedimiento)

    def visitProcedimiento(self, ctx):
        # Visitar el bloque dentro del procedimiento
        procedure_name = ctx.ID_CAP().getText()
        self.procedures[procedure_name] = ctx
        print(f"Defining and Executing procedure: {procedure_name}")
        self.visit(ctx.bloque())

    def visitInvocacion(self, ctx):
        # Obtener el nombre del procedimiento a invocar
        procedure_name = ctx.ID_CAP().getText()
        print(f"Invoking procedure: {procedure_name}")

        # Buscar si el procedimiento está definido
        if procedure_name in self.procedures:
            proc_ctx = self.procedures[procedure_name]
            self.visit(proc_ctx)  # Ejecutar el bloque del procedimiento
        else:
            print(f"Procedure {procedure_name} not found.")

    def visitBloque(self, ctx):
        # Visitar todas las instrucciones en el bloque
        for instruccion in ctx.instruccion():
            self.visit(instruccion)

    def generar_partitura_final(self, notas_reproducidas):
        """Genera el archivo de LilyPond y otros archivos relacionados."""
        # Especificamos la ruta de salida para los archivos generados (directamente en el directorio actual)
        output_path = os.getcwd()  # Usamos el directorio actual donde se ejecuta el código

        # Configuramos las rutas de LilyPond y TiMidity++
        lilypond_path = r"C:\Users\Florian\OneDrive\Escritorio\ilp\lilypond-2.24.4\bin\lilypond.exe"  # Ruta a LilyPond
        timidity_path = r"C:\Users\Florian\OneDrive\Escritorio\ilp\TiMidity++-2.15.0\timidity.exe"  # Ruta a TiMidity++

        # Llamamos al script converter.py para generar los archivos LilyPond, PDF, MIDI y WAV
        # Aquí se pasa directamente la lista de notas y las rutas de los ejecutables
        create_lilypond_file(notas_reproducidas, lilypond_path, timidity_path, output_path)

def run_program(file_name, procedure_name=None):
    with open(file_name, 'r') as file:
        code = file.read()

    input_stream = InputStream(code)
    lexer = algoritmiaLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = algoritmiaParser(token_stream)
    tree = parser.programa()  # Parsear el programa

    visitor = AlgoritmiaInterpreter()

    if procedure_name:
        # Buscar y ejecutar el procedimiento especificado si se da
        procedure_found = False
        for proc in tree.procedimiento():
            if proc.ID_CAP().getText() == procedure_name:
                visitor.visit(proc)  # Ejecutar el procedimiento especificado
                procedure_found = True
                break
        if not procedure_found:
            print(f"Procedure {procedure_name} not found.")
    else:
        # Ejecutar el procedimiento principal por defecto
        visitor.visit(tree)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 algoritmia.py <file.alg> [procedure_name]")
        sys.exit(1)

    file_name = sys.argv[1]
    procedure_name = sys.argv[2] if len(sys.argv) > 2 else None

    run_program(file_name, procedure_name)

if __name__ == "__main__":
    main()