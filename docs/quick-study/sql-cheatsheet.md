# SQL — Quick Reference

All SQL syntax you need for Paper 1. Clause order is mandatory: SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY.

---

## SELECT Structure

```sql
SELECT column1, column2         -- * for all columns
FROM TableName
WHERE condition                 -- optional filter
ORDER BY column ASC|DESC;      -- optional sort
```

---

## SELECT Variations

```sql
SELECT *                        -- all columns
SELECT DISTINCT column          -- unique values only
SELECT column AS 'Alias'        -- rename output column
SELECT COUNT(*) AS Total        -- count all rows
SELECT SUM(Mark) AS TotalMark
SELECT AVG(Mark) AS AverageMark
SELECT MAX(Mark) AS Highest
SELECT MIN(Mark) AS Lowest
```

---

## WHERE Operators

| Operator | Meaning | Example |
|---|---|---|
| `=` | Equal | `WHERE Grade = 11` |
| `<>` | Not equal | `WHERE Status <> 'Inactive'` |
| `<`, `>`, `<=`, `>=` | Comparison | `WHERE Mark >= 50` |
| `AND` | Both true | `WHERE Grade = 11 AND Mark > 60` |
| `OR` | Either true | `WHERE Grade = 10 OR Grade = 12` |
| `NOT` | Reverse | `WHERE NOT Grade = 10` |
| `LIKE 'C%'` | Starts with C | `WHERE Surname LIKE 'C%'` |
| `LIKE '%ee'` | Ends with ee | `WHERE Surname LIKE '%ee'` |
| `LIKE '%son%'` | Contains son | `WHERE Surname LIKE '%son%'` |
| `BETWEEN a AND b` | Inclusive range | `WHERE Mark BETWEEN 60 AND 79` |
| `IN (a, b, c)` | Matches any | `WHERE Grade IN (10, 11, 12)` |
| `IS NULL` | No value | `WHERE Email IS NULL` |
| `IS NOT NULL` | Has value | `WHERE Email IS NOT NULL` |

---

## ORDER BY

```sql
ORDER BY Mark              -- ascending (default)
ORDER BY Mark ASC          -- ascending (low → high)
ORDER BY Mark DESC         -- descending (high → low)
ORDER BY Surname, Mark DESC  -- multiple columns
```

---

## Aggregate Functions (GROUP BY)

```sql
SELECT Grade, COUNT(*) AS NumStudents, AVG(Mark) AS AvgMark
FROM Learners
GROUP BY Grade
HAVING AVG(Mark) > 60        -- filter on GROUP result (not individual rows)
ORDER BY Grade;
```

| Function | Returns |
|---|---|
| `COUNT(*)` | Number of rows |
| `COUNT(column)` | Rows where column is not NULL |
| `SUM(column)` | Total of all values |
| `AVG(column)` | Average of all values |
| `MAX(column)` | Largest value |
| `MIN(column)` | Smallest value |

> **WHERE** filters individual rows (before grouping).  
> **HAVING** filters group results (after grouping).

---

## Multi-Table Query (Two Tables)

In Microsoft Access via Delphi, list both tables in FROM and define the link in WHERE:

```sql
SELECT tblStudents.Surname, tblMarks.Subject, tblMarks.Mark
FROM tblStudents, tblMarks
WHERE tblStudents.StudentID = tblMarks.StudentID
AND tblMarks.Mark >= 50
ORDER BY tblStudents.Surname;
```

- Always prefix field names with the table name when the same field exists in both tables.
- The relationship condition (`tblStudents.StudentID = tblMarks.StudentID`) must come first in WHERE; add extra filters with AND.

---

## INSERT

```sql
INSERT INTO TableName (column1, column2, column3)
VALUES ('Smith', 11, 75);

-- Insert without listing columns (must match table order exactly):
INSERT INTO Learners VALUES (NULL, 'Smith', 'John', 11, 75);
```

---

## UPDATE

```sql
UPDATE TableName
SET column1 = value1, column2 = value2
WHERE condition;

-- Example: give all Grade 11 students a 5-mark bonus
UPDATE Learners
SET Mark = Mark + 5
WHERE Grade = 11;
```

> [!WARNING] Always Use WHERE with UPDATE/DELETE
> Without a WHERE clause, **every row** in the table is updated or deleted. This is almost never what you want.

---

## DELETE

```sql
DELETE FROM TableName
WHERE condition;

-- Example: remove all learners who never submitted work
DELETE FROM Learners
WHERE Mark IS NULL;
```

---

## CREATE TABLE

```sql
CREATE TABLE Learners (
  LearnerID   INTEGER       PRIMARY KEY,
  Surname     VARCHAR(50)   NOT NULL,
  FirstName   VARCHAR(50),
  Grade       INTEGER,
  Mark        INTEGER,
  Email       VARCHAR(100)  UNIQUE
);
```

**Common data types:**

| Type | Use for |
|---|---|
| `INTEGER` / `INT` | Whole numbers |
| `REAL` / `FLOAT` | Decimal numbers |
| `VARCHAR(n)` | Variable-length text (max n chars) |
| `TEXT` | Long text (no length limit) |
| `DATE` | Date values |
| `BOOLEAN` | True/False |

**Common constraints:**

| Constraint | Meaning |
|---|---|
| `PRIMARY KEY` | Unique identifier, not null |
| `NOT NULL` | Field cannot be empty |
| `UNIQUE` | All values must be different |
| `FOREIGN KEY` | Links to primary key in another table |
| `DEFAULT value` | Used if no value provided |

---

## Common Query Templates

**Top N records:**
```sql
-- Microsoft Access (used in CAPS exam):
SELECT TOP 5 Surname, Mark FROM Learners ORDER BY Mark DESC;
-- MySQL/SQLite use LIMIT instead of TOP:
SELECT Surname, Mark FROM Learners ORDER BY Mark DESC LIMIT 5;
```

**Percentage calculation:**
```sql
SELECT Surname, Mark, (Mark * 100.0 / 300) AS Percentage
FROM Learners;
```

**Find duplicates:**
```sql
SELECT Surname, COUNT(*) AS Occurrences
FROM Learners
GROUP BY Surname
HAVING COUNT(*) > 1;
```

---

## Keyword Order (Mandatory)

```
SELECT
FROM
WHERE
GROUP BY
HAVING
ORDER BY
```

Putting them in any other order is a syntax error.

---

## String Values vs Numbers

```sql
WHERE Name = 'Smith'      -- string: single quotes ✓
WHERE Grade = 11          -- number: no quotes ✓
WHERE Grade = '11'        -- wrong: don't quote numbers ❌
WHERE Name = Smith        -- wrong: missing quotes ❌
```
