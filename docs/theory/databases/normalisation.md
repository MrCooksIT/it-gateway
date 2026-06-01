# Normalisation

A poorly designed database is a source of pain: duplicate data takes extra space and leads to inconsistency when you update one record but forget another. **Normalisation** is the systematic process of structuring a database to reduce redundancy and improve data integrity.

> [!NOTE] Grade 12
> Normalisation to 3NF is a Grade 12 topic and appears in almost every Paper 2 examination. You need to identify problems in a given table and demonstrate how to fix them.

---

## Why Normalise?

Consider this un-normalised table of student marks:

```
StudentID | StudentName | Subject1 | Mark1 | Subject2 | Mark2 | Teacher | TeacherEmail
1001      | Alice Adams | IT       | 87    | Maths    | 92    | Smith   | smith@school.co.za
1002      | Bob Botha   | IT       | 65    | Maths    | 71    | Smith   | smith@school.co.za
1003      | Carol Cole  | IT       | 78    | NULL     | NULL  | Smith   | smith@school.co.za
```

**Problems:**
- `Teacher` and `TeacherEmail` repeated for every student → update anomaly (change one, forget another)
- `Subject1`, `Mark1`, `Subject2`, `Mark2` in columns → can't add a third subject without redesigning
- `NULL` values where Carol has no second subject

<div class="itg-norm-compare">
<div class="itg-norm-box">
<div class="itg-norm-hdr bad">✗ Un-normalised — problems highlighted</div>
<table class="itg-norm-table">
<thead><tr><th>StudentID</th><th>StudentName</th><th>Subject1</th><th>Mark1</th><th>Teacher</th><th>TeacherEmail</th></tr></thead>
<tbody>
<tr><td>1001</td><td>Alice</td><td>IT</td><td>87</td><td class="dup">Smith</td><td class="dup">smith@school.co.za</td></tr>
<tr><td>1002</td><td>Bob</td><td>IT</td><td>65</td><td class="dup">Smith</td><td class="dup">smith@school.co.za</td></tr>
<tr><td>1003</td><td>Carol</td><td>IT</td><td>78</td><td class="dup">Smith</td><td class="dup">smith@school.co.za</td></tr>
</tbody>
</table>
</div>
<div class="itg-norm-box">
<div class="itg-norm-hdr good">✓ After normalisation — each fact stored once</div>
<table class="itg-norm-table">
<thead><tr><th>STUDENT</th><th></th><th>MARK</th><th></th><th>TEACHER</th></tr></thead>
<tbody>
<tr><td class="fixed">StudentID</td><td></td><td class="fixed">MarkID</td><td></td><td class="fixed">TeacherID</td></tr>
<tr><td class="fixed">StudentName</td><td></td><td class="fixed">Subject</td><td></td><td class="fixed">TeacherName</td></tr>
<tr><td></td><td></td><td class="fixed">Mark</td><td></td><td class="fixed">TeacherEmail</td></tr>
<tr><td></td><td></td><td class="fixed">StudentID (FK)</td><td></td><td></td></tr>
</tbody>
</table>
</div>
</div>

Normalisation fixes all of these.

---

## The Normal Forms

| Normal Form | Requirement |
|---|---|
| **1NF** | Atomic values; no repeating groups; primary key defined |
| **2NF** | 1NF + no partial dependencies (all non-key fields depend on the WHOLE PK) |
| **3NF** | 2NF + no transitive dependencies (non-key fields depend only on the PK, not on each other) |

---

## First Normal Form (1NF)

**Rule:** A table is in 1NF if:
1. All values are **atomic** (single value per cell — no lists or multiple values)
2. There are **no repeating groups** (no Subject1, Subject2, Subject3 column patterns)
3. A **primary key** is defined

### Problem Example

**Not in 1NF:**

| StudentID | Name | Subjects (list) |
|---|---|---|
| 1001 | Alice | IT, Maths |
| 1002 | Bob | Maths |

Problems: `Subjects` contains multiple values (not atomic); there are implied repeating groups.

**Fixed to 1NF:**

| StudentID | Name | Subject |
|---|---|---|
| 1001 | Alice | IT |
| 1001 | Alice | Maths |
| 1002 | Bob | Maths |

Now `(StudentID, Subject)` forms a composite primary key.

But we still have a problem: `Name` repeats for every subject Alice takes → leads to 2NF issue.

---

## Second Normal Form (2NF)

**Rule:** A table is in 2NF if:
1. It is in 1NF, AND
2. Every non-key attribute depends on the **entire** primary key (no partial dependency)

A **partial dependency** occurs when a non-key column depends on only PART of a composite primary key.

### Problem Example

**In 1NF but NOT 2NF:**

Table: `StudentSubjects` — PK is `(StudentID, SubjectID)`

| StudentID | SubjectID | StudentName | SubjectName | Mark |
|---|---|---|---|---|
| 1001 | S01 | Alice | IT | 87 |
| 1001 | S02 | Alice | Maths | 92 |
| 1002 | S01 | Bob | IT | 65 |

**Partial dependencies:**
- `StudentName` depends on `StudentID` alone (not the whole PK)
- `SubjectName` depends on `SubjectID` alone (not the whole PK)
- Only `Mark` depends on the full `(StudentID, SubjectID)` combination

**Fixed to 2NF:** Split into three tables:

<div class="itg-norm-compare">
<div class="itg-norm-box">
<div class="itg-norm-hdr bad">✗ Partial dependencies (NOT 2NF)</div>
<table class="itg-norm-table">
<thead><tr><th>StudentID + SubjectID (PK)</th><th>StudentName</th><th>SubjectName</th><th>Mark</th></tr></thead>
<tbody>
<tr><td>1001 + S01</td><td class="dup">Alice ← depends on StudentID only</td><td class="dup">IT ← depends on SubjectID only</td><td>87</td></tr>
<tr><td>1001 + S02</td><td class="dup">Alice</td><td class="dup">Maths</td><td>92</td></tr>
<tr><td>1002 + S01</td><td class="dup">Bob</td><td class="dup">IT</td><td>65</td></tr>
</tbody>
</table>
</div>
<div class="itg-norm-box">
<div class="itg-norm-hdr good">✓ 2NF — each field depends on its whole PK</div>
<table class="itg-norm-table">
<thead><tr><th>STUDENTS</th><th>SUBJECTS</th><th>MARKS</th></tr></thead>
<tbody>
<tr><td class="fixed">StudentID (PK)</td><td class="fixed">SubjectID (PK)</td><td class="fixed">StudentID (PK,FK)</td></tr>
<tr><td class="fixed">StudentName</td><td class="fixed">SubjectName</td><td class="fixed">SubjectID (PK,FK)</td></tr>
<tr><td></td><td></td><td class="fixed">Mark</td></tr>
</tbody>
</table>
</div>
</div>

Now every non-key field in each table depends on the WHOLE primary key.

---

## Third Normal Form (3NF)

**Rule:** A table is in 3NF if:
1. It is in 2NF, AND
2. There are **no transitive dependencies** — non-key columns do not depend on other non-key columns

A **transitive dependency** occurs when: **Non-key A → Non-key B** (B depends on A, not directly on the PK).

### Problem Example

**In 2NF but NOT 3NF:**

| StudentID | Name | PostalCode | City | Province |
|---|---|---|---|---|
| 1001 | Alice | 7700 | Stellenbosch | Western Cape |
| 1002 | Bob | 7700 | Stellenbosch | Western Cape |
| 1003 | Carol | 8000 | Cape Town | Western Cape |

PK = `StudentID`

**Transitive dependency:**
- `StudentID → PostalCode` (PostalCode depends on PK ✓)
- BUT `PostalCode → City → Province` (City and Province depend on PostalCode, not the PK directly ✗)

If Stellenbosch's postal code changes, you must update multiple rows.

**Fixed to 3NF:** Split:

<div class="itg-norm-compare">
<div class="itg-norm-box">
<div class="itg-norm-hdr bad">✗ Transitive dependency (NOT 3NF)</div>
<table class="itg-norm-table">
<thead><tr><th>StudentID (PK)</th><th>Name</th><th>PostalCode</th><th>City</th><th>Province</th></tr></thead>
<tbody>
<tr><td>1001</td><td>Alice</td><td>7700</td><td class="dup">Stellenbosch</td><td class="dup">Western Cape</td></tr>
<tr><td>1002</td><td>Bob</td><td>7700</td><td class="dup">Stellenbosch</td><td class="dup">Western Cape</td></tr>
<tr><td>1003</td><td>Carol</td><td>8000</td><td class="dup">Cape Town</td><td class="dup">Western Cape</td></tr>
</tbody>
</table>
<p style="font-size:0.7rem;padding:0.4rem 0.5rem;color:var(--vp-c-text-2)">City &amp; Province depend on PostalCode, not StudentID directly</p>
</div>
<div class="itg-norm-box">
<div class="itg-norm-hdr good">✓ 3NF — each table stores one topic</div>
<table class="itg-norm-table">
<thead><tr><th>STUDENTS</th><th>POSTCODES</th></tr></thead>
<tbody>
<tr><td class="fixed">StudentID (PK)</td><td class="fixed">PostalCode (PK)</td></tr>
<tr><td class="fixed">Name</td><td class="fixed">City</td></tr>
<tr><td class="fixed">PostalCode (FK)</td><td class="fixed">Province</td></tr>
</tbody>
</table>
<p style="font-size:0.7rem;padding:0.4rem 0.5rem;color:var(--vp-c-text-2)">Change a city name once in POSTCODES — all students update automatically</p>
</div>
</div>

---

## Full Normalisation Example

**Start: Un-normalised**

| OrderID | CustomerName | CustomerEmail | ProductID | ProductName | UnitPrice | Quantity | Total |
|---|---|---|---|---|---|---|---|
| 1 | Alice | alice@mail.com | P01 | Laptop | 12000 | 2 | 24000 |
| 2 | Bob | bob@mail.com | P02 | Mouse | 200 | 5 | 1000 |
| 3 | Alice | alice@mail.com | P01 | Laptop | 12000 | 1 | 12000 |

**Problems:**
- CustomerName and Email repeat
- ProductName and UnitPrice repeat
- Total is calculated (derived) — unnecessary to store
- No repeating groups in rows, but data is not separated by entity

---

**After 1NF** — already in 1NF (all cells atomic, one value per cell). PK could be `(OrderID, ProductID)`.

**After 2NF** — remove partial dependencies:

```
Customers (CustomerID PK, CustomerName, CustomerEmail)
Products  (ProductID PK, ProductName, UnitPrice)
Orders    (OrderID PK, CustomerID FK, OrderDate)
OrderLines(OrderID FK, ProductID FK, Quantity)
           PK: (OrderID, ProductID)
```

**After 3NF** — check for transitive dependencies. In the 2NF version above, all non-key fields depend directly on their table's PK. We're in 3NF.

---

## Identifying Normal Form Problems — Exam Strategy

When given a table and asked to identify problems:

1. **Check 1NF**: Any multi-value cells? Any repeating column groups (Name1, Name2, Name3)?
2. **Check 2NF**: Is the PK composite? If yes, does any non-key column depend on only PART of the PK?
3. **Check 3NF**: Does any non-key column depend on another non-key column (not directly on the PK)?

When asked to convert to a normal form:
- **To fix 1NF**: Remove multi-value columns; create a new row for each value
- **To fix 2NF**: Split the table; move partially-dependent fields to a new table with their determinant as PK
- **To fix 3NF**: Split the table; move transitively-dependent fields to a new table with their determinant as PK

---

## Anomalies (Why Normalise?)

Un-normalised tables cause three types of anomalies:

| Anomaly | Description | Example |
|---|---|---|
| **Update anomaly** | Changing data requires updating multiple rows | Teacher changes email → must update every student row |
| **Insertion anomaly** | Can't insert new data without unrelated data | Can't add a new subject unless a student is enrolled |
| **Deletion anomaly** | Deleting one piece of data deletes unrelated data | Deleting a student's record also loses teacher info |

---

## Key Terms

| Term | Definition |
|---|---|
| **Normalisation** | Process of structuring a database to reduce redundancy |
| **Normal form** | A level of normalisation with specific rules |
| **1NF** | Atomic values, no repeating groups, primary key defined |
| **2NF** | 1NF + no partial dependencies |
| **3NF** | 2NF + no transitive dependencies |
| **Redundancy** | Storing the same data in multiple places |
| **Partial dependency** | Non-key field depends on part of a composite PK |
| **Transitive dependency** | Non-key field depends on another non-key field |
| **Update anomaly** | Inconsistency caused by updating data in only some rows |
| **Insertion anomaly** | Unable to insert data without adding unrelated data |
| **Deletion anomaly** | Deleting one record accidentally removes other data |

---

## Exam Focus

> [!IMPORTANT] High-Frequency Questions
>
> 1. **"Identify TWO problems with this table design"** — look for repeating groups, repeated data (redundancy), partial dependencies, transitive dependencies
>
> 2. **"The table is not in 2NF. Explain why and show the tables in 2NF"** — must identify the partial dependency and demonstrate the split
>
> 3. **"Explain what a transitive dependency is. Give an example."** — non-key column depending on another non-key column; example: PostalCode → City (city depends on postal code, not directly on StudentID)
>
> 4. **"What is a update anomaly? How does normalisation solve it?"** — having to update the same data in multiple rows; normalisation stores data once (in its own table), so one update is sufficient
>
> 5. **"Convert this table to 3NF. Show all tables with their primary keys and foreign keys."** — show the final structure: each entity in its own table, PKs and FKs clearly indicated
