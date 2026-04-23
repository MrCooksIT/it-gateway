# DDL — Creating and Defining Tables

> [!WARNING] Not Assessed in CAPS Grade 12 IT Paper 1
> DDL commands (CREATE TABLE, ALTER TABLE, DROP TABLE, CREATE INDEX, CREATE VIEW) are **not** part of the CAPS Grade 10–12 IT Paper 1 practical examination. This page is provided for general reference only. Focus your exam preparation on SELECT, DML (INSERT/UPDATE/DELETE), and multi-table queries instead.

Before you can store any data, you need to define the structure. Data Definition Language (DDL) is the set of SQL commands that create, modify, and delete database objects — tables, indexes, and constraints.

---

## DDL vs DML

| Category | Commands | Purpose |
|---|---|---|
| **DDL** | CREATE, ALTER, DROP | Define database structure |
| **DML** | SELECT, INSERT, UPDATE, DELETE | Manipulate data |

---

## CREATE TABLE

### Syntax

```sql
CREATE TABLE TableName (
  ColumnName  DataType  [Constraints],
  ColumnName  DataType  [Constraints],
  ...
  [table-level constraints]
);
```

### Data Types

| Data Type | Used for | Examples |
|---|---|---|
| `INTEGER` / `INT` | Whole numbers | Age, quantity, grade |
| `REAL` / `FLOAT` | Decimal numbers | Price, average, mark as decimal |
| `VARCHAR(n)` | Variable-length text up to n chars | Name, email |
| `CHAR(n)` | Fixed-length text, exactly n chars | Province code, gender |
| `TEXT` | Long text, unlimited | Notes, descriptions |
| `DATE` | Calendar date | DateOfBirth, EnrolmentDate |
| `DATETIME` | Date and time | TransactionTime |
| `BOOLEAN` / `BIT` | True/False | Active, Paid |
| `DECIMAL(p,s)` | Exact decimal (p digits, s after decimal) | Price: DECIMAL(10,2) |
| `AUTOINCREMENT` / `IDENTITY` | Automatically incrementing integer | Primary key |

---

## Constraints

**Constraints** enforce rules on what values can be stored.

| Constraint | Effect |
|---|---|
| `PRIMARY KEY` | Unique + not null; identifies each row |
| `NOT NULL` | Field cannot be empty |
| `UNIQUE` | All values must be different |
| `DEFAULT value` | Uses default if not specified |
| `CHECK (condition)` | Value must satisfy condition |
| `FOREIGN KEY` | References primary key of another table |

---

## Worked Examples

### Simple table — Students

```sql
CREATE TABLE Students (
  StudentID   INTEGER       PRIMARY KEY,
  FirstName   VARCHAR(50)   NOT NULL,
  Surname     VARCHAR(50)   NOT NULL,
  Grade       INTEGER       NOT NULL,
  Email       VARCHAR(100),
  DateOfBirth DATE,
  Active      BOOLEAN       DEFAULT TRUE
);
```

### Table with CHECK constraint

```sql
CREATE TABLE Marks (
  MarkID      INTEGER       PRIMARY KEY,
  Mark        INTEGER       NOT NULL CHECK (Mark >= 0 AND Mark <= 100),
  DateWritten DATE          NOT NULL,
  StudentID   INTEGER       NOT NULL,
  SubjectCode VARCHAR(10)   NOT NULL
);
```

### Table with FOREIGN KEY

```sql
CREATE TABLE Marks (
  MarkID      INTEGER     PRIMARY KEY,
  Mark        INTEGER     NOT NULL CHECK (Mark BETWEEN 0 AND 100),
  DateWritten DATE        NOT NULL,
  StudentID   INTEGER     NOT NULL,
  SubjectCode VARCHAR(10) NOT NULL,
  
  FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
  FOREIGN KEY (SubjectCode) REFERENCES Subjects(SubjectCode)
);
```

### Auto-increment primary key

**MySQL:**
```sql
CREATE TABLE Students (
  StudentID   INT           AUTO_INCREMENT PRIMARY KEY,
  FirstName   VARCHAR(50)   NOT NULL,
  Surname     VARCHAR(50)   NOT NULL
);
```

**SQLite:**
```sql
CREATE TABLE Students (
  StudentID   INTEGER       PRIMARY KEY AUTOINCREMENT,
  FirstName   TEXT          NOT NULL,
  Surname     TEXT          NOT NULL
);
```

**MS Access:** Use `AUTOINCREMENT` data type (or set field type to AutoNumber in the GUI).

---

## Full School Database Example

```sql
-- Create Teachers table first (no FKs)
CREATE TABLE Teachers (
  TeacherID   INTEGER       PRIMARY KEY,
  FirstName   VARCHAR(50)   NOT NULL,
  Surname     VARCHAR(50)   NOT NULL,
  Email       VARCHAR(100)  UNIQUE
);

-- Subjects reference Teachers
CREATE TABLE Subjects (
  SubjectCode  VARCHAR(10)   PRIMARY KEY,
  SubjectName  VARCHAR(100)  NOT NULL,
  TeacherID    INTEGER,
  FOREIGN KEY (TeacherID) REFERENCES Teachers(TeacherID)
);

-- Students stand alone
CREATE TABLE Students (
  StudentID    INTEGER       PRIMARY KEY,
  FirstName    VARCHAR(50)   NOT NULL,
  Surname      VARCHAR(50)   NOT NULL,
  Grade        INTEGER       NOT NULL CHECK (Grade BETWEEN 10 AND 12),
  Email        VARCHAR(100)
);

-- Enrolment is the junction table (many-to-many: Students ↔ Subjects)
CREATE TABLE Enrolment (
  StudentID    INTEGER     NOT NULL,
  SubjectCode  VARCHAR(10) NOT NULL,
  EnrolDate    DATE        NOT NULL,
  PRIMARY KEY (StudentID, SubjectCode),
  FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
  FOREIGN KEY (SubjectCode) REFERENCES Subjects(SubjectCode)
);

-- Marks reference both Students and Subjects
CREATE TABLE Marks (
  MarkID       INTEGER     PRIMARY KEY,
  Mark         INTEGER     NOT NULL CHECK (Mark BETWEEN 0 AND 100),
  DateWritten  DATE        NOT NULL,
  StudentID    INTEGER     NOT NULL,
  SubjectCode  VARCHAR(10) NOT NULL,
  FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
  FOREIGN KEY (SubjectCode) REFERENCES Subjects(SubjectCode)
);
```

> [!TIP] Table creation order matters
> Create tables that are **referenced by** foreign keys **first**.  
> Teachers → Subjects → Students → Enrolment, Marks

---

## ALTER TABLE — Modifying Structure

### Add a column

```sql
ALTER TABLE Students
ADD COLUMN PhoneNumber VARCHAR(15);
```

### Drop a column

```sql
ALTER TABLE Students
DROP COLUMN PhoneNumber;
```

### Modify a column's data type or size

```sql
-- MySQL
ALTER TABLE Students
MODIFY COLUMN Email VARCHAR(200);

-- SQL Server
ALTER TABLE Students
ALTER COLUMN Email VARCHAR(200);
```

### Add a constraint

```sql
ALTER TABLE Marks
ADD CONSTRAINT chk_mark CHECK (Mark BETWEEN 0 AND 100);
```

### Add a foreign key

```sql
ALTER TABLE Marks
ADD CONSTRAINT fk_student
FOREIGN KEY (StudentID) REFERENCES Students(StudentID);
```

---

## DROP TABLE — Deleting Tables

```sql
DROP TABLE Marks;        -- Delete the table and all its data
```

> [!WARNING] DROP TABLE is irreversible
> This deletes the table structure AND all data permanently. You cannot undo this without a backup.

```sql
-- Safer — only drops if table exists
DROP TABLE IF EXISTS Marks;
```

You cannot drop a table if other tables have foreign keys referencing it.  
Drop child tables first.

---

## CREATE INDEX

An index speeds up queries on specific columns.

```sql
-- Create an index on Surname (speeds up: WHERE Surname LIKE 'C%')
CREATE INDEX idx_surname ON Students(Surname);

-- Unique index (enforces uniqueness AND speeds up lookups)
CREATE UNIQUE INDEX idx_email ON Students(Email);
```

**When to index:**
- Columns frequently used in WHERE clauses
- Columns used in JOIN conditions
- Columns used in ORDER BY

**Trade-off:** Indexes speed up reads but slow down INSERT/UPDATE/DELETE (index must be updated).

---

## CREATE VIEW

A **view** is a saved SELECT query that acts like a virtual table.

```sql
CREATE VIEW vwStudentMarks AS
SELECT s.Surname, s.FirstName, s.Grade, sub.SubjectName, m.Mark
FROM Students AS s
INNER JOIN Marks AS m ON s.StudentID = m.StudentID
INNER JOIN Subjects AS sub ON m.SubjectCode = sub.SubjectCode;

-- Query the view like a table
SELECT * FROM vwStudentMarks WHERE Grade = 12 ORDER BY Mark DESC;
```

**Benefits of views:**
- Simplify complex joins — users query the view, not the raw tables
- Security — expose only specific columns/rows
- Reusable — write the join once, use it many times

---

## Practice Exercises

### Exercise 1 — Design a library database
Create tables for a library: Books, Members, and Loans.

<details>
<summary>Solution</summary>

```sql
CREATE TABLE Books (
  BookID      INTEGER       PRIMARY KEY,
  Title       VARCHAR(200)  NOT NULL,
  Author      VARCHAR(100)  NOT NULL,
  ISBN        VARCHAR(20)   UNIQUE,
  Available   BOOLEAN       DEFAULT TRUE
);

CREATE TABLE Members (
  MemberID    INTEGER       PRIMARY KEY,
  FirstName   VARCHAR(50)   NOT NULL,
  Surname     VARCHAR(50)   NOT NULL,
  Email       VARCHAR(100),
  JoinDate    DATE          NOT NULL
);

CREATE TABLE Loans (
  LoanID      INTEGER       PRIMARY KEY,
  BookID      INTEGER       NOT NULL,
  MemberID    INTEGER       NOT NULL,
  LoanDate    DATE          NOT NULL,
  ReturnDate  DATE,
  FOREIGN KEY (BookID) REFERENCES Books(BookID),
  FOREIGN KEY (MemberID) REFERENCES Members(MemberID)
);
```
</details>

---

### Exercise 2 — Add constraints to existing table
Given:
```sql
CREATE TABLE Products (
  ProductID   INTEGER,
  ProductName VARCHAR(100),
  Price       REAL,
  Stock       INTEGER
);
```

Rewrite this with appropriate constraints (PK, NOT NULL, CHECK for Price > 0 and Stock >= 0).

<details>
<summary>Solution</summary>

```sql
CREATE TABLE Products (
  ProductID   INTEGER       PRIMARY KEY,
  ProductName VARCHAR(100)  NOT NULL,
  Price       REAL          NOT NULL CHECK (Price > 0),
  Stock       INTEGER       NOT NULL DEFAULT 0 CHECK (Stock >= 0)
);
```
</details>
