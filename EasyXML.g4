grammar EasyXML;
/*
* Parser Rules
*/
var_init: TYPE VARNAME ASSIGMENT NEW TYPE OPEN_BRACKET expression? CLOSE_BRACKET SEMICOLON | (TYPE|ARRAY_TYPE) assignment;

assignment: VARNAME (OPEN_BRACKET NUMBER_LITERAL CLOSE_BRACKET)? ASSIGMENT expression SEMICOLON;

sum_assignment: VARNAME (OPEN_BRACKET NUMBER_LITERAL CLOSE_BRACKET)? SUM_ASSIGMENT expression SEMICOLON;

get: get SEMICOLON|
    get OPEN_BRACKET params? CLOSE_BRACKET|
    VARNAME COLON VARNAME;

get_array_element: VARNAME OPEN_SQUAR_EBRACKET (NUMBER_LITERAL | VARNAME) CLOSE_SQUARE_BRACKET;

func_call: VARNAME OPEN_BRACKET params? CLOSE_BRACKET SEMICOLON;

if_statement: if_block elif_block* else_block?;

if_block: IF  condition  COLON OPEN_FIGURE_BRACKET operation* CLOSE_FIGURE_BRACKET ;
elif_block:ELIF condition COLON  OPEN_FIGURE_BRACKET operation* CLOSE_FIGURE_BRACKET;
else_block:ELSE COLON  OPEN_FIGURE_BRACKET operation* CLOSE_FIGURE_BRACKET ;

for_statement: FOR range_statement COLON OPEN_FIGURE_BRACKET operation* CLOSE_FIGURE_BRACKET;

while_statement:WHILE condition COLON OPEN_FIGURE_BRACKET operation* CLOSE_FIGURE_BRACKET;

func_init: (TYPE|ARRAY_TYPE) VARNAME  params? COLON OPEN_FIGURE_BRACKET operation* RETURN expression? SEMICOLON CLOSE_FIGURE_BRACKET;

type_cast:OPEN_BRACKET (TYPE) CLOSE_BRACKET VARNAME;

range_statement: (TYPE|ARRAY_TYPE) VARNAME IN VARNAME;

condition:NOT? expression (ANDOR NOT? condition)*;

params: expression (',' expression)* | param (',' param)*;

param: (TYPE|ARRAY_TYPE) VARNAME;

expression: expression SEMICOLON|
            OPEN_BRACKET expression CLOSE_BRACKET|
            expression ACTION_OPERATOR expression|
            expression BOOL_OPERATOR expression|
            get_operation| type_cast|
            (NUMBER_LITERAL | STRING_LITERAL | VARNAME);

get_operation:get|func_call|get_array_element;

operation:get_operation|
          type_cast|
          var_init|
          assignment|
          sum_assignment|
          if_statement|
          for_statement|
          while_statement;
xml: (operation|func_init)+;
/*
* Lexer Rules
*/

ARRAY_TYPE:TYPE OPEN_SQUAR_EBRACKET CLOSE_SQUARE_BRACKET;

TYPE: TABLE|CELL|ATTRIBUTE|STRING|INT|FLOAT;

ACTION_OPERATOR: PlUS| MINUS| MULTIPLICATION| DIVISION;
BOOL_OPERATOR: MORE_THAN|MORE_EQUAL|LESS_THAN|LESS_EQUAL|EQUAL|NOT_EQUAL;
ANDOR: AND| OR;


TABLE: 'table';
CELL: 'cell';
ATTRIBUTE: 'attribute';
STRING: 'string';
INT: 'int';
FLOAT: 'float';

ELIF: 'elif';
ELSE: 'else';
IF: 'if';
FOR: 'for';
WHILE: 'while';
IN: 'in';
AND: 'and';
OR:'or';
NEW:'new';
RETURN: 'return';

VARNAME: [a-zA-Z_]+;
NUMBER_LITERAL: [0-9]+('.'[0-9]+)?;
STRING_LITERAL : QOUTES.*?QOUTES;

WHITESPACE: (' '|'\t'|'\n'| '\r') -> skip;

OPEN_BRACKET: '(';
CLOSE_BRACKET: ')';
OPEN_SQUAR_EBRACKET: '[';
CLOSE_SQUARE_BRACKET: ']';
OPEN_FIGURE_BRACKET: '{';
CLOSE_FIGURE_BRACKET: '}';

SEMICOLON: ';';
QOUTES: '\''|'"';
ASSIGMENT: '=';
SUM_ASSIGMENT: '+=';
DOT: '.';
COLON: ':';
MORE_THAN: '>';
LESS_THAN: '<';
EQUAL: '==';
NOT_EQUAL: '!=';
MORE_EQUAL: '>=';
LESS_EQUAL: '<=';
PlUS: '+';
MINUS: '-';
MULTIPLICATION: '*';
DIVISION: '/';
NOT: '!';

COMMENT : '#' ~[\r\n]* '\r'? '\n' -> skip ;
