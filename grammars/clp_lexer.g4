lexer grammar clp_lexer;

// Keywords
PGM: 'PGM';
ENDPGM: 'ENDPGM';
DCL: 'DCL';
DCLF: 'DCLF';
MONMSG: 'MONMSG';
CHGVAR: 'CHGVAR';
SNDPGMMSG: 'SNDPGMMSG';
CALL: 'CALL';
GOTO: 'GOTO';
IF: 'IF';
THEN: 'THEN';
ELSE: 'ELSE';
DO: 'DO';
ENDDO: 'ENDDO';

// Data Types
TYPE: '&' [A-Z]+;

// Literals
STRING: '\'' ( ~'\'' | '\'\'' )* '\'';
NUMBER: [0-9]+ ('.' [0-9]+)?;

// Identifiers
ID: [A-Z_] [A-Z0-9_]*;

// Operators
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
EQ: '=';
NE: '!=';
GT: '>';
LT: '<';
GE: '>=';
LE: '<=';

// Parentheses
LPAREN: '(';
RPAREN: ')';

// Other characters
CMD_SEP: ';';
LABEL_SEP: ':';

// Whitespace and Comments
WS: [ \t\r\n]+ -> skip;
COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT: '//' .*? '\n' -> skip;
