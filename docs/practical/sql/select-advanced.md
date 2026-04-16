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
-- VAT amount on each activity
SELECT Activity, RentingCost, (RentingCost * 15 / 100) AS VAT
FROM tblActivity

-- Cost including VAT (square brackets because heading has spaces)
SELECT Cost, (Cost + Cost * 15 / 100) AS [Amount Incl VAT]
FROM tblLearners

-- Average percentage — repeat the calculation in WHERE to filter on it
SELECT NAME, ROUND((Mark1 + Mark2) / 300 * 100) AS Average
FROM tblLearners
WHERE (Mark1 + Mark2) / 300 * 100 < 50
```

> [!IMPORTANT] Repeat the Calculation
> SQL does not allow you to reference an alias (like `Average`) in WHERE or ORDER BY. You must **repeat the full calculation** in the WHERE clause if filtering on it, and again in ORDER BY if sorting by it.

---

## Number Functions

These functions work on numeric fields or expressions.

| Function | Description | Example | Result |
|---|---|---|---|
| `Round(F)` | Rounds to the nearest integer. When the value is exactly .5, rounds to the nearest even number (banker's rounding). | `Round(122.5)` | `122` |
| `Round(F)` | (same rule, even target) | `Round(121.5)` | `122` |
| `Round(F, Y)` | Rounds F to Y decimal places | `Round(122.888, 1)` | `122.9` |
| `Int(F)` | Returns the integer part only — does not round, just truncates | `Int(122.8)` | `122` |
| `ABS(F)` | Returns the positive (absolute) value of F | `ABS(15000 - 20000)` | `5000` |

### Examples in queries

```sql
-- Round the average percentage to 1 decimal place
SELECT ROUND(AVG(percentage), 1) AS Average
FROM tblLearners
WHERE Grade = 11

-- Show the absolute difference between two costs
SELECT Activity, ABS(CostA - CostB) AS Difference
FROM tblActivity
```

---

## String / Text Functions

These functions work on text fields but can also be applied to other data types. All positions are **1-based** (the first character is at position 1).

| Function | Description | Example | Result |
|---|---|---|---|
| `Left(F, Y)` | First Y characters from the left | `Left('Ayden', 3)` | `Ayd` |
| `Right(F, Y)` | Last Y characters from the right | `Right('Ayden', 2)` | `en` |
| `MID(F, X, Y)` | Y characters starting at position X | `MID('Ayden', 2, 3)` | `yde` |
| `LEN(F)` | Total number of characters (including spaces) | `LEN('Ayden Cooks')` | `11` |
| `F & F` | Concatenate (join) fields or strings into one | `'Ayden' & ' ' & 'Cooks'` | `Ayden Cooks` |
| `INStr(F, "Z")` | Position of the first occurrence of Z in F. Returns 0 if not found. Not case-sensitive. | `INSTR('Ayden', 'E')` | `4` |
| `UCase(F)` | Converts all characters to uppercase | `UCase(LEFT('ayden', 1))` | `A` |
| `LCase(F)` | Converts all characters to lowercase | `LCase('AYDEN')` | `ayden` |

### Examples in queries

```sql
-- Show first 3 characters of each learner's name
SELECT Left(NAME, 3) AS Initials
FROM tblLearners

-- Combine first name and surname into one column
SELECT FirstName & ' ' & Surname AS [Full Name]
FROM tblLearners

-- Filter learners whose email contains '@'
SELECT NAME, Email
FROM tblLearners
WHERE INSTR(Email, '@') > 0

-- Show names in all caps
SELECT UCase(Surname) AS Surname
FROM tblLearners
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
-- Calculate each learner's age from their date of birth
SELECT NAME, Round((Date() - DOB) / 365.25) AS Age
FROM tblLearners

-- Learners born in the year 2008
SELECT NAME, DOB
FROM tblLearners
WHERE YEAR(DOB) = 2008

-- Learners born in September (month 9)
SELECT NAME, DOB
FROM tblLearners
WHERE MONTH(DOB) = 9

-- Display cost as currency
SELECT Activity, Format(RentingCost, "Currency") AS [Rental Cost]
FROM tblActivity

-- Display current time alongside each record
SELECT *, Format(Now(), "hh:mm") AS [Time Now]
FROM tblActivity
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
-- Total number of learners
SELECT Count(*) AS [Total Learners]
FROM tblLearners

-- Count only learners who have a cell number on record
SELECT Count(CellNum) AS [Have Cell]
FROM tblLearners

-- Highest and lowest marks
SELECT Max(Mark) AS Highest, Min(Mark) AS Lowest
FROM tblLearners

-- Sum of all rental costs
SELECT Sum(RentingCost) AS [Total Cost]
FROM tblActivity
```

### Calculations inside aggregate functions

You can nest a calculation inside an aggregate function:

```sql
-- Average percentage rounded to 1 decimal, for Grade 11 only
SELECT ROUND(AVG(percentage), 1) AS Average
FROM tblLearners
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
-- Count how many learners are in each grade
SELECT Grade, Count(*) AS [Number of Learners]
FROM tblLearners
GROUP BY Grade

-- Total ticket sales per company
SELECT CompanyID, Sum(TicketsSold) AS [Total Tickets]
FROM tblActivity
GROUP BY CompanyID
ORDER BY CompanyID
```

### HAVING

`HAVING` filters groups **after** they have been formed — it is the GROUP BY equivalent of WHERE.

- Use `WHERE` to filter individual rows **before** grouping.
- Use `HAVING` to filter groups **after** grouping.
- `HAVING` requires `GROUP BY` to be present.
- You can use aggregate functions inside `HAVING`.

```sql
-- Only show companies that sold more than 3 activities
SELECT CompanyID, Count(*) AS Activities
FROM tblActivity
GROUP BY CompanyID
HAVING Count(*) > 3

-- Grades where the average mark is 60 or above
SELECT Grade, Round(Avg(Mark), 1) AS Average
FROM tblLearners
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
SELECT tblCompany.CompanyName, tblActivity.Activity, tblActivity.TicketsSold
FROM tblCompany, tblActivity
WHERE tblCompany.CompanyID = tblActivity.CompanyID
  AND tblActivity.TicketsSold < 100
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
6. After the loop, set a prompt text: `cmbXXX.Text := 'Select a company'`.

> [!WARNING] Always include qry.Next inside the loop
> If you forget `qry.Next`, the record pointer never advances and the loop runs forever, freezing the application. This is a common exam mistake.

### Worked example

```pascal
procedure TfrmFestival.FormActivate(Sender: TObject);
begin
  qryFestival.SQL.Text := 'SELECT DISTINCT CompanyID FROM tblActivity ORDER BY CompanyID';
  qryFestival.Open;
  qryFestival.First;
  while not qryFestival.Eof do
  begin
    cmbCompany.Items.Add(qryFestival['CompanyID']);
    qryFestival.Next;
  end;
  cmbCompany.Text := 'Select a company';
end;
```

### Checking how many items loaded

```pascal
ShowMessage(IntToStr(cmbCompany.Items.Count) + ' companies loaded');
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
> **1.** Write a query that displays each learner's name and their mark as a percentage of 300, rounded to 1 decimal place, for all learners whose percentage is below 50. Label the column `Percentage`.
>
> **2.** Write a query that shows each company name and the total tickets sold by that company, but only for companies that sold more than 500 tickets in total. Use two tables: `tblCompany` (fields: `CompanyID`, `CompanyName`) and `tblActivity` (fields: `CompanyID`, `TicketsSold`).
>
> **3.** Write a query that displays each learner's full name (first name and surname joined with a space) and their date of birth formatted as `dd mmm yyyy`. Label the columns `[Full Name]` and `[Date of Birth]`.
>
> **4.** Write the Delphi code for a `FormActivate` event that populates a ComboBox called `cmbGrade` with all distinct grade values from `tblLearners`, ordered by grade, with a prompt of `'Select a grade'`.
>
> **5.** Write a query that counts how many learners were born in each year, showing only years that have more than 5 learners. Label the columns `BirthYear` and `Count`. Sort from most to least learners.
