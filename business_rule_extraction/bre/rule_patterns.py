"""
Comprehensive Business Rule Patterns for AS400 Code

This module contains extensive rule patterns for CL, RPG, DB2, and DSPF
based on IBM i best practices and common business logic patterns.
"""

from typing import Dict, List, Any
from enum import Enum

class RulePattern(Enum):
    """Comprehensive rule pattern categories for AS400 code."""
    
    # CL Rule Patterns
    CL_FILE_VALIDATION = "cl_file_validation"
    CL_ERROR_HANDLING = "cl_error_handling"
    CL_DATA_VALIDATION = "cl_data_validation"
    CL_WORKFLOW_CONTROL = "cl_workflow_control"
    CL_SECURITY_CHECKS = "cl_security_checks"
    CL_BUSINESS_CALCULATION = "cl_business_calculation"
    
    # RPG Rule Patterns
    RPG_FIELD_VALIDATION = "rpg_field_validation"
    RPG_CALCULATION_RULES = "rpg_calculation_rules"
    RPG_FILE_OPERATIONS = "rpg_file_operations"
    RPG_INDICATOR_LOGIC = "rpg_indicator_logic"
    RPG_PROCEDURE_CALLS = "rpg_procedure_calls"
    RPG_DATA_TRANSFORMATION = "rpg_data_transformation"
    
    # DB2 Rule Patterns
    DB2_CONSTRAINT_VALIDATION = "db2_constraint_validation"
    DB2_TRIGGER_BUSINESS_RULES = "db2_trigger_business_rules"
    DB2_STORED_PROCEDURE_LOGIC = "db2_stored_procedure_logic"
    DB2_DATA_INTEGRITY = "db2_data_integrity"
    DB2_BUSINESS_CALCULATIONS = "db2_business_calculations"
    DB2_ACCESS_CONTROL = "db2_access_control"
    
    # DSPF Rule Patterns
    DSPF_FIELD_VALIDATION = "dspf_field_validation"
    DSPF_INDICATOR_CONDITIONS = "dspf_indicator_conditions"
    DSPF_USER_INTERFACE_RULES = "dspf_user_interface_rules"
    DSPF_DATA_ENTRY_RULES = "dspf_data_entry_rules"
    DSPF_FUNCTION_KEY_HANDLING = "dspf_function_key_handling"

class AS400RulePatterns:
    """Comprehensive rule pattern library for AS400 business rules."""
    
    def __init__(self):
        self.cl_patterns = self._initialize_cl_patterns()
        self.rpg_patterns = self._initialize_rpg_patterns()
        self.db2_patterns = self._initialize_db2_patterns()
        self.dspf_patterns = self._initialize_dspf_patterns()
    
    def _initialize_cl_patterns(self) -> Dict[str, List[Dict]]:
        """Initialize comprehensive CL rule patterns."""
        return {
            RulePattern.CL_FILE_VALIDATION.value: [
                {
                    "pattern": "CHKOBJ",
                    "description": "Check if object exists before operation",
                    "business_rule": "Object existence validation",
                    "priority": "HIGH",
                    "example": "CHKOBJ OBJ(&LIBRARY/&FILE) OBJTYPE(*FILE)"
                },
                {
                    "pattern": "RTVOBJD",
                    "description": "Retrieve object description for validation",
                    "business_rule": "Object metadata validation",
                    "priority": "MEDIUM",
                    "example": "RTVOBJD OBJ(&LIBRARY/&FILE) OBJTYPE(*FILE) RTNLIB(&SRC_LIB)"
                }
            ],
            RulePattern.CL_ERROR_HANDLING.value: [
                {
                    "pattern": "MONMSG",
                    "description": "Monitor for specific error messages",
                    "business_rule": "Error handling and recovery",
                    "priority": "CRITICAL",
                    "example": "MONMSG MSGID(CPF0000) EXEC(GOTO ERROR_HANDLER)"
                },
                {
                    "pattern": "SNDPGMMSG",
                    "description": "Send program messages for error reporting",
                    "business_rule": "Error communication",
                    "priority": "HIGH",
                    "example": "SNDPGMMSG MSG('File not found') MSGTYPE(*ESCAPE)"
                }
            ],
            RulePattern.CL_DATA_VALIDATION.value: [
                {
                    "pattern": "IF COND",
                    "description": "Conditional data validation",
                    "business_rule": "Business rule validation",
                    "priority": "HIGH",
                    "example": "IF COND(&AMOUNT *GT 0) THEN(DO)"
                },
                {
                    "pattern": "CHGVAR",
                    "description": "Variable assignment with validation",
                    "business_rule": "Data transformation",
                    "priority": "MEDIUM",
                    "example": "CHGVAR VAR(&RESULT) VALUE(&AMOUNT * 1.05)"
                }
            ],
            RulePattern.CL_WORKFLOW_CONTROL.value: [
                {
                    "pattern": "CALL PGM",
                    "description": "Program call workflow",
                    "business_rule": "Business process flow",
                    "priority": "HIGH",
                    "example": "CALL PGM(ORDERPROC) PARM(&ORDER &STATUS)"
                },
                {
                    "pattern": "GOTO CMDLBL",
                    "description": "Control flow transfer",
                    "business_rule": "Process routing",
                    "priority": "MEDIUM",
                    "example": "GOTO CMDLBL(PROCESS_COMPLETE)"
                }
            ],
            RulePattern.CL_SECURITY_CHECKS.value: [
                {
                    "pattern": "CHKUSRPRF",
                    "description": "Check user profile authorization",
                    "business_rule": "Security validation",
                    "priority": "CRITICAL",
                    "example": "CHKUSRPRF USRPRF(&USER) AUT(*CHANGE)"
                },
                {
                    "pattern": "RTVDTAARA",
                    "description": "Retrieve data area for security checks",
                    "business_rule": "Access control validation",
                    "priority": "HIGH",
                    "example": "RTVDTAARA DTAARA(SECURITY/&USER) RTNVAR(&ACCESS)"
                }
            ],
            RulePattern.CL_BUSINESS_CALCULATION.value: [
                {
                    "pattern": "CHGVAR VAR",
                    "description": "Business calculations",
                    "business_rule": "Business logic computation",
                    "priority": "MEDIUM",
                    "example": "CHGVAR VAR(&TOTAL) VALUE(&SUBTOTAL * 1.07)"
                },
                {
                    "pattern": "RTVSYSVAL",
                    "description": "System value retrieval for calculations",
                    "business_rule": "System-based calculations",
                    "priority": "LOW",
                    "example": "RTVSYSVAL SYSVAL(QDAT) RTNVAR(&CURRENT_DATE)"
                }
            ]
        }
    
    def _initialize_rpg_patterns(self) -> Dict[str, List[Dict]]:
        """Initialize comprehensive RPG rule patterns."""
        return {
            RulePattern.RPG_FIELD_VALIDATION.value: [
                {
                    "pattern": "CHAIN",
                    "description": "Chain to file for record validation",
                    "business_rule": "Record existence validation",
                    "priority": "CRITICAL",
                    "example": "CHAIN CUSTMAST 90"
                },
                {
                    "pattern": "SETLL",
                    "description": "Set lower limit for range validation",
                    "business_rule": "Range validation",
                    "priority": "HIGH",
                    "example": "SETLL (CUSTNO) CUSTMAST"
                },
                {
                    "pattern": "CHECK",
                    "description": "Check indicator for validation",
                    "business_rule": "Field validation",
                    "priority": "HIGH",
                    "example": "CHECK AMOUNT > 0 90"
                }
            ],
            RulePattern.RPG_CALCULATION_RULES.value: [
                {
                    "pattern": "EVAL",
                    "description": "Expression evaluation for calculations",
                    "business_rule": "Business calculation",
                    "priority": "MEDIUM",
                    "example": "EVAL TOTAL = SUBTOTAL * TAX_RATE"
                },
                {
                    "pattern": "Z-ADD",
                    "description": "Zero-suppressed addition",
                    "business_rule": "Numeric calculation",
                    "priority": "MEDIUM",
                    "example": "Z-ADD AMOUNT TOTAL"
                },
                {
                    "pattern": "MULT",
                    "description": "Multiplication operation",
                    "business_rule": "Business calculation",
                    "priority": "MEDIUM",
                    "example": "MULT AMOUNT TAX_RATE TAX_AMOUNT"
                }
            ],
            RulePattern.RPG_FILE_OPERATIONS.value: [
                {
                    "pattern": "READ",
                    "description": "Read record from file",
                    "business_rule": "Data retrieval",
                    "priority": "HIGH",
                    "example": "READ CUSTMAST 90"
                },
                {
                    "pattern": "WRITE",
                    "description": "Write record to file",
                    "business_rule": "Data persistence",
                    "priority": "HIGH",
                    "example": "WRITE ORDERHDR 90"
                },
                {
                    "pattern": "UPDATE",
                    "description": "Update existing record",
                    "business_rule": "Data modification",
                    "priority": "HIGH",
                    "example": "UPDATE CUSTMAST 90"
                },
                {
                    "pattern": "DELETE",
                    "description": "Delete record from file",
                    "business_rule": "Data removal",
                    "priority": "HIGH",
                    "example": "DELETE CUSTMAST 90"
                }
            ],
            RulePattern.RPG_INDICATOR_LOGIC.value: [
                {
                    "pattern": "IF",
                    "description": "Conditional indicator logic",
                    "business_rule": "Conditional processing",
                    "priority": "HIGH",
                    "example": "IF *IN90"
                },
                {
                    "pattern": "SETON",
                    "description": "Set indicator on",
                    "business_rule": "Status indication",
                    "priority": "MEDIUM",
                    "example": "SETON 90"
                },
                {
                    "pattern": "SETOFF",
                    "description": "Set indicator off",
                    "business_rule": "Status indication",
                    "priority": "MEDIUM",
                    "example": "SETOFF 90"
                }
            ],
            RulePattern.RPG_PROCEDURE_CALLS.value: [
                {
                    "pattern": "CALLP",
                    "description": "Call procedure with parameters",
                    "business_rule": "Business process invocation",
                    "priority": "HIGH",
                    "example": "CALLP CALC_TAX(SUBTOTAL:TAX_AMOUNT)"
                },
                {
                    "pattern": "CALLB",
                    "description": "Call bound procedure",
                    "business_rule": "System integration",
                    "priority": "MEDIUM",
                    "example": "CALLB 'CALC_TAX' 2 SUBTOTAL TAX_AMOUNT"
                }
            ],
            RulePattern.RPG_DATA_TRANSFORMATION.value: [
                {
                    "pattern": "MOVE",
                    "description": "Move data between fields",
                    "business_rule": "Data transformation",
                    "priority": "MEDIUM",
                    "example": "MOVE INPUT_FIELD OUTPUT_FIELD"
                },
                {
                    "pattern": "MOVEL",
                    "description": "Move left-justified",
                    "business_rule": "Data formatting",
                    "priority": "LOW",
                    "example": "MOVEL NAME FORMATTED_NAME"
                },
                {
                    "pattern": "CAT",
                    "description": "Concatenate strings",
                    "business_rule": "Data combination",
                    "priority": "LOW",
                    "example": "CAT FIRST_NAME LAST_NAME FULL_NAME"
                }
            ]
        }
    
    def _initialize_db2_patterns(self) -> Dict[str, List[Dict]]:
        """Initialize comprehensive DB2 rule patterns."""
        return {
            RulePattern.DB2_CONSTRAINT_VALIDATION.value: [
                {
                    "pattern": "CHECK",
                    "description": "Check constraint for data validation",
                    "business_rule": "Data integrity validation",
                    "priority": "CRITICAL",
                    "example": "CHECK (AMOUNT > 0 AND AMOUNT <= 999999.99)"
                },
                {
                    "pattern": "NOT NULL",
                    "description": "Null value constraint",
                    "business_rule": "Required field validation",
                    "priority": "HIGH",
                    "example": "CUSTOMER_NAME VARCHAR(50) NOT NULL"
                },
                {
                    "pattern": "UNIQUE",
                    "description": "Unique constraint",
                    "business_rule": "Uniqueness validation",
                    "priority": "HIGH",
                    "example": "UNIQUE (CUSTOMER_ID)"
                },
                {
                    "pattern": "FOREIGN KEY",
                    "description": "Foreign key constraint",
                    "business_rule": "Referential integrity",
                    "priority": "CRITICAL",
                    "example": "FOREIGN KEY (CUSTOMER_ID) REFERENCES CUSTOMERS(CUSTOMER_ID)"
                }
            ],
            RulePattern.DB2_TRIGGER_BUSINESS_RULES.value: [
                {
                    "pattern": "CREATE TRIGGER",
                    "description": "Trigger for business rule enforcement",
                    "business_rule": "Automated business logic",
                    "priority": "CRITICAL",
                    "example": "CREATE TRIGGER ORDER_VALIDATION BEFORE INSERT ON ORDERS"
                },
                {
                    "pattern": "BEFORE INSERT",
                    "description": "Pre-insert validation trigger",
                    "business_rule": "Data validation before insert",
                    "priority": "HIGH",
                    "example": "BEFORE INSERT ON ORDERS FOR EACH ROW BEGIN"
                },
                {
                    "pattern": "AFTER UPDATE",
                    "description": "Post-update business logic",
                    "business_rule": "Business process after update",
                    "priority": "MEDIUM",
                    "example": "AFTER UPDATE ON CUSTOMERS FOR EACH ROW BEGIN"
                }
            ],
            RulePattern.DB2_STORED_PROCEDURE_LOGIC.value: [
                {
                    "pattern": "CREATE PROCEDURE",
                    "description": "Stored procedure for business logic",
                    "business_rule": "Encapsulated business process",
                    "priority": "HIGH",
                    "example": "CREATE PROCEDURE CALCULATE_ORDER_TOTAL (IN ORDER_ID INT)"
                },
                {
                    "pattern": "DECLARE CURSOR",
                    "description": "Cursor for data processing",
                    "business_rule": "Batch processing logic",
                    "priority": "MEDIUM",
                    "example": "DECLARE CURSOR_ORDER CURSOR FOR SELECT * FROM ORDERS"
                },
                {
                    "pattern": "IF THEN ELSE",
                    "description": "Conditional logic in procedures",
                    "business_rule": "Business rule validation",
                    "priority": "HIGH",
                    "example": "IF ORDER_TOTAL > 10000 THEN SET DISCOUNT = 0.10"
                }
            ],
            RulePattern.DB2_DATA_INTEGRITY.value: [
                {
                    "pattern": "PRIMARY KEY",
                    "description": "Primary key constraint",
                    "business_rule": "Entity integrity",
                    "priority": "CRITICAL",
                    "example": "PRIMARY KEY (ORDER_ID)"
                },
                {
                    "pattern": "REFERENCES",
                    "description": "Referential integrity",
                    "business_rule": "Relationship integrity",
                    "priority": "CRITICAL",
                    "example": "CUSTOMER_ID INT REFERENCES CUSTOMERS(CUSTOMER_ID)"
                }
            ],
            RulePattern.DB2_BUSINESS_CALCULATIONS.value: [
                {
                    "pattern": "CASE WHEN",
                    "description": "Conditional calculation",
                    "business_rule": "Business rule calculation",
                    "priority": "MEDIUM",
                    "example": "CASE WHEN AMOUNT > 1000 THEN AMOUNT * 0.95 ELSE AMOUNT END"
                },
                {
                    "pattern": "COALESCE",
                    "description": "Null handling in calculations",
                    "business_rule": "Data handling logic",
                    "priority": "MEDIUM",
                    "example": "COALESCE(DISCOUNT, 0)"
                }
            ],
            RulePattern.DB2_ACCESS_CONTROL.value: [
                {
                    "pattern": "GRANT",
                    "description": "Grant access permissions",
                    "business_rule": "Access control",
                    "priority": "CRITICAL",
                    "example": "GRANT SELECT ON ORDERS TO ORDER_CLERK"
                },
                {
                    "pattern": "REVOKE",
                    "description": "Revoke access permissions",
                    "business_rule": "Access control",
                    "priority": "CRITICAL",
                    "example": "REVOKE INSERT ON ORDERS FROM ORDER_CLERK"
                }
            ]
        }
    
    def _initialize_dspf_patterns(self) -> Dict[str, List[Dict]]:
        """Initialize comprehensive DSPF rule patterns."""
        return {
            RulePattern.DSPF_FIELD_VALIDATION.value: [
                {
                    "pattern": "CHECK(VN)",
                    "description": "Field validation check",
                    "business_rule": "Input validation",
                    "priority": "HIGH",
                    "example": "CHECK(VN) 90"
                },
                {
                    "pattern": "COMP",
                    "description": "Field comparison",
                    "business_rule": "Data comparison validation",
                    "priority": "MEDIUM",
                    "example": "COMP(EQ FIELD1 FIELD2 90)"
                },
                {
                    "pattern": "RANGE",
                    "description": "Range validation",
                    "business_rule": "Range check validation",
                    "priority": "HIGH",
                    "example": "RANGE(1 9999 AMOUNT 90)"
                }
            ],
            RulePattern.DSPF_INDICATOR_CONDITIONS.value: [
                {
                    "pattern": "INDARA",
                    "description": "Indicator array usage",
                    "business_rule": "Conditional display logic",
                    "priority": "MEDIUM",
                    "example": "INDARA"
                },
                {
                    "pattern": "SETON",
                    "description": "Set indicator on condition",
                    "business_rule": "Display control",
                    "priority": "MEDIUM",
                    "example": "SETON(90)"
                },
                {
                    "pattern": "SETOFF",
                    "description": "Set indicator off condition",
                    "business_rule": "Display control",
                    "priority": "MEDIUM",
                    "example": "SETOFF(90)"
                }
            ],
            RulePattern.DSPF_USER_INTERFACE_RULES.value: [
                {
                    "pattern": "DSPATR",
                    "description": "Display attributes",
                    "business_rule": "UI formatting rules",
                    "priority": "LOW",
                    "example": "DSPATR(HI)"
                },
                {
                    "pattern": "COLOR",
                    "description": "Color display attributes",
                    "business_rule": "UI color coding",
                    "priority": "LOW",
                    "example": "COLOR(RED)"
                },
                {
                    "pattern": "EDTCDE",
                    "description": "Editing codes for display",
                    "business_rule": "Data formatting",
                    "priority": "MEDIUM",
                    "example": "EDTCDE(Z)"
                }
            ],
            RulePattern.DSPF_DATA_ENTRY_RULES.value: [
                {
                    "pattern": "VALUES",
                    "description": "Valid values for field",
                    "business_rule": "Input constraint",
                    "priority": "HIGH",
                    "example": "VALUES('Y' 'N')"
                },
                {
                    "pattern": "DFT",
                    "description": "Default value",
                    "business_rule": "Default value logic",
                    "priority": "MEDIUM",
                    "example": "DFT('N')"
                },
                {
                    "pattern": "INZ",
                    "description": "Initialize field",
                    "business_rule": "Field initialization",
                    "priority": "LOW",
                    "example": "INZ('')"
                }
            ],
            RulePattern.DSPF_FUNCTION_KEY_HANDLING.value: [
                {
                    "pattern": "CF",
                    "description": "Command function keys",
                    "business_rule": "Function key handling",
                    "priority": "MEDIUM",
                    "example": "CF03(EXIT)"
                },
                {
                    "pattern": "ENTER",
                    "description": "Enter key handling",
                    "business_rule": "Enter key processing",
                    "priority": "MEDIUM",
                    "example": "ENTER"
                }
            ]
        }
    
    def get_pattern_for_language(self, language: str) -> Dict[str, List[Dict]]:
        """Get rule patterns for a specific language."""
        patterns = {
            'cl': self.cl_patterns,
            'rpg': self.rpg_patterns,
            'db2': self.db2_patterns,
            'dspf': self.dspf_patterns
        }
        return patterns.get(language.lower(), {})
    
    def find_matching_patterns(self, language: str, code_snippet: str) -> List[Dict]:
        """Find patterns that match code snippet."""
        patterns = self.get_pattern_for_language(language)
        matches = []
        
        for category, pattern_list in patterns.items():
            for pattern in pattern_list:
                if pattern['pattern'].lower() in code_snippet.lower():
                    matches.append({
                        'category': category,
                        'pattern': pattern['pattern'],
                        'description': pattern['description'],
                        'business_rule': pattern['business_rule'],
                        'priority': pattern['priority'],
                        'example': pattern['example']
                    })
        
        return matches
