# SQL Joins

A single table is rarely enough. Real databases split data across multiple tables to avoid duplication. **Joins** bring that data back together in a query, letting you combine information from two or more tables.

> [!NOTE] Grade 12
> Joins are a Grade 12 topic. The CAPS specification limits Paper 1 to a maximum of **two tables**. INNER JOIN is the most common. LEFT JOIN appears less frequently but is examined.

---

## Why Joins?

Consider storing student marks. You could put everything in one table:

```
Marks (flat) — BAD
StudentID | Surname | SubjectID | SubjectName | Mark
1001      | Adams   | S01       | IT          | 87
1001      | Adams   | S02       | Math        | 72     ← "Adams" repeated
```

Better design: separate tables with a FK linking them:

```
Students           Marks              Subjects
StudentID|Surname  MarkID|StuID|SubID|Mark  SubID|SubjectName
1001     |Adams    1     |1001 |S01  |87    S01  |IT
1002     |Botha    2     |1001 |S02  |72    S02  |Math
                   3     |1002 |S01  |91
```

A JOIN query reassembles this into a readable result.

---

## INNER JOIN

Returns only rows where there is a **match in both tables**.

```sql
SELECT table1.column, table2.column
FROM table1
INNER JOIN table2 ON table1.PKcolumn = table2.FKcolumn;
```

### Worked Example

**Tables:**

`Students`: StudentID, Surname, Grade  
`Marks`: MarkID, StudentID (FK), Subject, Mark

```sql
-- Show each student's name with their mark
SELECT Students.Surname, Students.Grade, Marks.Subject, Marks.Mark
FROM Students
INNER JOIN Marks ON Students.StudentID = Marks.StudentID;
```

Result: Only students who HAVE marks appear. Students with no marks are excluded.

### With WHERE and ORDER BY

```sql
-- Students who passed (mark >= 50), sorted by surname
SELECT Students.Surname, Marks.Subject, Marks.Mark
FROM Students
INNER JOIN Marks ON Students.StudentID = Marks.StudentID
WHERE Marks.Mark >= 50
ORDER BY Students.Surname;
```

### Using Table Aliases

Long table names repeated many times get tedious. Aliases make queries shorter:

```sql
SELECT s.Surname, s.Grade, m.Subject, m.Mark
FROM Students AS s
INNER JOIN Marks AS m ON s.StudentID = m.StudentID
WHERE m.Mark >= 50
ORDER BY s.Surname;
```

---

## Three-Table Join

When you have three related tables:

**Tables:**
- `Students`: StudentID, Surname
- `Marks`: MarkID, StudentID (FK), SubjectID (FK), Mark
- `Subjects`: SubjectID, SubjectName

```sql
SELECT s.Surname, sub.SubjectName, m.Mark
FROM Students AS s
INNER JOIN Marks AS m ON s.StudentID = m.StudentID
INNER JOIN Subjects AS sub ON m.SubjectID = sub.SubjectID
WHERE m.Mark >= 50
ORDER BY s.Surname, sub.SubjectName;
```

> [!WARNING] CAPS Limit: Maximum 2 Tables in Paper 1
> The CAPS specification states joins involving at most **two tables** in the Paper 1 examination. In practice, some exams may have a 3-table join. Know the 2-table pattern cold; the 3-table version is an extension of the same logic.

---

## LEFT JOIN (LEFT OUTER JOIN)

Returns **all rows from the left table**, plus matched rows from the right table. Where there is no match in the right table, the result shows `NULL`.

```sql
SELECT Students.Surname, Marks.Mark
FROM Students
LEFT JOIN Marks ON Students.StudentID = Marks.StudentID;
```

Result: ALL students appear. Those with no marks show `NULL` in the Mark column.

| Surname | Mark |
|---|---|
| Adams | 87 |
| Botha | NULL ← no mark record for Botha |
| Coetzee | 91 |

### When to use LEFT JOIN

Use LEFT JOIN when you need **all records from the main table**, even those without matching records in the secondary table:
- "Show all students, even those not yet marked"
- "Show all products, even those with no orders"

---

## INNER vs LEFT JOIN — Summary

| | INNER JOIN | LEFT JOIN |
|---|---|---|
| **Returns** | Only rows with matches in BOTH tables | ALL rows from left table + matched from right |
| **Unmatched rows** | Excluded | Shown with NULL values |
| **Use when** | You only want complete data | You want all records even without a match |

---

## Common Mistakes

> [!WARNING] Watch Out For
> 1. **Wrong JOIN condition** — always match PK to FK: `ON Students.StudentID = Marks.StudentID`, not a name field
> 2. **Ambiguous column names** — if both tables have a column called `Name`, specify: `Students.Name`; without the prefix you get an error
> 3. **Forgetting the ON clause** — `FROM Students INNER JOIN Marks` with no ON creates a Cartesian product (every student × every mark)
> 4. **Using column names from wrong table** — in a JOIN, be explicit: `Marks.Mark`, not just `Mark`
> 5. **LEFT JOIN order** — the "left" table (in FROM) is the one that returns all rows; swap the order and you get different results

---

## Practice Exercises

**Tables for all exercises:**

**Students**: `StudentID (PK)`, `Surname`, `Grade`  
**Marks**: `MarkID (PK)`, `StudentID (FK)`, `Subject`, `Mark`

Sample data:  
- Students: (1001, Adams, 11), (1002, Botha, 12), (1003, Coetzee, 11), (1004, Dlamini, 12)
- Marks: (1, 1001, IT, 87), (2, 1001, Math, 72), (3, 1002, IT, 91), (4, 1003, IT, 55)
  - Note: Dlamini (1004) has NO marks recorded

---

**Exercise 1** — Show the surname, subject, and mark for all Grade 11 students, sorted by mark descending.

<details>
<summary>Show solution</summary>

```sql
SELECT Students.Surname, Marks.Subject, Marks.Mark
FROM Students
INNER JOIN Marks ON Students.StudentID = Marks.StudentID
WHERE Students.Grade = 11
ORDER BY Marks.Mark DESC;
```

Result: Adams (IT: 87), Adams (Math: 72), Coetzee (IT: 55)
</details>

---

**Exercise 2** — Show all students (including those without marks). Display surname, grade, and mark. If no mark exists, show "No Mark" (use ISNULL or IS NULL check).

<details>
<summary>Show solution</summary>

```sql
-- Basic LEFT JOIN showing NULL
SELECT Students.Surname, Students.Grade, Marks.Mark
FROM Students
LEFT JOIN Marks ON Students.StudentID = Marks.StudentID
ORDER BY Students.Surname;

-- Dlamini will show with NULL in the Mark column
```
</details>

---

**Exercise 3** — Using aggregate functions with JOIN: Show each student's surname and their average mark across all subjects. Only include students with at least one mark. Sort by average descending.

<details>
<summary>Show solution</summary>

```sql
SELECT Students.Surname, ROUND(AVG(Marks.Mark), 1) AS Average
FROM Students
INNER JOIN Marks ON Students.StudentID = Marks.StudentID
GROUP BY Students.StudentID, Students.Surname
ORDER BY AVG(Marks.Mark) DESC;
```
</details>

---

> [!TIP] Exam Tip
> The JOIN condition (`ON table1.PK = table2.FK`) is the most important part — get that wrong and nothing works. Before writing a JOIN query, identify: (1) which field links the two tables, (2) which table has the PK and which has the FK. Write the ON clause first, then build the SELECT and WHERE around it.
