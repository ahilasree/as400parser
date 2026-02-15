parser grammar SqlRpgleParser;

options { tokenVocab = Sqlrpgle_lexer; }

// Root rule for SQLRPGLE program
sqlrpgleProgram: statement* EOF;

// Statements
statement:
    rpgleStatement
    | sqlStatement
    | commentStatement
    ;

// RPGLE statements
rpgleStatement:
    declarationStatement
    | controlStatement
    | fileStatement
    | errorHandlingStatement
    | labelStatement
    | gotoStatement
    | returnStatement
    ;

// Declaration statements
declarationStatement:
    DCL variableName dataType (LEN length)?
    | DCLF fileName
    ;

variableName: IDENTIFIER;
dataType: CHAR | VARCHAR | DECIMAL | PACKED | ZONED | BINARY | INTEGER | FLOAT | DATE | TIME | TIMESTAMP;
length: NUMBER;
fileName: IDENTIFIER;

// Control statements
controlStatement:
    ifStatement
    | selectStatement
    | doWhileStatement
    | forStatement
    ;

ifStatement:
    IF condition THEN
        statement*
    (ELSE statement*)?
    ENDIF
    ;

selectStatement:
    SELECT
        whenClause+
        (OTHER statement*)?
    ENDSELECT
    ;

whenClause:
    WHEN condition statement*
    ;

doWhileStatement:
    DOWHILE condition
        statement*
    ENDDO
    ;

forStatement:
    FOR variableName FROM startValue TO endValue
        statement*
    ENDFOR
    ;

condition: expression;
startValue: expression;
endValue: expression;

// File operations
fileStatement:
    readStatement
    | writeStatement
    | updateStatement
    | deleteStatement
    | openStatement
    | closeStatement
    ;

readStatement: READ recordFormat (INTO variableName)?;
writeStatement: WRITE recordFormat (FROM variableName)?;
updateStatement: UPDATE recordFormat (FROM variableName)?;
deleteStatement: DELETE recordFormat;
openStatement: OPEN fileName;
closeStatement: CLOSE fileName;
recordFormat: IDENTIFIER;

// Error handling
errorHandlingStatement: MONMSG errorCode;
errorCode: IDENTIFIER;

// Other RPGLE statements
labelStatement: LABEL labelName;
gotoStatement: GOTO labelName;
returnStatement: RETURN;
labelName: IDENTIFIER;

// SQL statements
sqlStatement:
    execSqlBlock
    | declareCursorStatement
    | prepareStatement
    | executeStatement
    | openCursorStatement
    | fetchStatement
    | closeCursorStatement
    ;

// EXEC SQL block
execSqlBlock:
    EXEC_SQL
        sqlStatementList
    END_EXEC
    ;

sqlStatementList:
    sqlStatementItem*
    ;

sqlStatementItem:
    selectStatement
    | insertStatement
    | updateStatement
    | deleteStatement
    | createStatement
    | alterStatement
    | dropStatement
    | commitStatement
    | rollbackStatement
    | setStatement
    ;

// SQL DML statements
selectStatement:
    SELECT (DISTINCT)? selectList
    FROM tableExpression
    (WHERE whereClause)?
    (GROUP BY groupByClause)?
    (HAVING havingClause)?
    (ORDER BY orderByClause)?
    ;

selectList:
    selectItem (COMMA selectItem)*
    | ASTERISK
    ;

selectItem:
    expression (AS? alias)?
    ;

alias: IDENTIFIER | STRING;

tableExpression:
    tableReference
    | tableExpression joinClause
    ;

tableReference:
    tableName (AS? alias)?
    | LPAREN selectStatement RPAREN (AS? alias)?
    ;

tableName: IDENTIFIER;

joinClause:
    (INNER | (LEFT | RIGHT) OUTER?)? JOIN tableReference ON joinCondition
    ;

joinCondition: expression;

whereClause: expression;
groupByClause: expression (COMMA expression)*;
havingClause: expression;
orderByClause: orderByItem (COMMA orderByItem)*;
orderByItem: expression (ASC | DESC)?;

// SQL DML continued
insertStatement:
    INSERT INTO tableName (LPAREN columnList RPAREN)?
    VALUES valueList
    ;

columnList: columnName (COMMA columnName)*;
columnName: IDENTIFIER;
valueList: LPAREN expression (COMMA expression)* RPAREN;

updateStatement:
    UPDATE tableName
    SET setClause (COMMA setClause)*
    (WHERE whereClause)?
    ;

setClause: columnName EQUALS expression;

deleteStatement:
    DELETE FROM tableName
    (WHERE whereClause)?
    ;

// SQL DDL
createStatement:
    CREATE TABLE tableName LPAREN columnDefinition (COMMA columnDefinition)* RPAREN
    ;

columnDefinition:
    columnName dataType (columnConstraint)*
    ;

columnConstraint:
    NOT NULL
    | DEFAULT defaultValue
    | PRIMARY KEY
    | UNIQUE
    ;

defaultValue: expression;

alterStatement:
    ALTER TABLE tableName alterAction
    ;

alterAction:
    ADD COLUMN columnDefinition
    | DROP COLUMN columnName
    ;

dropStatement:
    DROP TABLE tableName
    ;

// Transaction control
commitStatement: COMMIT;
rollbackStatement: ROLLBACK;

// SQL session control
setStatement: SET optionName EQUALS optionValue;
optionName: IDENTIFIER;
optionValue: expression;

// Cursor operations
declareCursorStatement:
    DECLARE cursorName CURSOR FOR selectStatement
    ;

cursorName: IDENTIFIER;

prepareStatement:
    PREPARE statementName FROM sqlStatement
    ;

statementName: IDENTIFIER;

executeStatement:
    EXECUTE statementName (USING parameterList)?
    ;

parameterList: parameter (COMMA parameter)*;
parameter: expression;

openCursorStatement:
    OPEN_CURSOR cursorName
    ;

fetchStatement:
    FETCH cursorName INTO variableList
    ;

variableList: variableName (COMMA variableName)*;

closeCursorStatement:
    CLOSE_CURSOR cursorName
    ;

// Comments
commentStatement: COMMENT | LINE_COMMENT;

// Expressions
expression:
    primaryExpression
    | expression operator expression
    | LPAREN expression RPAREN
    | functionCall
    | caseExpression
    ;

primaryExpression:
    literal
    | variableReference
    | columnReference
    | functionCall
    ;

literal: NUMBER | STRING | QUOTED_STRING | *N | *BLANK | *NULL | *ZEROS | *BLANKS;
variableReference: variableName;
columnReference: (tableName DOT)? columnName;

operator:
    arithmeticOperator
    | comparisonOperator
    | logicalOperator
    ;

arithmeticOperator: PLUS | MINUS | ASTERISK | SLASH | PERCENT;
comparisonOperator: EQUALS | GT | LT | GE | LE | LIKE | IN | BETWEEN | IS | EXISTS;
logicalOperator: AND | OR | NOT;

// Functions
functionCall:
    functionName LPAREN argumentList? RPAREN
    ;

functionName: IDENTIFIER | COUNT | SUM | AVG | MIN | MAX | COALESCE | NULLIF;
argumentList: expression (COMMA expression)*;

// CASE expression
caseExpression:
    CASE (expression)? whenClause+ (ELSE elseExpression)? END
    ;

whenClause: WHEN whenExpression THEN thenExpression;
whenExpression: expression;
thenExpression: expression;
elseExpression: expression;
