parser grammar DspfParser;

options { tokenVocab = DspfLexer; }

// Root rule for DSPF file
dspfFile: recordDefinition* EOF;

// Record definition
recordDefinition:
    RECORD recordName recordOptions?
    (fieldDefinition | indicatorDefinition | functionKeyDefinition)*
    ;

recordName: IDENTIFIER;
recordOptions: recordOption*;

recordOption:
    FORMAT formatName
    | SFL subfileName
    | SFLCTL subfileControlName
    | SFLINZ subfileInitName
    | SFLDSP subfileDisplayName
    | SFLCLR subfileClearName
    | SFLEND subfileEndName
    | SFLMSG subfileMessageName
    | SFLMSGID subfileMessageIdName
    | SFLMSGKEY subfileMessageKeyName
    | SFLMSGPGM subfileMessagePgmName
    | SFLMSGCTL subfileMessageCtlName
    | SFLMSGINZ subfileMessageInitName
    | SFLMSGDSP subfileMessageDisplayName
    | SFLMSGCLR subfileMessageClearName
    | SFLMSGEND subfileMessageEndName
    ;

formatName: IDENTIFIER;
subfileName: IDENTIFIER;
subfileControlName: IDENTIFIER;
subfileInitName: IDENTIFIER;
subfileDisplayName: IDENTIFIER;
subfileClearName: IDENTIFIER;
subfileEndName: IDENTIFIER;
subfileMessageName: IDENTIFIER;
subfileMessageIdName: IDENTIFIER;
subfileMessageKeyName: IDENTIFIER;
subfileMessagePgmName: IDENTIFIER;
subfileMessageCtlName: IDENTIFIER;
subfileMessageInitName: IDENTIFIER;
subfileMessageDisplayName: IDENTIFIER;
subfileMessageClearName: IDENTIFIER;
subfileMessageEndName: IDENTIFIER;

// Field definition
fieldDefinition:
    FIELD fieldName fieldType fieldOptions?
    ;

fieldName: IDENTIFIER;
fieldType: CHAR | VARCHAR | DECIMAL | PACKED | ZONED | BINARY | INTEGER | FLOAT | DATE | TIME | TIMESTAMP | GRAPHIC | VARGRAPHIC | UCS2 | VARUCS2;

fieldOptions: fieldOption*;

fieldOption:
    LEN length
    | FROM startPosition
    | TO endPosition
    | DSPATR displayAttributeList
    | CHK checkAttributeList
    | VALUES valueList
    | RANGE rangeList
    | COMP comparisonList
    | DFT defaultValue
    | EDTCDE editCode
    | EDTWRD editWord
    | PASS passOption
    | PASSRRN passRrnOption
    | PASSVAL passValOption
    | PASSIND passIndOption
    | PASSMSG passMsgOption
    | PASSMSGID passMsgIdOption
    | PASSMSGTXT passMsgTxtOption
    | PASSMSGTXT2 passMsgTxt2Option
    | PASSMSGTXT3 passMsgTxt3Option
    | PASSMSGTXT4 passMsgTxt4Option
    | PASSMSGTXT5 passMsgTxt5Option
    | PASSMSGTXT6 passMsgTxt6Option
    | PASSMSGTXT7 passMsgTxt7Option
    | PASSMSGTXT8 passMsgTxt8Option
    | PASSMSGTXT9 passMsgTxt9Option
    | PASSMSGTXT10 passMsgTxt10Option
    ;

length: NUMBER;
startPosition: NUMBER;
endPosition: NUMBER;
defaultValue: STRING | QUOTED_STRING | *N | *BLANK | *NULL | *ZEROS | *BLANKS;
editCode: IDENTIFIER;
editWord: IDENTIFIER;

displayAttributeList: displayAttribute (COMMA displayAttribute)*;
displayAttribute: BLINK | BOLD | HIGH | INTENS | MDT | ND | NONDSP | OUTPUT | PROT | REVERSE | UNDERLINE | ZERO;

checkAttributeList: checkAttribute (COMMA checkAttribute)*;
checkAttribute: VALUES | RANGE | COMP | DFT;

valueList: LPAREN value (COMMA value)* RPAREN;
value: STRING | QUOTED_STRING | NUMBER | *N | *BLANK | *NULL | *ZEROS | *BLANKS;

rangeList: LPAREN range (COMMA range)* RPAREN;
range: rangeStart TO rangeEnd;
rangeStart: value;
rangeEnd: value;

comparisonList: LPAREN comparison (COMMA comparison)* RPAREN;
comparison: comparisonOperator value;
comparisonOperator: EQ | NE | GT | LT | GE | LE;

passOption: *N | *YES | *NO;
passRrnOption: *N | *YES | *NO;
passValOption: *N | *YES | *NO;
passIndOption: *N | *YES | *NO;
passMsgOption: *N | *YES | *NO;
passMsgIdOption: *N | *YES | *NO;
passMsgTxtOption: *N | *YES | *NO;
passMsgTxt2Option: *N | *YES | *NO;
passMsgTxt3Option: *N | *YES | *NO;
passMsgTxt4Option: *N | *YES | *NO;
passMsgTxt5Option: *N | *YES | *NO;
passMsgTxt6Option: *N | *YES | *NO;
passMsgTxt7Option: *N | *YES | *NO;
passMsgTxt8Option: *N | *YES | *NO;
passMsgTxt9Option: *N | *YES | *NO;
passMsgTxt10Option: *N | *YES | *NO;

// Indicator definition
indicatorDefinition:
    INDICATOR indicatorName indicatorOptions?
    ;

indicatorName: IDENTIFIER;
indicatorOptions: indicatorOption*;

indicatorOption:
    DSPATR displayAttributeList
    | CHK checkAttributeList
    | VALUES valueList
    | RANGE rangeList
    | COMP comparisonList
    | DFT defaultValue
    | PASS passOption
    | PASSRRN passRrnOption
    | PASSVAL passValOption
    | PASSIND passIndOption
    | PASSMSG passMsgOption
    | PASSMSGID passMsgIdOption
    | PASSMSGTXT passMsgTxtOption
    | PASSMSGTXT2 passMsgTxt2Option
    | PASSMSGTXT3 passMsgTxt3Option
    | PASSMSGTXT4 passMsgTxt4Option
    | PASSMSGTXT5 passMsgTxt5Option
    | PASSMSGTXT6 passMsgTxt6Option
    | PASSMSGTXT7 passMsgTxt7Option
    | PASSMSGTXT8 passMsgTxt8Option
    | PASSMSGTXT9 passMsgTxt9Option
    | PASSMSGTXT10 passMsgTxt10Option
    ;

// Function key definition
functionKeyDefinition:
    FUNCTION functionKeyName functionKeyOptions?
    ;

functionKeyName: F01 | F02 | F03 | F04 | F05 | F06 | F07 | F08 | F09 | F10 | F11 | F12 | F13 | F14 | F15 | F16 | F17 | F18 | F19 | F20 | F21 | F22 | F23 | F24;
functionKeyOptions: functionKeyOption*;

functionKeyOption:
    DSPATR displayAttributeList
    | CHK checkAttributeList
    | VALUES valueList
    | RANGE rangeList
    | COMP comparisonList
    | DFT defaultValue
    | PASS passOption
    | PASSRRN passRrnOption
    | PASSVAL passValOption
    | PASSIND passIndOption
    | PASSMSG passMsgOption
    | PASSMSGID passMsgIdOption
    | PASSMSGTXT passMsgTxtOption
    | PASSMSGTXT2 passMsgTxt2Option
    | PASSMSGTXT3 passMsgTxt3Option
    | PASSMSGTXT4 passMsgTxt4Option
    | PASSMSGTXT5 passMsgTxt5Option
    | PASSMSGTXT6 passMsgTxt6Option
    | PASSMSGTXT7 passMsgTxt7Option
    | PASSMSGTXT8 passMsgTxt8Option
    | PASSMSGTXT9 passMsgTxt9Option
    | PASSMSGTXT10 passMsgTxt10Option
    ;
