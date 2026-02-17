"""
Business Rule Extraction (BRE) Module for AS400 Parser

Extracts and categorizes business rules from CL, RPG, and DB2 code.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from enum import Enum

class RuleType(Enum):
    VALIDATION = "validation"
    CALCULATION = "calculation"
    WORKFLOW = "workflow"
    ERROR_HANDLING = "error_handling"
    DATA_ACCESS = "data_access"
    INTEGRATION = "integration"
    SECURITY = "security"

class RulePriority(Enum):
    CRITICAL = 1
    HIGH = 2
    MEDIUM = 3
    LOW = 4

@dataclass
class BusinessRule:
    """Represents a business rule extracted from AS400 code."""
    
    rule_id: str
    rule_type: RuleType
    priority: RulePriority
    description: str
    condition: str
    action: str
    source_file: str
    line_number: int
    variables: List[str] = field(default_factory=list)
    files_accessed: List[str] = field(default_factory=list)
    related_rules: List[str] = field(default_factory=list)
    business_context: str = ""
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'rule_id': self.rule_id,
            'rule_type': self.rule_type.value,
            'priority': self.priority.value,
            'description': self.description,
            'condition': self.condition,
            'action': self.action,
            'source_file': self.source_file,
            'line_number': self.line_number,
            'variables': self.variables,
            'files_accessed': self.files_accessed,
            'related_rules': self.related_rules,
            'business_context': self.business_context
        }

@dataclass
class RuleSet:
    """Collection of business rules from a program."""
    
    program_name: str
    rules: List[BusinessRule] = field(default_factory=list)
    dependencies: Dict[str, List[str]] = field(default_factory=dict)
    metrics: Dict[str, int] = field(default_factory=dict)
    
    def add_rule(self, rule: BusinessRule):
        self.rules.append(rule)
        self._update_metrics()
    
    def _update_metrics(self):
        self.metrics = {
            'total_rules': len(self.rules),
            'validation_rules': len([r for r in self.rules if r.rule_type == RuleType.VALIDATION]),
            'calculation_rules': len([r for r in self.rules if r.rule_type == RuleType.CALCULATION]),
            'workflow_rules': len([r for r in self.rules if r.rule_type == RuleType.WORKFLOW]),
            'error_handling_rules': len([r for r in self.rules if r.rule_type == RuleType.ERROR_HANDLING]),
            'data_access_rules': len([r for r in self.rules if r.rule_type == RuleType.DATA_ACCESS]),
            'integration_rules': len([r for r in self.rules if r.rule_type == RuleType.INTEGRATION]),
            'security_rules': len([r for r in self.rules if r.rule_type == RuleType.SECURITY])
        }

class BusinessRuleExtractor:
    """Extracts business rules from AS400 AST."""
    
    def __init__(self):
        self.rule_counter = 0
        self.patterns = self._initialize_patterns()
    
    def _initialize_patterns(self) -> Dict[str, Dict]:
        """Initialize rule extraction patterns."""
        return {
            'cl': {
                'validation': [
                    {'pattern': 'IF COND', 'description': 'Conditional validation'},
                    {'pattern': 'CHGVAR', 'description': 'Variable assignment rule'},
                    {'pattern': 'DCL', 'description': 'Variable declaration rule'}
                ],
                'workflow': [
                    {'pattern': 'CALL PGM', 'description': 'Program call workflow'},
                    {'pattern': 'GOTO CMDLBL', 'description': 'Control flow transfer'},
                    {'pattern': 'DOFOR', 'description': 'Loop workflow'}
                ],
                'error_handling': [
                    {'pattern': 'MONMSG', 'description': 'Error monitoring'},
                    {'pattern': 'SNDPGMMSG', 'description': 'Error messaging'}
                ],
                'data_access': [
                    {'pattern': 'DCLF', 'description': 'File declaration'},
                    {'pattern': 'RTVOBJD', 'description': 'Object description retrieval'},
                    {'pattern': 'CRTDUPOBJ', 'description': 'Object creation'}
                ]
            },
            'rpg': {
                'validation': [
                    {'pattern': 'IF', 'description': 'Conditional validation'},
                    {'pattern': 'CHAIN', 'description': 'Record validation'},
                    {'pattern': 'SETLL', 'description': 'File position validation'}
                ],
                'calculation': [
                    {'pattern': 'EVAL', 'description': 'Calculation operation'},
                    {'pattern': 'MOVE', 'description': 'Data movement'},
                    {'pattern': 'Z-ADD', 'description': 'Numeric addition'}
                ],
                'data_access': [
                    {'pattern': 'READ', 'description': 'File read operation'},
                    {'pattern': 'WRITE', 'description': 'File write operation'},
                    {'pattern': 'UPDATE', 'description': 'File update operation'},
                    {'pattern': 'DELETE', 'description': 'File delete operation'}
                ]
            },
            'db2': {
                'validation': [
                    {'pattern': 'CHECK', 'description': 'Data constraint'},
                    {'pattern': 'WHERE', 'description': 'Data filtering'}
                ],
                'data_access': [
                    {'pattern': 'SELECT', 'description': 'Data retrieval'},
                    {'pattern': 'INSERT', 'description': 'Data insertion'},
                    {'pattern': 'UPDATE', 'description': 'Data modification'},
                    {'pattern': 'DELETE', 'description': 'Data deletion'}
                ],
                'security': [
                    {'pattern': 'GRANT', 'description': 'Permission grant'},
                    {'pattern': 'REVOKE', 'description': 'Permission revoke'}
                ]
            }
        }
    
    def extract_from_cl(self, ast, source_file: str) -> RuleSet:
        """Extract business rules from CL AST."""
        rule_set = RuleSet(program_name=source_file)
        
        if not ast or not hasattr(ast, 'commands'):
            return rule_set
        
        for cmd in ast.commands:
            rule = self._extract_cl_rule(cmd, source_file)
            if rule:
                rule_set.add_rule(rule)
        
        return rule_set
    
    def extract_from_rpg(self, ast, source_file: str) -> RuleSet:
        """Extract business rules from RPG AST."""
        rule_set = RuleSet(program_name=source_file)
        
        if not ast:
            return rule_set
        
        # Extract rules from main body
        if hasattr(ast, 'main_body'):
            for stmt in ast.main_body:
                rule = self._extract_rpg_rule(stmt, source_file)
                if rule:
                    rule_set.add_rule(rule)
        
        # Extract rules from procedures
        if hasattr(ast, 'procedures'):
            for proc in ast.procedures:
                if hasattr(proc, 'body'):
                    for stmt in proc.body:
                        rule = self._extract_rpg_rule(stmt, source_file)
                        if rule:
                            rule_set.add_rule(rule)
        
        return rule_set
    
    def extract_from_db2(self, ast, source_file: str) -> RuleSet:
        """Extract business rules from DB2 AST."""
        rule_set = RuleSet(program_name=source_file)
        
        if not ast:
            return rule_set
        
        # Extract rules from SQL statements
        if hasattr(ast, 'statements'):
            for stmt in ast.statements:
                rule = self._extract_db2_rule(stmt, source_file)
                if rule:
                    rule_set.add_rule(rule)
        
        return rule_set
    
    def extract_from_dspf(self, ast, source_file: str) -> RuleSet:
        """Extract business rules from DSPF AST."""
        rule_set = RuleSet(program_name=source_file)
        
        if not ast:
            return rule_set
        
        # Extract rules from screen records and fields
        if hasattr(ast, 'records'):
            for record in ast.records:
                rule = self._extract_dspf_rule(record, source_file)
                if rule:
                    rule_set.add_rule(rule)
        
        return rule_set
    
    def _extract_cl_rule(self, cmd, source_file: str) -> Optional[BusinessRule]:
        """Extract rule from a single CL command."""
        self.rule_counter += 1
        
        # Determine rule type based on command name
        rule_type = self._classify_cl_command(cmd.name)
        
        # Extract condition and action
        condition = self._extract_condition(cmd)
        action = self._extract_action(cmd)
        
        # Extract variables and files
        variables = self._extract_variables(cmd)
        files_accessed = self._extract_files(cmd)
        
        # Generate description
        description = self._generate_description(cmd.name, condition, action)
        
        return BusinessRule(
            rule_id=f"RULE_{self.rule_counter:04d}",
            rule_type=rule_type,
            priority=self._determine_priority(cmd.name),
            description=description,
            condition=condition,
            action=action,
            source_file=source_file,
            line_number=getattr(cmd, 'loc', {}).line if hasattr(cmd, 'loc') else 0,
            variables=variables,
            files_accessed=files_accessed
        )
    
    def _classify_cl_command(self, cmd_name: str) -> RuleType:
        """Classify CL command into rule type."""
        if cmd_name in ['IF', 'COND']:
            return RuleType.VALIDATION
        elif cmd_name in ['CALL', 'GOTO', 'DOFOR', 'DOWHILE']:
            return RuleType.WORKFLOW
        elif cmd_name in ['MONMSG', 'SNDPGMMSG']:
            return RuleType.ERROR_HANDLING
        elif cmd_name in ['DCLF', 'RTVOBJD', 'CRTDUPOBJ', 'DLTF']:
            return RuleType.DATA_ACCESS
        else:
            return RuleType.WORKFLOW
    
    def _determine_priority(self, cmd_name: str) -> RulePriority:
        """Determine rule priority based on command."""
        high_priority = ['MONMSG', 'SNDPGMMSG', 'IF', 'CALL']
        medium_priority = ['DCL', 'CHGVAR', 'DCLF']
        
        if cmd_name in high_priority:
            return RulePriority.HIGH
        elif cmd_name in medium_priority:
            return RulePriority.MEDIUM
        else:
            return RulePriority.LOW
    
    def _extract_condition(self, cmd) -> str:
        """Extract condition from command."""
        if hasattr(cmd, 'parameters'):
            for param in cmd.parameters:
                if param.keyword == 'COND':
                    return str(param.value.text) if hasattr(param.value, 'text') else str(param.value)
        return ""
    
    def _extract_action(self, cmd) -> str:
        """Extract action from command."""
        action_parts = []
        if hasattr(cmd, 'parameters'):
            for param in cmd.parameters:
                if param.keyword != 'COND':
                    param_text = str(param.value.text) if hasattr(param.value, 'text') else str(param.value)
                    action_parts.append(f"{param.keyword or ''}({param_text})")
        return " ".join(action_parts)
    
    def _extract_variables(self, cmd) -> List[str]:
        """Extract variable names from command."""
        variables = []
        if hasattr(cmd, 'parameters'):
            for param in cmd.parameters:
                if hasattr(param.value, 'text') and param.value.text.startswith('&'):
                    variables.append(param.value.text)
        return variables
    
    def _extract_files(self, cmd) -> List[str]:
        """Extract file names from command."""
        files = []
        if hasattr(cmd, 'parameters'):
            for param in cmd.parameters:
                if param.keyword in ['FILE', 'OBJ']:
                    file_text = str(param.value.text) if hasattr(param.value, 'text') else str(param.value)
                    files.append(file_text)
        return files
    
    def _generate_description(self, cmd_name: str, condition: str, action: str) -> str:
        """Generate human-readable rule description."""
        if condition:
            return f"If {condition}, then {action}"
        else:
            return f"Execute {cmd_name}: {action}"
    
    def _extract_rpg_rule(self, stmt, source_file: str) -> Optional[BusinessRule]:
        """Extract rule from a single RPG statement."""
        self.rule_counter += 1
        
        # Get statement type
        stmt_type = type(stmt).__name__.lower()
        
        # Determine rule type based on statement
        rule_type = self._classify_rpg_statement(stmt_type)
        
        # Extract condition and action
        condition = self._extract_rpg_condition(stmt)
        action = self._extract_rpg_action(stmt)
        
        # Extract variables and files
        variables = self._extract_rpg_variables(stmt)
        files_accessed = self._extract_rpg_files(stmt)
        
        # Generate description
        description = self._generate_rpg_description(stmt_type, condition, action)
        
        return BusinessRule(
            rule_id=f"RULE_{self.rule_counter:04d}",
            rule_type=rule_type,
            priority=self._determine_rpg_priority(stmt_type),
            description=description,
            condition=condition,
            action=action,
            source_file=source_file,
            line_number=getattr(stmt, 'loc', {}).line if hasattr(stmt, 'loc') else 0,
            variables=variables,
            files_accessed=files_accessed
        )
    
    def _extract_db2_rule(self, stmt, source_file: str) -> Optional[BusinessRule]:
        """Extract rule from a single DB2 SQL statement."""
        self.rule_counter += 1
        
        # Get statement type
        stmt_type = getattr(stmt, 'type', type(stmt).__name__.lower())
        
        # Determine rule type based on statement
        rule_type = self._classify_db2_statement(stmt_type)
        
        # Extract condition and action
        condition = self._extract_db2_condition(stmt)
        action = self._extract_db2_action(stmt)
        
        # Extract tables and variables
        variables = self._extract_db2_variables(stmt)
        files_accessed = self._extract_db2_tables(stmt)
        
        # Generate description
        description = self._generate_db2_description(stmt_type, condition, action)
        
        return BusinessRule(
            rule_id=f"RULE_{self.rule_counter:04d}",
            rule_type=rule_type,
            priority=self._determine_db2_priority(stmt_type),
            description=description,
            condition=condition,
            action=action,
            source_file=source_file,
            line_number=getattr(stmt, 'loc', {}).line if hasattr(stmt, 'loc') else 0,
            variables=variables,
            files_accessed=files_accessed
        )
    
    def _classify_rpg_statement(self, stmt_type: str) -> RuleType:
        """Classify RPG statement into rule type."""
        if 'if' in stmt_type:
            return RuleType.VALIDATION
        elif 'eval' in stmt_type or 'calc' in stmt_type:
            return RuleType.CALCULATION
        elif 'call' in stmt_type or 'exsr' in stmt_type:
            return RuleType.WORKFLOW
        elif 'read' in stmt_type or 'write' in stmt_type or 'update' in stmt_type or 'delete' in stmt_type:
            return RuleType.DATA_ACCESS
        elif 'chain' in stmt_type or 'setll' in stmt_type:
            return RuleType.VALIDATION
        else:
            return RuleType.WORKFLOW
    
    def _classify_db2_statement(self, stmt_type: str) -> RuleType:
        """Classify DB2 statement into rule type."""
        if 'select' in stmt_type:
            return RuleType.DATA_ACCESS
        elif 'insert' in stmt_type or 'update' in stmt_type or 'delete' in stmt_type:
            return RuleType.DATA_ACCESS
        elif 'create' in stmt_type or 'alter' in stmt_type or 'drop' in stmt_type:
            return RuleType.DATA_ACCESS
        elif 'grant' in stmt_type or 'revoke' in stmt_type:
            return RuleType.SECURITY
        elif 'check' in stmt_type or 'constraint' in stmt_type:
            return RuleType.VALIDATION
        else:
            return RuleType.DATA_ACCESS
    
    def _determine_rpg_priority(self, stmt_type: str) -> RulePriority:
        """Determine RPG rule priority."""
        high_priority = ['if', 'call', 'chain']
        medium_priority = ['eval', 'read', 'write', 'update', 'delete']
        
        if any(hp in stmt_type for hp in high_priority):
            return RulePriority.HIGH
        elif any(mp in stmt_type for mp in medium_priority):
            return RulePriority.MEDIUM
        else:
            return RulePriority.LOW
    
    def _determine_db2_priority(self, stmt_type: str) -> RulePriority:
        """Determine DB2 rule priority."""
        high_priority = ['grant', 'revoke', 'create', 'drop']
        medium_priority = ['select', 'insert', 'update', 'delete']
        
        if any(hp in stmt_type for hp in high_priority):
            return RulePriority.HIGH
        elif any(mp in stmt_type for mp in medium_priority):
            return RulePriority.MEDIUM
        else:
            return RulePriority.LOW
    
    def _extract_rpg_condition(self, stmt) -> str:
        """Extract condition from RPG statement."""
        if hasattr(stmt, 'condition'):
            return str(stmt.condition) if stmt.condition else ""
        return ""
    
    def _extract_rpg_action(self, stmt) -> str:
        """Extract action from RPG statement."""
        action_parts = []
        if hasattr(stmt, 'target'):
            action_parts.append(f"Target: {stmt.target}")
        if hasattr(stmt, 'expression'):
            action_parts.append(f"Expression: {stmt.expression}")
        return " | ".join(action_parts)
    
    def _extract_rpg_variables(self, stmt) -> List[str]:
        """Extract variable names from RPG statement."""
        variables = []
        # Extract from target
        if hasattr(stmt, 'target') and stmt.target:
            variables.append(str(stmt.target))
        # Extract from expression
        if hasattr(stmt, 'expression') and stmt.expression:
            # Simple variable extraction
            expr_str = str(stmt.expression)
            if expr_str.isalpha() and len(expr_str) <= 10:
                variables.append(expr_str)
        return variables
    
    def _extract_rpg_files(self, stmt) -> List[str]:
        """Extract file names from RPG statement."""
        files = []
        if hasattr(stmt, 'file'):
            files.append(str(stmt.file))
        return files
    
    def _extract_db2_condition(self, stmt) -> str:
        """Extract condition from DB2 statement."""
        if hasattr(stmt, 'where_clause'):
            return str(stmt.where_clause)
        return ""
    
    def _extract_db2_action(self, stmt) -> str:
        """Extract action from DB2 statement."""
        action_parts = []
        if hasattr(stmt, 'type'):
            action_parts.append(f"Type: {stmt.type}")
        if hasattr(stmt, 'table'):
            action_parts.append(f"Table: {stmt.table}")
        return " | ".join(action_parts)
    
    def _extract_db2_variables(self, stmt) -> List[str]:
        """Extract variable names from DB2 statement."""
        variables = []
        if hasattr(stmt, 'columns'):
            for col in stmt.columns:
                if hasattr(col, 'name'):
                    variables.append(col.name)
        return variables
    
    def _extract_db2_tables(self, stmt) -> List[str]:
        """Extract table names from DB2 statement."""
        tables = []
        if hasattr(stmt, 'table'):
            tables.append(str(stmt.table))
        if hasattr(stmt, 'from_clause'):
            tables.append(str(stmt.from_clause))
        return tables
    
    def _generate_rpg_description(self, stmt_type: str, condition: str, action: str) -> str:
        """Generate human-readable RPG rule description."""
        if condition:
            return f"RPG {stmt_type}: If {condition}, then {action}"
        else:
            return f"RPG {stmt_type}: {action}"
    
    def _generate_db2_description(self, stmt_type: str, condition: str, action: str) -> str:
        """Generate human-readable DB2 rule description."""
        if condition:
            return f"SQL {stmt_type}: If {condition}, then {action}"
        else:
            return f"SQL {stmt_type}: {action}"
    
    def _extract_dspf_rule(self, record, source_file: str) -> Optional[BusinessRule]:
        """Extract rule from a single DSPF record."""
        self.rule_counter += 1
        
        # Get record name
        record_name = getattr(record, 'name', 'Unknown')
        
        # Determine rule type (DSPF is primarily validation/data access)
        rule_type = RuleType.VALIDATION
        
        # Extract condition and action
        condition = self._extract_dspf_condition(record)
        action = self._extract_dspf_action(record)
        
        # Extract variables and files
        variables = self._extract_dspf_fields(record)
        files_accessed = []  # DSPF doesn't typically access files
        
        # Generate description
        description = self._generate_dspf_description(record_name, condition, action)
        
        return BusinessRule(
            rule_id=f"RULE_{self.rule_counter:04d}",
            rule_type=rule_type,
            priority=RulePriority.MEDIUM,
            description=description,
            condition=condition,
            action=action,
            source_file=source_file,
            line_number=getattr(record, 'loc', {}).line if hasattr(record, 'loc') else 0,
            variables=variables,
            files_accessed=files_accessed
        )
    
    def _extract_dspf_condition(self, record) -> str:
        """Extract condition from DSPF record."""
        # DSPF records don't typically have conditions, but may have indicators
        if hasattr(record, 'indicators'):
            return f"Indicators: {record.indicators}"
        return ""
    
    def _extract_dspf_action(self, record) -> str:
        """Extract action from DSPF record."""
        action_parts = []
        if hasattr(record, 'name'):
            action_parts.append(f"Record: {record.name}")
        if hasattr(record, 'fields'):
            action_parts.append(f"Fields: {len(record.fields)}")
        return " | ".join(action_parts)
    
    def _extract_dspf_fields(self, record) -> List[str]:
        """Extract field names from DSPF record."""
        fields = []
        if hasattr(record, 'fields'):
            for field in record.fields:
                if hasattr(field, 'name'):
                    fields.append(field.name)
        return fields
    
    def _generate_dspf_description(self, record_name: str, condition: str, action: str) -> str:
        """Generate human-readable DSPF rule description."""
        if condition:
            return f"DSPF Record {record_name}: {condition} - {action}"
        else:
            return f"DSPF Record {record_name}: {action}"
