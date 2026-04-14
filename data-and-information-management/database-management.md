---
layout: page
title: Database Management
parent: Data and Information Management
nav_order: 3
---

# Database Management

{: .note }
This topic is part of the Grade 12 CAPS curriculum and builds on the database concepts covered in Grades 10 and 11. Understanding database management is critical for both theoretical knowledge and practical database applications.

## Caring for and Managing Data

In our digital world, data has become one of the most valuable resources. Organizations collect and store massive amounts of data, but this data is only valuable if it is properly managed and protected.

### The Value of Data

Data is valuable for several reasons:

- **Business intelligence**: Informs strategic decision-making
- **Customer insights**: Helps understand customer behavior and preferences
- **Operational efficiency**: Optimizes business processes
- **Competitive advantage**: Provides market insights and trends
- **Historical record**: Preserves organizational knowledge
- **Compliance**: Fulfills legal and regulatory requirements
- **Resource allocation**: Guides where to invest time and money

![Value of Data Pyramid](../../../assets/images/data-value-pyramid.jpg)
*Image needed: A pyramid showing the progression from raw data to information to knowledge to wisdom*

### How to Protect Data

Protecting data requires a multi-faceted approach:

#### 1. Data Validation

Data validation ensures that data entered into the system conforms to expected formats and values:

- **Format validation**: Checks that data follows required patterns (e.g., email format)
- **Range validation**: Ensures values fall within acceptable ranges
- **Type validation**: Verifies correct data types (numbers, text, dates)
- **Consistency validation**: Checks for logical consistency between related data items
- **Uniqueness validation**: Ensures values are unique where required
- **Referential validation**: Confirms that referenced values exist in related tables

Example validation in SQL:
```sql
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) CHECK (Email LIKE '%@%.%'),
    Age INT CHECK (Age BETWEEN 14 AND 22),
    EnrollmentDate DATE CHECK (EnrollmentDate <= CURRENT_DATE)
);
```

#### 2. Data Verification

While validation checks if data is in the correct format, verification checks if it is accurate:

- **Double entry**: Data is entered twice and compared
- **Checksums**: Mathematical calculations verify data integrity
- **Visual verification**: Manual comparison against source documents
- **Cross-referencing**: Comparing with other data sources
- **Sampling**: Checking a representative subset of data

#### A practical example of data verification:

When a user enters their address, an API might check against postal service records to verify that the address actually exists.

#### 3. Data Integrity

Data integrity ensures that data remains accurate and consistent throughout its lifecycle:

- **Entity integrity**: Each record has a unique identifier
- **Referential integrity**: Relationships between tables remain valid
- **Domain integrity**: Values conform to defined constraints
- **User-defined integrity**: Custom business rules are enforced

![Data Integrity Types](../../../assets/images/data-integrity-types.png)
*Diagram needed: Visual representation of the different types of data integrity*

#### 4. Logging Changes (Audit Trail)

An audit trail tracks all changes to the database:

- Who made the change
- What change was made
- When the change occurred
- Why the change was made (reason or reference)
- Previous and new values

This provides accountability and enables:
- Troubleshooting errors
- Investigating security incidents
- Compliance with regulations
- Recovering from mistakes
- Tracking data history

#### 5. Data Warehousing

Data warehousing involves consolidating data from multiple sources into a central repository designed for query and analysis:

- Stores historical data
- Separates analytical processing from transactional processing
- Integrates data from different sources
- Organizes data by subject rather than by application
- Provides a consistent view of organizational data

![Data Warehouse Architecture](../../../assets/images/data-warehouse-architecture.jpg)
*Diagram needed: Basic data warehouse architecture showing data sources, ETL process, and data warehouse components*

#### 6. Controlling Access

Access control protects data from unauthorized use:

- **Authentication**: Verifies user identity (passwords, biometrics, tokens)
- **Authorization**: Determines what authenticated users can do
- **Role-based access control**: Assigns permissions based on job functions
- **Principle of least privilege**: Users have only the access they need
- **Access logs**: Track who accessed what data and when

#### 7. Parallel Data Sets

Maintaining parallel data sets provides redundancy:

- **Backups**: Regular copies of the database stored securely
- **Mirrors**: Real-time duplicates that can be switched to if primary fails
- **Distributed databases**: Data stored across multiple locations
- **RAID systems**: Redundant array of independent disks for hardware redundancy

## Hacking Through Data

Data security breaches can occur through various vulnerabilities in database systems.

### Invalid/False Data

Invalid or false data can compromise database integrity and security:

- **Data poisoning**: Intentionally introducing incorrect data
- **Malformed input**: Submitting unexpected data formats
- **Boundary testing**: Inputting extreme values to cause overflows
- **Logical inconsistencies**: Creating contradictory data states

### Database Management Software (DBMS) Flaws

#### SQL Injection

SQL injection is one of the most common and dangerous database attacks:

1. **What is SQL Injection?**
   A code injection technique that exploits vulnerabilities in the way user input is processed in database queries.

2. **How it works:**
   Instead of providing expected input, attackers insert malicious SQL code that changes the intended query.

   **Example:**
   
   Vulnerable code:
   ```sql
   "SELECT * FROM Users WHERE Username = '" + userInput + "' AND Password = '" + passwordInput + "'";
   ```
   
   Malicious input:
   ```
   Username: admin' --
   Password: anything
   ```
   
   Resulting query:
   ```sql
   SELECT * FROM Users WHERE Username = 'admin' -- ' AND Password = 'anything'
   ```
   
   The `--` comments out the password check, allowing login without a valid password.

![SQL Injection Attack](../../../assets/images/sql-injection.png)
*Diagram needed: Visual representation of an SQL injection attack*

3. **Protection against SQL injection:**
   - Use parameterized queries/prepared statements
   - Implement input validation
   - Use stored procedures
   - Apply principle of least privilege for database accounts
   - Regular security audits

   **Safe code example:**
   ```pascal
   Query.SQL.Text := 'SELECT * FROM Users WHERE Username = :Username AND Password = :Password';
   Query.Parameters.ParamByName('Username').Value := UsernameEdit.Text;
   Query.Parameters.ParamByName('Password').Value := PasswordEdit.Text;
   ```

## Database Management Roles and Responsibilities

Managing a database system requires specialized roles:

### Database Administrator (DBA)

The DBA is responsible for the overall management of database systems:

- **Database design and implementation**
- **Performance monitoring and optimization**
- **Security management**
- **Backup and recovery planning**
- **User access management**
- **Troubleshooting database issues**
- **Upgrade and patch management**
- **Capacity planning**

### UNIX Administrators

For databases running on UNIX/Linux systems:

- **Operating system maintenance**
- **Server hardware management**
- **Network configuration**
- **Security hardening**
- **Automation through shell scripting**
- **Performance tuning at the OS level**

### Programmers

Programmers interact with databases through code:

- **Developing database-driven applications**
- **Writing efficient SQL queries**
- **Implementing data access layers**
- **Creating stored procedures and triggers**
- **Building data migration scripts**
- **Performance optimization**

### Analysts

Analysts bridge the gap between business needs and technical implementation:

- **Gathering requirements**
- **Data modeling**
- **Process analysis**
- **Report design**
- **User interface design**
- **Testing and validation**
- **Documentation**

### Project Managers

Project managers oversee database development projects:

- **Project planning and scheduling**
- **Resource allocation**
- **Risk management**
- **Stakeholder communication**
- **Budget management**
- **Quality assurance**
- **Change management**

![Database Management Roles](../../../assets/images/db-management-roles.jpg)
*Image needed: An organizational chart showing the relationships between different database management roles*

## Paper 2 Connection

In Paper 2 examinations, expect questions that require you to:
- Explain the importance of data validation and verification
- Describe methods to protect and secure database systems
- Explain the risks of SQL injection and how to prevent it
- Compare different data integrity types
- Discuss the roles and responsibilities in database management
- Explain the concept and benefits of data warehousing

{: .highlight }
When answering questions about database management, always consider both technical aspects (how it works) and business implications (why it matters).

## Practice Questions

1. Explain four methods used to protect data in a database system and provide an example of each.

2. What is SQL injection? Explain how it works and provide three ways to prevent it.

3. Compare and contrast the roles of a Database Administrator and a Database Programmer.

4. Explain the concept of data warehousing and discuss three benefits it provides to organizations.

5. A school management system contains sensitive student information. Describe a comprehensive approach to protecting this data.

## Self-Assessment

Check your understanding:

- [ ] I can explain the value of data in modern organizations
- [ ] I understand different methods of data validation and verification
- [ ] I can explain what data integrity is and its different types
- [ ] I understand how audit trails work and why they're important
- [ ] I can explain the concept of data warehousing
- [ ] I understand what SQL injection is and how to prevent it
- [ ] I can describe the different roles involved in database management