grammar prueba;
// Reglas principales
// Reglas principales
prog: comment* procedure+ comment* ; // El programa está compuesto por uno o más procedimientos

procedure: ID_CAP ID_MIN* '|:' block ':|' ; // Procedimientos con bloques delimitados

block: statement* ; // Un bloque puede tener múltiples instrucciones

statement:
    writeStatement       // Instrucción de escritura
    | variableAssignment // Asignación de variables
    | comment            // Comentarios
    | musicalNote        // Notas musicales
    | play               // Instrucción de "tocar" notas musicales
    | salidaMelodia      // Salida de melodía acumulada
    | read
    | functionCall
    | loop_for
    | loop_while
    | condition
    | conditional_if
    | conditional_else
    | asignation
    ;

writeStatement: '<w>' STRING* ID_MIN* ; // Instrucción de escritura

functionCall: ID_CAP ID_MIN* ;
variableAssignment: ID_MIN '=' (STRING | INT | ID_MIN) ; // Asignación de variables sin punto y coma

musicalNote: ID_CAP ; // Notas musicales representadas por letras mayúsculas

play: '(:)' '{' (ID_CAP WS?)* '}' ; // Bloques "play" que contienen notas musicales

read: '<?>' ID_MIN;

binary_and: STRING '&&' STRING; // aqui van los and - or

binary_or: STRING '||' STRING;

greater: (INT|ID_MIN) '>' (INT|ID_MIN);

grater_equals: (INT|ID_MIN) '>=' (INT|ID_MIN);

lesser: (INT|ID_MIN) '<' (INT|ID_MIN);

lesser_equeals: (INT|ID_MIN) '<=' (INT|ID_MIN);

equals: (ID_MIN|INT) '=' (ID_MIN|INT);
equalsnt: (ID_MIN|INT) '/=' (ID_MIN|INT);

condition: lesser|lesser_equeals|grater_equals|greater|equals|equalsnt|binary_and|binary_or ;

conditional_if: ('IF'|'if') condition '|:' block ':|'; // los if else

conditional_else:('ELSE'|'else')'|:' block ':|';

loop_while: ('WHILE'|'while') condition '|:' block ':|'; // los while - for

asignation: ID_MIN '<-'  (ID_MIN|INT|add|substract);

loop_for:'FOR' (INT|STRING) 'IN' range '|:' block ':|';

range: INT|STRING;

substract: (INT|ID_MIN) '-' (INT|ID_MIN);

add: (INT|ID_MIN) '+' (INT|ID_MIN);

comment: '###' (~'#')* '###' ; // Comentario delimitado por ###

salidaMelodia: 'salida_melodia' '=' '[:]' (ID_CAP WS?)* '[:]' ; // Salida de la melodía con notas musicales de los bloques "play"

// Tokens
ID_CAP: [A-Z][a-zA-Z0-9]* ; // Identificadores que empiezan con mayúscula (procedimientos o notas musicales)
ID_MIN: [a-z][a-zA-Z0-9]* ; // Identificadores que empiezan con minúscula (variables)
STRING: '"' (~["])* '"' ;    // Cadenas de texto delimitadas por comillas dobles
INT: [0-9]+ ;               // Números enteros

// Ignorar espacios en blanco
WS: [ \t\r\n]+ -> skip ;
