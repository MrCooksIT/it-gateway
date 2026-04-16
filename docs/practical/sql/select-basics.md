# SQL SELECT — The Basics

In Delphi, all SQL runs as a text string assigned to a query component — you build the SQL with Pascal string operations, then open the query to execute it. Clause order is fixed and must follow the mnemonic **SFWGHO**: Select, From, Where, Group By, Having, Order By.

> [!NOTE] Grade 11–12
> Basic SELECT (SELECT, FROM, WHERE, ORDER BY, DISTINCT) is introduced in Grade 11. Grade 12 extends this to joins, aggregate functions, GROUP BY, and HAVING. Every Paper 1 paper has at least one SQL section.

---

## Clause Order — SFWGHO

Clauses must appear in this exact order. Writing them out of order causes a syntax error.

| # | Clause | Purpose | Required? |
|---|---|---|---|
| 1 | `SELECT` | Which fields to display | Yes |
| 2 | `FROM` | Which table(s) to query | Yes |
| 3 | `WHERE` | Filter rows by condition | No |
| 4 | `GROUP BY` | Group rows for aggregation | No |
| 5 | `HAVING` | Filter groups (used with GROUP BY) | No |
| 6 | `ORDER BY` | Sort the result set | No |

---

## SELECT

### Specific fields

```sql
SELECT StudentID, Surname, Mark
FROM tblStudents
```

Only the listed fields appear in the result, in the order listed.

### All fields

```sql
SELECT *
FROM tblStudents
```

`*` means every field in the table.

### DISTINCT — remove duplicates

```sql
SELECT DISTINCT Province
FROM tblStudents
```

Returns each unique value of `Province` once. By default, `DISTINCT` sorts the result ascending.

Two fields with DISTINCT finds unique **combinations** of those fields:

```sql
SELECT DISTINCT Grade, Gender
FROM tblStudents
```

Returns each unique Grade + Gender pair — for example, (10, M), (10, F), (11, M) — with no repeated combinations.

---

## ORDER BY

```sql
-- Sort by mark ascending (lowest first) — ASC is the default and can be omitted
SELECT Surname, Mark
FROM tblStudents
ORDER BY Mark ASC

-- Sort by mark descending (highest first)
SELECT Surname, Mark
FROM tblStudents
ORDER BY Mark DESC

-- Multiple sort fields: sort by grade ascending, then by mark descending within each grade
SELECT Surname, Grade, Mark
FROM tblStudents
ORDER BY Grade ASC, Mark DESC
```

---

## WHERE — Filtering Rows

### Relational operators

| Operator | Meaning | Example |
|---|---|---|
| `=` | Equal to | `WHERE Grade = 11` |
| `<>` | Not equal to | `WHERE Status <> "Inactive"` |
| `>` | Greater than | `WHERE Mark > 80` |
| `<` | Less than | `WHERE Mark < 50` |
| `>=` | Greater than or equal | `WHERE Mark >= 50` |
| `<=` | Less than or equal | `WHERE Age <= 17` |

### AND / OR / NOT

```sql
-- Both conditions must be true
WHERE Grade = 11 AND Mark >= 60

-- Either condition is enough
WHERE Grade = 10 OR Grade = 12

-- Exclude rows
WHERE NOT Grade = 10
-- Equivalent:
WHERE Grade <> 10

-- Combining — use brackets to control precedence
WHERE (Grade = 11 OR Grade = 12) AND Mark >= 50
```

### BETWEEN (inclusive on both ends)

```sql
WHERE Mark BETWEEN 60 AND 79
```

Equivalent to `WHERE Mark >= 60 AND Mark <= 79`. Both endpoints are included.

### IN — match a list

```sql
WHERE Grade IN (10, 11, 12)

-- Same as:
WHERE Grade = 10 OR Grade = 11 OR Grade = 12

-- Works with text values too:
WHERE Province IN ("GP", "WC", "KZN")
```

### IS NULL / IS NOT NULL

```sql
-- Records with no email on file
WHERE Email IS NULL

-- Records that do have an email
WHERE Email IS NOT NULL
```

> [!NOTE]
> `NULL` means "no value at all". You cannot use `= NULL` — it never matches. Always use `IS NULL` or `IS NOT NULL`.

---

## LIKE — Pattern Matching

`LIKE` finds values that match a pattern. It only works on **Text** and **Date/Time** fields.

| Wildcard | Meaning |
|---|---|
| `%` | Any number of characters (including zero) |
| `_` | Exactly one character |

### Examples

```sql
-- Starts with "Car"
WHERE Name LIKE "Car%"
-- matches: Carlos, Carla, Car

-- Ends with "GP"
WHERE Reg LIKE "%GP"
-- matches: CA 123 GP, GP

-- Contains "bosch" anywhere
WHERE Suburb LIKE "%bosch%"
-- matches: Constantiabosch, Boschenmeer, bosch

-- Exactly one character before "at"
WHERE Animal LIKE "_at"
-- matches: Cat, Bat, Rat  —  does NOT match "Goat" (two chars before "at")
```

---

## User Input in Delphi SQL

All SQL runs as a Pascal string. When you insert a variable into that string, the quoting rules depend on the field's data type in the Access database.

### String fields (Text in Access)

Access SQL uses `"` to delimit string values inside the query. In Pascal you build this with either `QuotedStr()` or direct string concatenation.

```pascal
var
  sInput: string;
begin
  sInput := InputBox('Search', 'Enter surname:', '');

  // Option 1 — QuotedStr wraps the value in double quotes automatically
  qry.SQL.Text := 'SELECT * FROM tblStudents WHERE Surname = ' + QuotedStr(sInput);

  // Option 2 — manual double-quote concatenation
  qry.SQL.Text := 'SELECT * FROM tblStudents WHERE Surname = "' + sInput + '"';

  // From a component (e.g. TEdit named edtSurname):
  qry.SQL.Text := 'SELECT * FROM tblStudents WHERE Surname = ' + QuotedStr(edtSurname.Text);

  qry.Open;
end;
```

### Number, Currency, and AutoNumber fields

These field types do not use quotes in the SQL. Store the user's input as a string variable and concatenate it directly — no conversion needed.

```pascal
var
  sNum: string;
  iNum: integer;
begin
  // From InputBox — already a string, concatenate directly
  sNum := InputBox('Search', 'Enter student ID:', '');
  qry.SQL.Text := 'SELECT * FROM tblStudents WHERE StudentID = ' + sNum;

  // If you already have an integer variable:
  iNum := 1042;
  qry.SQL.Text := 'SELECT * FROM tblStudents WHERE StudentID = ' + IntToStr(iNum);

  qry.Open;
end;
```

### Date/Time fields

Access SQL uses `#` to delimit date values. Convert a date to a string with `DateToStr`, then wrap it in `#`.

```pascal
var
  sDate, sDate1, sDate2: string;
begin
  // Single date comparison
  sDate := DateToStr(Date);  // today's date as a string
  qry.SQL.Text := 'SELECT * FROM tblStudents WHERE DOB < #' + sDate + '#';

  // From a DateTimePicker component named dtpDOB:
  sDate := DateToStr(dtpDOB.Date);
  qry.SQL.Text := 'SELECT * FROM tblStudents WHERE DOB < #' + sDate + '#';

  // Date range with BETWEEN
  sDate1 := DateToStr(dtpFrom.Date);
  sDate2 := DateToStr(dtpTo.Date);
  qry.SQL.Text := 'SELECT * FROM tblStudents ' +
                  'WHERE DOB BETWEEN #' + sDate1 + '# AND #' + sDate2 + '#';

  qry.Open;
end;
```

### Boolean (Yes/No) fields

Use `BoolToStr` to convert a Boolean value to a string for the SQL.

```pascal
var
  bFlag: boolean;
begin
  // From a variable:
  bFlag := chkActive.Checked;
  qry.SQL.Text := 'SELECT * FROM tblStudents WHERE Active = ' + BoolToStr(bFlag);

  // Directly from a TCheckBox component:
  qry.SQL.Text := 'SELECT * FROM tblStudents WHERE Active = ' + BoolToStr(chkActive.Checked);

  qry.Open;
end;
```

### Accessing field values from a query result

```pascal
// Read a field value from the current record:
ShowMessage(qry['Surname']);
lblMark.Caption := IntToStr(qry['Mark']);
```

### LIKE with user input

Wrap the wildcard characters inside the string value before concatenating:

```pascal
// Option 1 — QuotedStr adds the double quotes; % goes inside the value
qry.SQL.Text := 'SELECT * FROM tblStudents WHERE Surname LIKE ' +
                QuotedStr('%' + sInput + '%');

// Option 2 — manual concatenation
qry.SQL.Text := 'SELECT * FROM tblStudents WHERE Surname LIKE "%' + sInput + '%"';
```

---

## Common Runtime Errors

| Error message | Most likely cause |
|---|---|
| `Parameter XXX has no default value` | Field name spelled wrong, field does not exist in that table, or a Text field value is missing its quotes |
| `Cannot find input table XXX` | Table name spelled wrong |
| `Syntax error in From clause` | Missing `WHERE` keyword before a condition, or missing space in `ORDER BY` / `GROUP BY` |
| `Syntax error (missing operator) in query expression XXX` | Missing `FROM`, clauses written out of SFWGHO order, missing `AND`/`OR`, or field name needs square brackets |

---

## Key Terms

| Term | Meaning |
|---|---|
| `SELECT` | Specifies which fields to return |
| `FROM` | Specifies the table(s) to query |
| `WHERE` | Filters rows; only rows where the condition is true are returned |
| `ORDER BY` | Sorts the result set; ASC (default) or DESC |
| `DISTINCT` | Removes duplicate rows from the result; sorts ascending by default |
| `BETWEEN x AND y` | Range check, inclusive of both x and y |
| `IN (...)` | Matches any value in the given list |
| `LIKE` | Pattern match using `%` (any chars) or `_` (one char); Text and Date fields only |
| `IS NULL` | Tests whether a field has no value |
| `QuotedStr()` | Delphi function that wraps a string in double quotes for use in Access SQL |
| `BoolToStr()` | Delphi function that converts a Boolean to its string representation |
| `DateToStr()` | Delphi function that converts a TDate/TDateTime to a string |
| SFWGHO | Mnemonic for clause order: Select, From, Where, Group By, Having, Order By |

---

> [!TIP] Exam Focus
> Typical exam questions on this topic:
> 1. Write a SELECT query that filters on a text field entered by the user — you must use `QuotedStr()` or `'"' + var + '"'` correctly.
> 2. Write a SELECT query that filters on a date range using `BETWEEN #date1# AND #date2#`.
> 3. Use `LIKE` with `%` to find records where a name **contains** a specific substring entered by the user.
> 4. Explain what the error "Parameter XXX has no default value" means and give one possible cause.
> 5. Write a complete Delphi code snippet — `InputBox`, build the SQL string, and call `qry.Open` — for a given scenario involving a number or Boolean field.
