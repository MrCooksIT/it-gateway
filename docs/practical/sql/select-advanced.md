# SQL SELECT — Advanced Queries

Advanced SQL goes beyond basic retrieval: you can calculate new values on the fly, manipulate text and dates, aggregate rows into summary results, query multiple tables at once, and feed query results directly into Delphi controls.

> [!NOTE] Grade 12
> Calculations, built-in functions, aggregate functions, GROUP BY, HAVING, multi-table queries, and populating Delphi controls from SQL are all Grade 12 CAPS content. Expect at least one of these in every Paper 1.

---

## Calculations in SELECT

You can perform arithmetic directly inside a SELECT statement — Access calculates the result for every row and displays it as a new column.

**Operators:** `( )` &nbsp; `*` &nbsp; `/` &nbsp; `+` &nbsp; `-`

Normal order of operations applies: brackets first, then `*` and `/`, then `+` and `-`.

### Syntax

Place the calculation in the **SELECT part**, before FROM. Give it a heading with `AS`:

```sql
SELECT Field1, (calculation) AS HeadingName
FROM tblTableName
```

Use **square brackets** for headings that contain a space or use a reserved word:

```sql
AS [Amount Incl VAT]
```

### Examples

```sql
-- VAT amount on each product
SELECT ProductName, Price, (Price * 15 / 100) AS VAT
FROM tblProducts

-- Price including VAT (square brackets because heading has spaces)
SELECT ProductName, Price, (Price + Price * 15 / 100) AS [Amount Incl VAT]
FROM tblProducts

-- Student's percentage out of 300, filtered to below 50
SELECT Surname, Mark, (Mark / 300 * 100) AS Percentage
FROM tblStudents
WHERE (Mark / 300 * 100) < 50
```

> [!IMPORTANT] Repeat the Calculation
> SQL does not allow you to reference an alias (like `Percentage`) in WHERE or ORDER BY. You must **repeat the full calculation** in the WHERE clause if filtering on it, and again in ORDER BY if sorting by it.

---

## Number Functions

These functions work on numeric fields or expressions.

| Function | Description | Example | Result |
|---|---|---|---|
| `Round(F)` | Rounds to the nearest integer. When the value is exactly .5, rounds to the nearest even number (banker's rounding). | `Round(122.5)` | `122` |
| `Round(F)` | (same rule, even target) | `Round(121.5)` | `122` |
| `Round(F, Y)` | Rounds F to Y decimal places | `Round(122.888, 1)` | `122.9` |
| `Int(F)` | Returns the integer part only — does not round, just truncates | `Int(122.8)` | `122` |

### Examples in queries

```sql
-- Round the average mark to 1 decimal place for Grade 11 students
SELECT ROUND(AVG(Mark), 1) AS Average
FROM tblStudents
WHERE Grade = 11

-- Truncate a calculated percentage to a whole number (no rounding)
SELECT Surname, INT(Mark / 300 * 100) AS Percentage
FROM tblStudents
```

---

## String / Text Functions

These functions work on text fields but can also be applied to other data types. All positions are **1-based** (the first character is at position 1).

| Function | Description | Example | Result |
|---|---|---|---|
| `Left(F, Y)` | First Y characters from the left | `Left('Sarah', 3)` | `Sar` |
| `Right(F, Y)` | Last Y characters from the right | `Right('Sarah', 2)` | `ah` |
| `MID(F, X, Y)` | Y characters starting at position X | `MID('Sarah', 2, 3)` | `ara` |
| `LEN(F)` | Total number of characters (including spaces) | `LEN('Sarah Botha')` | `11` |
| `F & F` | Concatenate (join) fields or strings into one | `'Sarah' & ' ' & 'Botha'` | `Sarah Botha` |

### Examples in queries

```sql
-- Show first 3 characters of each student's surname
SELECT Left(Surname, 3) AS Initial
FROM tblStudents

-- Combine first name and surname into one column
SELECT FirstName & ' ' & Surname AS [Full Name]
FROM tblStudents

-- Students whose surname is exactly 5 characters long
SELECT Surname
FROM tblStudents
WHERE LEN(Surname) = 5
```

---

## Date and Formatting Functions

### Formatting Functions

| Function | Description | Example | Result |
|---|---|---|---|
| `Format(F, "Currency")` | Displays a number as Rand currency | `Format(121.2323, "Currency")` | `R 121.23` |
| `Date()` | Returns the current system date | `Round((Date() - DOB) / 365.25)` | Age in years |
| `Now()` | Returns the current date and time | `SELECT *, NOW() AS [Right Now]` | — |
| `Format(F, "hh:mm")` | Displays only the time portion | `Format(NOW(), "hh:mm") AS [Right Now]` | `14:35` |
| `Format(F, "dd-mm-yyyy")` | Displays a date in day-month-year format | `Format(Date(), "dd-mm-yyyy")` | `10-04-2026` |
| `Format(Date(), "d mmm yy")` | Short date format | `Format(Date(), "d mmm yy")` | `10 Apr 26` |
| `Year(F)` | Extracts the year from a date | `WHERE YEAR(DOB) = 2008` | — |
| `Month(F)` | Extracts the month number from a date | `WHERE MONTH(DOB) = 9` | — |
| `Day(F)` | Extracts the day number from a date | `WHERE Day(DOB) = 1` | — |

### Date Format Codes

| Code | Meaning | Example Output |
|---|---|---|
| `yyyy` | 4-digit year | `2026` |
| `yy` | 2-digit year | `26` |
| `mmmm` | Full month name | `April` |
| `mmm` | Abbreviated month | `Apr` |
| `mm` | 2-digit month | `04` |
| `m` | Month without leading zero | `4` |
| `dd` | 2-digit day | `05` |
| `d` | Day without leading zero | `5` |

### Examples in queries

```sql
-- Calculate each student's age from their date of birth
SELECT Surname, Round((Date() - DOB) / 365.25) AS Age
FROM tblStudents

-- Students born in the year 2008
SELECT Surname, DOB
FROM tblStudents
WHERE YEAR(DOB) = 2008

-- Students born in September (month 9)
SELECT Surname, DOB
FROM tblStudents
WHERE MONTH(DOB) = 9

-- Display price as currency
SELECT ProductName, Format(Price, "Currency") AS [Product Price]
FROM tblProducts

-- Display current time alongside each record
SELECT *, Format(Now(), "hh:mm") AS [Time Now]
FROM tblStudents
```

---

## Aggregate Functions

Aggregate functions operate on a **set of rows** and return a **single result**. When used without GROUP BY, the entire query produces one cell or one row in the DBGrid.

| Function | Description | Note |
|---|---|---|
| `Count(*)` | Counts all active records in the table | Includes every row |
| `Count(Field)` | Counts records where the field has a value | `Count(CellNum)` may be less than `Count(*)` if some cells are blank |
| `Min(Field)` | Returns the smallest value in the field | |
| `Max(Field)` | Returns the largest value in the field | |
| `Sum(Field)` | Returns the total of all values in the field | |
| `Avg(Field)` | Returns the average — **excludes NULL values** but counts 0 | A field that is blank is excluded; a field storing 0 is included |

### Using aggregate functions

```sql
-- Total number of students
SELECT Count(*) AS [Total Students]
FROM tblStudents

-- Count only students who have a cell number on record
SELECT Count(CellNum) AS [Have Cell]
FROM tblStudents

-- Highest and lowest marks
SELECT Max(Mark) AS Highest, Min(Mark) AS Lowest
FROM tblStudents

-- Total value of all products
SELECT Sum(Price) AS [Total Value]
FROM tblProducts
```

### Calculations inside aggregate functions

You can nest a calculation inside an aggregate function:

```sql
-- Average mark rounded to 1 decimal, for Grade 11 only
SELECT ROUND(AVG(Mark), 1) AS Average
FROM tblStudents
WHERE Grade = 11
```

### Displaying an aggregate result in a Delphi label

When a query returns a single numeric value, read it from the query and display it in a label using `FloatToStrF`:

```pascal
lblOutput.Caption := FloatToStrF(qry['Owing'], ffCurrency, 10, 2);
```

- `ffCurrency` formats the number as currency (R symbol, 2 decimal places).
- `10` is the total field width; `2` is the number of decimal places.

---

## GROUP BY and HAVING

### GROUP BY

`GROUP BY` collects all rows that share the same value in a column and collapses them into one row per group. You then apply aggregate functions to each group.

```sql
-- Count how many students are in each grade
SELECT Grade, Count(*) AS [Number of Students]
FROM tblStudents
GROUP BY Grade

-- Average mark per subject
SELECT Subject, Round(Avg(Mark), 1) AS [Average Mark]
FROM tblMarks
GROUP BY Subject
ORDER BY Subject
```

### HAVING

`HAVING` filters groups **after** they have been formed — it is the GROUP BY equivalent of WHERE.

- Use `WHERE` to filter individual rows **before** grouping.
- Use `HAVING` to filter groups **after** grouping.
- `HAVING` requires `GROUP BY` to be present.
- You can use aggregate functions inside `HAVING`.

```sql
-- Only show subjects with more than 3 mark entries
SELECT Subject, Count(*) AS [Entries]
FROM tblMarks
GROUP BY Subject
HAVING Count(*) > 3

-- Grades where the average mark is 60 or above
SELECT Grade, Round(Avg(Mark), 1) AS Average
FROM tblStudents
GROUP BY Grade
HAVING Avg(Mark) >= 60
ORDER BY Average DESC
```

---

## Multi-Table Queries

When data is spread across two tables, list both tables in the FROM clause (separated by a comma) and define the **relationship** in the WHERE clause.

> [!IMPORTANT] Correct Method for Access via Delphi
> In Microsoft Access accessed through Delphi ADO, use the comma-separation method shown below. Do not use INNER JOIN syntax.

### Syntax

```sql
SELECT tblA.Field1, tblB.Field2
FROM tblA, tblB
WHERE tblA.KeyField = tblB.KeyField
```

- The relationship condition links the primary key in one table to the foreign key in the other.
- Add extra filter conditions with `AND` after the relationship condition.
- **Prefix field names with the table name** whenever the same field name exists in both tables.

### Full example

```sql
SELECT tblStudents.Surname, tblMarks.Subject, tblMarks.Mark
FROM tblStudents, tblMarks
WHERE tblStudents.StudentID = tblMarks.StudentID
  AND tblMarks.Mark < 50
```

### Key points

- List both tables in FROM, separated by a comma.
- The relationship is defined in WHERE using `table.column = table.column`.
- Use the `table.field` prefix whenever field names could clash between tables.
- Add `AND` for every additional filter condition after the relationship.
- You can still use ORDER BY, GROUP BY, and HAVING with multi-table queries.

---

## Populating a ComboBox from SQL

You often need to fill a ComboBox, ListBox, or RadioGroup with values from the database at runtime so the user can make a selection. Do this in the **FormActivate** event (or a dedicated procedure called from FormActivate), so the control is ready as soon as the form opens.

### Steps

1. Set the query SQL text and open the query. Use `DISTINCT` if you do not want duplicate entries; add `WHERE` to filter if needed.
2. Move to the first record with `qry.First`.
3. Loop through every record until end-of-file: `while not qry.Eof do begin ... end`.
4. Inside the loop, add the field value to the control: `cmbXXX.Items.Add(qry['FieldName'])`. No type conversion is needed — `Items.Add` accepts the value directly.
5. After adding, call `qry.Next` to advance to the next record.
6. After the loop, set a prompt text: `cmbXXX.Text := 'Select a grade'`.

> [!WARNING] Always include qry.Next inside the loop
> If you forget `qry.Next`, the record pointer never advances and the loop runs forever, freezing the application. This is a common exam mistake.

### Worked example

```pascal
procedure TfrmStudents.FormActivate(Sender: TObject);
begin
  qryData.SQL.Text := 'SELECT DISTINCT Grade FROM tblStudents ORDER BY Grade';
  qryData.Open;
  qryData.First;
  while not qryData.Eof do
  begin
    cmbGrade.Items.Add(qryData['Grade']);
    qryData.Next;
  end;
  cmbGrade.Text := 'Select a grade';
end;
```

### Checking how many items loaded

```pascal
ShowMessage(IntToStr(cmbGrade.Items.Count) + ' grades loaded');
```

`Items.Count` returns the number of items currently in the ComboBox.

---

## Key Terms

| Term | Meaning |
|---|---|
| `AS` | Gives a calculated column or field a display heading (alias) |
| Square brackets `[ ]` | Required around an alias that contains spaces or reserved words |
| Aggregate function | A function that processes a set of rows and returns one result (COUNT, SUM, AVG, MIN, MAX) |
| `GROUP BY` | Groups rows with the same value so aggregate functions apply per group |
| `HAVING` | Filters groups after GROUP BY — use instead of WHERE when the condition involves an aggregate |
| `DISTINCT` | Removes duplicate values from the result |
| Concatenation (`&`) | Joins two or more fields or strings into a single value |
| `Date()` | Returns today's system date |
| `Now()` | Returns current date and time |
| `Format(F, "mask")` | Formats a value for display using a format mask |
| Foreign key | A field in one table that matches the primary key in another, defining a relationship |
| `qry.First` | Moves the record pointer to the first record |
| `qry.Next` | Advances the record pointer by one record |
| `qry.Eof` | True when the record pointer has passed the last record |
| `Items.Add` | Adds a string item to a ComboBox, ListBox, or similar control |
| `Items.Count` | Returns the number of items in a ComboBox or ListBox |

---

> [!TIP] Exam Focus
>
> Work through these exam-style questions:
>
> **1.** Write a query that displays each student's surname and their mark as a percentage of 300, rounded to 1 decimal place, for all students whose percentage is below 50. Label the column `Percentage`.
>
> **2.** Write a query that shows each student's surname and their total marks across all subjects, but only for students who have a total above 400. Use two tables: `tblStudents` (fields: `StudentID`, `Surname`) and `tblMarks` (fields: `StudentID`, `Mark`).
>
> **3.** Write a query that displays each student's full name (first name and surname joined with a space) and their date of birth formatted as `dd mmm yyyy`. Label the columns `[Full Name]` and `[Date of Birth]`.
>
> **4.** Write the Delphi code for a `FormActivate` event that populates a ComboBox called `cmbGrade` with all distinct grade values from `tblStudents`, ordered by grade, with a prompt of `'Select a grade'`.
>
> **5.** Write a query that counts how many students were born in each year, showing only years that have more than 5 students. Label the columns `BirthYear` and `Count`. Sort from most to least students.
