"""
Business Rule Extractor - Main extraction interface
"""

from typing import List, Dict, Any
from pathlib import Path

from .business_rules import BusinessRuleExtractor, RuleSet
from cl.runner import run_cl_file
from rpg.runner import run_rpg_file
from db2.runner import run_db2_file

class BREAnalyzer:
    """Main Business Rule Extraction analyzer."""
    
    def __init__(self):
        self.extractor = BusinessRuleExtractor()
        self.all_rules = {}
    
    def analyze_file(self, file_path: str) -> RuleSet:
        """Analyze a single file and extract business rules."""
        file_path = Path(file_path)
        
        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        
        # Determine file type and extract rules
        if file_path.suffix.lower() in ['.cl', '.clle']:
            result = run_cl_file(str(file_path))
            return self.extractor.extract_from_cl(result.ast, str(file_path))
        elif file_path.suffix.lower() in ['.rpg', '.rpgle', '.sqlrpgle']:
            result = run_rpg_file(str(file_path))
            return self.extractor.extract_from_rpg(result.ast, str(file_path))
        elif file_path.suffix.lower() in ['.sql']:
            result = run_db2_file(str(file_path))
            return self.extractor.extract_from_db2(result.ast, str(file_path))
        else:
            raise ValueError(f"Unsupported file type: {file_path.suffix}")
    
    def analyze_directory(self, dir_path: str, pattern: str = "*") -> Dict[str, RuleSet]:
        """Analyze all files in a directory."""
        dir_path = Path(dir_path)
        results = {}
        
        for file_path in dir_path.glob(pattern):
            if file_path.is_file():
                try:
                    rule_set = self.analyze_file(str(file_path))
                    results[str(file_path)] = rule_set
                except Exception as e:
                    print(f"Error analyzing {file_path}: {e}")
        
        return results
    
    def generate_report(self, rule_sets: Dict[str, RuleSet]) -> Dict[str, Any]:
        """Generate comprehensive BRE report."""
        report = {
            'summary': self._generate_summary(rule_sets),
            'programs': {},
            'cross_references': self._find_cross_references(rule_sets),
            'recommendations': self._generate_recommendations(rule_sets)
        }
        
        for file_path, rule_set in rule_sets.items():
            report['programs'][file_path] = {
                'metrics': rule_set.metrics,
                'rules': [rule.to_dict() for rule in rule_set.rules]
            }
        
        return report
    
    def _generate_summary(self, rule_sets: Dict[str, RuleSet]) -> Dict[str, Any]:
        """Generate summary statistics."""
        total_rules = sum(len(rs.rules) for rs in rule_sets.values())
        
        summary = {
            'total_programs': len(rule_sets),
            'total_rules': total_rules,
            'rule_types': {},
            'priority_distribution': {},
            'files_analyzed': list(rule_sets.keys())
        }
        
        # Aggregate rule types and priorities
        for rule_set in rule_sets.values():
            for rule in rule_set.rules:
                rule_type = rule.rule_type.value
                priority = rule.priority.value
                
                summary['rule_types'][rule_type] = summary['rule_types'].get(rule_type, 0) + 1
                summary['priority_distribution'][priority] = summary['priority_distribution'].get(priority, 0) + 1
        
        return summary
    
    def _find_cross_references(self, rule_sets: Dict[str, RuleSet]) -> Dict[str, List[str]]:
        """Find cross-program references."""
        cross_refs = {}
        
        for file_path, rule_set in rule_sets.items():
            refs = []
            
            # Find program calls in rules
            for rule in rule_set.rules:
                if 'CALL PGM' in rule.action:
                    # Extract called program name
                    parts = rule.action.split('PGM(')
                    if len(parts) > 1:
                        called_pgm = parts[1].split(')')[0].strip()
                        refs.append(called_pgm)
            
            cross_refs[file_path] = refs
        
        return cross_refs
    
    def _generate_recommendations(self, rule_sets: Dict[str, RuleSet]) -> List[str]:
        """Generate improvement recommendations."""
        recommendations = []
        
        total_rules = sum(len(rs.rules) for rs in rule_sets.values())
        
        if total_rules == 0:
            recommendations.append("No business rules found. Check file parsing.")
            return recommendations
        
        # Check for complex programs
        for file_path, rule_set in rule_sets.items():
            if len(rule_set.rules) > 50:
                recommendations.append(f"Complex program detected: {file_path} ({len(rule_set.rules)} rules)")
        
        # Check for error handling
        error_rules = sum(
            len([r for r in rs.rules if r.rule_type.value == 'error_handling'])
            for rs in rule_sets.values()
        )
        
        if error_rules == 0:
            recommendations.append("No error handling rules found. Consider adding MONMSG commands.")
        
        # Check for validation rules
        validation_rules = sum(
            len([r for r in rs.rules if r.rule_type.value == 'validation'])
            for rs in rule_sets.values()
        )
        
        if validation_rules < total_rules * 0.1:
            recommendations.append("Low validation rule coverage. Consider adding input validation.")
        
        return recommendations
