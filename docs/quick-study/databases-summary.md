# Databases — Quick Summary

No prose. Tables and key facts for Data & Information Management.

---

## Terminology

| Term | Definition |
|---|---|
| Table | Grid of rows and columns for one entity |
| Field | Column — one attribute (e.g. Surname) |
| Record | Row — one complete set of data |
| Primary Key (PK) | Unique, not NULL, identifies each record |
| Foreign Key (FK) | References PK in another table |
| DBMS | Software managing the database (Access, MySQL) |

---

## Relationships

| Type | Symbol | Example |
|---|---|---|
| One-to-One | 1:1 | One student ↔ One locker |
| One-to-Many | 1:M | One student → Many marks |
| Many-to-Many | M:M | Students ↔ Subjects (needs junction table) |

---

## Data Integrity Types

| Type | What it enforces |
|---|---|
| Entity integrity | PK must be unique and not NULL |
| Referential integrity | FK must reference existing PK |
| Domain integrity | Values match data type and rules |
| User-defined | Custom business rules |

---

## Validation Types

| Type | Rule | Example |
|---|---|---|
| Presence | Cannot be empty | Name required |
| Type | Correct data type | Mark must be Integer |
| Range | Within min–max | Mark: 0–100 |
| Length | Min/max characters | ID: exactly 13 digits |
| Format | Matches pattern | Email must contain @ |
| Lookup | Must be in a list | Province in list of 9 |
| Check digit | Calculated digit validates number | Barcode last digit |

---

## Validation vs Verification

| | Validation | Verification |
|---|---|---|
| Who | Computer/DBMS | Human or system |
| Catches | Wrong type/range/format | Transcription errors |
| Example | Range check 0–100 | Enter password twice |

---

## Normalisation

| Normal Form | Rule |
|---|---|
| 1NF | Atomic values; no repeating groups; PK defined |
| 2NF | 1NF + no partial dependencies (non-key depends on WHOLE PK) |
| 3NF | 2NF + no transitive dependencies (non-key depends only on PK) |

### Anomalies (why normalise)

| Anomaly | Problem |
|---|---|
| Update | Must change same data in multiple rows |
| Insertion | Can't add data without unrelated data |
| Deletion | Deleting one record removes other data |

### Partial dependency
Non-key field depends on PART of a composite PK.  
**Fix:** move it to its own table with its determinant as PK.

### Transitive dependency
Non-key field depends on another non-key field.  
**Fix:** move it to its own table.

---

## SQL Quick Reference

### Clause order (mandatory)
```sql
SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY
```

### Filtering
```sql
WHERE Mark >= 50 AND Grade = 11
WHERE Surname LIKE 'C%'
WHERE Mark BETWEEN 60 AND 79
WHERE Grade IN (10, 11, 12)
WHERE Email IS NULL
```

### Aggregate
```sql
SELECT COUNT(*), SUM(Mark), AVG(Mark), MAX(Mark), MIN(Mark)
FROM Learners
GROUP BY Grade
HAVING AVG(Mark) > 60
```

### Join
```sql
SELECT s.Surname, m.Mark
FROM Students AS s
INNER JOIN Marks AS m ON s.StudentID = m.StudentID
WHERE m.Mark >= 50
```

### Modifying data
```sql
INSERT INTO Table (col1, col2) VALUES ('Smith', 87)
UPDATE Table SET Mark = Mark + 5 WHERE Grade = 11
DELETE FROM Table WHERE Mark IS NULL
```

---

## Common SQL Mistakes

- String values need `'quotes'`; numbers don't
- `HAVING` filters groups (after GROUP BY); `WHERE` filters rows (before)
- `IS NULL` not `= NULL`
- JOIN condition: `ON t1.PK = t2.FK`
- Clause order is mandatory — wrong order = syntax error
