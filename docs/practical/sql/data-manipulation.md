# Data Manipulation — INSERT, UPDATE, DELETE

SELECT retrieves data. But databases also need to receive new data, update existing records, and remove records that are no longer needed. These three operations — INSERT, UPDATE, DELETE — are called Data Manipulation Language (DML).

---

## The Three DML Commands

| Command | Purpose |
|---|---|
| `INSERT` | Add new rows to a table |
| `UPDATE` | Modify existing rows |
| `DELETE` | Remove rows from a table |

---

## INSERT — Adding New Rows

### Syntax

```sql
INSERT INTO TableName (col1, col2, col3, ...)
VALUES (val1, val2, val3, ...);
```

The columns and values must match — same number, same order.

### Examples

```sql
-- Add a new student
INSERT INTO Students (StudentID, FirstName, Surname, Grade, Email)
VALUES (1010, 'Ayden', 'Coetzee', 12, 'ayden@school.co.za');

-- Columns can be omitted if providing values for ALL columns in table order
INSERT INTO Students
VALUES (1011, 'Luca', 'Petersen', 11, 'luca@school.co.za');

-- Omit optional fields (they must accept NULL or have a default)
INSERT INTO Students (FirstName, Surname, Grade)
VALUES ('Marco', 'Ferreira', 10);
```

### Inserting multiple rows (MySQL / SQL Server)

```sql
INSERT INTO Students (FirstName, Surname, Grade)
VALUES ('Ayden', 'Coetzee', 12),
       ('Luca', 'Petersen', 11),
       ('Marco', 'Ferreira', 10);
```

### String values vs numeric values

```sql
-- Strings in single quotes
INSERT INTO Students (FirstName, Surname, Grade, Active)
VALUES ('Ayden', 'Coetzee', 12, TRUE);
--      ^^^^^^   ^^^^^^^^  ^^  ^^^^
--      string   string    num boolean
```

> [!WARNING] Text needs quotes, numbers don't
> `VALUES ('Ayden', 12)` ✓ — string in quotes, number without  
> `VALUES (Ayden, '12')` ✗ — both wrong

---

## UPDATE — Modifying Existing Rows

### Syntax

```sql
UPDATE TableName
SET col1 = val1, col2 = val2
WHERE condition;
```

> [!WARNING] ALWAYS include WHERE with UPDATE
> `UPDATE Students SET Grade = 12` — changes ALL students' grade to 12!  
> Always specify which rows to update.

### Examples

```sql
-- Update one student's email
UPDATE Students
SET Email = 'new.email@school.co.za'
WHERE StudentID = 1010;

-- Update multiple fields at once
UPDATE Students
SET Grade = 12, Email = 'ayden.gr12@school.co.za'
WHERE StudentID = 1010;

-- Increase all marks by 5
UPDATE Marks
SET Mark = Mark + 5
WHERE SubjectCode = 'IT';

-- Update all Grade 11 students to Grade 12 (end of year promotion)
UPDATE Students
SET Grade = 12
WHERE Grade = 11;

-- Set email to NULL where not provided
UPDATE Students
SET Email = NULL
WHERE Email = '';
```

---

## DELETE — Removing Rows

### Syntax

```sql
DELETE FROM TableName
WHERE condition;
```

> [!WARNING] ALWAYS include WHERE with DELETE
> `DELETE FROM Students` — deletes EVERY student in the table!  
> This cannot be undone (unless in a transaction). Always double-check.

### Examples

```sql
-- Delete one student
DELETE FROM Students
WHERE StudentID = 1010;

-- Delete all students who have no marks
DELETE FROM Students
WHERE StudentID NOT IN (SELECT StudentID FROM Marks);

-- Delete all marks below 0 (invalid data cleanup)
DELETE FROM Marks
WHERE Mark < 0;

-- Delete all records for a specific subject
DELETE FROM Marks
WHERE SubjectCode = 'OLD_SUBJ';
```

---

## Referential Integrity and DML

Foreign key constraints affect what you can INSERT, UPDATE, and DELETE.

### Cannot INSERT a FK value that doesn't exist as a PK:
```sql
-- Fails if StudentID 9999 doesn't exist in Students table
INSERT INTO Marks (StudentID, Mark)
VALUES (9999, 85);    -- ERROR: referential integrity violation
```

### Cannot DELETE a parent if children exist:
```sql
-- Fails if student 1010 has marks in the Marks table
DELETE FROM Students WHERE StudentID = 1010;    -- ERROR (if RESTRICT)
```

**Solutions:**
- Delete child records first, then parent
- Use CASCADE DELETE (configured in table definition)

---

## Transactions (conceptual)

A **transaction** groups multiple SQL statements into an atomic unit:

```sql
BEGIN TRANSACTION;

UPDATE Accounts SET Balance = Balance - 500 WHERE AccountID = 101;
UPDATE Accounts SET Balance = Balance + 500 WHERE AccountID = 202;

COMMIT;    -- Save both changes
-- or ROLLBACK;  -- Undo both if something went wrong
```

**ACID properties:**
| Property | Meaning |
|---|---|
| **Atomicity** | All statements succeed or all are rolled back |
| **Consistency** | Database remains in valid state |
| **Isolation** | Concurrent transactions don't interfere |
| **Durability** | Committed changes are permanent |

---

## Practice Exercises

### Exercise 1 — Add new records

Given this Students table:

| StudentID | FirstName | Surname | Grade |
|---|---|---|---|
| 1001 | Ayden | Coetzee | 12 |
| 1002 | Luca | Petersen | 11 |

Write SQL to:
a) Add a new student: Marco Ferreira, Grade 10, StudentID 1003  
b) Add another student without specifying StudentID (it's an auto-number)

<details>
<summary>Solution</summary>

```sql
-- a) Specify all fields
INSERT INTO Students (StudentID, FirstName, Surname, Grade)
VALUES (1003, 'Marco', 'Ferreira', 10);

-- b) Let auto-number generate StudentID
INSERT INTO Students (FirstName, Surname, Grade)
VALUES ('Priya', 'Naidoo', 11);
```
</details>

---

### Exercise 2 — Update records

```sql
-- Write SQL to:
-- a) Change Luca Petersen's grade to 12
-- b) Add 10 marks to all students in Grade 12 in the Marks table
-- c) Set all blank email fields to 'noemail@school.co.za'
```

<details>
<summary>Solution</summary>

```sql
-- a)
UPDATE Students
SET Grade = 12
WHERE FirstName = 'Luca' AND Surname = 'Petersen';

-- b)
UPDATE Marks
SET Mark = Mark + 10
WHERE StudentID IN (SELECT StudentID FROM Students WHERE Grade = 12);

-- c)
UPDATE Students
SET Email = 'noemail@school.co.za'
WHERE Email IS NULL OR Email = '';
```
</details>

---

### Exercise 3 — Delete records

```sql
-- Write SQL to:
-- a) Delete the student with StudentID = 1003
-- b) Delete all marks where the mark is NULL
-- c) Delete all students in Grade 10 who have no marks
```

<details>
<summary>Solution</summary>

```sql
-- a)
DELETE FROM Students
WHERE StudentID = 1003;

-- b)
DELETE FROM Marks
WHERE Mark IS NULL;

-- c)
DELETE FROM Students
WHERE Grade = 10
  AND StudentID NOT IN (SELECT StudentID FROM Marks);
```
</details>

---

## Common Mistakes

| Mistake | Consequence | Fix |
|---|---|---|
| UPDATE without WHERE | Updates every row in the table | Always specify WHERE |
| DELETE without WHERE | Deletes every row | Always specify WHERE |
| Wrong quotes on strings | Syntax error | Text → 'quotes', numbers → no quotes |
| Inserting invalid FK | Referential integrity error | Insert parent first |
| Deleting parent with children | Error (if RESTRICT) | Delete children first |
| Column count mismatch | Syntax error | Count columns = count values |
