---
layout: page
title: Database Theory in SQL
parent: Solution Development
nav_order: 3
---

# Database Theory in SQL

This page demonstrates how theoretical database concepts are implemented in practical SQL code and database development.

## Normalization in Practice

### The Theory: Normalization

Database normalization is a systematic approach to organizing database tables to reduce redundancy and improve data integrity. The main normal forms are:

1. **First Normal Form (1NF)**:
   - Eliminate duplicate columns
   - Create separate tables for related data
   - Identify each row with a unique column (primary key)

2. **Second Normal Form (2NF)**:
   - Meet all 1NF requirements
   - Remove partial dependencies (fields that depend only on part of the primary key)

3. **Third Normal Form (3NF)**:
   - Meet all 2NF requirements
   - Remove transitive dependencies (fields that depend on non-key fields)

### The Practice: SQL Implementation

#### Before Normalization

An unnormalized table often looks like this:

```sql
CREATE TABLE Orders (
    OrderID INT,
    CustomerName VARCHAR(100),
    CustomerAddress VARCHAR(200),
    CustomerPhone VARCHAR(15),
    ProductID INT,
    ProductName VARCHAR(100),
    ProductCategory VARCHAR(50),
    ProductPrice DECIMAL(10,2),
    Quantity INT,
    OrderDate DATE
);
```

This design has several problems:
- Customer data is repeated for every product they order
- Product data is repeated for every order of that product
- Updating product information requires changes to multiple rows

#### After Normalization (3NF)

```sql
-- Customers table (contains customer information)
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(100),
    CustomerAddress VARCHAR(200),
    CustomerPhone VARCHAR(15)
);

-- Products table (contains product information)
CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100),
    ProductCategory VARCHAR(50),
    ProductPrice DECIMAL(10,2)
);

-- Orders table (contains order header information)
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- OrderDetails table (contains order line items)
CREATE TABLE OrderDetails (
    OrderID INT,
    ProductID INT,
    Quantity INT,
    PRIMARY KEY (OrderID, ProductID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);
```

## Entity Relationship Diagrams and SQL

### The Theory: Entity Relationship Diagrams (ERDs)

ERDs visually represent the relationships between entities (tables) in a database:

![Entity Relationship Diagram](../../assets/images/erd-example.png)

The main relationship types are:
- **One-to-One (1:1)**: One record in Table A relates to exactly one record in Table B
- **One-to-Many (1:M)**: One record in Table A relates to multiple records in Table B
- **Many-to-Many (M:N)**: Multiple records in Table A relate to multiple records in Table B

### The Practice: SQL Relationships

#### One-to-One Relationship

```sql
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50)
);

CREATE TABLE StudentDetails (
    StudentID INT PRIMARY KEY,
    DateOfBirth DATE,
    Address VARCHAR(200),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID)
);
```

#### One-to-Many Relationship

```sql
CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(50)
);

CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    EmployeeName VARCHAR(100),
    DepartmentID INT,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);
```

#### Many-to-Many Relationship

```sql
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    StudentName VARCHAR(100)
);

CREATE TABLE Courses (
    CourseID INT PRIMARY KEY,
    CourseName VARCHAR(100)
);

CREATE TABLE Enrollments (
    StudentID INT,
    CourseID INT,
    EnrollmentDate DATE,
    PRIMARY KEY (StudentID, CourseID),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);
```

## Data Integrity in SQL

### The Theory: Data Integrity

Data integrity ensures that data in a database remains:
- Accurate
- Consistent
- Valid
- Reliable

Types of integrity constraints:
1. **Entity Integrity**: Each row has a unique identifier (primary key)
2. **Referential Integrity**: Foreign key values must match existing primary key values
3. **Domain Integrity**: Values must conform to defined data types and constraints

### The Practice: SQL Constraints

```sql
CREATE TABLE Students (
    -- Entity Integrity: Primary Key constraint
    StudentID INT PRIMARY KEY,
    
    -- Domain Integrity: NOT NULL constraint
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    
    -- Domain Integrity: CHECK constraint
    Age INT CHECK (Age >= 14 AND Age <= 22),
    
    -- Domain Integrity: DEFAULT constraint
    EnrollmentDate DATE DEFAULT CURRENT_DATE,
    
    -- Domain Integrity: UNIQUE constraint
    Email VARCHAR(100) UNIQUE
);

CREATE TABLE Courses (
    CourseID INT PRIMARY KEY,
    CourseName VARCHAR(100) NOT NULL
);

CREATE TABLE Enrollments (
    EnrollmentID INT PRIMARY KEY,
    StudentID INT,
    CourseID INT,
    
    -- Referential Integrity: FOREIGN KEY constraints
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID)
        ON DELETE CASCADE, -- Automatically delete enrollment if student is deleted
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
        ON UPDATE CASCADE  -- Automatically update CourseID if it changes in Courses table
);
```

## Transactions in SQL

### The Theory: Transaction Processing

A transaction is a sequence of operations performed as a single logical unit of work. Transaction properties (ACID):
- **Atomicity**: All operations complete successfully or none of them do
- **Consistency**: Database remains in a consistent state before and after transaction
- **Isolation**: Transactions operate independently of each other
- **Durability**: Changes made by committed transactions are permanent

### The Practice: SQL Transaction Implementation

```sql
-- Begin a transaction
BEGIN TRANSACTION;

-- Attempt to withdraw money from one account
UPDATE Accounts 
SET Balance = Balance - 1000 
WHERE AccountID = 101;

-- Attempt to deposit into another account
UPDATE Accounts 
SET Balance = Balance + 1000 
WHERE AccountID = 202;

-- Check if both operations were successful
IF @@ERROR = 0
    -- If successful, commit the transaction
    COMMIT TRANSACTION;
ELSE
    -- If any errors occurred, roll back the transaction
    ROLLBACK TRANSACTION;
```

## Connecting Theory to Delphi Code

In Delphi applications, these database concepts are implemented using ADO components:

```pascal
procedure TForm1.EnsureReferentialIntegrity;
var
  Query: TADOQuery;
begin
  Query := TADOQuery.Create(nil);
  try
    Query.Connection := ADOConnection1;
    
    // Begin a transaction
    ADOConnection1.BeginTrans;
    try
      // Delete a department
      Query.SQL.Text := 'DELETE FROM Departments WHERE DepartmentID = :ID';
      Query.Parameters.ParamByName('ID').Value := 101;
      Query.ExecSQL;
      
      // Check if any employees still reference the department
      Query.SQL.Text := 'SELECT COUNT(*) FROM Employees WHERE DepartmentID = :ID';
      Query.Parameters.ParamByName('ID').Value := 101;
      Query.Open;
      
      if Query.Fields[0].AsInteger > 0 then
      begin
        // Referential integrity would be violated
        ADOConnection1.RollbackTrans;
        ShowMessage('Cannot delete department with assigned employees.');
      end
      else
      begin
        // Safe to commit
        ADOConnection1.CommitTrans;
        ShowMessage('Department deleted successfully.');
      end;
    except
      on E: Exception do
      begin
        ADOConnection1.RollbackTrans;
        ShowMessage('Error: ' + E.Message);
      end;
    end;
  finally
    Query.Free;
  end;
end;
```

## Paper 1 and Paper 2 Connections

### How This Appears in Paper 2 (Theory)

In Paper 2, you might be asked to:
- Identify normalization problems in a given database design
- Explain the benefits of using foreign keys
- Describe different relationship types
- Analyze the level of normalization in a database schema
- Explain how transactions ensure data integrity

### How This Appears in Paper 1 (Practical)

In Paper 1, you might need to:
- Create normalized tables using SQL
- Implement foreign key constraints
- Write queries that join tables based on their relationships
- Implement transaction handling in Delphi code
- Debug issues related to referential integrity

## Practice Questions

1. Given a table with the following structure:
   ```
   Orders(OrderID, CustomerName, CustomerEmail, ProductName, ProductPrice, Quantity, OrderDate)
   ```
   Normalize this table to 3NF and write the SQL CREATE TABLE statements.

2. Identify the relationship types (1:1, 1:M, M:N) that would be appropriate for the following scenarios and explain how you would implement them in SQL:
   - A student has one student ID card
   - A teacher can teach multiple classes
   - Students can enroll in multiple courses and courses can have multiple students

3. Write SQL code to create a table that enforces the following constraints:
   - Employee ID must be unique
   - Salary must be between R15,000 and R50,000
   - Department ID must exist in the Departments table
   - Email address must be unique
   - Start date cannot be in the future