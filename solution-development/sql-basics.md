---
layout: page
title: SQL Basics
parent: Solution Development
nav_order: 2
---

# SQL Basics

{: .note }
SQL (Structured Query Language) is covered in Grade 11 and 12, and appears prominently in Paper 1 practical exams.

## What is SQL?

SQL (pronounced "sequel" or "S-Q-L") is a standardized programming language used for managing relational databases. It allows you to:

- Create database structures
- Insert, update, and delete data
- Query data to retrieve specific information
- Define relationships between data elements

## Basic SQL Commands

SQL commands fall into several categories:

### Data Definition Language (DDL)

These commands create and modify database structures:

```sql
-- Create a new table
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Grade INT,
    DateOfBirth DATE
);

-- Modify an existing table
ALTER TABLE Students ADD Email VARCHAR(100);

-- Remove a table
DROP TABLE Students;
```

### Data Manipulation Language (DML)

These commands work with the data within tables:

```sql
-- Insert a new record
INSERT INTO Students (StudentID, FirstName, LastName, Grade, DateOfBirth)
VALUES (1, 'John', 'Smith', 11, '2006-05-15');

-- Update existing records
UPDATE Students
SET Grade = 12
WHERE StudentID = 1;

-- Delete records
DELETE FROM Students
WHERE StudentID = 1;
```

### Data Query Language (DQL)

These commands retrieve data from the database:

```sql
-- Basic SELECT statement
SELECT * FROM Students;

-- Select specific columns
SELECT FirstName, LastName FROM Students;

-- Filter with WHERE clause
SELECT * FROM Students WHERE Grade = 12;

-- Sort results
SELECT * FROM Students ORDER BY LastName ASC;

-- Group results
SELECT Grade, COUNT(*) AS NumberOfStudents
FROM Students
GROUP BY Grade;
```

## SQL in Delphi

When working with databases in Delphi, you'll use SQL through components like:
- `ADOQuery`
- `ADOTable`
- `ADOConnection`

Example of SQL in Delphi code:

```pascal
procedure TForm1.ButtonSearchClick(Sender: TObject);
begin
  // Clear previous results
  ADOQuery1.Close;
  
  // Set up the SQL query
  ADOQuery1.SQL.Clear;
  ADOQuery1.SQL.Add('SELECT * FROM Students');
  ADOQuery1.SQL.Add('WHERE LastName = :LastName');
  
  // Set parameter value
  ADOQuery1.Parameters.ParamByName('LastName').Value := EditLastName.Text;
  
  // Execute the query
  ADOQuery1.Open;
  
  // Display results count
  LabelResults.Caption := 'Results found: ' + IntToStr(ADOQuery1.RecordCount);
end;
```

## Formatting SQL Statements

Good formatting makes SQL more readable:

1. Capitalize SQL keywords (SELECT, FROM, WHERE, etc.)
2. Place each clause on a new line
3. Indent subqueries and conditions
4. Use meaningful table and field names
5. Add comments to explain complex queries

## Common SQL Errors

| Error | Description | Solution |
|-------|-------------|----------|
| Syntax Error | Incorrect SQL command structure | Check spelling of keywords, verify parentheses are balanced |
| Column not found | Referenced column doesn't exist | Check column name spelling, ensure table contains the column |
| Table not found | Referenced table doesn't exist | Check table name spelling, verify the table exists |
| Data type mismatch | Trying to compare incompatible data types | Cast values to appropriate types, check data types |
| Ambiguous column name | Column name exists in multiple tables | Use table name qualifier (e.g., Students.Grade) |

## Practice Questions

1. Write an SQL statement to create a table named "Teachers" with columns for ID (integer), Name (text), Subject (text), and YearsOfExperience (integer).

2. Write a query to select all students in Grade 11 whose last name begins with 'S'.

3. How would you update the Grade value to 12 for all students currently in Grade 11?

4. Write a query to find the average grade for each subject, sorted from highest to lowest average.

## Paper 1 Connection

In Paper 1 exams, you'll typically need to:
- Write SQL queries to retrieve specific information
- Create SQL statements to modify database data
- Debug and fix errors in existing SQL code
- Implement database operations within Delphi code

{: .warning }
In the exam, pay careful attention to the exact requirements for each query. Using the wrong SQL statement type or omitting filtering conditions can cost you significant marks.
