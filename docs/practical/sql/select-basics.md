# SQL SELECT — The Basics

SQL (Structured Query Language) is the language used to communicate with a relational database. In Paper 1, you write SQL queries — usually to retrieve, filter, and sort data from one or more tables.

> [!NOTE] Grade 11+
> Basic SELECT queries are introduced in Grade 11. Grade 12 extends to JOINs, GROUP BY, and aggregate functions. Every Paper 1 paper has at least one SQL section.

---

## The SELECT Statement

The core structure of every query:

```sql
SELECT column1, column2
FROM TableName
WHERE condition
ORDER BY column;
```

Each clause has a specific role:

| Clause | Purpose | Required? |
|---|---|---|
| `SELECT` | Which columns to display | Yes |
| `FROM` | Which table(s) to query | Yes |
| `WHERE` | Filter rows (only show matching rows) | No |
| `ORDER BY` | Sort the results | No |

---

## SELECT All Columns

```sql
SELECT *
FROM Students;
```

`*` means "all columns". Use it when you want every field from the table.

---

## SELECT Specific Columns

```sql
SELECT StudentID, Surname, Mark
FROM Students;
```

Only the listed columns appear in the result. Order matters — columns display in the order you list them.

---

## WHERE — Filtering Rows

`WHERE` keeps only rows where the condition is true.

```sql
-- Students who passed (mark >= 50)
SELECT Surname, Mark
FROM Students
WHERE Mark >= 50;

-- Students in Grade 11
SELECT *
FROM Students
WHERE Grade = 11;

-- Specific student by name
SELECT *
FROM Students
WHERE Surname = 'Coetzee';
```

> [!WARNING] String Values Need Quotes
> String values in WHERE conditions must be in **single quotes** (or double quotes — depends on the database):
> ```sql
> WHERE Surname = 'Coetzee'    -- correct ✓
> WHERE Surname = Coetzee      -- error ❌
> ```
> Numbers do NOT use quotes:
> ```sql
> WHERE Mark >= 50             -- correct ✓
> WHERE Mark >= '50'           -- wrong ❌
> ```

---

## Relational Operators in WHERE

| Operator | Meaning | Example |
|---|---|---|
| `=` | Equal to | `WHERE Grade = 11` |
| `<>` or `!=` | Not equal to | `WHERE Status <> 'Inactive'` |
| `<` | Less than | `WHERE Mark < 50` |
| `>` | Greater than | `WHERE Mark > 80` |
| `<=` | Less than or equal | `WHERE Age <= 17` |
| `>=` | Greater than or equal | `WHERE Mark >= 50` |

---

## AND / OR — Multiple Conditions

```sql
-- Both conditions must be true (AND)
SELECT Surname, Mark, Grade
FROM Students
WHERE Grade = 11 AND Mark >= 60;

-- Either condition is enough (OR)
SELECT Surname, Grade
FROM Students
WHERE Grade = 10 OR Grade = 12;

-- Combining AND and OR — use brackets to be safe
SELECT *
FROM Students
WHERE (Grade = 11 OR Grade = 12) AND Mark >= 50;
```

---

## NOT — Exclude Rows

```sql
-- Everyone except Grade 10
SELECT *
FROM Students
WHERE NOT Grade = 10;

-- Equivalent:
WHERE Grade <> 10;
```

---

## LIKE — Pattern Matching

Used to find values that **match a pattern**. Uses two wildcards:

| Wildcard | Meaning | Example |
|---|---|---|
| `%` | Any number of characters (including none) | `'Co%'` matches `'Coetzee'`, `'Cole'`, `'Co'` |
| `_` | Exactly ONE character | `'Co_'` matches `'Cox'`, `'Col'` (not `'Coetzee'`) |

```sql
-- Surnames starting with C
WHERE Surname LIKE 'C%';

-- Surnames ending in 'ee'
WHERE Surname LIKE '%ee';

-- Surnames containing 'Smith' anywhere
WHERE Surname LIKE '%Smith%';

-- Email addresses from school.co.za domain
WHERE Email LIKE '%@school.co.za';

-- ID numbers starting with 01 (born in January)
WHERE IDNumber LIKE '01%';
```

---

## BETWEEN — Range Check

```sql
-- Marks from 60 to 79 (inclusive of both endpoints)
WHERE Mark BETWEEN 60 AND 79;

-- Same as:
WHERE Mark >= 60 AND Mark <= 79;

-- Dates in a range
WHERE OrderDate BETWEEN '2024-01-01' AND '2024-12-31';
```

---

## IN — Match a List of Values

```sql
-- Students in Grade 10, 11, or 12
WHERE Grade IN (10, 11, 12);

-- Same as:
WHERE Grade = 10 OR Grade = 11 OR Grade = 12;

-- Specific surnames
WHERE Surname IN ('Smith', 'Jones', 'Brown');
```

---

## IS NULL / IS NOT NULL

Used to check for missing values:

```sql
-- Students with no email address on record
WHERE Email IS NULL;

-- Students who DO have an email
WHERE Email IS NOT NULL;
```

> [!NOTE] NULL vs Empty String
> `NULL` means "no value at all" — it is not the same as an empty string `''`. `= NULL` never works in SQL; always use `IS NULL`.

---

## ORDER BY — Sorting Results

```sql
-- Sort by mark, lowest first (ASC = ascending, default)
SELECT Surname, Mark
FROM Students
ORDER BY Mark ASC;

-- Sort by mark, highest first
SELECT Surname, Mark
FROM Students
ORDER BY Mark DESC;

-- Sort by surname alphabetically
SELECT *
FROM Students
ORDER BY Surname;

-- Sort by grade, then by mark within each grade
SELECT Surname, Grade, Mark
FROM Students
ORDER BY Grade ASC, Mark DESC;
```

---

## Aliases — Rename Columns in Output

```sql
SELECT Surname AS 'Last Name', Mark AS 'Test Score'
FROM Students;
```

The result column headers will show "Last Name" and "Test Score" instead of the field names.

---

## SELECT DISTINCT — Remove Duplicate Values

```sql
-- Show each grade only once (no duplicates)
SELECT DISTINCT Grade
FROM Students;

-- All different cities in the database
SELECT DISTINCT City
FROM Customers;
```

---

## Combining Clauses — Full Example

```sql
-- Show the surname and mark of all Grade 11 students
-- who scored between 60 and 100,
-- whose surname starts with 'A' or 'B',
-- sorted by mark descending

SELECT Surname, Mark
FROM Students
WHERE Grade = 11
  AND Mark BETWEEN 60 AND 100
  AND (Surname LIKE 'A%' OR Surname LIKE 'B%')
ORDER BY Mark DESC;
```

---

## Common Mistakes

> [!WARNING] Watch Out For
> 1. **Forgetting quotes around string values** — `WHERE Name = Smith` fails; use `'Smith'`
> 2. **Using `=` instead of `LIKE`** for pattern matching — `= 'C%'` looks for the literal text `'C%'`
> 3. **`ORDER BY` before `WHERE`** — clauses must be in order: SELECT → FROM → WHERE → ORDER BY
> 4. **`= NULL` instead of `IS NULL`** — always `IS NULL` / `IS NOT NULL`
> 5. **Case sensitivity** — SQL keywords are case-insensitive (`select` = `SELECT`) but string values may be case-sensitive depending on the database

---

## Quick Reference — Clause Order

```sql
SELECT   -- 1. What columns
FROM     -- 2. Which table
WHERE    -- 3. Filter rows (optional)
ORDER BY -- 4. Sort result (optional)
```

The clauses **must** appear in this order. Swapping them causes a syntax error.

---

## Practice Exercises

Use this table for all exercises:

**Table: `Learners`**

| LearnerID | Surname | Grade | Mark | Gender |
|---|---|---|---|---|
| 1 | Adams | 10 | 72 | F |
| 2 | Botha | 11 | 45 | M |
| 3 | Coetzee | 12 | 88 | M |
| 4 | Dlamini | 11 | 91 | F |
| 5 | Evans | 10 | 55 | M |
| 6 | Fortuin | 12 | 38 | F |
| 7 | Gordon | 11 | 67 | M |

---

**Exercise 1** — Write a query to show all learners in Grade 11 with a mark above 60, sorted by surname.

<details>
<summary>Show solution</summary>

```sql
SELECT Surname, Grade, Mark
FROM Learners
WHERE Grade = 11 AND Mark > 60
ORDER BY Surname;
```

Result: Dlamini (91), Gordon (67)
</details>

---

**Exercise 2** — Show all learners whose surname starts with a letter from A to D, displaying only surname and mark.

<details>
<summary>Show solution</summary>

```sql
SELECT Surname, Mark
FROM Learners
WHERE Surname LIKE 'A%'
   OR Surname LIKE 'B%'
   OR Surname LIKE 'C%'
   OR Surname LIKE 'D%';
```

Alternative using BETWEEN on a string (works in some databases):
```sql
WHERE Surname BETWEEN 'A' AND 'D~';
```

Result: Adams, Botha, Coetzee, Dlamini
</details>

---

**Exercise 3** — Show all learners who failed (mark below 50), sorted by mark from lowest to highest.

<details>
<summary>Show solution</summary>

```sql
SELECT Surname, Grade, Mark
FROM Learners
WHERE Mark < 50
ORDER BY Mark ASC;
```

Result: Fortuin (38), Botha (45)
</details>

---

> [!TIP] Exam Tip
> In Paper 1 SQL questions, read the question twice before writing. Check: (1) which table, (2) which columns to SELECT, (3) what the WHERE condition is exactly, (4) whether an ORDER BY is needed and in which direction. Writing the clauses in order — SELECT, FROM, WHERE, ORDER BY — prevents syntax errors from reordering.
