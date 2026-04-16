# Data Integrity

Storing data is only useful if the data is trustworthy. Data integrity is about ensuring that data remains accurate, consistent, and valid throughout its entire lifecycle — from the moment it's entered to when it's retrieved years later.

> [!NOTE] Grade 11–12
> Data integrity and validation are introduced in Grade 11. SQL injection as a threat is a Grade 12 extension.

---

## What is Data Integrity?

**Data integrity** means the data in a database is:
- **Accurate** — reflects reality
- **Consistent** — the same value in all related tables
- **Valid** — meets defined rules and constraints
- **Reliable** — can be trusted for decision-making

---

## Types of Data Integrity

| Type | What it ensures | How enforced |
|---|---|---|
| **Entity integrity** | Primary key is unique and not NULL | PK constraint |
| **Referential integrity** | Foreign key matches an existing PK | FK constraint |
| **Domain integrity** | Values match the field's data type and rules | Data type, validation rules |
| **User-defined integrity** | Custom business rules | CHECK constraints, triggers |

### Entity Integrity
Every table must have a primary key.  
The PK must be unique and cannot be NULL.

```sql
CREATE TABLE Students (
  StudentID INTEGER PRIMARY KEY,  -- enforces entity integrity
  FirstName TEXT NOT NULL
);
```

### Referential Integrity
A foreign key must reference an existing primary key.  
You cannot add a mark for a student who doesn't exist.

```sql
-- Cannot insert a Mark with a StudentID that doesn't exist in Student
INSERT INTO Marks (StudentID, Mark) VALUES (9999, 85);  -- ERROR if StudentID 9999 not in Student
```

**Cascade actions:**
| Action | Effect |
|---|---|
| CASCADE DELETE | Deleting a parent record also deletes related child records |
| RESTRICT | Prevents deletion of parent if child records exist |
| SET NULL | Sets FK to NULL when parent is deleted |

---

## Data Validation

**Validation** is the process of checking that data meets predefined rules before it is accepted.

> [!TIP] Validation vs Verification
> **Validation** — computer checks data meets rules (is the mark between 0 and 100?)  
> **Verification** — human or system confirms data was entered correctly (re-enter your password)

### Validation Types

| Type | Rule | Example | Error message |
|---|---|---|---|
| **Presence check** | Field cannot be empty | Name must not be blank | "Name is required" |
| **Type check** | Must match expected data type | Mark must be a number | "Enter a numeric value" |
| **Range check** | Must be within min–max | Mark: 0–100 | "Mark must be between 0 and 100" |
| **Length check** | Must meet min/max character count | ID: exactly 13 digits | "ID number must be 13 digits" |
| **Format check** | Must match a pattern | Email must contain @ and . | "Invalid email format" |
| **Lookup check** | Must match a value in a list | Province must be one of 9 SA provinces | "Select a valid province" |
| **Check digit** | Calculated digit validates the number | Barcode, SA ID last digit | "Invalid ID number" |
| **Cross-field check** | Relationship between two fields | End date must be after start date | "End date must be after start date" |

---

## Validation in Microsoft Access

**Input mask** — controls the format of data entry:
- `000-000-0000` — phone number format
- `>L<??????????` — capitalised first letter

**Validation rule** — expression that data must satisfy:
- `>= 0 And <= 100` — for a mark field
- `>= Date()` — for a future date
- `In ("Gauteng", "Western Cape", "KwaZulu-Natal")` — for a province

**Validation text** — error message shown when rule is violated:
- "Mark must be between 0 and 100"

**Required** — setting Yes means field cannot be left blank

---

## Data Security

**Data security** protects data from unauthorised access, corruption, or loss.

### User Accounts and Permissions

| Access Level | Rights |
|---|---|
| **Administrator / DBA** | Full access — read, write, delete, change structure |
| **Editor** | Read and write — can add and update data |
| **Viewer / Read-only** | Read only — cannot modify data |
| **No access** | Cannot view or modify data |

**Principle of least privilege:** users are given only the minimum access needed for their role.

### Password Policies
- Minimum length (8+ characters)
- Complexity (uppercase, lowercase, numbers, symbols)
- Expiry (force periodic password changes)
- No reuse of recent passwords
- Account lockout after failed attempts

### Audit Trail

An **audit trail** (audit log) records:
- Who accessed data
- When they accessed it
- What changes were made
- From which device/location

This allows detection of suspicious activity and reconstruction of events after a breach.

---

## Backup and Recovery

| Strategy | Description |
|---|---|
| **Full backup** | Complete copy of all data |
| **Incremental backup** | Only changes since last backup |
| **Differential backup** | Changes since last full backup |
| **Transaction log backup** | Record of every database transaction |

**Recovery point objective (RPO):** maximum acceptable data loss (how old can the backup be?)  
**Recovery time objective (RTO):** maximum acceptable downtime before systems must be restored

---

## SQL Injection

**SQL injection** is a cyberattack where malicious SQL code is inserted into a form input field, which is then executed by the database.

### How it works:

**Normal login query:**
```sql
SELECT * FROM Users WHERE Username = 'ayden' AND Password = 'mypassword'
```

**Attacker enters in the username field:** `ayden' OR '1'='1`

**Resulting query:**
```sql
SELECT * FROM Users WHERE Username = 'ayden' OR '1'='1' AND Password = ''
```

Since `'1'='1'` is always true, this returns all users — bypassing authentication entirely.

### What attackers can do:
- Bypass login authentication
- Read all data from the database
- Delete or corrupt data
- Execute admin operations

### Prevention:

| Measure | How it helps |
|---|---|
| **Parameterised queries** | Input treated as data, never as SQL code — most effective |
| **Input validation** | Reject unexpected characters (quotes, semicolons) |
| **Escaping special characters** | Neutralise dangerous characters before processing |
| **Least privilege** | Database account only has minimum necessary permissions |
| **Web Application Firewall (WAF)** | Detects and blocks malicious requests |
| **Error handling** | Don't display database error messages to users |

**Parameterised query example (PHP):**
```php
// Safe — parameter not interpreted as SQL
$stmt = $pdo->prepare("SELECT * FROM Users WHERE Username = ? AND Password = ?");
$stmt->execute([$username, $password]);
```

---

## Key Terms

| Term | Definition |
|---|---|
| **Data integrity** | Accuracy, consistency, and validity of data |
| **Entity integrity** | PK must be unique and not NULL |
| **Referential integrity** | FK must reference an existing PK |
| **Domain integrity** | Values must match data type and defined rules |
| **Validation** | Computer checks data meets rules before accepting |
| **Verification** | Confirming data was entered correctly |
| **Audit trail** | Log of who accessed/changed data and when |
| **SQL injection** | Attack inserting malicious SQL into a form input |
| **Parameterised query** | Query using placeholders — prevents SQL injection |
| **Least privilege** | Users given only minimum necessary access rights |
| **Check digit** | Calculated digit used to validate a number (e.g. barcode) |

---

## Exam Focus

> [!IMPORTANT] High-Frequency Questions
>
> 1. **"What is the difference between validation and verification?"** — Validation: computer checks data meets rules (range, type, format); Verification: confirming data was entered correctly (double entry, proofreading)
>
> 2. **"Give FOUR types of validation with examples"** — Presence check (name required); Range check (mark 0–100); Type check (mark must be integer); Format check (email must contain @); Length check (ID = 13 digits)
>
> 3. **"What is referential integrity?"** — Rule that a foreign key must reference an existing primary key in the related table — prevents orphan records
>
> 4. **"Explain SQL injection. How can it be prevented?"** — Attacker inserts malicious SQL into a form field; it executes against the database; prevent with parameterised queries, input validation, least privilege
>
> 5. **"What is an audit trail? Why is it important?"** — A log recording who accessed data, what changes were made, and when; important for detecting unauthorised access and investigating security incidents
