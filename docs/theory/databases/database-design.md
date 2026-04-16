# Database Design

A well-designed database stores data efficiently, without redundancy, and makes it easy to retrieve exactly what you need. Poor design leads to duplicate data, inconsistencies, and queries that return wrong results. Getting the design right before writing a single line of SQL is essential.

> [!NOTE] Grade 11
> Database design (ERDs, entities, relationships, keys) is a Grade 11 topic. Normalisation (the formal design process) is covered at Grade 12.

---

## Database Design Process

```
Requirements analysis → Conceptual design (ERD) → Logical design (tables, keys) → Physical design (create tables in DBMS) → Implementation → Testing
```

1. **Identify entities** — what "things" does the database need to store?
2. **Identify attributes** — what properties does each entity have?
3. **Identify relationships** — how do entities relate to each other?
4. **Draw ERD** — visual representation of the design
5. **Map to tables** — convert ERD to actual tables with primary and foreign keys
6. **Normalise** — apply normalisation rules to eliminate redundancy

---

## Entities and Attributes

**Entity** — a real-world object or concept about which we store data  
**Attribute** — a property or characteristic of an entity  
**Instance** — one specific occurrence of an entity (one row in a table)

| Entity | Attributes |
|---|---|
| **Student** | StudentID, FirstName, Surname, DateOfBirth, Grade |
| **Subject** | SubjectCode, SubjectName, Department |
| **Teacher** | TeacherID, FirstName, Surname, Email |
| **Mark** | MarkID, Mark, Date, StudentID (FK), SubjectCode (FK) |

---

## Entity-Relationship Diagrams (ERDs)

An **ERD** is a visual diagram showing entities, their attributes, and how they relate to each other.

### ERD Notation

```
┌─────────────┐         ┌─────────────┐
│   STUDENT   │────────>│    MARK     │
│             │  1:M    │             │
│ StudentID   │         │ MarkID (PK) │
│ FirstName   │         │ Mark        │
│ Surname     │         │ Date        │
│ Grade       │         │ StudentID   │
└─────────────┘         └─────────────┘
```

**Crow's foot notation** (used in professional ERDs):

| Symbol | Meaning |
|---|---|
| Single line `─` | One |
| Double line `═` | One and only one |
| Crow's foot `<` | Many |
| Circle `○` | Zero or one |

---

## Relationships

### One-to-One (1:1)
Each record in table A relates to exactly one record in table B.

**Example:** One Student ↔ One Locker  
```
Student ──── Locker
```
Relatively rare in databases — often combined into one table.

### One-to-Many (1:M) ← Most common
Each record in table A relates to many records in table B; each record in B relates to one record in A.

**Example:** One Student → Many Marks; One Teacher → Many Classes  
```
Student ──<< Mark
```
Implemented with a **foreign key** in the "many" table.

### Many-to-Many (M:M)
Each record in A relates to many in B, and vice versa.

**Example:** Students enrol in many Subjects; Subjects have many Students  
```
Student >>──<< Subject
```

**Cannot be implemented directly** — requires a **junction table (linking table)**:

```
STUDENT          ENROLMENT           SUBJECT
StudentID ──── StudentID (FK)    SubjectCode (FK) ──── SubjectCode
               SubjectCode (FK)
               EnrolmentDate
```

The junction table holds both foreign keys (which together form a composite primary key).

---

## Primary Keys

A **primary key (PK)** uniquely identifies each record in a table.

**Requirements:**
- Must be **unique** — no two records share the same PK value
- Must be **not NULL** — cannot be empty
- Must be **stable** — should not change over time
- Should be **simple** — ideally a single field

**Types of primary keys:**

| Type | Description | Example |
|---|---|---|
| **Natural key** | An existing attribute that is naturally unique | SA ID Number, Email address |
| **Surrogate key** | An artificial unique identifier added to the table | Auto-number (1001, 1002, 1003...) |
| **Composite key** | Two or more fields combined to form a unique identifier | StudentID + SubjectCode in a junction table |

**Why surrogate keys are preferred:**
- Natural keys can change (email addresses change)
- Natural keys can be long (SA ID is 13 digits)
- Surrogate keys are simple integers — fast to join and index

---

## Foreign Keys

A **foreign key (FK)** is a field in one table that references the primary key of another table.

```
STUDENT table:    StudentID (PK) | FirstName | Surname
MARK table:       MarkID (PK) | Mark | Date | StudentID (FK → Student.StudentID)
```

**Rules:**
- FK value must exist as a PK in the referenced table (**referential integrity**)
- FK can be NULL (if the relationship is optional)
- Multiple FKs can exist in one table

---

## Worked Example: School Database ERD

**Scenario:** A school needs to track students, subjects, teachers, and marks.

**Entities identified:**
- Student
- Subject
- Teacher
- Enrolment (junction: Student ↔ Subject)
- Mark

**ERD:**
```
TEACHER                     SUBJECT
TeacherID (PK)──────1:M──>SubjectCode (PK)
FirstName                  SubjectName
Surname                    TeacherID (FK)
Email
                               |
                              1:M (via junction)
                               |
STUDENT ────M:M──── ENROLMENT ──────> MARK
StudentID (PK)      StudentID (FK)     MarkID (PK)
FirstName           SubjectCode (FK)   Mark
Surname             EnrolmentDate      Date
Grade                                  StudentID (FK)
                                       SubjectCode (FK)
```

**Tables:**

| STUDENT | | SUBJECT | | ENROLMENT | | MARK |
|---|---|---|---|---|---|---|
| StudentID (PK) | | SubjectCode (PK) | | StudentID (PK, FK) | | MarkID (PK) |
| FirstName | | SubjectName | | SubjectCode (PK, FK) | | Mark |
| Surname | | TeacherID (FK) | | EnrolmentDate | | Date |
| Grade | | | | | | StudentID (FK) |
| | | | | | | SubjectCode (FK) |

---

## Data Dictionary

A **data dictionary** documents every field in every table:

| Field | Table | Data Type | Size | Constraints | Description |
|---|---|---|---|---|---|
| StudentID | Student | AutoNumber | | PK, Not Null | Unique student identifier |
| FirstName | Student | Text | 50 | Not Null | Student's first name |
| Grade | Student | Integer | | 10–12 | Current grade level |
| Mark | Mark | Integer | | 0–100 | Assessment mark |
| Date | Mark | Date | | Not Null | Date assessment written |

---

## Key Terms

| Term | Definition |
|---|---|
| **Entity** | Real-world object about which data is stored |
| **Attribute** | Property of an entity |
| **ERD** | Entity-Relationship Diagram — visual database design |
| **Primary key** | Field(s) uniquely identifying each record |
| **Foreign key** | Field referencing the PK of another table |
| **Junction table** | Table resolving a many-to-many relationship |
| **Composite key** | Primary key made up of two or more fields |
| **Surrogate key** | Artificial PK (auto-number) not derived from data |
| **Natural key** | PK from existing real-world data |
| **Data dictionary** | Documentation of every field in the database |
| **Referential integrity** | Rule that FK values must match existing PK values |

---

## Exam Focus

> [!IMPORTANT] High-Frequency Questions
>
> 1. **"What is an entity? Give an example."** — A real-world object about which data is stored; example: Student, Teacher, Product, Order
>
> 2. **"What is the difference between a primary key and a foreign key?"** — PK uniquely identifies each record in its own table; FK references the PK of another table to establish a link
>
> 3. **"How is a many-to-many relationship implemented in a relational database?"** — Using a junction (linking) table that contains the foreign keys of both related tables
>
> 4. **"Give TWO requirements for a primary key"** — Must be unique (no two records have the same value); must not be NULL; must be stable (not change over time)
>
> 5. **"A student can take many subjects and a subject can have many students. What type of relationship is this? How would you implement it?"** — Many-to-many; implement using a junction table (e.g. Enrolment) with StudentID and SubjectCode as foreign keys
