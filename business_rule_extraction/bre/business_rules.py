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
        
        # Implementation for RPG rule extraction
        # TODO: Implement based on RPG AST structure
        
        return rule_set
    
    def extract_from_db2(self, ast, source_file: str) -> RuleSet:
        """Extract business rules from DB2 AST."""
        rule_set = RuleSet(program_name=source_file)
        
        # Implementation for DB2 rule extraction
        # TODO: Implement based on DB2 AST structure
        
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
