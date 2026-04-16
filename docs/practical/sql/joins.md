# Multi-Table Queries

Real databases split data across multiple tables to avoid duplication. A festival database, for example, stores company details in one table and activity details in another. When you need information from both — such as a company name alongside the activities they run — you must query both tables at the same time. The two tables are linked by a common field: the **primary key** in one table matches a **foreign key** in the other. Your SQL tells Access which field forms that link, and Access combines the rows for you.

> [!NOTE] Grade 12
> Multi-table queries are a Grade 12 CAPS topic. Expect at least one in every Paper 1 exam. The CAPS specification covers queries involving two tables; knowing how to extend the pattern to three tables is useful for full marks questions.

---

## How It Works

Four rules cover every multi-table query you will write:

- List **all tables** in the `FROM` clause, separated by a comma.
- Write the **relationship condition** in `WHERE` using `table1.field = table2.field` — this tells Access how the tables are connected.
- Any **extra filter conditions** go after the relationship condition, joined with `AND`.
- When the **same field name exists in more than one table**, always prefix it with the table name: `tblCompany.CompanyID`, not just `CompanyID`.

---

## Basic Syntax

```sql
SELECT table1.Field1, table2.Field2
FROM table1, table2
WHERE table1.LinkField = table2.LinkField
```

Replace `LinkField` with the actual primary key / foreign key pair that connects the two tables.

---

## Worked Example — Festivals Database

**Tables:**

`tblCompany`: CompanyID (PK), CompanyName, ContactPerson  
`tblActivity`: ActivityID (PK), CompanyID (FK), Activity, TicketsSold, Price

The two tables are linked by `CompanyID`. It is the primary key in `tblCompany` and the foreign key in `tblActivity`.

**Query:** Show the company name, activity, and tickets sold for every activity.

```sql
SELECT tblCompany.CompanyName, tblActivity.Activity, tblActivity.TicketsSold
FROM tblCompany, tblActivity
WHERE tblCompany.CompanyID = tblActivity.CompanyID
```

**Reading the query step by step:**

| Part | What it does |
|---|---|
| `SELECT tblCompany.CompanyName, tblActivity.Activity, tblActivity.TicketsSold` | Choose the columns to display, prefixed with their table names |
| `FROM tblCompany, tblActivity` | Tell Access both tables are needed |
| `WHERE tblCompany.CompanyID = tblActivity.CompanyID` | Define the link — only combine rows where the CompanyID matches across both tables |

---

## In Delphi

SQL is written as a string and assigned to `qryFestival.SQL.Text`. Open the query with `.Open` to run a SELECT.

```pascal
qryFestival.Close;
qryFestival.SQL.Clear;
qryFestival.SQL.Text := 'SELECT tblCompany.CompanyName, tblActivity.Activity, tblActivity.TicketsSold ' +
                        'FROM tblCompany, tblActivity ' +
                        'WHERE tblCompany.CompanyID = tblActivity.CompanyID';
qryFestival.Open;
```

> [!TIP]
> Each string segment in the concatenation must end with a **space before the closing quote**, or the keywords from different lines will run together (e.g. `...tblActivityWHERE...`).

---

## Adding Extra Filter Conditions

Place extra conditions **after** the relationship condition using `AND`. The relationship condition always comes first.

**Query:** Show the company name, activity, and tickets sold where fewer than 100 tickets were sold.

```sql
SELECT tblCompany.CompanyName, tblActivity.Activity, tblActivity.TicketsSold
FROM tblCompany, tblActivity
WHERE tblCompany.CompanyID = tblActivity.CompanyID
AND tblActivity.TicketsSold < 100
```

In Delphi:

```pascal
qryFestival.Close;
qryFestival.SQL.Clear;
qryFestival.SQL.Text := 'SELECT tblCompany.CompanyName, tblActivity.Activity, tblActivity.TicketsSold ' +
                        'FROM tblCompany, tblActivity ' +
                        'WHERE tblCompany.CompanyID = tblActivity.CompanyID ' +
                        'AND tblActivity.TicketsSold < 100';
qryFestival.Open;
```

---

## When to Prefix Field Names

**Rule:** If a field name appears in **only one** of the queried tables, the prefix is optional but strongly recommended. If the same field name appears in **more than one** table, the prefix is **required** — Access cannot tell which table you mean, and the query will fail with an ambiguous field error.

In the Festivals database, `CompanyID` exists in both `tblCompany` and `tblActivity`. You must always write `tblCompany.CompanyID` or `tblActivity.CompanyID` — never just `CompanyID`.

**Good habit:** prefix every field name in a multi-table query, regardless of whether it is ambiguous. This makes your intent clear and prevents errors when table structures change.

```sql
-- Correct — every field is prefixed
SELECT tblCompany.CompanyName, tblActivity.Activity
FROM tblCompany, tblActivity
WHERE tblCompany.CompanyID = tblActivity.CompanyID

-- Will cause an error — CompanyID is ambiguous
SELECT CompanyName, Activity
FROM tblCompany, tblActivity
WHERE CompanyID = CompanyID
```

---

## Three Tables

When three tables are involved, list all three in `FROM` and write **two** relationship conditions in `WHERE` chained with `AND`.

```sql
SELECT tblA.Field1, tblB.Field2, tblC.Field3
FROM tblA, tblB, tblC
WHERE tblA.ID = tblB.ID AND tblB.ID = tblC.ID
```

Each condition links one pair of adjacent tables. The pattern extends naturally: four tables would need three relationship conditions.

---

## With User Input

When the user types a value that will be included in the SQL string, store it in a variable and concatenate it in. For text fields, wrap the value in `QuotedStr()` to add the required single quotes around it.

**Query:** Ask the user for a company ID and show only that company's activities.

```pascal
var
  sCompany: string;
begin
  sCompany := InputBox('Company', 'Enter company ID', '');
  qryFestival.Close;
  qryFestival.SQL.Clear;
  qryFestival.SQL.Text := 'SELECT tblCompany.CompanyName, tblActivity.Activity ' +
                          'FROM tblCompany, tblActivity ' +
                          'WHERE tblCompany.CompanyID = tblActivity.CompanyID ' +
                          'AND tblCompany.CompanyID = ' + QuotedStr(sCompany);
  qryFestival.Open;
end;
```

`QuotedStr(sCompany)` wraps the value in single quotes, producing SQL like:

```sql
AND tblCompany.CompanyID = 'C001'
```

For numeric fields, do not use `QuotedStr` — concatenate the number directly:

```pascal
'AND tblActivity.TicketsSold < ' + IntToStr(nLimit)
```

---

## Common Mistakes

| Mistake | What happens | Fix |
|---|---|---|
| Forgetting the relationship condition in `WHERE` entirely | Access combines every row from table 1 with every row from table 2 — a **Cartesian product**. If `tblCompany` has 10 rows and `tblActivity` has 50, you get 500 rows of garbage. | Always include `WHERE table1.PK = table2.FK` |
| Omitting the table prefix when the field name exists in both tables | Access returns an "ambiguous field name" error and the query does not run | Prefix every field with its table name |
| Writing the extra filter condition **before** the relationship condition | The query may still run but is harder to read and can cause logic errors with complex conditions | Write the relationship condition first, then `AND` for each filter |
| Forgetting a space at the end of a string segment in Delphi | Keywords merge across lines: `...tblActivityWHERE...` — Access returns a syntax error | End each string segment with a space before the closing quote |
| Using a field from the wrong table | Results may be incorrect or the query may fail | Know which table owns each field; check the database design |

---

## Key Terms

| Term | Meaning |
|---|---|
| **Primary key (PK)** | A field that uniquely identifies each record in a table — e.g. `CompanyID` in `tblCompany` |
| **Foreign key (FK)** | A field in one table that stores the primary key value of a related record in another table — e.g. `CompanyID` in `tblActivity` |
| **Relationship condition** | The `WHERE` clause expression that links two tables: `tblCompany.CompanyID = tblActivity.CompanyID` |
| **Cartesian product** | The result when no relationship condition is given — every row from table 1 is combined with every row from table 2, producing meaningless data |
| **Ambiguous field name** | An error caused by using a field name that exists in more than one of the queried tables without specifying which table it belongs to |
| **QuotedStr()** | A Delphi function that wraps a string in single quotes so it can be embedded safely in a SQL string |

---

## Exam Focus

**1.** A database has two tables: `tblStudent` (StudentID PK, Surname, Grade) and `tblMark` (MarkID PK, StudentID FK, Subject, Mark). Write a SQL query to show the surname, subject, and mark for all students in Grade 12.

<details>
<summary>Show answer</summary>

```sql
SELECT tblStudent.Surname, tblMark.Subject, tblMark.Mark
FROM tblStudent, tblMark
WHERE tblStudent.StudentID = tblMark.StudentID
AND tblStudent.Grade = 12
```
</details>

---

**2.** Using the same tables, write the Delphi code to run the query above and display results in a `DBGrid` connected to `qryMarks`. Assume the query component is already linked to the database.

<details>
<summary>Show answer</summary>

```pascal
qryMarks.Close;
qryMarks.SQL.Clear;
qryMarks.SQL.Text := 'SELECT tblStudent.Surname, tblMark.Subject, tblMark.Mark ' +
                     'FROM tblStudent, tblMark ' +
                     'WHERE tblStudent.StudentID = tblMark.StudentID ' +
                     'AND tblStudent.Grade = 12';
qryMarks.Open;
```

The `DBGrid` updates automatically when the query is opened, provided its `DataSource` is linked to `qryMarks`.
</details>

---

**3.** A learner writes the following query. Identify the error and explain what result it would produce.

```sql
SELECT Surname, Subject, Mark
FROM tblStudent, tblMark
```

<details>
<summary>Show answer</summary>

Two errors: (1) The `WHERE` clause with the relationship condition is missing entirely, so Access produces a Cartesian product — every student row is combined with every mark row, producing a meaningless result with many duplicate rows. (2) If `StudentID` or any other field name exists in both tables, the query will also fail with an ambiguous field name error. The fix is to add `WHERE tblStudent.StudentID = tblMark.StudentID` and prefix all field names with their table names.
</details>

---

**4.** Write a SQL query that asks the user to type a subject name and then displays the surname and mark of every student who took that subject. Use `InputBox` and `QuotedStr` in your Delphi code.

<details>
<summary>Show answer</summary>

```pascal
var
  sSubject: string;
begin
  sSubject := InputBox('Subject', 'Enter subject name', '');
  qryMarks.Close;
  qryMarks.SQL.Clear;
  qryMarks.SQL.Text := 'SELECT tblStudent.Surname, tblMark.Mark ' +
                       'FROM tblStudent, tblMark ' +
                       'WHERE tblStudent.StudentID = tblMark.StudentID ' +
                       'AND tblMark.Subject = ' + QuotedStr(sSubject);
  qryMarks.Open;
end;
```
</details>

---

**5.** A database has three tables: `tblDepartment` (DeptID PK, DeptName), `tblEmployee` (EmpID PK, DeptID FK, EmpName), and `tblProject` (ProjID PK, EmpID FK, ProjectName). Write a SQL query to show the department name, employee name, and project name for all records.

<details>
<summary>Show answer</summary>

```sql
SELECT tblDepartment.DeptName, tblEmployee.EmpName, tblProject.ProjectName
FROM tblDepartment, tblEmployee, tblProject
WHERE tblDepartment.DeptID = tblEmployee.DeptID
AND tblEmployee.EmpID = tblProject.EmpID
```
</details>
