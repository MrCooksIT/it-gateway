# DBMS Software

A database is only as useful as the software managing it. A Database Management System (DBMS) is the engine behind every application that stores structured data — from a school timetable to a bank's transaction records.

> [!NOTE] Grade 11
> DBMS concepts, software types, and roles are Grade 11 content.

---

## What is a DBMS?

A **DBMS** (Database Management System) is software that creates, manages, and controls access to a database.

The DBMS sits between the user/application and the raw data:

```
User / Application
       ↓
     DBMS
       ↓
   Database (stored data files)
```

**Functions of a DBMS:**
- Create and define database structure (tables, fields, keys)
- Add, update, delete, and retrieve data
- Enforce data integrity rules
- Manage concurrent access (multiple users at once)
- Control security and access permissions
- Handle backup and recovery
- Provide query language (SQL)

---

## Types of DBMS

| Type | Description | Examples |
|---|---|---|
| **Relational DBMS (RDBMS)** | Data stored in related tables; uses SQL | MySQL, MS Access, PostgreSQL, Oracle |
| **NoSQL DBMS** | Non-tabular storage (documents, graphs, key-value) | MongoDB, Firebase, Redis |
| **Hierarchical DBMS** | Data in tree structure (parent-child) | IBM IMS — legacy mainframes |
| **Network DBMS** | Data in graph structure | Legacy — rarely used |
| **Object-oriented DBMS** | Data as objects (with methods) | db4o — mostly research |

The **RDBMS** is by far the most common and is the focus of the CAPS IT curriculum.

---

## Common RDBMS Software

### Microsoft Access
- Desktop RDBMS included in Microsoft Office
- Designed for small to medium databases
- Graphical interface — no coding required for basic use
- Supports SQL queries, forms, reports
- File format: `.accdb`
- **Used in**: school computer labs, small business record-keeping
- **Limitations**: single-user (or small multi-user via network share), max 2 GB database size

### MySQL
- Open-source, free RDBMS
- Server-based — handles thousands of concurrent users
- Used by most websites and web applications
- Command-line interface + many GUI tools (MySQL Workbench)
- **Used in**: web development (WordPress, Facebook originally), e-commerce
- **Managed by**: Oracle Corporation

### PostgreSQL
- Open-source, feature-rich RDBMS
- More advanced than MySQL — better for complex queries
- Excellent standards compliance
- Used in enterprise and data-intensive applications
- **Used in**: scientific applications, GIS, enterprise systems

### Microsoft SQL Server
- Enterprise RDBMS by Microsoft
- Powerful — high performance and security features
- Integrates tightly with Microsoft technologies
- Expensive — used in large corporations
- **Used in**: banking, enterprise applications, Microsoft ecosystems

### Oracle Database
- Industry-leading enterprise RDBMS
- Most feature-rich and powerful commercial option
- Very expensive — used by large corporations and governments
- **Used in**: major banks, airlines, government systems

### SQLite
- Lightweight, file-based RDBMS
- No separate server process — runs inside the application
- Entire database stored in a single `.db` file
- **Used in**: mobile apps (iOS, Android), browsers, small applications, testing

---

## DBMS Comparison

| Feature | MS Access | MySQL | PostgreSQL | SQL Server | SQLite |
|---|---|---|---|---|---|
| Cost | Paid (Office) | Free | Free | Expensive | Free |
| Users | Single/small | Thousands | Thousands | Thousands | Single |
| Interface | GUI | CLI + GUI | CLI + GUI | GUI + CLI | CLI + GUI |
| Scale | Small | Medium-large | Large | Enterprise | Small/embedded |
| SQL support | Partial | Full | Full | Full | Most |
| Use case | School/small biz | Web apps | Enterprise | Corporate | Mobile/embedded |

---

## Roles in Database Management

### Database Administrator (DBA)
The **DBA** is responsible for the overall management of the database system.

**Responsibilities:**
- Installing and configuring DBMS software
- Designing database structure
- Creating user accounts and assigning permissions
- Monitoring performance and optimising queries
- Scheduling and managing backups
- Ensuring security and data integrity
- Applying patches and upgrades
- Disaster recovery planning

### Database Developer / Programmer
Writes SQL queries, stored procedures, and integrates databases into applications.

**Responsibilities:**
- Writing complex SQL queries
- Creating stored procedures and triggers
- Connecting databases to application code (e.g. Delphi, PHP)
- Optimising slow queries

### Database Analyst / BI Analyst
Analyses data to extract insights for business decision-making.

**Responsibilities:**
- Writing reporting queries
- Creating dashboards and reports
- Data cleaning and preparation
- Identifying trends in data

### End User
Uses the database through an application — usually without directly writing SQL.

---

## Query Processing

When a SQL query is submitted to a DBMS:

1. **Parser** — checks SQL syntax for errors
2. **Query optimiser** — determines the most efficient execution plan
3. **Execution engine** — retrieves data according to the plan
4. **Buffer manager** — manages data in memory vs disk
5. **Result** — returned to the application

**Indexes:**
- An **index** speeds up data retrieval, similar to a book index
- Created on frequently searched columns
- Trade-off: indexes speed up reads but slow down writes (index must be updated when data changes)

---

## Backup and Recovery in DBMS

| Method | Description |
|---|---|
| **Full database backup** | Complete copy of all data |
| **Transaction log backup** | Record of every change — allows point-in-time recovery |
| **Incremental backup** | Only changes since last backup |
| **Hot backup** | Backup while database is online (no downtime) |
| **Cold backup** | Backup while database is offline |

**Recovery scenarios:**
- Hardware failure → restore from backup
- Corruption → restore + replay transaction logs
- Accidental deletion → restore to point before deletion

---

## Key Terms

| Term | Definition |
|---|---|
| **DBMS** | Software managing and controlling access to a database |
| **RDBMS** | Relational DBMS — data stored in related tables |
| **MS Access** | Desktop RDBMS for small databases |
| **MySQL** | Open-source server RDBMS for web applications |
| **PostgreSQL** | Open-source enterprise RDBMS |
| **DBA** | Database Administrator — manages the overall database system |
| **Index** | Data structure speeding up retrieval of specific values |
| **Query optimiser** | DBMS component that finds the most efficient execution plan |
| **Stored procedure** | Pre-compiled SQL stored in the database for reuse |
| **Concurrent access** | Multiple users reading/writing simultaneously |

---

## Exam Focus

> [!IMPORTANT] High-Frequency Questions
>
> 1. **"What is a DBMS? Give TWO examples."** — Software that manages and controls access to a database; examples: Microsoft Access, MySQL, PostgreSQL, SQL Server
>
> 2. **"Give THREE functions of a DBMS"** — Define database structure; retrieve/add/update/delete data; enforce data integrity; manage security and access; backup and recovery; handle concurrent access
>
> 3. **"What are the responsibilities of a DBA?"** — Installing/configuring DBMS; designing structure; creating users and permissions; backup and recovery; monitoring performance; ensuring security
>
> 4. **"Give ONE advantage and ONE disadvantage of Microsoft Access compared to MySQL"** — Advantage: graphical interface, no setup required, suitable for beginners; Disadvantage: limited to small databases, poor multi-user support, max 2 GB
>
> 5. **"What is an index in a database? What is the trade-off?"** — Speeds up data retrieval on searched columns; trade-off: slows down write operations as the index must be updated with every data change
