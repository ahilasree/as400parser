parser grammar db2_parser;

options { tokenVocab = db2_lexer; }

// Root rule for DB2 SQL
sqlScript: sqlStatement* EOF;

// SQL statements
sqlStatement:
    selectStatement
    | insertStatement
    | updateStatement
    | deleteStatement
    | mergeStatement
    | createStatement
    | alterStatement
    | dropStatement
    | grantStatement
    | revokeStatement
    | commitStatement
    | rollbackStatement
    | beginStatement
    | setStatement
    | commentStatement
    | semicolon
    ;

semicolon: SEMICOLON;

// SELECT statement
selectStatement:
    SELECT (DISTINCT | ALL)? selectList
    FROM tableExpression
    (WHERE whereClause)?
    (GROUP BY groupByClause)?
    (HAVING havingClause)?
    (ORDER BY orderByClause)?
    (LIMIT limitClause)?
    (OFFSET offsetClause)?
    (FETCH fetchClause)?
    ;

selectList:
    selectItem (COMMA selectItem)*
    | ASTERISK
    ;

selectItem:
    expression (AS? alias)?
    | tableName DOT ASTERISK
    ;

alias: IDENTIFIER | STRING;

tableExpression:
    tableReference
    | tableExpression joinClause
    | LPAREN tableExpression RPAREN
    ;

tableReference:
    tableName (AS? alias)?
    | LPAREN selectStatement RPAREN (AS? alias)?
    | tableFunctionName LPAREN arguments? RPAREN (AS? alias)?
    ;
    
tableFunctionName: IDENTIFIER;
viewName: IDENTIFIER;
indexName: IDENTIFIER; 
sequenceName: IDENTIFIER;

joinClause:
    (INNER | (LEFT | RIGHT | FULL) OUTER? | CROSS | NATURAL)?
    JOIN tableReference (ON joinCondition | USING LPAREN columnList RPAREN)?
    ;

joinCondition: expression;
columnList: columnName (COMMA columnName)*;

whereClause: expression;
groupByClause: expression (COMMA expression)*;
havingClause: expression;
orderByClause: orderByItem (COMMA orderByItem)*;
orderByItem: expression (ASC | DESC)?;

limitClause: NUMBER;
offsetClause: NUMBER;
fetchClause: FIRST | NEXT NUMBER ROWS? ONLY;

// INSERT statement
insertStatement:
    INSERT INTO tableName (LPAREN columnList RPAREN)?
    (VALUES valueList | selectStatement)
    ;

valueList: LPAREN expression (COMMA expression)* RPAREN;

arguments: expression (COMMA expression)*;

// UPDATE statement
updateStatement:
    UPDATE tableName
    SET setClause (COMMA setClause)*
    (WHERE whereClause)?
    ;

setClause: columnName EQUALS expression;

// DELETE statement
deleteStatement:
    DELETE FROM tableName
    (WHERE whereClause)?
    ;

// MERGE statement
mergeStatement:
    MERGE INTO tableName (AS? alias)?
    USING tableReference (AS? alias)?
    ON mergeCondition
    (WHEN MATCHED THEN updateClause)?
    (WHEN NOT MATCHED THEN insertClause)?
    ;

mergeCondition: expression;
updateClause: UPDATE SET setClause (COMMA setClause)*;
insertClause: INSERT (LPAREN columnList RPAREN)? VALUES valueList;

// CREATE statement
createStatement:
    createTableStatement
    | createViewStatement
    | createIndexStatement
    | createSequenceStatement
    ;

createTableStatement:
    CREATE TABLE tableName LPAREN columnDefinition (COMMA columnDefinition)* RPAREN
    ;

columnDefinition:
    columnName dataType (columnConstraint)*
    ;

dataType:
    INTEGER | SMALLINT | BIGINT
    | DECIMAL (LPAREN precision (COMMA scale)? RPAREN)?
    | REAL | DOUBLE | FLOAT
    | CHAR (LPAREN length RPAREN)?
    | VARCHAR (LPAREN length RPAREN)?
    | DATE | TIME | TIMESTAMP
    ;

precision: NUMBER;
scale: NUMBER;
length: NUMBER;

columnConstraint:
    NOT_NULL
    | DEFAULT defaultValue
    | PRIMARY KEY
    | UNIQUE
    | CHECK LPAREN checkCondition RPAREN
    | REFERENCES tableName (LPAREN columnName RPAREN)?
    ;

defaultValue: expression;
checkCondition: expression;

createViewStatement:
    CREATE VIEW IDENTIFIER (LPAREN columnList RPAREN)?
    AS selectStatement
    ;

createIndexStatement:
    CREATE INDEX IDENTIFIER ON tableName LPAREN columnList RPAREN
    ;

createSequenceStatement:
    CREATE SEQUENCE IDENTIFIER
    (START WITH startValue)?
    (INCREMENT BY incrementValue)?
    (MINVALUE minValue)?
    (MAXVALUE maxValue)?
    ;

startValue: NUMBER;
incrementValue: NUMBER;
minValue: NUMBER;
maxValue: NUMBER;

// ALTER statement
alterStatement:
    ALTER TABLE tableName alterAction
    ;

alterAction:
    ADD COLUMN columnDefinition
    | DROP COLUMN columnName
    | MODIFY COLUMN columnDefinition
    | ADD CONSTRAINT constraintName constraintDefinition
    | DROP CONSTRAINT constraintName
    ;

constraintName: IDENTIFIER;
constraintDefinition:
    PRIMARY KEY LPAREN columnList RPAREN
    | UNIQUE LPAREN columnList RPAREN
    | FOREIGN KEY LPAREN columnList RPAREN REFERENCES tableName (LPAREN columnList RPAREN)?
    | CHECK LPAREN checkCondition RPAREN
    ;

// DROP statement
dropStatement:
    DROP (TABLE | VIEW | INDEX | SEQUENCE) objectName
    ;

objectName: IDENTIFIER;

// GRANT statement
grantStatement:
    GRANT privilegeList ON objectType objectName TO granteeList
    ;

privilegeList: privilege (COMMA privilege)*;
privilege: SELECT | INSERT | UPDATE | DELETE | ALL;
objectType: TABLE | VIEW | SEQUENCE;
granteeList: grantee (COMMA grantee)*;
grantee: IDENTIFIER | PUBLIC;

// REVOKE statement
revokeStatement:
    REVOKE privilegeList ON objectType objectName FROM granteeList
    ;

// Transaction control
commitStatement: COMMIT (WORK)?;
rollbackStatement: ROLLBACK (WORK)? (TO SAVEPOINT savepointName)?;
beginStatement: BEGIN (WORK | TRANSACTION)?;
savepointName: IDENTIFIER;

// SET statement
setStatement: SET optionName EQUALS optionValue;
optionName: IDENTIFIER;
optionValue: expression;

// COMMENT statement
commentStatement: COMMENT ON (TABLE | COLUMN) objectName IS STRING;

// Expressions
expression:
    primaryExpression
    | expression operator expression
    | LPAREN expression RPAREN
    | functionCall
    | caseExpression
    | castExpression
    ;

primaryExpression:
    literal
    | columnReference
    | parameter
    | subquery
    ;

literal: NUMBER | STRING | DOUBLE_QUOTED_STRING | HEX_STRING | NULL | CURRENT_DATE | CURRENT_TIME | CURRENT_TIMESTAMP;

columnReference: (tableName DOT)? columnName;
tableName: IDENTIFIER;
columnName: IDENTIFIER;
parameter: QUESTION;

operator:
    arithmeticOperator
    | comparisonOperator
    | logicalOperator
    ;

arithmeticOperator: PLUS | MINUS | ASTERISK | SLASH | PERCENT | POWER;
comparisonOperator: EQ | NE | GT | LT | GE | LE | LIKE | NOT_LIKE | IN | NOT_IN | BETWEEN | NOT_BETWEEN | IS | IS_NOT | EXISTS | NOT_EXISTS;
logicalOperator: AND | OR | NOT | XOR;

// Functions
functionCall:
    functionName LPAREN (DISTINCT | ALL)? (argumentList | ASTERISK)? RPAREN
    | windowFunction
    ;

functionName: IDENTIFIER | COUNT | SUM | AVG | MIN | MAX | COALESCE | NULLIF | SUBSTRING | LENGTH | UPPER | LOWER | TRIM | LTRIM | RTRIM | REPLACE | TRANSLATE | POSITION | LOCATE;
argumentList: expression (COMMA expression)*;

// Window functions
windowFunction:
    windowFunctionName LPAREN argumentList? RPAREN OVER windowSpecification
    ;

windowFunctionName: ROW_NUMBER | RANK | DENSE_RANK | NTILE | LAG | LEAD | FIRST_VALUE | LAST_VALUE | NTH_VALUE | PERCENT_RANK | CUME_DIST | PERCENTILE_CONT | PERCENTILE_DISC;

windowSpecification:
    LPAREN (PARTITION BY expression (COMMA expression)*)? (ORDER BY orderByItem (COMMA orderByItem)*)? (ROWS | RANGE | GROUPS) frameSpecification? RPAREN
    ;

frameSpecification:
    frameStart
    | BETWEEN frameStart AND frameEnd
    ;

frameStart: UNBOUNDED PRECEDING | CURRENT ROW | expression PRECEDING | expression FOLLOWING;
frameEnd: UNBOUNDED FOLLOWING | CURRENT ROW | expression PRECEDING | expression FOLLOWING;

// CASE expression
caseExpression:
    CASE (expression)? whenClause+ (ELSE elseExpression)? END
    ;

whenClause: WHEN whenExpression THEN thenExpression;
whenExpression: expression;
thenExpression: expression;
elseExpression: expression;

// CAST expression
castExpression: CAST LPAREN expression AS dataType RPAREN;

// Subquery
subquery: LPAREN selectStatement RPAREN;
