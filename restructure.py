#!/usr/bin/env python3
"""
IT Gateway Structure Replacement Script
Automatically removes old structure and creates new one
Run this in your VS Code terminal in your repo directory
"""

import os
import shutil
from pathlib import Path

# Old folders to remove
OLD_FOLDERS = [
    "core-concepts",
    "practical-skills", 
    "theory-practical-connections",
    "exam-preparation",
    "resources"
]

# New structure with content
NEW_STRUCTURE = {
    "fundamentals": {
        "index.md": """---
layout: page
title: Computer Fundamentals
permalink: /fundamentals/
nav_order: 3
has_children: true
---

# Computer Fundamentals
{: .text-blue-200 }

Start your IT journey with basic computing concepts.

## What You'll Learn
- What is a computer and how does it work?
- How computers represent and store data
- Impact of technology on society

## By Grade Level
- **Grade 10**: Computer basics, data representation
- **Grade 11**: Advanced concepts and applications  
- **Grade 12**: Complex scenarios and emerging issues

## Topics in this Section
- [Grade 10 Basics](./grade10)
- [Data Representation](./data-representation)
- [Social Impact](./social-impact)
""",
        "grade10/index.md": """---
layout: page
title: Grade 10 Basics
parent: Computer Fundamentals
nav_order: 1
has_children: true
---

# Grade 10: Computer Fundamentals

Foundation concepts for understanding computers and technology.

## Topics
- Computer basics and components
- Hardware vs software
- Advantages and disadvantages of computers
- Types of computers

*Content coming soon...*
""",
        "data-representation/index.md": """---
layout: page
title: Data Representation
parent: Computer Fundamentals
nav_order: 2
has_children: true
---

# Data Representation

How computers store and process information.

## Topics
- Number systems (binary, decimal, hexadecimal)
- Character encoding (ASCII, Unicode)
- File management and organization

*Content coming soon...*
""",
        "social-impact/index.md": """---
layout: page
title: Social Impact
parent: Computer Fundamentals
nav_order: 3
has_children: true
---

# Social Impact of Technology

Understanding how IT affects society, ethics, and the environment.

## Topics
- Digital divide
- Ethics and legal issues
- Health and environmental impact
- Responsible computing

*Content coming soon...*
"""
    },
    
    "systems": {
        "index.md": """---
layout: page
title: Systems Technologies
permalink: /systems/
nav_order: 4
has_children: true
---

# Systems Technologies
{: .text-blue-200 }

Discover how computer hardware and software work together.

## Topics Covered
- **Hardware**: CPU, memory, storage, mobile tech
- **Software**: Operating systems, utilities, cloud computing
- **Management**: Security, maintenance, optimization
- **Emerging Tech**: VR, AR, IoT, AI basics

## Learning Progression
**Grade 10** → **Grade 11** → **Grade 12**
Basic components → Detailed architecture → Advanced concepts

## Sections
- [Hardware Components](./hardware)
- [Software Systems](./software)
- [Computer Management](./management)
- [Emerging Technologies](./emerging)
""",
        "hardware/index.md": """---
layout: page
title: Hardware Components
parent: Systems Technologies
nav_order: 1
has_children: true
---

# Hardware Components

Physical parts that make up computer systems.

## Grade Progression
- **Grade 10**: Basic input, output, storage, processing
- **Grade 11**: Motherboard, CPU, memory details
- **Grade 12**: Mobile technologies, performance factors

*Content coming soon...*
""",
        "software/index.md": """---
layout: page
title: Software Systems
parent: Systems Technologies
nav_order: 2
has_children: true
---

# Software Systems

Programs and operating systems that control hardware.

## Topics
- Operating systems
- Utility programs
- Virtualization
- Cloud computing

*Content coming soon...*
"""
    },
    
    "networks": {
        "index.md": """---
layout: page
title: Communication & Internet
permalink: /networks/
nav_order: 5
has_children: true
---

# Communication & Internet Technologies
{: .text-blue-200 }

Explore how computers connect globally.

## Core Areas
- **Networking**: LANs, WANs, protocols
- **Internet**: Web technologies, services
- **Communication**: Email, messaging, collaboration
- **Security**: Protecting data and systems

## Grade Progression
- **Grade 10**: Network basics, internet fundamentals
- **Grade 11**: Protocols, wireless technologies, security
- **Grade 12**: Network setup, advanced security

## Sections
- [Grade 10 Networking](./grade10)
- [Grade 11 Networking](./grade11)
- [Grade 12 Networking](./grade12)
- [Internet Services](./internet-services)

*Content coming soon...*
""",
        "grade10/index.md": """---
layout: page
title: Grade 10 Networking
parent: Communication & Internet
nav_order: 1
---

# Grade 10: Networking Basics

Introduction to computer networks and the internet.
*Content coming soon...*
""",
        "grade11/index.md": """---
layout: page
title: Grade 11 Networking
parent: Communication & Internet
nav_order: 2
---

# Grade 11: Advanced Networking

Network protocols, wireless technologies, and security.
*Content coming soon...*
""",
        "grade12/index.md": """---
layout: page
title: Grade 12 Networking
parent: Communication & Internet
nav_order: 3
---

# Grade 12: Network Implementation

Setting up networks and advanced security concepts.
*Content coming soon...*
"""
    },
    
    "data": {
        "index.md": """---
layout: page
title: Data & Information Management
permalink: /data/
nav_order: 6
has_children: true
---

# Data & Information Management
{: .text-blue-200 }

Learn to organize, store, and retrieve information effectively.

## What You'll Learn
- **Database Concepts**: Understanding data organization
- **Database Design**: Creating efficient structures
- **Data Quality**: Ensuring accurate information
- **Modern Concepts**: Big data and analytics

## Database Journey
- **Grade 10**: Files and basic data concepts
- **Grade 11**: Introduction to databases, simple design
- **Grade 12**: Advanced design, complex relationships

*Content coming soon...*
"""
    },
    
    "programming": {
        "index.md": """---
layout: page
title: Programming & Development
permalink: /programming/
nav_order: 7
has_children: true
---

# Programming & Development
{: .text-blue-200 }

Build coding skills from basics to advanced applications.

## Skills Development
- **Grade 10**: Introduction to Delphi programming
- **Grade 11**: Arrays, files, methods, GUI development  
- **Grade 12**: Object-oriented programming, complex solutions

## Key Topics
- Programming fundamentals
- Control structures and algorithms
- Data structures and file handling
- Software engineering practices

## Sections
- [Grade 10 Programming](./grade10)
- [Grade 11 Programming](./grade11)
- [Grade 12 Programming](./grade12)
- [Algorithms](./algorithms)
- [Best Practices](./best-practices)

*Content coming soon...*
""",
        "grade10/index.md": """---
layout: page
title: Grade 10 Programming
parent: Programming & Development
nav_order: 1
---

# Grade 10: Introduction to Programming

Your first steps in coding with Delphi.
*Content coming soon...*
""",
        "grade11/index.md": """---
layout: page
title: Grade 11 Programming
parent: Programming & Development
nav_order: 2
---

# Grade 11: Intermediate Programming

Arrays, files, methods, and GUI development.
*Content coming soon...*
""",
        "grade12/index.md": """---
layout: page
title: Grade 12 Programming
parent: Programming & Development
nav_order: 3
---

# Grade 12: Advanced Programming

Object-oriented programming and complex solutions.
*Content coming soon...*
"""
    },
    
    "database-dev": {
        "index.md": """---
layout: page
title: Database Development
permalink: /database-dev/
nav_order: 8
has_children: true
---

# Database Development
{: .text-blue-200 }

Learn to build database-driven applications.

## What You'll Learn
- Connecting programs to databases
- SQL programming
- Database transactions
- Data-driven applications

## Grade Progression
- **Grade 11**: Basic database programming, simple queries
- **Grade 12**: Advanced SQL, complex applications

*Content coming soon...*
"""
    },
    
    "problem-solving": {
        "index.md": """---
layout: page
title: Algorithms & Problem Solving
permalink: /problem-solving/
nav_order: 9
has_children: true
---

# Algorithms & Problem Solving
{: .text-blue-200 }

Develop computational thinking and problem-solving skills.

## Core Skills
- Breaking down complex problems
- Algorithm design and implementation
- Pattern recognition
- Logical thinking

*Content coming soon...*
"""
    },
    
    "projects": {
        "index.md": """---
layout: page
title: Practical Assessment Tasks
permalink: /projects/
nav_order: 10
has_children: true
---

# Practical Assessment Tasks (PAT)
{: .text-blue-200 }

Guidance for your major programming projects.

## PAT Support
- Project planning and analysis
- Development strategies
- Testing and documentation
- Example projects

*Content coming soon...*
"""
    },
    
    "exam-prep": {
        "index.md": """---
layout: page
title: Examination Preparation
permalink: /exam-prep/
nav_order: 11
has_children: true
---

# Examination Preparation
{: .text-blue-200 }

Get ready for success in both practical and theory exams.

## Two-Paper System
- **Paper 1**: Practical programming (3 hours)
- **Paper 2**: Theory knowledge (3 hours)

## Preparation Resources
- Past paper analysis
- Common question types
- Time management strategies
- Grade-specific focus areas

## Sections
- [Paper 1 Preparation](./paper1)
- [Paper 2 Preparation](./paper2)
- [Past Papers Analysis](./past-papers)

*Content coming soon...*
""",
        "paper1/index.md": """---
layout: page
title: Paper 1 Preparation
parent: Examination Preparation
nav_order: 1
---

# Paper 1: Practical Programming

Prepare for the 3-hour practical programming exam.
*Content coming soon...*
""",
        "paper2/index.md": """---
layout: page
title: Paper 2 Preparation
parent: Examination Preparation
nav_order: 2
---

# Paper 2: Theory Knowledge

Prepare for the 3-hour theory exam.
*Content coming soon...*
"""
    },
    
    "resources": {
        "index.md": """---
layout: page
title: Additional Resources
permalink: /resources/
nav_order: 12
has_children: true
---

# Additional Resources
{: .text-blue-200 }

Quick reference materials and practice resources.

## Available Resources
- **Quick Reference**: Syntax guides and cheat sheets
- **Glossary**: IT terminology explained
- **Practice**: Exercises and mini-projects

*Content coming soon...*
"""
    }
}

# New config and homepage
CONFIG_CONTENT = """title: IT Gateway
description: Comprehensive IT theory and practical resource for Grade 10-12
theme: jekyll-theme-just-the-docs

# Color scheme - blue theme
color_scheme: blue

# Enable search
search_enabled: true
search:
  heading_level: 2
  previews: 3

# Navigation
nav_sort: case_insensitive
nav_external_links:
  - title: Google Classroom
    url: https://classroom.google.com
    hide_icon: false

# Enable features
enable_copy_code_button: true
back_to_top: true
back_to_top_text: "Back to top"

# Footer
footer_content: "IT Gateway - Your bridge between theory and practice © 2025"

# Plugins
plugins:
  - jekyll-default-layout
  - jekyll-seo-tag
"""

HOMEPAGE_CONTENT = """---
layout: home
title: IT Gateway
nav_order: 1
permalink: /
---

# IT Gateway
{: .fs-9 }

Your bridge between IT theory and practical programming
{: .fs-6 .fw-300 }

[Get Started Now](#quick-start){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
[Exam Prep](./exam-prep){: .btn .btn-outline .fs-5 .mb-4 .mb-md-0 }

---

## Quick Start
{: .text-blue-200 }

<div class="code-example" markdown="1">

**New to IT?** Start with [Computer Fundamentals](./fundamentals)

**Need exam help?** Jump to [Exam Preparation](./exam-prep)

**Working on PAT?** Check out [Project Guidance](./projects)

**Programming practice?** Visit [Programming & Development](./programming)

</div>

## Learning Pathways
{: .text-blue-200 }

### 📚 Theory Foundations
Master the concepts that power modern technology
- **[Computer Fundamentals](./fundamentals)** - Basic computing concepts
- **[Systems Technologies](./systems)** - Hardware and software
- **[Communication & Internet](./networks)** - Connected world
- **[Data Management](./data)** - Information systems

### 💻 Programming Skills  
Build practical coding abilities
- **[Programming Basics](./programming)** - Start coding in Delphi
- **[Database Development](./database-dev)** - SQL and data apps
- **[Problem Solving](./problem-solving)** - Algorithms and logic

### 🎯 Exam Success
Targeted preparation for success
- **[Paper 1 Prep](./exam-prep/paper1)** - Practical programming exam
- **[Paper 2 Prep](./exam-prep/paper2)** - Theory knowledge exam
- **[PAT Guidance](./projects)** - Practical Assessment Tasks

---

## Grade-Specific Quick Access

| Grade 10 | Grade 11 | Grade 12 |
|-----------|----------|----------|
| [Computing Basics](./fundamentals/grade10) | [Advanced Programming](./programming/grade11) | [Complex Systems](./systems/hardware/grade12) |
| [First Programs](./programming/grade10) | [Database Programming](./database-dev/grade11) | [Advanced SQL](./database-dev/grade12) |
| [Internet Basics](./networks/grade10) | [Network Security](./networks/grade11) | [Emerging Tech](./systems/emerging) |

---

## Recent Updates
{: .text-blue-200 }

- ✅ New website structure with improved navigation
- ✅ Blue theme for better readability  
- ✅ Grade-specific organization
- 🔄 Content migration in progress

## Need Help?
{: .text-blue-200 }

- 💬 Ask questions in [Google Classroom](https://classroom.google.com)
- 📧 Email your teacher
- 🔍 Use the search bar above to find specific topics
"""

def remove_old_structure():
    """Remove old folder structure"""
    print("🗑️  Removing old structure...")
    
    for folder in OLD_FOLDERS:
        if os.path.exists(folder):
            shutil.rmtree(folder)
            print(f"   ✅ Removed {folder}")
        else:
            print(f"   ⚠️  {folder} not found (already removed)")

def create_new_structure():
    """Create new folder structure with content"""
    print("🏗️  Creating new structure...")
    
    for folder_name, folder_contents in NEW_STRUCTURE.items():
        print(f"   📁 Creating {folder_name}/")
        
        for file_path, content in folder_contents.items():
            full_path = Path(folder_name) / file_path
            full_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"      ✅ Created {full_path}")

def update_config_and_homepage():
    """Update configuration and homepage"""
    print("⚙️  Updating configuration...")
    
    # Update _config.yml
    with open('_config.yml', 'w', encoding='utf-8') as f:
        f.write(CONFIG_CONTENT)
    print("   ✅ Updated _config.yml")
    
    # Update homepage
    with open('index.md', 'w', encoding='utf-8') as f:
        f.write(HOMEPAGE_CONTENT)
    print("   ✅ Updated index.md")

def main():
    """Main execution function"""
    print("🚀 IT Gateway Structure Replacement")
    print("=" * 40)
    
    # Check if we're in the right directory
    if not os.path.exists('.git'):
        print("❌ Error: Not in a git repository!")
        print("   Make sure you're in your it-gateway repository folder")
        return
    
    try:
        # Step 1: Remove old structure
        remove_old_structure()
        
        # Step 2: Create new structure
        create_new_structure()
        
        # Step 3: Update config and homepage
        update_config_and_homepage()
        
        print("\n" + "=" * 40)
        print("✅ SUCCESS! New structure created!")
        print("\nNext steps:")
        print("1. Review the changes in VS Code")
        print("2. Commit and push to GitHub:")
        print("   git add .")
        print('   git commit -m "Restructure website with new navigation"')
        print("   git push")
        print("3. Wait 2-3 minutes for GitHub Pages to update")
        print("4. Visit your site to see the new structure!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Please check the error and try again.")

if __name__ == "__main__":
    main()