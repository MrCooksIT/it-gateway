#!/usr/bin/env python3
"""
IT Gateway Navigation Diagnostic and Fix Tool
Identifies and fixes Jekyll navigation issues
Run this in your VS Code terminal in your repo directory
"""

import os
import re
from pathlib import Path
from collections import defaultdict, Counter

class NavigationDiagnostic:
    def __init__(self):
        self.files_checked = 0
        self.navigation_data = []
        self.issues = []
        self.nav_order_conflicts = defaultdict(list)
        self.parent_child_issues = []
        
    def extract_frontmatter(self, file_path):
        """Extract YAML frontmatter from markdown file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if file has frontmatter
            if not content.startswith('---\n'):
                return None
                
            # Extract frontmatter
            parts = content.split('---\n', 2)
            if len(parts) < 3:
                return None
                
            frontmatter = parts[1]
            
            # Parse key frontmatter fields
            data = {
                'file_path': str(file_path),
                'title': self._extract_value(frontmatter, 'title'),
                'parent': self._extract_value(frontmatter, 'parent'),
                'grand_parent': self._extract_value(frontmatter, 'grand_parent'),
                'nav_order': self._extract_value(frontmatter, 'nav_order'),
                'has_children': self._extract_value(frontmatter, 'has_children'),
                'permalink': self._extract_value(frontmatter, 'permalink'),
                'layout': self._extract_value(frontmatter, 'layout')
            }
            
            return data
            
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return None
    
    def _extract_value(self, frontmatter, key):
        """Extract a specific value from frontmatter"""
        pattern = rf'^{key}:\s*(.+)$'
        match = re.search(pattern, frontmatter, re.MULTILINE)
        if match:
            value = match.group(1).strip()
            # Remove quotes if present
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            elif value.startswith("'") and value.endswith("'"):
                value = value[1:-1]
            # Convert to appropriate type
            if value.lower() == 'true':
                return True
            elif value.lower() == 'false':
                return False
            elif value.isdigit():
                return int(value)
            return value
        return None
    
    def scan_navigation(self):
        """Scan all markdown files for navigation data"""
        print("🔍 Scanning navigation structure...")
        
        for md_file in Path('.').rglob('*.md'):
            if str(md_file).startswith('./.git'):
                continue
                
            self.files_checked += 1
            data = self.extract_frontmatter(md_file)
            
            if data and (data['title'] or data['nav_order'] is not None):
                self.navigation_data.append(data)
        
        print(f"   ✅ Scanned {self.files_checked} files, found {len(self.navigation_data)} with navigation data")
    
    def analyze_navigation_issues(self):
        """Analyze navigation data for common issues"""
        print("🕵️ Analyzing navigation for issues...")
        
        # Group by parent for analysis
        by_parent = defaultdict(list)
        nav_orders_used = defaultdict(list)
        
        for item in self.navigation_data:
            parent = item['parent'] or 'ROOT'
            by_parent[parent].append(item)
            
            # Track nav_order conflicts within same parent
            if item['nav_order'] is not None:
                nav_orders_used[parent].append((item['nav_order'], item['title'], item['file_path']))
        
        # Check for nav_order conflicts
        for parent, orders in nav_orders_used.items():
            order_counts = Counter([order[0] for order in orders])
            for nav_order, count in order_counts.items():
                if count > 1:
                    conflicting_files = [item for item in orders if item[0] == nav_order]
                    self.nav_order_conflicts[parent].append({
                        'nav_order': nav_order,
                        'files': conflicting_files
                    })
        
        # Check parent-child relationships
        all_titles = {item['title'] for item in self.navigation_data if item['title']}
        
        for item in self.navigation_data:
            if item['parent'] and item['parent'] not in all_titles:
                # Parent doesn't exist as a page title
                self.parent_child_issues.append({
                    'type': 'missing_parent',
                    'file': item['file_path'],
                    'title': item['title'],
                    'missing_parent': item['parent']
                })
        
        # Check has_children consistency
        parents_with_children = set()
        for item in self.navigation_data:
            if item['parent']:
                parents_with_children.add(item['parent'])
        
        for item in self.navigation_data:
            if item['title'] in parents_with_children and not item['has_children']:
                self.parent_child_issues.append({
                    'type': 'missing_has_children',
                    'file': item['file_path'],
                    'title': item['title'],
                    'issue': 'Should have has_children: true'
                })
    
    def report_issues(self):
        """Report all found navigation issues"""
        print("\n" + "="*60)
        print("📊 NAVIGATION DIAGNOSTIC REPORT")
        print("="*60)
        
        total_issues = len(self.nav_order_conflicts) + len(self.parent_child_issues)
        
        if total_issues == 0:
            print("✅ No navigation issues found! Your navigation structure looks good.")
            return
        
        print(f"⚠️  Found {total_issues} navigation issues")
        
        # Report nav_order conflicts
        if self.nav_order_conflicts:
            print(f"\n🔴 NAV_ORDER CONFLICTS ({len(self.nav_order_conflicts)} groups):")
            for parent, conflicts in self.nav_order_conflicts.items():
                print(f"\n   Parent: {parent}")
                for conflict in conflicts:
                    print(f"   ❌ nav_order {conflict['nav_order']} used by:")
                    for order, title, file_path in conflict['files']:
                        print(f"      - {title} ({file_path})")
        
        # Report parent-child issues
        if self.parent_child_issues:
            print(f"\n🔴 PARENT-CHILD RELATIONSHIP ISSUES ({len(self.parent_child_issues)}):")
            for issue in self.parent_child_issues:
                if issue['type'] == 'missing_parent':
                    print(f"   ❌ {issue['file']} references missing parent '{issue['missing_parent']}'")
                elif issue['type'] == 'missing_has_children':
                    print(f"   ❌ {issue['file']} needs 'has_children: true' (has child pages)")
    
    def generate_navigation_map(self):
        """Generate a visual navigation map"""
        print(f"\n📍 CURRENT NAVIGATION STRUCTURE:")
        print("-" * 40)
        
        # Group items by parent
        by_parent = defaultdict(list)
        for item in self.navigation_data:
            parent = item['parent'] or 'ROOT'
            by_parent[parent].append(item)
        
        # Sort each group by nav_order
        for parent in by_parent:
            by_parent[parent].sort(key=lambda x: x['nav_order'] if x['nav_order'] is not None else 999)
        
        def print_level(parent_name, level=0):
            indent = "  " * level
            items = by_parent.get(parent_name, [])
            
            for item in items:
                nav_order = f"[{item['nav_order']}]" if item['nav_order'] is not None else "[no order]"
                has_children_marker = " 📁" if item['has_children'] else ""
                
                print(f"{indent}{nav_order} {item['title']}{has_children_marker}")
                
                # Print children
                if item['title'] in by_parent:
                    print_level(item['title'], level + 1)
        
        print_level('ROOT')
    
    def suggest_fixes(self):
        """Suggest specific fixes for found issues"""
        if not self.nav_order_conflicts and not self.parent_child_issues:
            return
            
        print(f"\n🔧 SUGGESTED FIXES:")
        print("-" * 30)
        
        # Fix nav_order conflicts
        if self.nav_order_conflicts:
            print("🔢 Nav Order Conflicts:")
            for parent, conflicts in self.nav_order_conflicts.items():
                print(f"\n   For parent '{parent}', reassign nav_order values:")
                for conflict in conflicts:
                    for i, (order, title, file_path) in enumerate(conflict['files']):
                        new_order = conflict['nav_order'] + i
                        print(f"   📝 Change {file_path}: nav_order: {new_order}")
        
        # Fix parent-child issues
        if self.parent_child_issues:
            print(f"\n🔗 Parent-Child Issues:")
            for issue in self.parent_child_issues:
                if issue['type'] == 'missing_has_children':
                    print(f"   📝 Add to {issue['file']}: has_children: true")
                elif issue['type'] == 'missing_parent':
                    print(f"   📝 Fix parent reference in {issue['file']} or create parent page")

def create_fixed_navigation():
    """Create a properly structured navigation"""
    print(f"\n🛠️  CREATING FIXED NAVIGATION STRUCTURE...")
    
    # Define the correct navigation structure based on your content
    navigation_structure = {
        # Root level pages
        'index.md': {
            'title': 'IT Gateway',
            'layout': 'home',
            'nav_order': 1,
            'permalink': '/'
        },
        'how-to-use.md': {
            'title': 'How to Use This Site',
            'nav_order': 2
        },
        
        # Main sections (top level)
        'digital-technology/index.md': {
            'title': 'Digital Technology (Grades 8-9)',
            'nav_order': 3,
            'has_children': True,
            'permalink': '/digital-technology/'
        },
        'fundamentals/index.md': {
            'title': 'Computer Fundamentals',
            'nav_order': 4,
            'has_children': True,
            'permalink': '/fundamentals/'
        },
        'systems/index.md': {
            'title': 'Systems Technologies',
            'nav_order': 5,
            'has_children': True,
            'permalink': '/systems/'
        },
        'networks/index.md': {
            'title': 'Communication & Internet',
            'nav_order': 6,
            'has_children': True,
            'permalink': '/networks/'
        },
        'data/index.md': {
            'title': 'Data & Information Management',
            'nav_order': 7,
            'has_children': True,
            'permalink': '/data/'
        },
        'programming/index.md': {
            'title': 'Programming & Development',
            'nav_order': 8,
            'has_children': True,
            'permalink': '/programming/'
        },
        'database-dev/index.md': {
            'title': 'Database Development',
            'nav_order': 9,
            'has_children': True,
            'permalink': '/database-dev/'
        },
        'problem-solving/index.md': {
            'title': 'Algorithms & Problem Solving',
            'nav_order': 10,
            'has_children': True,
            'permalink': '/problem-solving/'
        },
        'projects/index.md': {
            'title': 'Practical Assessment Tasks',
            'nav_order': 11,
            'has_children': True,
            'permalink': '/projects/'
        },
        'exam-prep/index.md': {
            'title': 'Examination Preparation',
            'nav_order': 12,
            'has_children': True,
            'permalink': '/exam-prep/'
        },
        'resources/index.md': {
            'title': 'Additional Resources',
            'nav_order': 13,
            'has_children': True,
            'permalink': '/resources/'
        },
        
        # Exam prep subsections
        'exam-prep/paper1/index.md': {
            'title': 'Paper 1 Preparation',
            'parent': 'Examination Preparation',
            'nav_order': 1,
            'has_children': True
        },
        'exam-prep/paper2/index.md': {
            'title': 'Paper 2 Preparation',
            'parent': 'Examination Preparation',
            'nav_order': 2,
            'has_children': True
        },
        
        # Paper 2 study guides - fix the ordering issue
        'exam-prep/paper2/grade10-study-guide.md': {
            'title': 'Grade 10 Mid-Year Paper 2 Study Guide',
            'parent': 'Paper 2 Preparation',
            'nav_order': 1
        },
        'exam-prep/paper2/grade11-study-guide.md': {
            'title': 'Grade 11 Mid-Year Paper 2 Study Guide',
            'parent': 'Paper 2 Preparation',
            'nav_order': 2
        },
        'exam-prep/paper2/grade12-study-guide.md': {
            'title': 'Grade 12 Mid-Year Paper 2 Study Guide',
            'parent': 'Paper 2 Preparation',
            'nav_order': 3
        }
    }
    
    return navigation_structure

def apply_navigation_fixes():
    """Apply the navigation fixes to actual files"""
    print(f"\n🔧 Would you like to apply automatic fixes?")
    print("This will update the frontmatter in your markdown files.")
    print("Make sure you have committed your current changes first!")
    
    response = input("Apply fixes? (y/n): ").lower()
    if response != 'y':
        print("Fixes not applied. You can manually update the files using the suggestions above.")
        return
    
    fixes_applied = 0
    navigation_structure = create_fixed_navigation()
    
    for file_path, nav_data in navigation_structure.items():
        if os.path.exists(file_path):
            try:
                # Read current file
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Update frontmatter
                if content.startswith('---\n'):
                    parts = content.split('---\n', 2)
                    if len(parts) >= 3:
                        # Build new frontmatter
                        new_frontmatter = "---\n"
                        
                        # Preserve layout if it exists
                        if 'layout' in nav_data:
                            new_frontmatter += f"layout: {nav_data['layout']}\n"
                        elif 'layout: ' in parts[1]:
                            layout_match = re.search(r'layout:\s*(.+)', parts[1])
                            if layout_match:
                                new_frontmatter += f"layout: {layout_match.group(1).strip()}\n"
                        
                        # Add navigation fields
                        new_frontmatter += f"title: {nav_data['title']}\n"
                        
                        if 'parent' in nav_data:
                            new_frontmatter += f"parent: {nav_data['parent']}\n"
                        
                        if 'grand_parent' in nav_data:
                            new_frontmatter += f"grand_parent: {nav_data['grand_parent']}\n"
                        
                        if 'nav_order' in nav_data:
                            new_frontmatter += f"nav_order: {nav_data['nav_order']}\n"
                        
                        if 'has_children' in nav_data:
                            new_frontmatter += f"has_children: {nav_data['has_children']}\n"
                        
                        if 'permalink' in nav_data:
                            new_frontmatter += f"permalink: {nav_data['permalink']}\n"
                        
                        new_frontmatter += "---\n"
                        
                        # Combine with content
                        new_content = new_frontmatter + parts[2]
                        
                        # Write back to file
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        
                        fixes_applied += 1
                        print(f"   ✅ Fixed {file_path}")
                        
            except Exception as e:
                print(f"   ❌ Error fixing {file_path}: {e}")
    
    print(f"\n✅ Applied fixes to {fixes_applied} files")
    print("Please test your navigation and commit the changes if everything looks good!")

def main():
    """Main diagnostic function"""
    print("🚀 IT Gateway Navigation Diagnostic Tool")
    print("="*50)
    
    # Check if we're in the right directory
    if not os.path.exists('.git'):
        print("❌ Error: Not in a git repository!")
        print("   Make sure you're in your it-gateway repository folder")
        return
    
    # Create diagnostic instance
    diagnostic = NavigationDiagnostic()
    
    try:
        # Step 1: Scan all files
        diagnostic.scan_navigation()
        
        # Step 2: Analyze for issues
        diagnostic.analyze_navigation_issues()
        
        # Step 3: Report issues
        diagnostic.report_issues()
        
        # Step 4: Show current structure
        diagnostic.generate_navigation_map()
        
        # Step 5: Suggest fixes
        diagnostic.suggest_fixes()
        
        # Step 6: Offer to apply fixes
        if diagnostic.nav_order_conflicts or diagnostic.parent_child_issues:
            apply_navigation_fixes()
        
        print(f"\n🎉 Navigation diagnostic complete!")
        print("If issues were found and fixed, test your site and commit the changes.")
        
    except Exception as e:
        print(f"❌ Error during diagnostic: {e}")
        print("Please check the error and try again.")

if __name__ == "__main__":
    main()