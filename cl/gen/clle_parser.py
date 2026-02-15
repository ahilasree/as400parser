# Generated from C:/Users/natar/AI/AS400Parser/grammars/clle_parser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,114,285,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,
        7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,
        13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,5,0,40,
        8,0,10,0,12,0,43,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,3,1,53,8,1,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,69,8,
        2,1,3,1,3,1,3,1,3,3,3,75,8,3,1,4,1,4,5,4,79,8,4,10,4,12,4,82,9,4,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,
        5,6,100,8,6,10,6,12,6,103,9,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,5,7,117,8,7,10,7,12,7,120,9,7,1,7,1,7,1,7,5,7,125,
        8,7,10,7,12,7,128,9,7,1,7,1,7,5,7,132,8,7,10,7,12,7,135,9,7,3,7,
        137,8,7,1,7,3,7,140,8,7,1,8,1,8,1,8,1,8,1,9,1,9,5,9,148,8,9,10,9,
        12,9,151,9,9,1,9,1,9,1,10,1,10,5,10,157,8,10,10,10,12,10,160,9,10,
        1,10,3,10,163,8,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,172,8,
        11,1,11,1,11,1,11,1,11,1,11,3,11,179,8,11,1,12,4,12,182,8,12,11,
        12,12,12,183,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,3,14,275,8,14,1,15,1,15,1,16,1,16,1,17,1,17,1,18,1,18,1,18,0,
        0,19,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,0,2,2,0,
        12,17,89,94,1,0,78,88,310,0,41,1,0,0,0,2,52,1,0,0,0,4,54,1,0,0,0,
        6,74,1,0,0,0,8,76,1,0,0,0,10,83,1,0,0,0,12,93,1,0,0,0,14,106,1,0,
        0,0,16,141,1,0,0,0,18,145,1,0,0,0,20,162,1,0,0,0,22,178,1,0,0,0,
        24,181,1,0,0,0,26,185,1,0,0,0,28,274,1,0,0,0,30,276,1,0,0,0,32,278,
        1,0,0,0,34,280,1,0,0,0,36,282,1,0,0,0,38,40,3,18,9,0,39,38,1,0,0,
        0,40,43,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,44,1,0,0,0,43,41,
        1,0,0,0,44,45,5,0,0,1,45,1,1,0,0,0,46,53,3,4,2,0,47,53,3,10,5,0,
        48,53,3,12,6,0,49,53,3,14,7,0,50,53,3,16,8,0,51,53,3,20,10,0,52,
        46,1,0,0,0,52,47,1,0,0,0,52,48,1,0,0,0,52,49,1,0,0,0,52,50,1,0,0,
        0,52,51,1,0,0,0,53,3,1,0,0,0,54,55,5,28,0,0,55,56,5,58,0,0,56,57,
        5,5,0,0,57,58,5,4,0,0,58,59,5,6,0,0,59,60,5,59,0,0,60,61,5,5,0,0,
        61,62,3,6,3,0,62,68,5,6,0,0,63,64,5,60,0,0,64,65,5,5,0,0,65,66,3,
        8,4,0,66,67,5,6,0,0,67,69,1,0,0,0,68,63,1,0,0,0,68,69,1,0,0,0,69,
        5,1,0,0,0,70,75,3,30,15,0,71,72,5,18,0,0,72,75,3,30,15,0,73,75,5,
        1,0,0,74,70,1,0,0,0,74,71,1,0,0,0,74,73,1,0,0,0,75,7,1,0,0,0,76,
        80,5,3,0,0,77,79,5,3,0,0,78,77,1,0,0,0,79,82,1,0,0,0,80,78,1,0,0,
        0,80,81,1,0,0,0,81,9,1,0,0,0,82,80,1,0,0,0,83,84,5,27,0,0,84,85,
        5,58,0,0,85,86,5,5,0,0,86,87,5,4,0,0,87,88,5,6,0,0,88,89,5,61,0,
        0,89,90,5,5,0,0,90,91,3,28,14,0,91,92,5,6,0,0,92,11,1,0,0,0,93,94,
        5,30,0,0,94,95,5,62,0,0,95,96,5,5,0,0,96,97,3,26,13,0,97,101,5,6,
        0,0,98,100,3,2,1,0,99,98,1,0,0,0,100,103,1,0,0,0,101,99,1,0,0,0,
        101,102,1,0,0,0,102,104,1,0,0,0,103,101,1,0,0,0,104,105,5,31,0,0,
        105,13,1,0,0,0,106,107,5,32,0,0,107,108,5,62,0,0,108,109,5,5,0,0,
        109,110,3,26,13,0,110,139,5,6,0,0,111,112,5,33,0,0,112,113,5,5,0,
        0,113,114,5,34,0,0,114,118,5,6,0,0,115,117,3,2,1,0,116,115,1,0,0,
        0,117,120,1,0,0,0,118,116,1,0,0,0,118,119,1,0,0,0,119,121,1,0,0,
        0,120,118,1,0,0,0,121,140,5,31,0,0,122,126,5,33,0,0,123,125,3,2,
        1,0,124,123,1,0,0,0,125,128,1,0,0,0,126,124,1,0,0,0,126,127,1,0,
        0,0,127,136,1,0,0,0,128,126,1,0,0,0,129,133,5,35,0,0,130,132,3,2,
        1,0,131,130,1,0,0,0,132,135,1,0,0,0,133,131,1,0,0,0,133,134,1,0,
        0,0,134,137,1,0,0,0,135,133,1,0,0,0,136,129,1,0,0,0,136,137,1,0,
        0,0,137,138,1,0,0,0,138,140,5,36,0,0,139,111,1,0,0,0,139,122,1,0,
        0,0,140,15,1,0,0,0,141,142,5,113,0,0,142,143,5,9,0,0,143,144,3,2,
        1,0,144,17,1,0,0,0,145,149,5,63,0,0,146,148,3,2,1,0,147,146,1,0,
        0,0,148,151,1,0,0,0,149,147,1,0,0,0,149,150,1,0,0,0,150,152,1,0,
        0,0,151,149,1,0,0,0,152,153,5,64,0,0,153,19,1,0,0,0,154,158,5,114,
        0,0,155,157,3,22,11,0,156,155,1,0,0,0,157,160,1,0,0,0,158,156,1,
        0,0,0,158,159,1,0,0,0,159,163,1,0,0,0,160,158,1,0,0,0,161,163,5,
        65,0,0,162,154,1,0,0,0,162,161,1,0,0,0,163,21,1,0,0,0,164,171,5,
        1,0,0,165,166,5,5,0,0,166,167,3,24,12,0,167,168,5,6,0,0,168,172,
        1,0,0,0,169,170,5,8,0,0,170,172,3,28,14,0,171,165,1,0,0,0,171,169,
        1,0,0,0,171,172,1,0,0,0,172,179,1,0,0,0,173,174,5,5,0,0,174,175,
        3,24,12,0,175,176,5,6,0,0,176,179,1,0,0,0,177,179,3,28,14,0,178,
        164,1,0,0,0,178,173,1,0,0,0,178,177,1,0,0,0,179,23,1,0,0,0,180,182,
        3,28,14,0,181,180,1,0,0,0,182,183,1,0,0,0,183,181,1,0,0,0,183,184,
        1,0,0,0,184,25,1,0,0,0,185,186,3,28,14,0,186,187,7,0,0,0,187,188,
        3,28,14,0,188,27,1,0,0,0,189,275,5,2,0,0,190,275,5,3,0,0,191,275,
        5,4,0,0,192,275,5,1,0,0,193,194,5,5,0,0,194,195,3,28,14,0,195,196,
        5,6,0,0,196,275,1,0,0,0,197,275,5,18,0,0,198,199,5,98,0,0,199,200,
        5,5,0,0,200,201,3,28,14,0,201,202,5,6,0,0,202,275,1,0,0,0,203,204,
        5,99,0,0,204,205,5,5,0,0,205,206,3,28,14,0,206,207,5,6,0,0,207,275,
        1,0,0,0,208,209,5,100,0,0,209,210,5,5,0,0,210,211,3,28,14,0,211,
        212,5,6,0,0,212,275,1,0,0,0,213,214,5,101,0,0,214,215,5,5,0,0,215,
        216,3,28,14,0,216,217,5,6,0,0,217,275,1,0,0,0,218,219,5,102,0,0,
        219,220,5,5,0,0,220,221,3,28,14,0,221,222,5,6,0,0,222,275,1,0,0,
        0,223,224,5,103,0,0,224,225,5,5,0,0,225,226,3,28,14,0,226,227,5,
        6,0,0,227,275,1,0,0,0,228,229,5,104,0,0,229,230,5,5,0,0,230,231,
        3,28,14,0,231,232,5,6,0,0,232,275,1,0,0,0,233,234,5,105,0,0,234,
        235,5,5,0,0,235,236,3,28,14,0,236,237,5,6,0,0,237,275,1,0,0,0,238,
        239,5,106,0,0,239,240,5,5,0,0,240,241,3,28,14,0,241,242,5,6,0,0,
        242,275,1,0,0,0,243,244,5,107,0,0,244,245,5,5,0,0,245,246,3,28,14,
        0,246,247,5,6,0,0,247,275,1,0,0,0,248,249,5,108,0,0,249,250,5,5,
        0,0,250,251,3,28,14,0,251,252,5,6,0,0,252,275,1,0,0,0,253,254,5,
        109,0,0,254,255,5,5,0,0,255,256,3,28,14,0,256,257,5,6,0,0,257,275,
        1,0,0,0,258,259,5,110,0,0,259,260,5,5,0,0,260,261,3,28,14,0,261,
        262,5,6,0,0,262,275,1,0,0,0,263,264,5,111,0,0,264,265,5,5,0,0,265,
        266,3,28,14,0,266,267,5,6,0,0,267,275,1,0,0,0,268,269,5,112,0,0,
        269,270,5,5,0,0,270,271,3,28,14,0,271,272,5,6,0,0,272,275,1,0,0,
        0,273,275,5,113,0,0,274,189,1,0,0,0,274,190,1,0,0,0,274,191,1,0,
        0,0,274,192,1,0,0,0,274,193,1,0,0,0,274,197,1,0,0,0,274,198,1,0,
        0,0,274,203,1,0,0,0,274,208,1,0,0,0,274,213,1,0,0,0,274,218,1,0,
        0,0,274,223,1,0,0,0,274,228,1,0,0,0,274,233,1,0,0,0,274,238,1,0,
        0,0,274,243,1,0,0,0,274,248,1,0,0,0,274,253,1,0,0,0,274,258,1,0,
        0,0,274,263,1,0,0,0,274,268,1,0,0,0,274,273,1,0,0,0,275,29,1,0,0,
        0,276,277,7,1,0,0,277,31,1,0,0,0,278,279,5,3,0,0,279,33,1,0,0,0,
        280,281,5,3,0,0,281,35,1,0,0,0,282,283,5,3,0,0,283,37,1,0,0,0,18,
        41,52,68,74,80,101,118,126,133,136,139,149,158,162,171,178,183,274
    ]

class clle_parser ( Parser ):

    grammarFileName = "clle_parser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'('", "')'", "','", "'='", "':'", "'+'", 
                     "'-'", "'*GT'", "'*LT'", "'*GE'", "'*LE'", "'*EQ'", 
                     "'*NE'", "'*'", "'/'", "'%'", "'#'", "'@'", "'$'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'CHGVAR'", 
                     "'DCL'", "'DCLF'", "'DOWHILE'", "'ENDDO'", "'IF'", 
                     "'THEN'", "'DO'", "'ELSE'", "'ENDIF'", "'SELECT'", 
                     "'WHEN'", "'OTHER'", "'ENDSELECT'", "'CALL'", "'CALLPRC'", 
                     "'MONMSG'", "'GOTO'", "'LABEL'", "'SNDMSG'", "'RCVMSG'", 
                     "'SNDF'", "'RCVF'", "'READ'", "'WRITE'", "'UPDATE'", 
                     "'DELETE'", "'OPEN'", "'CLOSE'", "'COMMIT'", "'ROLLBACK'", 
                     "'VAR'", "'TYPE'", "'LEN'", "'VALUE'", "'COND'", "'PGM'", 
                     "'ENDPGM'", "'RETURN'", "'SBMJOB'", "'WRKJOB'", "'ENDJOB'", 
                     "'CRTCLPGM'", "'CRTPF'", "'CRTLF'", "'CRTDSPF'", "'CRTPRTF'", 
                     "'CRTCMD'", "'CRTUSRPRF'", "'DLTUSRPRF'", "'CHGUSRPRF'", 
                     "'CHAR'", "'VARCHAR'", "'DEC'", "'PACKED'", "'ZONED'", 
                     "'BIN'", "'INT'", "'FLOAT'", "'DATE'", "'TIME'", "'TIMESTAMP'", 
                     "'EQ'", "'NE'", "'GT'", "'LT'", "'GE'", "'LE'", "'AND'", 
                     "'OR'", "'NOT'", "'%LEN'", "'%TRIM'", "'%TRIML'", "'%TRIMR'", 
                     "'%UPPER'", "'%LOWER'", "'%SCAN'", "'%REPLACE'", "'%SUBST'", 
                     "'%INT'", "'%FLOAT'", "'%CHAR'", "'%DATE'", "'%TIME'", 
                     "'%TIMESTAMP'" ]

    symbolicNames = [ "<INVALID>", "PARAMETER", "STRING", "NUMBER", "VARIABLE", 
                      "LPAREN", "RPAREN", "COMMA", "EQUALS", "COLON", "PLUS", 
                      "MINUS", "ASTERISK_GT", "ASTERISK_LT", "ASTERISK_GE", 
                      "ASTERISK_LE", "ASTERISK_EQ", "ASTERISK_NE", "ASTERISK", 
                      "SLASH", "PERCENT", "HASH", "AT", "DOLLAR", "WS", 
                      "COMMENT", "LINE_COMMENT", "CHGVAR", "DCL", "DCLF", 
                      "DOWHILE", "ENDDO", "IF", "THEN", "DO", "ELSE", "ENDIF", 
                      "SELECT", "WHEN", "OTHER", "ENDSELECT", "CALL", "CALLPRC", 
                      "MONMSG", "GOTO", "LABEL", "SNDMSG", "RCVMSG", "SNDF", 
                      "RCVF", "READ", "WRITE", "UPDATE", "DELETE", "OPEN", 
                      "CLOSE", "COMMIT", "ROLLBACK", "VAR", "TYPE", "LEN", 
                      "VALUE", "COND", "PGM", "ENDPGM", "RETURN", "SBMJOB", 
                      "WRKJOB", "ENDJOB", "CRTCLPGM", "CRTPF", "CRTLF", 
                      "CRTDSPF", "CRTPRTF", "CRTCMD", "CRTUSRPRF", "DLTUSRPRF", 
                      "CHGUSRPRF", "CHAR", "VARCHAR", "DECIMAL", "PACKED", 
                      "ZONED", "BINARY", "INTEGER", "FLOAT", "DATE", "TIME", 
                      "TIMESTAMP", "EQ", "NE", "GT", "LT", "GE", "LE", "AND", 
                      "OR", "NOT", "PERCENT_LEN", "PERCENT_TRIM", "PERCENT_TRIML", 
                      "PERCENT_TRIMR", "PERCENT_UPPER", "PERCENT_LOWER", 
                      "PERCENT_SCAN", "PERCENT_REPLACE", "PERCENT_SUBST", 
                      "PERCENT_INT", "PERCENT_FLOAT", "PERCENT_CHAR", "PERCENT_DATE", 
                      "PERCENT_TIME", "PERCENT_TIMESTAMP", "IDENTIFIER", 
                      "COMMAND" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_variableDeclaration = 2
    RULE_typeValue = 3
    RULE_lenValue = 4
    RULE_assignment = 5
    RULE_loop = 6
    RULE_conditional = 7
    RULE_label = 8
    RULE_pgmStatement = 9
    RULE_command = 10
    RULE_commandParam = 11
    RULE_paramValue = 12
    RULE_condition = 13
    RULE_expression = 14
    RULE_dataType = 15
    RULE_startValue = 16
    RULE_endValue = 17
    RULE_stepValue = 18

    ruleNames =  [ "program", "statement", "variableDeclaration", "typeValue", 
                   "lenValue", "assignment", "loop", "conditional", "label", 
                   "pgmStatement", "command", "commandParam", "paramValue", 
                   "condition", "expression", "dataType", "startValue", 
                   "endValue", "stepValue" ]

    EOF = Token.EOF
    PARAMETER=1
    STRING=2
    NUMBER=3
    VARIABLE=4
    LPAREN=5
    RPAREN=6
    COMMA=7
    EQUALS=8
    COLON=9
    PLUS=10
    MINUS=11
    ASTERISK_GT=12
    ASTERISK_LT=13
    ASTERISK_GE=14
    ASTERISK_LE=15
    ASTERISK_EQ=16
    ASTERISK_NE=17
    ASTERISK=18
    SLASH=19
    PERCENT=20
    HASH=21
    AT=22
    DOLLAR=23
    WS=24
    COMMENT=25
    LINE_COMMENT=26
    CHGVAR=27
    DCL=28
    DCLF=29
    DOWHILE=30
    ENDDO=31
    IF=32
    THEN=33
    DO=34
    ELSE=35
    ENDIF=36
    SELECT=37
    WHEN=38
    OTHER=39
    ENDSELECT=40
    CALL=41
    CALLPRC=42
    MONMSG=43
    GOTO=44
    LABEL=45
    SNDMSG=46
    RCVMSG=47
    SNDF=48
    RCVF=49
    READ=50
    WRITE=51
    UPDATE=52
    DELETE=53
    OPEN=54
    CLOSE=55
    COMMIT=56
    ROLLBACK=57
    VAR=58
    TYPE=59
    LEN=60
    VALUE=61
    COND=62
    PGM=63
    ENDPGM=64
    RETURN=65
    SBMJOB=66
    WRKJOB=67
    ENDJOB=68
    CRTCLPGM=69
    CRTPF=70
    CRTLF=71
    CRTDSPF=72
    CRTPRTF=73
    CRTCMD=74
    CRTUSRPRF=75
    DLTUSRPRF=76
    CHGUSRPRF=77
    CHAR=78
    VARCHAR=79
    DECIMAL=80
    PACKED=81
    ZONED=82
    BINARY=83
    INTEGER=84
    FLOAT=85
    DATE=86
    TIME=87
    TIMESTAMP=88
    EQ=89
    NE=90
    GT=91
    LT=92
    GE=93
    LE=94
    AND=95
    OR=96
    NOT=97
    PERCENT_LEN=98
    PERCENT_TRIM=99
    PERCENT_TRIML=100
    PERCENT_TRIMR=101
    PERCENT_UPPER=102
    PERCENT_LOWER=103
    PERCENT_SCAN=104
    PERCENT_REPLACE=105
    PERCENT_SUBST=106
    PERCENT_INT=107
    PERCENT_FLOAT=108
    PERCENT_CHAR=109
    PERCENT_DATE=110
    PERCENT_TIME=111
    PERCENT_TIMESTAMP=112
    IDENTIFIER=113
    COMMAND=114

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(clle_parser.EOF, 0)

        def pgmStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(clle_parser.PgmStatementContext)
            else:
                return self.getTypedRuleContext(clle_parser.PgmStatementContext,i)


        def getRuleIndex(self):
            return clle_parser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = clle_parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==63:
                self.state = 38
                self.pgmStatement()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 44
            self.match(clle_parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self):
            return self.getTypedRuleContext(clle_parser.VariableDeclarationContext,0)


        def assignment(self):
            return self.getTypedRuleContext(clle_parser.AssignmentContext,0)


        def loop(self):
            return self.getTypedRuleContext(clle_parser.LoopContext,0)


        def conditional(self):
            return self.getTypedRuleContext(clle_parser.ConditionalContext,0)


        def label(self):
            return self.getTypedRuleContext(clle_parser.LabelContext,0)


        def command(self):
            return self.getTypedRuleContext(clle_parser.CommandContext,0)


        def getRuleIndex(self):
            return clle_parser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = clle_parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 52
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.variableDeclaration()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.assignment()
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 3)
                self.state = 48
                self.loop()
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 4)
                self.state = 49
                self.conditional()
                pass
            elif token in [113]:
                self.enterOuterAlt(localctx, 5)
                self.state = 50
                self.label()
                pass
            elif token in [65, 114]:
                self.enterOuterAlt(localctx, 6)
                self.state = 51
                self.command()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DCL(self):
            return self.getToken(clle_parser.DCL, 0)

        def VAR(self):
            return self.getToken(clle_parser.VAR, 0)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(clle_parser.LPAREN)
            else:
                return self.getToken(clle_parser.LPAREN, i)

        def VARIABLE(self):
            return self.getToken(clle_parser.VARIABLE, 0)

        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(clle_parser.RPAREN)
            else:
                return self.getToken(clle_parser.RPAREN, i)

        def TYPE(self):
            return self.getToken(clle_parser.TYPE, 0)

        def typeValue(self):
            return self.getTypedRuleContext(clle_parser.TypeValueContext,0)


        def LEN(self):
            return self.getToken(clle_parser.LEN, 0)

        def lenValue(self):
            return self.getTypedRuleContext(clle_parser.LenValueContext,0)


        def getRuleIndex(self):
            return clle_parser.RULE_variableDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclaration" ):
                listener.enterVariableDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclaration" ):
                listener.exitVariableDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclaration" ):
                return visitor.visitVariableDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclaration(self):

        localctx = clle_parser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_variableDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(clle_parser.DCL)
            self.state = 55
            self.match(clle_parser.VAR)
            self.state = 56
            self.match(clle_parser.LPAREN)
            self.state = 57
            self.match(clle_parser.VARIABLE)
            self.state = 58
            self.match(clle_parser.RPAREN)
            self.state = 59
            self.match(clle_parser.TYPE)
            self.state = 60
            self.match(clle_parser.LPAREN)
            self.state = 61
            self.typeValue()
            self.state = 62
            self.match(clle_parser.RPAREN)
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==60:
                self.state = 63
                self.match(clle_parser.LEN)
                self.state = 64
                self.match(clle_parser.LPAREN)
                self.state = 65
                self.lenValue()
                self.state = 66
                self.match(clle_parser.RPAREN)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dataType(self):
            return self.getTypedRuleContext(clle_parser.DataTypeContext,0)


        def ASTERISK(self):
            return self.getToken(clle_parser.ASTERISK, 0)

        def PARAMETER(self):
            return self.getToken(clle_parser.PARAMETER, 0)

        def getRuleIndex(self):
            return clle_parser.RULE_typeValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeValue" ):
                listener.enterTypeValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeValue" ):
                listener.exitTypeValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeValue" ):
                return visitor.visitTypeValue(self)
            else:
                return visitor.visitChildren(self)




    def typeValue(self):

        localctx = clle_parser.TypeValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_typeValue)
        try:
            self.state = 74
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88]:
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.dataType()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 71
                self.match(clle_parser.ASTERISK)
                self.state = 72
                self.dataType()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 73
                self.match(clle_parser.PARAMETER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LenValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(clle_parser.NUMBER)
            else:
                return self.getToken(clle_parser.NUMBER, i)

        def getRuleIndex(self):
            return clle_parser.RULE_lenValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLenValue" ):
                listener.enterLenValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLenValue" ):
                listener.exitLenValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLenValue" ):
                return visitor.visitLenValue(self)
            else:
                return visitor.visitChildren(self)




    def lenValue(self):

        localctx = clle_parser.LenValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_lenValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(clle_parser.NUMBER)
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 77
                self.match(clle_parser.NUMBER)
                self.state = 82
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHGVAR(self):
            return self.getToken(clle_parser.CHGVAR, 0)

        def VAR(self):
            return self.getToken(clle_parser.VAR, 0)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(clle_parser.LPAREN)
            else:
                return self.getToken(clle_parser.LPAREN, i)

        def VARIABLE(self):
            return self.getToken(clle_parser.VARIABLE, 0)

        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(clle_parser.RPAREN)
            else:
                return self.getToken(clle_parser.RPAREN, i)

        def VALUE(self):
            return self.getToken(clle_parser.VALUE, 0)

        def expression(self):
            return self.getTypedRuleContext(clle_parser.ExpressionContext,0)


        def getRuleIndex(self):
            return clle_parser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = clle_parser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(clle_parser.CHGVAR)
            self.state = 84
            self.match(clle_parser.VAR)
            self.state = 85
            self.match(clle_parser.LPAREN)
            self.state = 86
            self.match(clle_parser.VARIABLE)
            self.state = 87
            self.match(clle_parser.RPAREN)
            self.state = 88
            self.match(clle_parser.VALUE)
            self.state = 89
            self.match(clle_parser.LPAREN)
            self.state = 90
            self.expression()
            self.state = 91
            self.match(clle_parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOWHILE(self):
            return self.getToken(clle_parser.DOWHILE, 0)

        def COND(self):
            return self.getToken(clle_parser.COND, 0)

        def LPAREN(self):
            return self.getToken(clle_parser.LPAREN, 0)

        def condition(self):
            return self.getTypedRuleContext(clle_parser.ConditionContext,0)


        def RPAREN(self):
            return self.getToken(clle_parser.RPAREN, 0)

        def ENDDO(self):
            return self.getToken(clle_parser.ENDDO, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(clle_parser.StatementContext)
            else:
                return self.getTypedRuleContext(clle_parser.StatementContext,i)


        def getRuleIndex(self):
            return clle_parser.RULE_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop" ):
                listener.enterLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop" ):
                listener.exitLoop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop" ):
                return visitor.visitLoop(self)
            else:
                return visitor.visitChildren(self)




    def loop(self):

        localctx = clle_parser.LoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(clle_parser.DOWHILE)
            self.state = 94
            self.match(clle_parser.COND)
            self.state = 95
            self.match(clle_parser.LPAREN)
            self.state = 96
            self.condition()
            self.state = 97
            self.match(clle_parser.RPAREN)
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 5771362304) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & 844424930131969) != 0):
                self.state = 98
                self.statement()
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 104
            self.match(clle_parser.ENDDO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(clle_parser.IF, 0)

        def COND(self):
            return self.getToken(clle_parser.COND, 0)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(clle_parser.LPAREN)
            else:
                return self.getToken(clle_parser.LPAREN, i)

        def condition(self):
            return self.getTypedRuleContext(clle_parser.ConditionContext,0)


        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(clle_parser.RPAREN)
            else:
                return self.getToken(clle_parser.RPAREN, i)

        def THEN(self):
            return self.getToken(clle_parser.THEN, 0)

        def DO(self):
            return self.getToken(clle_parser.DO, 0)

        def ENDDO(self):
            return self.getToken(clle_parser.ENDDO, 0)

        def ENDIF(self):
            return self.getToken(clle_parser.ENDIF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(clle_parser.StatementContext)
            else:
                return self.getTypedRuleContext(clle_parser.StatementContext,i)


        def ELSE(self):
            return self.getToken(clle_parser.ELSE, 0)

        def getRuleIndex(self):
            return clle_parser.RULE_conditional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional" ):
                listener.enterConditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional" ):
                listener.exitConditional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditional" ):
                return visitor.visitConditional(self)
            else:
                return visitor.visitChildren(self)




    def conditional(self):

        localctx = clle_parser.ConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(clle_parser.IF)
            self.state = 107
            self.match(clle_parser.COND)
            self.state = 108
            self.match(clle_parser.LPAREN)
            self.state = 109
            self.condition()
            self.state = 110
            self.match(clle_parser.RPAREN)
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 111
                self.match(clle_parser.THEN)
                self.state = 112
                self.match(clle_parser.LPAREN)
                self.state = 113
                self.match(clle_parser.DO)
                self.state = 114
                self.match(clle_parser.RPAREN)
                self.state = 118
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 5771362304) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & 844424930131969) != 0):
                    self.state = 115
                    self.statement()
                    self.state = 120
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 121
                self.match(clle_parser.ENDDO)
                pass

            elif la_ == 2:
                self.state = 122
                self.match(clle_parser.THEN)
                self.state = 126
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 5771362304) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & 844424930131969) != 0):
                    self.state = 123
                    self.statement()
                    self.state = 128
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 136
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==35:
                    self.state = 129
                    self.match(clle_parser.ELSE)
                    self.state = 133
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 5771362304) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & 844424930131969) != 0):
                        self.state = 130
                        self.statement()
                        self.state = 135
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 138
                self.match(clle_parser.ENDIF)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(clle_parser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(clle_parser.COLON, 0)

        def statement(self):
            return self.getTypedRuleContext(clle_parser.StatementContext,0)


        def getRuleIndex(self):
            return clle_parser.RULE_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabel" ):
                listener.enterLabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabel" ):
                listener.exitLabel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabel" ):
                return visitor.visitLabel(self)
            else:
                return visitor.visitChildren(self)




    def label(self):

        localctx = clle_parser.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(clle_parser.IDENTIFIER)
            self.state = 142
            self.match(clle_parser.COLON)
            self.state = 143
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PgmStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PGM(self):
            return self.getToken(clle_parser.PGM, 0)

        def ENDPGM(self):
            return self.getToken(clle_parser.ENDPGM, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(clle_parser.StatementContext)
            else:
                return self.getTypedRuleContext(clle_parser.StatementContext,i)


        def getRuleIndex(self):
            return clle_parser.RULE_pgmStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPgmStatement" ):
                listener.enterPgmStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPgmStatement" ):
                listener.exitPgmStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPgmStatement" ):
                return visitor.visitPgmStatement(self)
            else:
                return visitor.visitChildren(self)




    def pgmStatement(self):

        localctx = clle_parser.PgmStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_pgmStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(clle_parser.PGM)
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 5771362304) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & 844424930131969) != 0):
                self.state = 146
                self.statement()
                self.state = 151
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 152
            self.match(clle_parser.ENDPGM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMAND(self):
            return self.getToken(clle_parser.COMMAND, 0)

        def commandParam(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(clle_parser.CommandParamContext)
            else:
                return self.getTypedRuleContext(clle_parser.CommandParamContext,i)


        def RETURN(self):
            return self.getToken(clle_parser.RETURN, 0)

        def getRuleIndex(self):
            return clle_parser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommand" ):
                return visitor.visitCommand(self)
            else:
                return visitor.visitChildren(self)




    def command(self):

        localctx = clle_parser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_command)
        try:
            self.state = 162
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [114]:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self.match(clle_parser.COMMAND)
                self.state = 158
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 155
                        self.commandParam() 
                    self.state = 160
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

                pass
            elif token in [65]:
                self.enterOuterAlt(localctx, 2)
                self.state = 161
                self.match(clle_parser.RETURN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARAMETER(self):
            return self.getToken(clle_parser.PARAMETER, 0)

        def LPAREN(self):
            return self.getToken(clle_parser.LPAREN, 0)

        def paramValue(self):
            return self.getTypedRuleContext(clle_parser.ParamValueContext,0)


        def RPAREN(self):
            return self.getToken(clle_parser.RPAREN, 0)

        def EQUALS(self):
            return self.getToken(clle_parser.EQUALS, 0)

        def expression(self):
            return self.getTypedRuleContext(clle_parser.ExpressionContext,0)


        def getRuleIndex(self):
            return clle_parser.RULE_commandParam

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommandParam" ):
                listener.enterCommandParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommandParam" ):
                listener.exitCommandParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommandParam" ):
                return visitor.visitCommandParam(self)
            else:
                return visitor.visitChildren(self)




    def commandParam(self):

        localctx = clle_parser.CommandParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_commandParam)
        try:
            self.state = 178
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.match(clle_parser.PARAMETER)
                self.state = 171
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                if la_ == 1:
                    self.state = 165
                    self.match(clle_parser.LPAREN)
                    self.state = 166
                    self.paramValue()
                    self.state = 167
                    self.match(clle_parser.RPAREN)

                elif la_ == 2:
                    self.state = 169
                    self.match(clle_parser.EQUALS)
                    self.state = 170
                    self.expression()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
                self.match(clle_parser.LPAREN)
                self.state = 174
                self.paramValue()
                self.state = 175
                self.match(clle_parser.RPAREN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 177
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(clle_parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(clle_parser.ExpressionContext,i)


        def getRuleIndex(self):
            return clle_parser.RULE_paramValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamValue" ):
                listener.enterParamValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamValue" ):
                listener.exitParamValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamValue" ):
                return visitor.visitParamValue(self)
            else:
                return visitor.visitChildren(self)




    def paramValue(self):

        localctx = clle_parser.ParamValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_paramValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 180
                self.expression()
                self.state = 183 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 262206) != 0) or ((((_la - 98)) & ~0x3f) == 0 and ((1 << (_la - 98)) & 65535) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(clle_parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(clle_parser.ExpressionContext,i)


        def EQ(self):
            return self.getToken(clle_parser.EQ, 0)

        def NE(self):
            return self.getToken(clle_parser.NE, 0)

        def GT(self):
            return self.getToken(clle_parser.GT, 0)

        def LT(self):
            return self.getToken(clle_parser.LT, 0)

        def GE(self):
            return self.getToken(clle_parser.GE, 0)

        def LE(self):
            return self.getToken(clle_parser.LE, 0)

        def ASTERISK_GT(self):
            return self.getToken(clle_parser.ASTERISK_GT, 0)

        def ASTERISK_LT(self):
            return self.getToken(clle_parser.ASTERISK_LT, 0)

        def ASTERISK_GE(self):
            return self.getToken(clle_parser.ASTERISK_GE, 0)

        def ASTERISK_LE(self):
            return self.getToken(clle_parser.ASTERISK_LE, 0)

        def ASTERISK_EQ(self):
            return self.getToken(clle_parser.ASTERISK_EQ, 0)

        def ASTERISK_NE(self):
            return self.getToken(clle_parser.ASTERISK_NE, 0)

        def getRuleIndex(self):
            return clle_parser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = clle_parser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.expression()
            self.state = 186
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 258048) != 0) or ((((_la - 89)) & ~0x3f) == 0 and ((1 << (_la - 89)) & 63) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 187
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(clle_parser.STRING, 0)

        def NUMBER(self):
            return self.getToken(clle_parser.NUMBER, 0)

        def VARIABLE(self):
            return self.getToken(clle_parser.VARIABLE, 0)

        def PARAMETER(self):
            return self.getToken(clle_parser.PARAMETER, 0)

        def LPAREN(self):
            return self.getToken(clle_parser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(clle_parser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(clle_parser.RPAREN, 0)

        def ASTERISK(self):
            return self.getToken(clle_parser.ASTERISK, 0)

        def PERCENT_LEN(self):
            return self.getToken(clle_parser.PERCENT_LEN, 0)

        def PERCENT_TRIM(self):
            return self.getToken(clle_parser.PERCENT_TRIM, 0)

        def PERCENT_TRIML(self):
            return self.getToken(clle_parser.PERCENT_TRIML, 0)

        def PERCENT_TRIMR(self):
            return self.getToken(clle_parser.PERCENT_TRIMR, 0)

        def PERCENT_UPPER(self):
            return self.getToken(clle_parser.PERCENT_UPPER, 0)

        def PERCENT_LOWER(self):
            return self.getToken(clle_parser.PERCENT_LOWER, 0)

        def PERCENT_SCAN(self):
            return self.getToken(clle_parser.PERCENT_SCAN, 0)

        def PERCENT_REPLACE(self):
            return self.getToken(clle_parser.PERCENT_REPLACE, 0)

        def PERCENT_SUBST(self):
            return self.getToken(clle_parser.PERCENT_SUBST, 0)

        def PERCENT_INT(self):
            return self.getToken(clle_parser.PERCENT_INT, 0)

        def PERCENT_FLOAT(self):
            return self.getToken(clle_parser.PERCENT_FLOAT, 0)

        def PERCENT_CHAR(self):
            return self.getToken(clle_parser.PERCENT_CHAR, 0)

        def PERCENT_DATE(self):
            return self.getToken(clle_parser.PERCENT_DATE, 0)

        def PERCENT_TIME(self):
            return self.getToken(clle_parser.PERCENT_TIME, 0)

        def PERCENT_TIMESTAMP(self):
            return self.getToken(clle_parser.PERCENT_TIMESTAMP, 0)

        def IDENTIFIER(self):
            return self.getToken(clle_parser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return clle_parser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = clle_parser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_expression)
        try:
            self.state = 274
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                self.match(clle_parser.STRING)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 190
                self.match(clle_parser.NUMBER)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 191
                self.match(clle_parser.VARIABLE)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 4)
                self.state = 192
                self.match(clle_parser.PARAMETER)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 5)
                self.state = 193
                self.match(clle_parser.LPAREN)
                self.state = 194
                self.expression()
                self.state = 195
                self.match(clle_parser.RPAREN)
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 6)
                self.state = 197
                self.match(clle_parser.ASTERISK)
                pass
            elif token in [98]:
                self.enterOuterAlt(localctx, 7)
                self.state = 198
                self.match(clle_parser.PERCENT_LEN)
                self.state = 199
                self.match(clle_parser.LPAREN)
                self.state = 200
                self.expression()
                self.state = 201
                self.match(clle_parser.RPAREN)
                pass
            elif token in [99]:
                self.enterOuterAlt(localctx, 8)
                self.state = 203
                self.match(clle_parser.PERCENT_TRIM)
                self.state = 204
                self.match(clle_parser.LPAREN)
                self.state = 205
                self.expression()
                self.state = 206
                self.match(clle_parser.RPAREN)
                pass
            elif token in [100]:
                self.enterOuterAlt(localctx, 9)
                self.state = 208
                self.match(clle_parser.PERCENT_TRIML)
                self.state = 209
                self.match(clle_parser.LPAREN)
                self.state = 210
                self.expression()
                self.state = 211
                self.match(clle_parser.RPAREN)
                pass
            elif token in [101]:
                self.enterOuterAlt(localctx, 10)
                self.state = 213
                self.match(clle_parser.PERCENT_TRIMR)
                self.state = 214
                self.match(clle_parser.LPAREN)
                self.state = 215
                self.expression()
                self.state = 216
                self.match(clle_parser.RPAREN)
                pass
            elif token in [102]:
                self.enterOuterAlt(localctx, 11)
                self.state = 218
                self.match(clle_parser.PERCENT_UPPER)
                self.state = 219
                self.match(clle_parser.LPAREN)
                self.state = 220
                self.expression()
                self.state = 221
                self.match(clle_parser.RPAREN)
                pass
            elif token in [103]:
                self.enterOuterAlt(localctx, 12)
                self.state = 223
                self.match(clle_parser.PERCENT_LOWER)
                self.state = 224
                self.match(clle_parser.LPAREN)
                self.state = 225
                self.expression()
                self.state = 226
                self.match(clle_parser.RPAREN)
                pass
            elif token in [104]:
                self.enterOuterAlt(localctx, 13)
                self.state = 228
                self.match(clle_parser.PERCENT_SCAN)
                self.state = 229
                self.match(clle_parser.LPAREN)
                self.state = 230
                self.expression()
                self.state = 231
                self.match(clle_parser.RPAREN)
                pass
            elif token in [105]:
                self.enterOuterAlt(localctx, 14)
                self.state = 233
                self.match(clle_parser.PERCENT_REPLACE)
                self.state = 234
                self.match(clle_parser.LPAREN)
                self.state = 235
                self.expression()
                self.state = 236
                self.match(clle_parser.RPAREN)
                pass
            elif token in [106]:
                self.enterOuterAlt(localctx, 15)
                self.state = 238
                self.match(clle_parser.PERCENT_SUBST)
                self.state = 239
                self.match(clle_parser.LPAREN)
                self.state = 240
                self.expression()
                self.state = 241
                self.match(clle_parser.RPAREN)
                pass
            elif token in [107]:
                self.enterOuterAlt(localctx, 16)
                self.state = 243
                self.match(clle_parser.PERCENT_INT)
                self.state = 244
                self.match(clle_parser.LPAREN)
                self.state = 245
                self.expression()
                self.state = 246
                self.match(clle_parser.RPAREN)
                pass
            elif token in [108]:
                self.enterOuterAlt(localctx, 17)
                self.state = 248
                self.match(clle_parser.PERCENT_FLOAT)
                self.state = 249
                self.match(clle_parser.LPAREN)
                self.state = 250
                self.expression()
                self.state = 251
                self.match(clle_parser.RPAREN)
                pass
            elif token in [109]:
                self.enterOuterAlt(localctx, 18)
                self.state = 253
                self.match(clle_parser.PERCENT_CHAR)
                self.state = 254
                self.match(clle_parser.LPAREN)
                self.state = 255
                self.expression()
                self.state = 256
                self.match(clle_parser.RPAREN)
                pass
            elif token in [110]:
                self.enterOuterAlt(localctx, 19)
                self.state = 258
                self.match(clle_parser.PERCENT_DATE)
                self.state = 259
                self.match(clle_parser.LPAREN)
                self.state = 260
                self.expression()
                self.state = 261
                self.match(clle_parser.RPAREN)
                pass
            elif token in [111]:
                self.enterOuterAlt(localctx, 20)
                self.state = 263
                self.match(clle_parser.PERCENT_TIME)
                self.state = 264
                self.match(clle_parser.LPAREN)
                self.state = 265
                self.expression()
                self.state = 266
                self.match(clle_parser.RPAREN)
                pass
            elif token in [112]:
                self.enterOuterAlt(localctx, 21)
                self.state = 268
                self.match(clle_parser.PERCENT_TIMESTAMP)
                self.state = 269
                self.match(clle_parser.LPAREN)
                self.state = 270
                self.expression()
                self.state = 271
                self.match(clle_parser.RPAREN)
                pass
            elif token in [113]:
                self.enterOuterAlt(localctx, 22)
                self.state = 273
                self.match(clle_parser.IDENTIFIER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHAR(self):
            return self.getToken(clle_parser.CHAR, 0)

        def VARCHAR(self):
            return self.getToken(clle_parser.VARCHAR, 0)

        def DECIMAL(self):
            return self.getToken(clle_parser.DECIMAL, 0)

        def PACKED(self):
            return self.getToken(clle_parser.PACKED, 0)

        def ZONED(self):
            return self.getToken(clle_parser.ZONED, 0)

        def BINARY(self):
            return self.getToken(clle_parser.BINARY, 0)

        def INTEGER(self):
            return self.getToken(clle_parser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(clle_parser.FLOAT, 0)

        def DATE(self):
            return self.getToken(clle_parser.DATE, 0)

        def TIME(self):
            return self.getToken(clle_parser.TIME, 0)

        def TIMESTAMP(self):
            return self.getToken(clle_parser.TIMESTAMP, 0)

        def getRuleIndex(self):
            return clle_parser.RULE_dataType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDataType" ):
                listener.enterDataType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDataType" ):
                listener.exitDataType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDataType" ):
                return visitor.visitDataType(self)
            else:
                return visitor.visitChildren(self)




    def dataType(self):

        localctx = clle_parser.DataTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_dataType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            _la = self._input.LA(1)
            if not(((((_la - 78)) & ~0x3f) == 0 and ((1 << (_la - 78)) & 2047) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StartValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(clle_parser.NUMBER, 0)

        def getRuleIndex(self):
            return clle_parser.RULE_startValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStartValue" ):
                listener.enterStartValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStartValue" ):
                listener.exitStartValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStartValue" ):
                return visitor.visitStartValue(self)
            else:
                return visitor.visitChildren(self)




    def startValue(self):

        localctx = clle_parser.StartValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_startValue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(clle_parser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EndValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(clle_parser.NUMBER, 0)

        def getRuleIndex(self):
            return clle_parser.RULE_endValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEndValue" ):
                listener.enterEndValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEndValue" ):
                listener.exitEndValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEndValue" ):
                return visitor.visitEndValue(self)
            else:
                return visitor.visitChildren(self)




    def endValue(self):

        localctx = clle_parser.EndValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_endValue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.match(clle_parser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StepValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(clle_parser.NUMBER, 0)

        def getRuleIndex(self):
            return clle_parser.RULE_stepValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStepValue" ):
                listener.enterStepValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStepValue" ):
                listener.exitStepValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStepValue" ):
                return visitor.visitStepValue(self)
            else:
                return visitor.visitChildren(self)




    def stepValue(self):

        localctx = clle_parser.StepValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_stepValue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.match(clle_parser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





