# SQL SELECT — Advanced Queries

Once you can SELECT with WHERE and ORDER BY, the next step is aggregating data — counting, averaging, grouping — which is what separates basic retrieval from actual data analysis.

> [!NOTE] Grade 12
> Aggregate functions (COUNT, SUM, AVG, MAX, MIN), GROUP BY, and HAVING are primarily Grade 12 content. They appear in every recent Paper 1 paper.

---

## Aggregate Functions

Aggregate functions operate on a **set of values** and return a single result.

| Function | Returns | Null handling |
|---|---|---|
| `COUNT(*)` | Total number of rows | Counts everything including NULLs |
| `COUNT(column)` | Number of non-NULL values in column | Ignores NULLs |
| `SUM(column)` | Total of all values | Ignores NULLs |
| `AVG(column)` | Average of all values | Ignores NULLs |
| `MAX(column)` | Largest value | Ignores NULLs |
| `MIN(column)` | Smallest value | Ignores NULLs |

### Using Aggregate Functions

```sql
-- Total number of students
SELECT COUNT(*) AS TotalStudents
FROM Learners;

-- Average mark across all students
SELECT AVG(Mark) AS AverageMark
FROM Learners;

-- Highest and lowest marks
SELECT MAX(Mark) AS Highest, MIN(Mark) AS Lowest
FROM Learners;

-- Sum of all marks
SELECT SUM(Mark) AS TotalMarks
FROM Learners;

-- Count students in Grade 11 only
SELECT COUNT(*) AS Grade11Count
FROM Learners
WHERE Grade = 11;
```

> [!WARNING] Aggregate Functions Can't Mix with Regular Columns (Without GROUP BY)
> This query is WRONG:
> ```sql
> SELECT Surname, COUNT(*)    -- ERROR: Surname is not aggregated
> FROM Learners;
> ```
> You must either aggregate ALL selected columns, or use GROUP BY.

---

## GROUP BY — Aggregating by Category

`GROUP BY` divides rows into groups based on one or more columns, then applies an aggregate function to each group.

```sql
SELECT Grade, COUNT(*) AS NumStudents, AVG(Mark) AS AvgMark
FROM Learners
GROUP BY Grade;
```

Result:
| Grade | NumStudents | AvgMark |
|---|---|---|
| 10 | 45 | 72.4 |
| 11 | 48 | 68.9 |
| 12 | 42 | 74.1 |

### More GROUP BY examples

```sql
-- Count students per gender
SELECT Gender, COUNT(*) AS Total
FROM Learners
GROUP BY Gender;

-- Average mark per subject
SELECT SubjectName, AVG(Mark) AS Average
FROM Marks
INNER JOIN Subjects ON Marks.SubjectID = Subjects.SubjectID
GROUP BY SubjectName;

-- Count and average per Grade, sorted by grade
SELECT Grade, COUNT(*) AS Count, ROUND(AVG(Mark), 1) AS Average
FROM Learners
GROUP BY Grade
ORDER BY Grade;
```

---

## HAVING — Filtering Group Results

`HAVING` filters groups **after** `GROUP BY` has been applied. It's the GROUP BY equivalent of WHERE.

**Rule:** 
- `WHERE` filters **individual rows** (before grouping)
- `HAVING` filters **groups** (after grouping)

```sql
-- Grades where the average mark is above 70
SELECT Grade, AVG(Mark) AS AvgMark
FROM Learners
GROUP BY Grade
HAVING AVG(Mark) > 70;

-- Subjects with more than 30 students enrolled
SELECT SubjectName, COUNT(*) AS Enrolled
FROM Enrolment
INNER JOIN Subjects ON Enrolment.SubjectID = Subjects.SubjectID
GROUP BY SubjectName
HAVING COUNT(*) > 30;

-- Grades with average above 60, ordered by average descending
SELECT Grade, ROUND(AVG(Mark), 2) AS Avg
FROM Learners
GROUP BY Grade
HAVING AVG(Mark) >= 60
ORDER BY AVG(Mark) DESC;
```

### WHERE vs HAVING — Key Distinction

```sql
-- WHERE: filter rows first, THEN group
SELECT Grade, AVG(Mark) AS Avg
FROM Learners
WHERE Mark >= 30          -- exclude marks below 30 before grouping
GROUP BY Grade;

-- HAVING: group first, THEN filter groups
SELECT Grade, AVG(Mark) AS Avg
FROM Learners
GROUP BY Grade
HAVING AVG(Mark) >= 60;   -- only show grades with avg >= 60
```

---

## Subqueries

A **subquery** is a query inside another query. The inner query runs first, and its result is used by the outer query.

```sql
-- Students with above-average marks
SELECT Surname, Mark
FROM Learners
WHERE Mark > (SELECT AVG(Mark) FROM Learners)
ORDER BY Mark DESC;

-- Students in the same grade as 'Adams'
SELECT Surname
FROM Learners
WHERE Grade = (SELECT Grade FROM Learners WHERE Surname = 'Adams');
```

---

## ROUND — Formatting Decimal Results

Aggregate functions often return many decimal places. `ROUND` controls this:

```sql
SELECT ROUND(AVG(Mark), 2) AS AvgMark     -- 2 decimal places
FROM Learners;

SELECT ROUND(AVG(Mark), 0) AS AvgMark     -- rounded to integer
FROM Learners;
```

---

## Complete Clause Order

```sql
SELECT   column(s) or aggregate(s)     -- 1
FROM     table                          -- 2
WHERE    row_condition                  -- 3 (optional)
GROUP BY column(s)                      -- 4 (optional)
HAVING   group_condition                -- 5 (optional, needs GROUP BY)
ORDER BY column(s)                      -- 6 (optional)
```

This order is mandatory. Swapping any clause is a syntax error.

---

## Practice Exercises

Use this table for all exercises:

**Table: `Learners`**

| LearnerID | Surname | Grade | Mark | Gender | Subject |
|---|---|---|---|---|---|
| 1 | Adams | 10 | 72 | F | IT |
| 2 | Botha | 11 | 45 | M | IT |
| 3 | Coetzee | 12 | 88 | M | Math |
| 4 | Dlamini | 11 | 91 | F | IT |
| 5 | Evans | 10 | 55 | M | Math |
| 6 | Fortuin | 12 | 38 | F | IT |
| 7 | Gordon | 11 | 67 | M | Math |
| 8 | Hendricks | 10 | 80 | F | IT |

---

**Exercise 1** — How many learners are in each grade? Show grade and count, sorted by grade.

<details>
<summary>Show solution</summary>

```sql
SELECT Grade, COUNT(*) AS NumLearners
FROM Learners
GROUP BY Grade
ORDER BY Grade;
```
</details>

---

**Exercise 2** — What is the average mark for each subject? Only show subjects where the average is above 65.

<details>
<summary>Show solution</summary>

```sql
SELECT Subject, ROUND(AVG(Mark), 1) AS Average
FROM Learners
GROUP BY Subject
HAVING AVG(Mark) > 65;
```
</details>

---

**Exercise 3** — Show the highest mark, lowest mark, and number of learners for each grade. Sort by highest mark descending.

<details>
<summary>Show solution</summary>

```sql
SELECT Grade, MAX(Mark) AS Highest, MIN(Mark) AS Lowest, COUNT(*) AS Total
FROM Learners
GROUP BY Grade
ORDER BY MAX(Mark) DESC;
```
</details>

---

**Exercise 4** — Show all learners with a mark above the overall average.

<details>
<summary>Show solution</summary>

```sql
SELECT Surname, Grade, Mark
FROM Learners
WHERE Mark > (SELECT AVG(Mark) FROM Learners)
ORDER BY Mark DESC;
```
</details>

---

> [!TIP] Exam Tip
> The most common mistake with GROUP BY and HAVING is using `WHERE` to filter group results. Remember: if your condition involves an aggregate function like `AVG()` or `COUNT()`, it belongs in `HAVING` — not `WHERE`. Write yourself this rule: "WHERE = rows, HAVING = groups."
