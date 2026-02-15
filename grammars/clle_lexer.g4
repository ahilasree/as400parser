lexer grammar clle_lexer;

// Control Language Lexer Grammar
// CLLE is IBM i's Control Language for system commands

// Basic tokens - COMMAND must come after keywords so keywords match first
// PARAMETER covers values like MYPGM, ENDIT, *CHAR, *DEC, *DIAG
PARAMETER: [A-Za-z0-9_$#@*.\\-]+;
STRING: '\'' (~["\r\n])* '\'' | '"' (~["\r\n])* '"';
NUMBER: [0-9]+ ('.' [0-9]+)?;
VARIABLE: '&' [A-Za-z][A-Za-z0-9_]*;

// Special characters (ASTERISK_* before ASTERISK for *GT, *LT, etc.)
LPAREN: '(';
RPAREN: ')';
COMMA: ',';
EQUALS: '=';
COLON: ':';
PLUS: '+';
MINUS: '-';
ASTERISK_GT: '*GT';
ASTERISK_LT: '*LT';
ASTERISK_GE: '*GE';
ASTERISK_LE: '*LE';
ASTERISK_EQ: '*EQ';
ASTERISK_NE: '*NE';
ASTERISK: '*';
SLASH: '/';
PERCENT: '%';
HASH: '#';
AT: '@';
DOLLAR: '$';

// Whitespace and separators
WS: [ \t\r\n]+ -> skip;
COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;

// CLLE specific keywords
CHGVAR: 'CHGVAR';
DCL: 'DCL';
DCLF: 'DCLF';
DOWHILE: 'DOWHILE';
ENDDO: 'ENDDO';
IF: 'IF';
THEN: 'THEN';
DO: 'DO';
ELSE: 'ELSE';
ENDIF: 'ENDIF';
SELECT: 'SELECT';
WHEN: 'WHEN';
OTHER: 'OTHER';
ENDSELECT: 'ENDSELECT';
CALL: 'CALL';
CALLPRC: 'CALLPRC';
MONMSG: 'MONMSG';
GOTO: 'GOTO';
LABEL: 'LABEL';
SNDMSG: 'SNDMSG';
RCVMSG: 'RCVMSG';
SNDF: 'SNDF';
RCVF: 'RCVF';
READ: 'READ';
WRITE: 'WRITE';
UPDATE: 'UPDATE';
DELETE: 'DELETE';
OPEN: 'OPEN';
CLOSE: 'CLOSE';
COMMIT: 'COMMIT';
ROLLBACK: 'ROLLBACK';
VAR: 'VAR';
TYPE: 'TYPE';
LEN: 'LEN';
VALUE: 'VALUE';
COND: 'COND';

// Program control
PGM: 'PGM';
ENDPGM: 'ENDPGM';
RETURN: 'RETURN';
SBMJOB: 'SBMJOB';
WRKJOB: 'WRKJOB';
ENDJOB: 'ENDJOB';

// System commands
CRTCLPGM: 'CRTCLPGM';
CRTPF: 'CRTPF';
CRTLF: 'CRTLF';
CRTDSPF: 'CRTDSPF';
CRTPRTF: 'CRTPRTF';
CRTCMD: 'CRTCMD';
CRTUSRPRF: 'CRTUSRPRF';
DLTUSRPRF: 'DLTUSRPRF';
CHGUSRPRF: 'CHGUSRPRF';

// Data types
CHAR: 'CHAR';
VARCHAR: 'VARCHAR';
DECIMAL: 'DEC';
PACKED: 'PACKED';
ZONED: 'ZONED';
BINARY: 'BIN';
INTEGER: 'INT';
FLOAT: 'FLOAT';
DATE: 'DATE';
TIME: 'TIME';
TIMESTAMP: 'TIMESTAMP';

// Operators
EQ: 'EQ';
NE: 'NE';
GT: 'GT';
LT: 'LT';
GE: 'GE';
LE: 'LE';
AND: 'AND';
OR: 'OR';
NOT: 'NOT';

// Built-in functions
PERCENT_LEN: '%LEN';
PERCENT_TRIM: '%TRIM';
PERCENT_TRIML: '%TRIML';
PERCENT_TRIMR: '%TRIMR';
PERCENT_UPPER: '%UPPER';
PERCENT_LOWER: '%LOWER';
PERCENT_SCAN: '%SCAN';
PERCENT_REPLACE: '%REPLACE';
PERCENT_SUBST: '%SUBST';
PERCENT_INT: '%INT';
PERCENT_FLOAT: '%FLOAT';
PERCENT_CHAR: '%CHAR';
PERCENT_DATE: '%DATE';
PERCENT_TIME: '%TIME';
PERCENT_TIMESTAMP: '%TIMESTAMP';

// Identifiers
IDENTIFIER: [A-Za-z_][A-Za-z0-9_]*;

// Command names (after keywords - matches PGM, SNDPGMMSG, CALL, GOTO, etc.)
COMMAND: [A-Z][A-Z0-9]*;
