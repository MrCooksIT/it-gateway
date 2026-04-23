# Database Concepts

A spreadsheet stores data in rows and columns — so does a database. But a database goes further: it enforces rules, prevents duplicates, links related data across multiple tables, and lets you query millions of records in milliseconds. Understanding database concepts is essential for both Paper 1 (SQL) and Paper 2 (theory).

> [!NOTE] Grade 11+
> Database concepts are introduced in Grade 11. Normalisation and complex queries extend into Grade 12.

---

## Data vs Information vs Knowledge

| | Data | Information | Knowledge |
|---|---|---|---|
| **Definition** | Raw, unprocessed facts | Data processed into meaningful context | Information understood and applied |
| **Example** | `87`, `Finn`, `2024-03-15` | "Finn scored 87% on the March 2024 test" | "Finn consistently scores high in programming — recommend advanced class" |
| **Useful?** | Not on its own | Yes | Actionable |

---

## What is a Database?

A **database** is an organised collection of related data stored so it can be easily accessed, managed, and updated.

A **Database Management System (DBMS)** is the software that manages the database — it handles storing, retrieving, querying, and securing data.

**Examples of DBMS software:**

| DBMS | Type | Use |
|---|---|---|
| Microsoft Access | Desktop DBMS | Small databases, learning, small businesses |
| MySQL | Server DBMS (free, open source) | Websites, web apps |
| PostgreSQL | Server DBMS (free, open source) | Enterprise applications |
| Microsoft SQL Server | Enterprise DBMS | Large organisations, Microsoft ecosystem |
| Oracle | Enterprise DBMS | Banking, large corporations |
| SQLite | Embedded DBMS | Mobile apps, local storage |

---

## Database Terminology

| Term | Definition | Example |
|---|---|---|
| **Table (Relation)** | A grid of rows and columns storing data about one entity | `Students` table |
| **Field (Column / Attribute)** | A single category of data | `Surname`, `Mark`, `Grade` |
| **Record (Row / Tuple)** | One complete set of related field values | One student's data |
| **Primary Key (PK)** | A field that uniquely identifies each record — no duplicates, no NULL | `StudentID` |
| **Foreign Key (FK)** | A field in one table that references the PK of another table — creates a link | `SubjectID` in `Marks` table, referencing `Subjects` table |
| **Data type** | Specifies what kind of data a field holds | Integer, Text, Date, Boolean |

**Visualising the terms:**

```
Table: Students
┌──────────────┬──────────┬───────────┬───────┬──────┐
│  StudentID   │ Surname  │ FirstName │ Grade │ Mark │  ← Fields (columns)
├──────────────┼──────────┼───────────┼───────┼──────┤
│    1001      │  Adams   │   Alice   │  11   │  87  │  ← Record (row)
│    1002      │  Botha   │    Ben    │  11   │  72  │
│    1003      │ Coetzee  │  Carol    │  12   │  91  │
└──────────────┴──────────┴───────────┴───────┴──────┘
      ↑
  Primary Key (unique)
```

---

## Primary Key (PK)

A **primary key** is a field (or combination of fields) that:
- **Uniquely identifies** each record
- **Cannot be NULL** (empty)
- **Cannot be duplicated** — no two records can have the same PK value

**Examples of good PKs:**
- `StudentID` (auto-generated number)
- `IDNumber` (SA 13-digit ID — unique per person)
- `ISBN` (book identifier)
- `VehicleRegistration` (unique per vehicle)

**Natural vs Surrogate Keys:**
- **Natural key**: A field that exists naturally and is inherently unique (ID number, ISBN)
- **Surrogate key**: An artificial ID created specifically to be the PK (auto-increment integer like `StudentID = 1001`)

> [!TIP] When in Doubt, Use Surrogate Keys
> Auto-increment integers are reliable PKs. Natural keys can have exceptions (a person can change their ID number, a product barcode can be reprinted). Surrogate keys never change.

---

## Foreign Key (FK) — Linking Tables

A **foreign key** is a field in one table that holds the primary key value from another table. This is how relational databases **link** related data without storing duplicates.

**Example:**

```
Table: Students           Table: Marks
┌──────────┬─────────┐    ┌──────────┬───────────┬──────┐
│StudentID │ Surname │    │MarkID    │ StudentID │ Mark │
├──────────┼─────────┤    ├──────────┼───────────┼──────┤
│ 1001     │ Adams   │    │ 1        │ 1001      │  87  │
│ 1002     │ Botha   │    │ 2        │ 1001      │  92  │
└──────────┴─────────┘    │ 3        │ 1002      │  75  │
                          └──────────┴───────────┴──────┘
```

`Marks.StudentID` is a **foreign key** referencing `Students.StudentID`. This link lets you combine data from both tables in a query (using JOIN).

---

## Relationships Between Tables

| Relationship | Meaning | Example |
|---|---|---|
| **One-to-One (1:1)** | One record in A matches exactly one record in B | One student has one locker |
| **One-to-Many (1:M)** | One record in A matches many records in B | One student has many marks |
| **Many-to-Many (M:M)** | Many records in A match many in B | Students enrolled in many subjects; subjects have many students |

> [!NOTE] Many-to-Many Requires a Junction Table
> You cannot directly implement M:M in a relational database. You need a **junction table** (also called a bridge or linking table) that holds the FKs from both sides.

**Example: Students ↔ Subjects (many-to-many)**
```
Students table  →  Enrolment table  →  Subjects table
(StudentID PK)     (StudentID FK,      (SubjectID PK)
                    SubjectID FK)
```

---

## Data Integrity

**Data integrity** means the data is accurate, consistent, and valid. A good DBMS enforces integrity automatically.

| Type | What it enforces | Example |
|---|---|---|
| **Entity integrity** | PK is unique and not NULL | No two students with same StudentID |
| **Referential integrity** | FK must match an existing PK | Can't assign a mark to a non-existent student |
| **Domain integrity** | Values must match the field's data type and rules | Mark must be 0–100 (Integer); not "eighty" |
| **User-defined integrity** | Custom business rules | Grade must be 10, 11, or 12 |

---

## Data Validation vs Verification

| | Validation | Verification |
|---|---|---|
| **Definition** | Checking that data matches predefined rules | Checking that data was entered correctly (matches the source) |
| **Who does it?** | The computer/DBMS | The human or a double-entry system |
| **Catches** | Wrong type, out of range, wrong format | Transcription errors (user typed wrong thing) |
| **Examples** | Mark must be 0–100; Date must be valid | Enter password twice; print receipt for user to check |

### Validation Types

| Type | Description | Example |
|---|---|---|
| **Presence check** | Field cannot be left empty | Surname must be filled in |
| **Type check** | Data must be the correct data type | Mark must be Integer, not Text |
| **Range check** | Value must be within min–max | Mark: 0 ≤ mark ≤ 100 |
| **Length check** | String must be within min/max length | ID number must be exactly 13 digits |
| **Format check** | Data must match a pattern | Email must contain @ and . |
| **Lookup check** | Value must match a value in a list | Province must be one of 9 provinces |
| **Check digit** | Calculated digit validates the whole number | Barcode last digit, ISBN last digit |
| **Consistency check** | Two fields must be logically consistent | End date must be after start date |

---

## Database Advantages over Spreadsheets

| Feature | Spreadsheet | Database |
|---|---|---|
| Duplicate control | Manual | Automatic (PK constraint) |
| Multi-user access | Difficult (file locking) | Designed for it |
| Data relationships | No built-in links | Enforced via FK |
| Querying | Limited | Powerful SQL |
| Security | File-level | Field/record/user-level |
| Data volume | Millions of rows (practical limit) | Billions of records |
| Data integrity | No enforcement | Enforced by DBMS |

---

## Key Terms

| Term | Definition |
|---|---|
| **DBMS** | Database Management System — software managing the database |
| **Table** | Grid of rows and columns for one entity |
| **Field** | One column/attribute in a table |
| **Record** | One row of data in a table |
| **Primary key** | Field uniquely identifying each record |
| **Foreign key** | Field referencing the PK of another table |
| **Relationship** | Link between tables via PK-FK |
| **Data integrity** | Accuracy and consistency of data |
| **Validation** | Automatic rule-checking by the system |
| **Verification** | Human-check that data was entered correctly |
| **Entity integrity** | No NULL or duplicate PKs |
| **Referential integrity** | FK must reference an existing PK |
| **Junction table** | Bridge table implementing M:M relationships |

---

## Exam Focus

> [!IMPORTANT] High-Frequency Questions
>
> 1. **"What is a primary key? Give an example."** — unique, not null, identifies each record; `StudentID`
>
> 2. **"What is a foreign key and what is its purpose?"** — field referencing another table's PK; creates a relationship between tables
>
> 3. **"Give THREE types of validation and explain each"** — presence, range, type, length, format — always explain what the rule checks
>
> 4. **"Explain the difference between validation and verification"** — validation = system checks rules; verification = human confirms correct data entry
>
> 5. **"Give ONE advantage of a database over a spreadsheet"** — referential integrity, multi-user access, better querying, automatic duplicate prevention
