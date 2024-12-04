grammar algoritmia;

programa: (procedimiento | comentario)* EOF;

procedimiento: ID_CAP ID_MIN* '|:' bloque ':|';

bloque: instruccion*;

instruccion:
    lectura         // Instrucción de lectura <?> x
    | asignacion    // Instrucción de asignación x <- expresion
    | escritura     // Instrucción de escritura <w>
    | condicional     // Instrucción de condicional
    | while     // Instrucción de bucle while
    | invocacion     // Instrucción invocacion de procedimiento
    | reproduccion      // Instrucción de reproducción (:)
    | expresion      // Instrucción de expresion
    | adicionLista
    | eliminacionLista
    | comentario;   // Comentarios

// Reproducción: Instrucción de reproducir una nota
reproduccion: '(:)' (expresion | lista);

// Instrucción de lectura: lee un valor y lo almacena en una variable
lectura: '<?>' ID_MIN; // <?> seguido de un identificador de variable

// Instrucción de asignación: evalúa una expresión y asigna el resultado a una variable
asignacion: ID_MIN '<-' (expresion | lista); // Agregar soporte para listas

lista: '{' (expresion ( WS? expresion )*)? '}' ;

// Instrucción de escritura: escribe una expresión en la salida estándar
escritura: '<w>' (expresion | STRING | ID_MIN)*;  // <w> seguido de expresiones, cadenas o variables

condicional: 'if' expresion comparator expresion '|:' bloque ':|' ('else' '|:' bloque ':|')?;

while: 'while' expresion comparator expresion '|:' bloque ':|';


invocacion: ID_CAP ID_MIN*; // Invocación de procedimiento, sin paréntesis ni comas

comparator: '=' | '<' | '>' | '<=' | '>=' | '/=';  // Define los operadores de comparación posibles

adicionLista: ID_MIN '<<' expresion;  // v << x

eliminacionLista: '8<' ID_MIN '[' expresion ']' ;

// Expresiones, operaciones aritméticas, números y operadores
expresion: termino (( '+' | '-' ) termino)* | '#' ID_MIN | ID_MIN '[' expresion ']';
termino: factor (( '*' | '/' | '%') factor)* ;
factor: ID_MIN | ID_CAP | INT | '(' expresion ')';

// Comentarios
comentario: '###' (~'#')* '###';

// Definición de tokens
ID_CAP: [A-Z][a-zA-Z0-9]*;   // Identificadores de procedimientos (ej. Main)
ID_MIN: [a-z_][a-zA-Z0-9]*;   // Identificadores de variables (ej. x, contador)
STRING: '"' (~["])* '"';      // Cadenas de texto (ej. "Hello World")
INT: [0-9]+;                  // Números enteros
WS: [ \t\r\n]+ -> skip;       // Espacios en blanco