parser grammar clp_parser;

options { tokenVocab = clp_lexer; }

program: pgm_stmt (statement)* endpgm_stmt;

pgm_stmt: PGM;
endpgm_stmt: ENDPGM;

statement:
    dcl_stmt
    | dclf_stmt
    | monmsg_stmt
    | chgvar_stmt
    | sndpgmmsg_stmt
    | call_stmt
    | goto_stmt
    | if_stmt
    | do_block
    | label_stmt;

dcl_stmt: DCL ID ID (ID NUMBER)? (ID literal)?;
dclf_stmt: DCLF ID;
monmsg_stmt: MONMSG ID ID call_stmt;
chgvar_stmt: CHGVAR ID ID expression;
sndpgmmsg_stmt: SNDPGMMSG STRING;
call_stmt: CALL ID (ID expression_list)?;
goto_stmt: GOTO ID;
if_stmt: IF expression THEN (statement | do_block);
do_block: DO (statement)* ENDDO;
label_stmt: ID LABEL_SEP;

expression_list: expression (expression)*;
expression:
    LPAREN expression RPAREN
    | literal
    | ID
    | expression (MULT | DIV) expression
    | expression (PLUS | MINUS) expression
    | expression (EQ | NE | GT | LT | GE | LE) expression;

literal:
    STRING
    | NUMBER;
