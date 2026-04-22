---
layout: page
title: Database Design and Concepts
parent: Data and Information Management
nav_order: 2
---

# Database Design and Concepts

{: .note }
This topic forms a significant part of the Grade 12 curriculum and frequently appears in Paper 2, often worth substantial marks.

## Relational Database Design: Core Principles

A relational database organizes data into tables (relations) with rows (records) and columns (fields). Well-designed databases are essential for data integrity, efficiency, and usability.

### Normalization: Organizing Data Effectively

Normalization is a systematic approach to database design that reduces data redundancy and improves data integrity by organizing tables and relationships.

#### Why Normalize?

Unnormalized databases suffer from several problems:
- **Data redundancy**: The same information appears in multiple places
- **Update anomalies**: Changing data in one place but not others creates inconsistencies
- **Insertion anomalies**: Cannot add new records without having complete information
- **Deletion anomalies**: Deleting one record might unintentionally remove other important data

![Database Normalization Benefits](../../../assets/images/normalization-benefits.png)
*Diagram needed: A visual showing before/after normalization with examples of redundancy being eliminated*

#### Normal Forms

Databases are normalized through progressive stages called "normal forms":

**First Normal Form (1NF)**
- Each table cell contains a single value (atomic values)
- Each column has a unique name
- All entries in a column are of the same data type
- No duplicate rows

**Second Normal Form (2NF)**
- Table is in 1NF
- All non-key attributes depend on the entire primary key
- Eliminates partial dependencies

**Third Normal Form (3NF)**
- Table is in 2NF
- No transitive dependencies (non-key attributes don't depend on other non-key attributes)
- All attributes depend directly on the primary key

**Example of Normalization:**

Original unnormalized table:
```
Orders(OrderID, CustomerName, CustomerEmail, CustomerPhone, ProductID, ProductName, ProductPrice, Quantity, OrderDate)
```

After normalization to 3NF:
```
Customers(CustomerID, CustomerName, CustomerEmail, CustomerPhone)
Products(ProductID, ProductName, ProductPrice)
Orders(OrderID, CustomerID, OrderDate)
OrderDetails(OrderID, ProductID, Quantity)
```

### Where Unnormalized Data Comes From

In real-world scenarios, unnormalized data often comes from:

1. **Legacy systems** that weren't designed with modern database principles
2. **Data imports** from spreadsheets or flat files
3. **User-generated content** like forms or surveys
4. **Document-based sources** like receipts, invoices, or applications
5. **Integrated systems** where data from multiple sources is combined

### Analyzing Documents for Data Entities

When designing a database from scratch, you often start with documents or forms that represent business processes.

**Example: Analyzing a Till Slip**

![Till Slip Analysis](../../../assets/images/till-slip-analysis.jpg)
*Image needed: A sample till slip with annotations showing how different parts map to database entities*

From a simple till slip, we can identify several potential entities:
- **Store** (store name, address, contact details, tax number)
- **Cashier** (cashier ID, name)
- **Customer** (customer ID, loyalty program info)
- **Transaction** (date, time, receipt number, payment method)
- **Products** (product code, description, price)
- **Transaction_Details** (quantity, discount, line total)

## Database Entities, Keys, and Organization

### Entities and Records

An **entity** is a person, place, object, event, or concept about which we want to store information. In a relational database:
- Entities are represented as tables
- Each instance of an entity is a record (row)
- Each attribute of an entity is a field (column)

### Keys: The Foundation of Relationships

Keys play a critical role in database design:

**Primary Keys**
- Uniquely identify each record in a table
- Cannot contain NULL values
- Should rarely or never change
- Can be single fields or combinations of fields (composite keys)

**Foreign Keys**
- Reference a primary key in another table
- Create relationships between tables
- Enforce referential integrity
- Can be NULL (if the relationship is optional)

**Alternate Keys**
- Fields that could serve as primary keys but weren't chosen
- Still have uniqueness constraints
- Useful as alternative lookup methods

**Composite Keys**
- Primary keys made up of multiple fields
- Used when no single field uniquely identifies records
- Common in junction tables that establish many-to-many relationships

### Database Relationships

Relationships connect data between tables:

**One-to-One (1:1)**
- Each record in Table A relates to exactly one record in Table B
- Example: Each employee has one employee ID card
- Implementation: Primary key of one table is a foreign key in the other

**One-to-Many (1:M)**
- Each record in Table A can relate to multiple records in Table B
- Example: One department has many employees
- Implementation: Primary key of the "one" side becomes a foreign key in the "many" side

**Many-to-Many (M:N)**
- Multiple records in Table A relate to multiple records in Table B
- Example: Students can enroll in multiple courses, and courses can have multiple students
- Implementation: Requires a junction table with foreign keys to both tables

![Database Relationship Types](../../../assets/images/db-relationships.png)
*Diagram needed: Visual representation of the three relationship types with examples*

## Transaction Processing Systems

Transaction processing systems (TPS) handle database transactions—operations that read or modify database content.

### What is a Transaction?

A transaction is a logical unit of work that must be completed entirely or not at all. Transactions follow the ACID properties:

- **Atomicity**: All operations complete successfully or none do
- **Consistency**: The database moves from one valid state to another
- **Isolation**: Transactions operate independently of each other
- **Durability**: Completed transactions are permanently saved

### Database Transactions in Practice

Common database transactions include:
- Creating new records
- Reading existing data
- Updating information
- Deleting records
- Processing complex operations involving multiple tables

## Characteristics of a Good Database

A well-designed database should have these characteristics:

### Data Integrity

Data integrity ensures accuracy and consistency throughout the database lifecycle:

- **Entity integrity**: Each table has a primary key that uniquely identifies each row
- **Referential integrity**: Foreign key values must match existing primary key values
- **Domain integrity**: Field values must conform to defined data types and constraints

### Data Independence

Data independence separates data from the applications that use it:

- **Physical independence**: Applications aren't affected by changes to physical storage
- **Logical independence**: Applications aren't affected by non-destructive changes to table structure

### Minimal Data Redundancy

- Information should be stored in only one place when possible
- Controlled redundancy may be introduced for performance optimization
- Normalized design minimizes redundancy

### Data Security

- User authentication controls who can access the database
- Authorization determines what actions users can perform
- Encryption protects sensitive data
- Audit trails track database activities

### Ease of Maintenance

- Well-documented design
- Normalized structure
- Consistent naming conventions
- Clear relationships

## Paper 2 Connection

In Paper 2 examinations, expect questions that require you to:
- Analyze unnormalized data and convert it to normalized form
- Identify entities, attributes, and relationships
- Explain the advantages of normalization
- Identify and resolve database anomalies
- Create ER diagrams representing database design
- Explain how key fields enable relationships

{: .highlight }
When answering normalization questions, always work systematically through the normal forms. Identify primary keys first, then look for dependencies between attributes.

## Practice Questions

1. Given the following unnormalized table:
   ```
   Library(BookID, Title, Author, AuthorEmail, MemberID, MemberName, MemberPhone, BorrowDate, ReturnDate)
   ```
   Normalize this table to 3NF, clearly showing all tables, primary keys, and foreign keys.

2. Why is normalization important in database design? Explain three problems that can occur in an unnormalized database.

3. Identify the entities, attributes, and relationships in a school management system that tracks students, teachers, classes, and grades.

4. Explain how transaction processing systems ensure data integrity, with reference to the ACID properties.

5. Draw an ER diagram for a simple online shopping system that includes customers, products, orders, and order details.

## Self-Assessment

Check your understanding:

- [ ] I can explain the purpose and benefits of normalization
- [ ] I understand the first three normal forms and their requirements
- [ ] I can identify entities and attributes from real-world scenarios
- [ ] I understand the different types of keys and their purposes
- [ ] I can explain and implement different types of relationships
- [ ] I understand how transaction processing systems work
- [ ] I know the characteristics of a well-designed database