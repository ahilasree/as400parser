parser grammar clle_parser;

options { tokenVocab=clle_lexer; }

// Entry point
program
    : pgmStatement* EOF
    ;

// Program statement - PGM starts the program
// Removed the first pgmStatement rule

statement
    : variableDeclaration
    | assignment
    | loop
    | conditional
    | label
    | command
    ;

// IBM i: DCL VAR(&MSG) TYPE(*CHAR) LEN(50) or LEN(5 0)
variableDeclaration
    : DCL VAR LPAREN VARIABLE RPAREN TYPE LPAREN typeValue RPAREN (LEN LPAREN lenValue RPAREN)?
    ;

typeValue
    : dataType
    | ASTERISK dataType
    | PARAMETER
    ;

lenValue
    : NUMBER (NUMBER)*
    ;

assignment
    : CHGVAR VAR LPAREN VARIABLE RPAREN VALUE LPAREN expression RPAREN
    ;

loop
    : DOWHILE COND LPAREN condition RPAREN statement* ENDDO
    ;

// IBM i: IF COND(...) THEN(DO) ... ENDDO or IF ... THEN ... ENDIF
conditional
    : IF COND LPAREN condition RPAREN (THEN LPAREN DO RPAREN statement* ENDDO | THEN statement* (ELSE statement*)? ENDIF)
    ;

// IBM i: LABEL: followed by statement
label
    : IDENTIFIER COLON statement
    ;

// Program statement - PGM starts the program
pgmStatement
    : PGM statement* ENDPGM
    ;

// IBM i: CMD KEY(value) or CMD KEY value or CMD value  
command
    : COMMAND commandParam*
    | RETURN
    ;

commandParam
    : PARAMETER (LPAREN paramValue RPAREN | EQUALS expression)?
    | LPAREN paramValue RPAREN
    | expression
    ;

paramValue
    : expression+
    ;

condition
    : expression (EQ | NE | GT | LT | GE | LE | ASTERISK_GT | ASTERISK_LT | ASTERISK_GE | ASTERISK_LE | ASTERISK_EQ | ASTERISK_NE) expression
    ;

expression
    : STRING
    | NUMBER
    | VARIABLE
    | PARAMETER
    | LPAREN expression RPAREN
    | ASTERISK
    | PERCENT_LEN LPAREN expression RPAREN
    | PERCENT_TRIM LPAREN expression RPAREN
    | PERCENT_TRIML LPAREN expression RPAREN
    | PERCENT_TRIMR LPAREN expression RPAREN
    | PERCENT_UPPER LPAREN expression RPAREN
    | PERCENT_LOWER LPAREN expression RPAREN
    | PERCENT_SCAN LPAREN expression RPAREN
    | PERCENT_REPLACE LPAREN expression RPAREN
    | PERCENT_SUBST LPAREN expression RPAREN
    | PERCENT_INT LPAREN expression RPAREN
    | PERCENT_FLOAT LPAREN expression RPAREN
    | PERCENT_CHAR LPAREN expression RPAREN
    | PERCENT_DATE LPAREN expression RPAREN
    | PERCENT_TIME LPAREN expression RPAREN
    | PERCENT_TIMESTAMP LPAREN expression RPAREN
    | IDENTIFIER
    ;

dataType
    : CHAR
    | VARCHAR
    | DECIMAL
    | PACKED
    | ZONED
    | BINARY
    | INTEGER
    | FLOAT
    | DATE
    | TIME
    | TIMESTAMP
    ;

startValue
    : NUMBER
    ;

endValue
    : NUMBER
    ;

stepValue
    : NUMBER
    ;
