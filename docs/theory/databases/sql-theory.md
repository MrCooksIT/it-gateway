# SQL Theory

SQL (Structured Query Language) is the language you use to communicate with a relational database. Paper 2 tests whether you understand what SQL does and why — Paper 1 tests whether you can write it. This page focuses on the theory: concepts, syntax rules, and what each clause does.

> [!NOTE] Grade 11–12
> SQL SELECT and WHERE are Grade 11. JOINs, GROUP BY, aggregate functions, and INSERT/UPDATE/DELETE are Grade 12.

---

## What is SQL?

**SQL** (Structured Query Language) is the standard language for managing and querying relational databases.

- Originally developed at IBM in the 1970s
- Standardised by ANSI and ISO
- Used by virtually all relational database systems (MySQL, Microsoft Access, SQL Server, PostgreSQL, Oracle)
- **Not case-sensitive** — `SELECT` = `select`

**Four categories of SQL:**

| Category | Purpose | Commands |
|---|---|---|
| **DQL** | Data Query Language | `SELECT` |
| **DML** | Data Manipulation Language | `INSERT`, `UPDATE`, `DELETE` |
| **DDL** | Data Definition Language | `CREATE`, `ALTER`, `DROP` |
| **DCL** | Data Control Language | `GRANT`, `REVOKE` |

---

## How SQL Fits Into a Database System

```
Application (Delphi, website, report tool)
    ↓ SQL query
DBMS (MySQL, MS Access, PostgreSQL)
    ↓ processes query against
Database (tables, indexes, stored data)
    ↓ returns
Result set (table of matching rows)
    ↓ displayed in
Application (TDBGrid, web page, report)
```

---

## SELECT — The Query Command

**SELECT** retrieves data from one or more tables.

### Basic structure:
```sql
SELECT column1, column2
FROM TableName
WHERE condition
ORDER BY column1 ASC;
```

### SELECT all columns:
```sql
SELECT * FROM Students;
```

### SELECT specific columns:
```sql
SELECT Surname, FirstName, Grade
FROM Students;
```

### Eliminating duplicates:
```sql
SELECT DISTINCT Grade FROM Students;
```

### Column aliases:
```sql
SELECT FirstName AS 'First Name', Mark * 1.1 AS 'Adjusted Mark'
FROM Students;
```

---

## WHERE — Filtering Rows

**WHERE** filters which rows are returned.

### Comparison operators:

| Operator | Meaning | Example |
|---|---|---|
| `=` | Equal to | `WHERE Grade = 11` |
| `<>` or `!=` | Not equal | `WHERE Grade <> 10` |
| `>` | Greater than | `WHERE Mark > 60` |
| `<` | Less than | `WHERE Mark < 50` |
| `>=` | Greater or equal | `WHERE Mark >= 50` |
| `<=` | Less or equal | `WHERE Age <= 18` |

### Logical operators:
```sql
WHERE Grade = 11 AND Mark >= 50
WHERE Grade = 10 OR Grade = 11
WHERE NOT Province = 'Gauteng'
```

### BETWEEN (inclusive range):
```sql
WHERE Mark BETWEEN 60 AND 79
-- equivalent to: WHERE Mark >= 60 AND Mark <= 79
```

### IN (list of values):
```sql
WHERE Province IN ('Gauteng', 'Western Cape', 'KwaZulu-Natal')
```

### LIKE (pattern matching):
```sql
WHERE Surname LIKE 'C%'      -- starts with C
WHERE Surname LIKE '%son'    -- ends with son
WHERE Email LIKE '%@gmail%'  -- contains @gmail
WHERE Phone LIKE '012%'      -- starts with 012
```

**Wildcards:**
- `%` — any number of characters (including zero)
- `_` — exactly one character

### NULL values:
```sql
WHERE Email IS NULL          -- field is empty
WHERE Email IS NOT NULL      -- field has a value
```

---

## ORDER BY — Sorting Results

```sql
SELECT Surname, Mark
FROM Students
ORDER BY Mark DESC;          -- highest mark first

ORDER BY Surname ASC;        -- A to Z (default)
ORDER BY Grade DESC, Mark DESC;  -- sort by grade, then mark within grade
```

- `ASC` = ascending (smallest to largest, A to Z) — **default**
- `DESC` = descending (largest to smallest, Z to A)

---

## Aggregate Functions

Aggregate functions perform calculations on groups of rows.

| Function | Purpose | Example |
|---|---|---|
| `COUNT(*)` | Count all rows | `SELECT COUNT(*) FROM Students` |
| `COUNT(field)` | Count non-NULL values | `SELECT COUNT(Email) FROM Students` |
| `SUM(field)` | Total of a numeric field | `SELECT SUM(Mark) FROM Marks` |
| `AVG(field)` | Average of a numeric field | `SELECT AVG(Mark) FROM Marks` |
| `MAX(field)` | Largest value | `SELECT MAX(Mark) FROM Marks` |
| `MIN(field)` | Smallest value | `SELECT MIN(Mark) FROM Marks` |

```sql
SELECT COUNT(*) AS TotalStudents, AVG(Mark) AS ClassAverage, MAX(Mark) AS TopMark
FROM Marks
WHERE Grade = 11;
```

---

## GROUP BY — Grouping Rows

**GROUP BY** groups rows that have the same value in specified columns, allowing aggregate functions per group.

```sql
SELECT Grade, COUNT(*) AS NumberOfStudents, AVG(Mark) AS Average
FROM Students
GROUP BY Grade;
```

**Result:**
| Grade | NumberOfStudents | Average |
|---|---|---|
| 10 | 120 | 68.4 |
| 11 | 115 | 71.2 |
| 12 | 98 | 73.8 |

---

## HAVING — Filtering Groups

**HAVING** filters groups (like WHERE filters rows, but after GROUP BY).

```sql
SELECT Grade, AVG(Mark) AS Average
FROM Students
GROUP BY Grade
HAVING AVG(Mark) > 70;
```

**WHERE vs HAVING:**
| | WHERE | HAVING |
|---|---|---|
| Filters | Individual rows | Groups |
| Used with | Any query | GROUP BY only |
| Aggregate functions | Cannot use | Can use |
| Applied | Before grouping | After grouping |

---

## Multi-Table Queries — Combining Tables

A multi-table query retrieves data from two tables at once by linking them on a common field (primary key / foreign key pair).

> [!IMPORTANT] Access / Delphi Syntax
> In Microsoft Access accessed through Delphi ADO, list both tables in `FROM` separated by a comma and define the link in `WHERE`. Do **not** use `INNER JOIN` or `LEFT JOIN` syntax in Paper 1.

```sql
SELECT tblStudents.Surname, tblMarks.Subject, tblMarks.Mark
FROM tblStudents, tblMarks
WHERE tblStudents.StudentID = tblMarks.StudentID
AND tblMarks.Mark >= 50
ORDER BY tblStudents.Surname;
```

> [!NOTE] Standard SQL vs Access/Delphi
> Standard SQL (MySQL, SQL Server, PostgreSQL) uses `INNER JOIN … ON` and `LEFT JOIN … ON` syntax. These are equivalent in logic to the WHERE-based method above, but are not used in the CAPS Paper 1 exam environment. `INNER JOIN` returns only matching rows from both tables; `LEFT JOIN` returns all rows from the left table plus matched rows from the right (unmatched = NULL).

---

## DML — Modifying Data

### INSERT — Add new rows:
```sql
INSERT INTO Students (FirstName, Surname, Grade)
VALUES ('Thabo', 'Nkosi', 12);
```

### UPDATE — Modify existing rows:
```sql
UPDATE Students
SET Grade = 12
WHERE StudentID = 1001;

-- Update multiple fields:
UPDATE Students
SET Grade = 12, Active = TRUE
WHERE Surname = 'Nkosi';
```

### DELETE — Remove rows:
```sql
DELETE FROM Students
WHERE StudentID = 1001;

-- Delete all rows where condition is true:
DELETE FROM Marks
WHERE Mark IS NULL;
```

> [!WARNING] Always use WHERE with UPDATE and DELETE
> `UPDATE Students SET Grade = 12` — changes ALL students to Grade 12!  
> `DELETE FROM Students` — deletes ALL students!

---

## Correct SQL Clause Order

Clauses must appear in this exact order:

```sql
SELECT     -- what to retrieve
FROM       -- which table(s)
WHERE      -- filter rows (also defines table links for multi-table queries)
GROUP BY   -- group rows
HAVING     -- filter groups
ORDER BY   -- sort results
```

---

## Key Terms

| Term | Definition |
|---|---|
| **SQL** | Structured Query Language — language for relational databases |
| **SELECT** | Command to retrieve data |
| **WHERE** | Clause filtering which rows are returned |
| **ORDER BY** | Clause sorting results |
| **GROUP BY** | Clause grouping rows for aggregate calculations |
| **HAVING** | Clause filtering groups (after GROUP BY) |
| **Multi-table query** | A query that retrieves data from two tables linked by a primary/foreign key relationship |
| **Aggregate function** | Calculates a single value from multiple rows (COUNT, SUM, AVG) |
| **INSERT** | Adds new rows to a table |
| **UPDATE** | Modifies existing rows |
| **DELETE** | Removes rows from a table |

---

## Exam Focus

> [!IMPORTANT] High-Frequency Questions
>
> 1. **"What is the difference between WHERE and HAVING?"** — WHERE filters individual rows before grouping; HAVING filters groups after GROUP BY; HAVING can use aggregate functions, WHERE cannot
>
> 2. **"What is the purpose of GROUP BY?"** — Groups rows with the same value in specified columns, allowing aggregate functions (COUNT, AVG, SUM) to be applied per group
>
> 3. **"How do you query data from two tables in Microsoft Access via Delphi?"** — List both tables in the FROM clause separated by a comma, then define the link between them in the WHERE clause using `table1.PrimaryKey = table2.ForeignKey`; add extra conditions with AND
>
> 4. **"Write the correct order of SQL clauses"** — SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY
>
> 5. **"What is the LIKE operator used for?"** — Pattern matching in WHERE clause; % matches any number of characters; _ matches exactly one character
