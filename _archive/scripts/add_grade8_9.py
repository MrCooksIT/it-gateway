#!/usr/bin/env python3
"""
Add Grade 8-9 Digital Technology structure to IT Gateway
Run this in your VS Code terminal in your repo directory
"""

import os
from pathlib import Path

# Grade 8-9 Digital Technology structure
DIGITAL_TECH_STRUCTURE = {
    "digital-technology": {
        "index.md": """---
layout: page
title: Digital Technology (Grades 8-9)
permalink: /digital-technology/
nav_order: 2
has_children: true
---

# Digital Technology (Grades 8-9)
{: .text-blue-200 }

Foundation skills for the digital world - preparing for IT in Grades 10-12.

## Welcome to Digital Technology
These grades introduce you to the fundamentals of computing, digital citizenship, and basic programming concepts that will prepare you for Information Technology in the senior phase.

## What You'll Learn
- **Digital citizenship** and responsible technology use
- **Computer fundamentals** and digital literacy
- **Basic programming** concepts and computational thinking
- **Digital creation** with various software tools
- **Problem-solving** using technology

## Grade Structure
- **[Grade 8 Digital Technology](./grade8)** - Introduction to digital concepts
- **[Grade 9 Digital Technology](./grade9)** - Building on foundations for IT readiness

---

## Learning Outcomes

### 📱 Digital Citizenship
- Understand online safety and digital ethics
- Learn about digital footprints and privacy
- Explore cyberbullying prevention and digital wellness

### 💻 Computing Fundamentals  
- Discover how computers work
- Learn about input, processing, output, and storage
- Explore different types of technology devices

### 🎯 Problem Solving
- Introduction to computational thinking
- Basic algorithm design
- Simple programming concepts

### 🛠️ Digital Creation
- Using productivity software effectively
- Creating digital presentations and documents
- Introduction to multimedia creation

---

## Pathway to IT Success

Digital Technology in Grades 8-9 serves as your stepping stone to Information Technology:

**Grade 8-9 Digital Technology** → **Grade 10-12 Information Technology**

The skills you learn here will directly support your success in:
- [Computer Fundamentals](../fundamentals) (Grade 10-12)
- [Programming & Development](../programming) (Grade 10-12)
- [Systems Technologies](../systems) (Grade 10-12)

---

## Getting Started

Choose your grade level below to access age-appropriate content, activities, and projects designed to build your digital literacy and prepare you for advanced IT studies.

Ready to explore the digital world? Click on your grade to begin!
""",
        
        "grade8/index.md": """---
layout: page
title: Grade 8 Digital Technology
parent: Digital Technology (Grades 8-9)
nav_order: 1
has_children: true
---

# Grade 8: Digital Technology Foundations
{: .text-blue-200 }

Welcome to your digital journey! This year focuses on building essential digital literacy skills.

## Year Overview

In Grade 8, you'll explore the basics of technology and develop responsible digital citizenship habits that will serve you throughout your life.

## Key Topics This Year

### 🌐 Digital Citizenship
- **Online Safety**: Protecting yourself and others online
- **Digital Ethics**: Right and wrong in the digital world  
- **Privacy & Security**: Keeping your information safe
- **Digital Footprints**: Understanding your online presence

### 💻 Computer Basics
- **Hardware & Software**: Understanding computer components
- **Operating Systems**: How computers work
- **File Management**: Organizing your digital files
- **Input & Output**: How we interact with computers

### 🧠 Computational Thinking
- **Problem Solving**: Breaking big problems into smaller parts
- **Patterns**: Recognizing similarities and sequences
- **Algorithms**: Step-by-step instructions
- **Introduction to Programming**: Basic coding concepts

### 🎨 Digital Creation
- **Document Creation**: Professional word processing
- **Presentations**: Effective slideshow design
- **Digital Art**: Creating and editing images
- **Research Skills**: Finding reliable information online

---

## Learning Modules

### Module 1: Digital Citizen
Learn to be a responsible member of the digital community.
- [Online Safety Basics](./digital-citizenship/online-safety)
- [Digital Footprints](./digital-citizenship/digital-footprints)
- [Cyberbullying Prevention](./digital-citizenship/cyberbullying)

### Module 2: Computer Foundations
Understand how computers work and how to use them effectively.
- [Computer Components](./computer-basics/components)
- [Operating System Basics](./computer-basics/operating-systems)
- [File Organization](./computer-basics/file-management)

### Module 3: Problem Solving
Develop logical thinking skills for the digital age.
- [Computational Thinking](./problem-solving/computational-thinking)
- [Algorithm Design](./problem-solving/algorithms)
- [Introduction to Coding](./problem-solving/intro-coding)

### Module 4: Digital Creator
Build practical skills with digital tools.
- [Word Processing Mastery](./digital-creation/word-processing)
- [Presentation Skills](./digital-creation/presentations)
- [Image Editing Basics](./digital-creation/image-editing)

---

## Assessment & Projects

Throughout the year, you'll complete various projects to demonstrate your learning:

- **Digital Citizenship Portfolio**: Showcase your understanding of online responsibility
- **Computer Basics Presentation**: Explain how computers work
- **Algorithm Challenge**: Create step-by-step solutions to problems
- **Digital Creation Showcase**: Demonstrate your technical skills

---

## Preparing for Grade 9

The skills you learn in Grade 8 will prepare you for more advanced topics in Grade 9, including:
- More complex programming concepts
- Advanced digital creation techniques
- Deeper understanding of computer systems
- Introduction to databases and networks

*Ready to start your digital technology journey? Explore the modules above to begin learning!*
""",
        
        "grade9/index.md": """---
layout: page
title: Grade 9 Digital Technology
parent: Digital Technology (Grades 8-9)
nav_order: 2
has_children: true
---

# Grade 9: Advanced Digital Technology
{: .text-blue-200 }

Building on Grade 8 foundations to prepare for Information Technology in Grades 10-12.

## Year Overview

Grade 9 expands on your digital literacy foundation with more advanced concepts in programming, digital creation, and technology systems. This year specifically prepares you for the transition to formal Information Technology studies.

## Key Topics This Year

### 💡 Advanced Programming Concepts
- **Programming Languages**: Introduction to real programming languages
- **Control Structures**: Loops, conditions, and decision making
- **Data Types**: Numbers, text, and logical values
- **Simple Applications**: Creating basic interactive programs

### 🔧 Computer Systems  
- **Hardware Deep Dive**: CPU, memory, storage in detail
- **Software Systems**: How programs and operating systems work together
- **Networks**: How computers connect and communicate
- **Troubleshooting**: Solving common computer problems

### 📊 Data & Information
- **Data vs Information**: Understanding the difference
- **Data Organization**: Filing systems and databases
- **Spreadsheet Mastery**: Advanced calculations and charts
- **Research & Analysis**: Using data to solve problems

### 🌐 Digital Design & Media
- **Web Design Basics**: HTML and website creation
- **Multimedia Projects**: Combining text, images, audio, video
- **Graphic Design**: Creating professional digital graphics
- **Digital Storytelling**: Communicating effectively with technology

---

## Learning Modules

### Module 1: Programming Foundations
Build real programming skills that connect to Grade 10 IT.
- [Programming Language Basics](./programming/language-basics)
- [Control Structures](./programming/control-structures)
- [Simple Applications](./programming/simple-apps)

### Module 2: System Understanding
Deeper knowledge of how technology systems work.
- [Computer Architecture](./systems/architecture)
- [Network Fundamentals](./systems/networks)
- [System Maintenance](./systems/maintenance)

### Module 3: Data Literacy
Working with information in the digital age.
- [Data Types & Organization](./data/organization)
- [Spreadsheet Advanced Skills](./data/spreadsheets)
- [Database Introduction](./data/databases)

### Module 4: Digital Design
Creative and technical skills for digital media.
- [Web Design Principles](./design/web-design)
- [Multimedia Creation](./design/multimedia)
- [Design Thinking](./design/design-thinking)

---

## Bridge to Grade 10 IT

Grade 9 specifically prepares you for Information Technology by introducing:

### Programming Readiness
- Variables and data types → **Grade 10 Delphi Programming**
- Control structures → **Grade 10 Algorithms**
- Problem solving → **Grade 10 Solution Development**

### System Knowledge
- Computer components → **Grade 10 Systems Technologies**
- Networks → **Grade 10 Communication Technologies**
- File management → **Grade 10 Data Representation**

### Digital Citizenship
- Ethics and responsibility → **Grade 10-12 Social Implications**
- Online safety → **Grade 10-12 Security Concepts**

---

## Major Projects

This year includes substantial projects that mirror Grade 10 IT assessments:

### Semester 1 Projects
- **Programming Portfolio**: Collection of small programs demonstrating key concepts
- **System Analysis**: Research and present on a computer system component
- **Digital Ethics Case Study**: Analyze real-world technology ethical dilemmas

### Semester 2 Projects  
- **Website Creation Project**: Build a multi-page website on a chosen topic
- **Data Analysis Challenge**: Use spreadsheets to solve a real-world problem
- **Multimedia Presentation**: Combine programming, design, and presentation skills

---

## Getting Ready for Grade 10

By the end of Grade 9, you should be comfortable with:

✅ **Basic programming concepts** (variables, loops, conditions)  
✅ **Computer system components** and how they work together  
✅ **File and data organization** principles  
✅ **Digital citizenship** and ethical technology use  
✅ **Problem-solving** using computational thinking  
✅ **Digital creation** tools and techniques  

These skills form the foundation for success in Grade 10-12 Information Technology!

*Ready to advance your digital technology skills? Explore the modules above to continue your learning journey!*
""",
        
        # Grade 8 sub-modules
        "grade8/digital-citizenship/index.md": """---
layout: page
title: Digital Citizenship
parent: Grade 8 Digital Technology
grand_parent: Digital Technology (Grades 8-9)
nav_order: 1
has_children: true
---

# Digital Citizenship for Grade 8

Being a responsible member of the digital community.

## What is Digital Citizenship?

Digital citizenship means using technology safely, responsibly, and respectfully. Just like in the physical world, there are rules and expectations for how we behave online.

## Key Areas We'll Cover

- **Online Safety**: Protecting yourself from online dangers
- **Digital Footprints**: Understanding your permanent online presence  
- **Cyberbullying**: Preventing and responding to online harassment
- **Privacy**: Keeping your personal information secure
- **Digital Ethics**: Making good choices online

*Content modules coming soon...*
""",
        
        "grade8/computer-basics/index.md": """---
layout: page
title: Computer Basics
parent: Grade 8 Digital Technology
grand_parent: Digital Technology (Grades 8-9)
nav_order: 2
has_children: true
---

# Computer Basics for Grade 8

Understanding how computers work and how to use them effectively.

## Learning Objectives

By the end of this module, you'll understand:
- The main parts of a computer and what they do
- How to organize files and folders
- Basic troubleshooting when things go wrong
- Different types of software and their purposes

## Topics

- **Hardware Components**: CPU, memory, storage, input/output devices
- **Software Systems**: Operating systems, applications, and utilities
- **File Management**: Creating folders, saving files, staying organized
- **Basic Maintenance**: Keeping your computer running smoothly

*Content modules coming soon...*
""",
        
        "grade8/problem-solving/index.md": """---
layout: page
title: Problem Solving
parent: Grade 8 Digital Technology
grand_parent: Digital Technology (Grades 8-9)
nav_order: 3
has_children: true
---

# Problem Solving for Grade 8

Developing logical thinking skills for the digital age.

## Computational Thinking

Learn to think like a computer scientist:
- **Decomposition**: Breaking big problems into smaller parts
- **Pattern Recognition**: Finding similarities and trends
- **Abstraction**: Focusing on important details
- **Algorithms**: Creating step-by-step solutions

## What You'll Learn

- How to approach complex problems systematically
- Creating flowcharts and algorithms
- Introduction to programming logic
- Debugging and testing solutions

*Content modules coming soon...*
""",
        
        "grade8/digital-creation/index.md": """---
layout: page
title: Digital Creation
parent: Grade 8 Digital Technology
grand_parent: Digital Technology (Grades 8-9)
nav_order: 4
has_children: true
---

# Digital Creation for Grade 8

Building practical skills with digital tools.

## Creating with Technology

Learn to use technology as a tool for creativity and communication:
- Professional document creation
- Engaging presentation design
- Basic image editing and graphics
- Effective research and information gathering

## Skills You'll Develop

- **Word Processing**: Creating professional documents with formatting
- **Presentations**: Designing clear, engaging slideshows
- **Digital Art**: Using software to create and edit images
- **Research**: Finding reliable information and avoiding fake news

*Content modules coming soon...*
""",
        
        # Grade 9 sub-modules  
        "grade9/programming/index.md": """---
layout: page
title: Programming Foundations
parent: Grade 9 Digital Technology
grand_parent: Digital Technology (Grades 8-9)
nav_order: 1
has_children: true
---

# Programming Foundations for Grade 9

Building real programming skills that prepare you for Grade 10 IT.

## Programming Languages

This year you'll work with actual programming languages:
- **Scratch**: Visual programming for complex projects
- **Python**: Introduction to text-based programming
- **HTML/CSS**: Web programming basics

## Core Concepts

- **Variables**: Storing and using data
- **Control Structures**: Making decisions and repeating actions
- **Functions**: Organizing code into reusable parts
- **Debugging**: Finding and fixing errors

*Content modules coming soon...*
""",
        
        "grade9/systems/index.md": """---
layout: page
title: System Understanding
parent: Grade 9 Digital Technology
grand_parent: Digital Technology (Grades 8-9)
nav_order: 2
has_children: true
---

# System Understanding for Grade 9

Deeper knowledge of how technology systems work.

## Computer Architecture

Understanding the internal workings of computers:
- How the CPU processes information
- Memory hierarchy and storage systems
- Input/output system coordination
- Performance factors

## Networks & Communication

How computers connect and share information:
- Network types and topologies
- Internet protocols and services
- Wireless technologies
- Network security basics

*Content modules coming soon...*
""",
        
        "grade9/data/index.md": """---
layout: page
title: Data Literacy
parent: Grade 9 Digital Technology
grand_parent: Digital Technology (Grades 8-9)
nav_order: 3
has_children: true
---

# Data Literacy for Grade 9

Working with information in the digital age.

## Data vs Information

Understanding the relationship between raw data and useful information:
- Data types and formats
- Information processing cycle
- Data quality and reliability
- Making decisions with data

## Tools & Techniques

- **Spreadsheets**: Advanced formulas, charts, and analysis
- **Databases**: Introduction to organizing large amounts of data
- **Data Visualization**: Creating meaningful charts and graphs

*Content modules coming soon...*
""",
        
        "grade9/design/index.md": """---
layout: page
title: Digital Design
parent: Grade 9 Digital Technology
grand_parent: Digital Technology (Grades 8-9)
nav_order: 4
has_children: true
---

# Digital Design for Grade 9

Creative and technical skills for digital media.

## Web Design

Creating websites that are both attractive and functional:
- HTML structure and content
- CSS styling and layout
- User experience principles
- Responsive design basics

## Multimedia Creation

Combining different media types effectively:
- Digital graphics and image editing
- Audio recording and editing
- Video production basics
- Interactive presentations

*Content modules coming soon...*
"""
    }
}

# Updated config to include Digital Technology
UPDATED_CONFIG = """title: IT Gateway
description: Comprehensive resource for Digital Technology (Grades 8-9) and Information Technology (Grades 10-12)

# Use remote theme
remote_theme: just-the-docs/just-the-docs

# Enable search
search_enabled: true

# Navigation
nav_external_links:
  - title: Google Classroom
    url: https://classroom.google.com

# Enable features
enable_copy_code_button: true

# Footer
footer_content: "IT Gateway - Digital Technology & Information Technology © 2025"

# Plugins
plugins:
  - jekyll-feed
  - jekyll-sitemap
  - jekyll-seo-tag

# Exclude files
exclude:
  - README.md
  - "*.py"
"""

# Updated homepage to include Grade 8-9
UPDATED_HOMEPAGE = """---
layout: home
title: IT Gateway
---

# IT Gateway

**Your complete resource for Digital Technology (Grades 8-9) and Information Technology (Grades 10-12)**

Welcome to your comprehensive guide for technology education. This site provides age-appropriate content from foundational digital literacy through advanced programming and system design.

---

## 🚀 Quick Start by Grade Level

**Grade 8-9?** → Start with [Digital Technology](./digital-technology) foundations

**Grade 10-12?** → Explore [Information Technology](./fundamentals) concepts

**Need exam help?** → Jump to [Exam Preparation](./exam-prep)

**Working on projects?** → Check out [Project Guidance](./projects)

---

## 📚 Learning Pathways

### 🎯 Digital Technology (Grades 8-9)
Foundation skills for the digital world:

- **[Grade 8 Digital Technology](./digital-technology/grade8)** - Digital citizenship, computer basics, introduction to programming
- **[Grade 9 Digital Technology](./digital-technology/grade9)** - Advanced programming, system understanding, preparing for IT

### 📊 Information Technology (Grades 10-12)
Advanced concepts and practical skills:

- **[Computer Fundamentals](./fundamentals)** - Computing concepts and data representation
- **[Systems Technologies](./systems)** - Hardware, software, and system management  
- **[Communication & Internet](./networks)** - Networks, protocols, and web technologies
- **[Data Management](./data)** - Database concepts and information systems

### 💻 Programming & Development
Build coding skills across all grade levels:

- **[Programming & Development](./programming)** - Delphi programming from basics to advanced
- **[Database Development](./database-dev)** - SQL programming and database applications
- **[Problem Solving](./problem-solving)** - Algorithms, logic, and computational thinking

### 🎯 Assessment Success
Targeted preparation for projects and exams:

- **[Exam Preparation](./exam-prep)** - Paper 1 (Practical) and Paper 2 (Theory) preparation
- **[Project Guidance](./projects)** - PAT (Practical Assessment Task) support
- **[Additional Resources](./resources)** - Quick reference, glossary, and practice materials

---

## 🎯 Grade-Specific Quick Access

| **Grade 8** | **Grade 9** | **Grade 10** | **Grade 11** | **Grade 12** |
|-------------|-------------|---------------|---------------|---------------|
| [Digital Citizenship](./digital-technology/grade8/digital-citizenship) | [Programming Foundations](./digital-technology/grade9/programming) | [Computing Basics](./fundamentals/grade10) | [Advanced Programming](./programming/grade11) | [Complex Systems](./systems) |
| [Computer Basics](./digital-technology/grade8/computer-basics) | [System Understanding](./digital-technology/grade9/systems) | [First Programs](./programming/grade10) | [Database Programming](./database-dev/grade11) | [Advanced SQL](./database-dev/grade12) |
| [Problem Solving](./digital-technology/grade8/problem-solving) | [Digital Design](./digital-technology/grade9/design) | [Internet Basics](./networks/grade10) | [Network Security](./networks/grade11) | [Emerging Tech](./systems/emerging) |

---

## 🛤️ Learning Progression

Our curriculum builds progressively across the grades:

### Foundation Phase (Grades 8-9): Digital Technology
- **Digital citizenship** and responsible technology use
- **Computer literacy** and basic system understanding
- **Introduction to programming** concepts and logic
- **Digital creation** and multimedia skills

### Development Phase (Grade 10): Information Technology Introduction  
- **Programming fundamentals** with Delphi
- **System architecture** and hardware concepts
- **Network basics** and internet technologies
- **Data representation** and file management

### Advanced Phase (Grades 11-12): Information Technology Mastery
- **Complex programming** and software engineering
- **Database design** and SQL development
- **Advanced networking** and security concepts
- **Emerging technologies** and industry applications

---

## 📖 How to Use This Site

This resource is designed to work alongside your regular technology classes:

1. **Choose your grade level** using the quick access table above
2. **Browse by topic** using the main navigation menu
3. **Search for specific content** using your browser's search (Ctrl+F)
4. **Follow the learning progressions** from Grade 8 → 12
5. **Practice with examples** and work through tutorials
6. **Prepare for assessments** with targeted materials

---

## 🆕 Recent Updates

- ✅ **Added Grade 8-9 Digital Technology** sections
- ✅ **Progressive curriculum structure** across all grades
- ✅ **Enhanced navigation** for multi-grade content
- ✅ **Mobile-friendly design** for learning anywhere
- 🔄 **Content development** - adding materials regularly

---

## 💡 Need Help?

- 💬 **Ask questions** in your Google Classroom
- 📧 **Email your teacher** for specific guidance  
- 🔍 **Use browser search** (Ctrl+F) to find topics quickly
- 📚 **Check the glossary** in [Resources](./resources) for definitions

---

**Ready to start your technology journey?** Choose your grade level above and begin exploring the digital world!
"""

def create_digital_tech_structure():
    """Create the Digital Technology structure for Grades 8-9"""
    print("🏗️  Creating Digital Technology structure for Grades 8-9...")
    
    for file_path, content in DIGITAL_TECH_STRUCTURE["digital-technology"].items():
        full_path = Path("digital-technology") / file_path
        full_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"   ✅ Created {full_path}")

def update_config_and_homepage():
    """Update configuration and homepage to include Digital Technology"""
    print("⚙️  Updating configuration and homepage...")
    
    # Update _config.yml
    with open('_config.yml', 'w', encoding='utf-8') as f:
        f.write(UPDATED_CONFIG)
    print("   ✅ Updated _config.yml with Digital Technology")
    
    # Update homepage
    with open('index.md', 'w', encoding='utf-8') as f:
        f.write(UPDATED_HOMEPAGE)
    print("   ✅ Updated index.md with Grade 8-9 content")

def main():
    """Main execution function"""
    print("🚀 Adding Grade 8-9 Digital Technology to IT Gateway")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists('.git'):
        print("❌ Error: Not in a git repository!")
        print("   Make sure you're in your it-gateway repository folder")
        return
    
    try:
        # Step 1: Create Digital Technology structure
        create_digital_tech_structure()
        
        # Step 2: Update config and homepage
        update_config_and_homepage()
        
        print("\n" + "=" * 50)
        print("✅ SUCCESS! Grade 8-9 Digital Technology structure added!")
        print("\n📁 New structure created:")
        print("   digital-technology/")
        print("   ├── index.md (main overview)")
        print("   ├── grade8/ (Grade 8 content)")
        print("   │   ├── digital-citizenship/")
        print("   │   ├── computer-basics/")
        print("   │   ├── problem-solving/")
        print("   │   └── digital-creation/")
        print("   └── grade9/ (Grade 9 content)")
        print("       ├── programming/")
        print("       ├── systems/")
        print("       ├── data/")
        print("       └── design/")
        
        print("\n🔄 Next steps:")
        print("1. Review the new structure in VS Code")
        print("2. Customize content for your specific curriculum needs")
        print("3. Commit and push to GitHub:")
        print("   git add .")
        print('   git commit -m "Add Grade 8-9 Digital Technology structure"')
        print("   git push")
        print("4. Wait 2-3 minutes for GitHub Pages to update")
        print("5. Visit your site to see the new Digital Technology section!")
        
        print("\n💡 Tips:")
        print("- The Grade 8-9 content prepares students for Grade 10-12 IT")
        print("- Each grade has age-appropriate modules and projects")
        print("- Content templates are ready for you to customize")
        print("- Navigation automatically includes the new sections")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Please check the error and try again.")

if __name__ == "__main__":
    main()