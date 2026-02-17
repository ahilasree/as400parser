#!/usr/bin/env python3
"""
Business Rule Extraction Demo

Demonstrates BRE capabilities on example AS400 files.
"""

import json
from pathlib import Path

from bre.extractor import BREAnalyzer

def demo_bre_extraction():
    """Run BRE extraction demo on example files."""
    
    print("🔍 Business Rule Extraction Demo")
    print("=" * 50)
    
    # Initialize analyzer
    analyzer = BREAnalyzer()
    
    # Analyze example files
    examples_dir = Path("examples")
    
    if not examples_dir.exists():
        print("❌ Examples directory not found")
        return
    
    # Find CL files
    cl_files = list(examples_dir.glob("*.clle"))
    
    if not cl_files:
        print("❌ No CL files found in examples directory")
        return
    
    print(f"📁 Found {len(cl_files)} CL files")
    
    # Analyze each file
    all_rule_sets = {}
    
    for cl_file in cl_files:
        print(f"\n🔍 Analyzing: {cl_file.name}")
        
        try:
            rule_set = analyzer.analyze_file(str(cl_file))
            all_rule_sets[str(cl_file)] = rule_set
            
            print(f"  📊 Rules found: {len(rule_set.rules)}")
            print(f"  📋 Types: {rule_set.metrics}")
            
            # Show top rules
            for i, rule in enumerate(rule_set.rules[:3]):
                print(f"    {i+1}. [{rule.rule_type.value.upper()}] {rule.description}")
        
        except Exception as e:
            print(f"  ❌ Error: {e}")
    
    # Generate comprehensive report
    if all_rule_sets:
        print("\n📈 Generating comprehensive report...")
        report = analyzer.generate_report(all_rule_sets)
        
        # Display summary
        summary = report['summary']
        print(f"\n📊 Summary:")
        print(f"  Total Programs: {summary['total_programs']}")
        print(f"  Total Rules: {summary['total_rules']}")
        print(f"  Rule Types: {summary['rule_types']}")
        print(f"  Priority Distribution: {summary['priority_distribution']}")
        
        # Display recommendations
        if report['recommendations']:
            print(f"\n💡 Recommendations:")
            for rec in report['recommendations']:
                print(f"  • {rec}")
        
        # Save detailed report
        output_file = "bre_report.json"
        with open(output_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"\n💾 Detailed report saved to: {output_file}")
    
    print("\n✅ Demo completed!")

def demo_cross_reference_analysis():
    """Demonstrate cross-reference analysis."""
    
    print("\n🔗 Cross-Reference Analysis Demo")
    print("=" * 50)
    
    analyzer = BREAnalyzer()
    
    # Analyze examples directory
    examples_dir = Path("examples")
    if not examples_dir.exists():
        print("❌ Examples directory not found")
        return
    
    rule_sets = analyzer.analyze_directory(str(examples_dir), "*.clle")
    
    if not rule_sets:
        print("❌ No rule sets found")
        return
    
    # Generate cross-reference report
    cross_refs = analyzer._find_cross_references(rule_sets)
    
    print("📋 Program Call Relationships:")
    for program, refs in cross_refs.items():
        if refs:
            prog_name = Path(program).name
            print(f"  {prog_name} calls: {', '.join(refs)}")
    
    print("\n✅ Cross-reference analysis completed!")

if __name__ == "__main__":
    demo_bre_extraction()
    demo_cross_reference_analysis()
