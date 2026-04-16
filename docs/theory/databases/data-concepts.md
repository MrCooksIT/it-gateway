# Data Concepts

Before a database can be designed, we need to understand what data actually is — and why "data" and "information" are not the same thing. The quality of data determines the quality of every decision made from it.

> [!NOTE] Grade 10–11
> Data vs information vs knowledge is introduced in Grade 10. Data quality characteristics and data types are extended in Grade 11.

---

## Data vs Information vs Knowledge

| Concept | Definition | Example |
|---|---|---|
| **Data** | Raw, unprocessed facts — no context or meaning | `85`, `2024-03-15`, `Ayden` |
| **Information** | Data that has been processed, organised, and given context | "Ayden scored 85% on the March 2024 test" |
| **Knowledge** | Information applied with understanding and experience | "Ayden is performing well and likely to pass; a 90%+ target is achievable" |

```
Data → [Process] → Information → [Apply experience] → Knowledge
```

**Why the difference matters:**
- A database stores **data**
- Reports and dashboards present **information**
- Decisions require **knowledge**

---

## Characteristics of Quality Data

For data to be useful, it must be:

| Characteristic | Meaning | Bad Example | Good Example |
|---|---|---|---|
| **Accurate** | Correct and error-free | Date of birth: 30 Feb | Date of birth: 28 Feb |
| **Complete** | All required fields filled | Missing phone number | All contact details present |
| **Consistent** | Same format throughout | "012 555 1234" / "0125551234" mixed | All numbers formatted the same |
| **Relevant** | Appropriate for the purpose | Storing shoe size in a school database | Only collecting educationally relevant data |
| **Timely** | Up to date | Using a 5-year-old address | Updated address at last visit |
| **Valid** | Within acceptable range/format | Mark: 150 | Mark: 85 |
| **Unique** | No duplicate records | Same student entered twice | Each student appears once |

---

## Data Types

Every field in a database stores a specific type of data:

| Data Type | Description | Examples |
|---|---|---|
| **Text / String** | Characters — letters, numbers, symbols | Name, email address, suburb |
| **Integer** | Whole numbers | Age, quantity, grade level |
| **Real / Float** | Numbers with decimals | Mark as percentage, price |
| **Boolean** | True/False only | Paid: Yes/No, Active: True/False |
| **Date** | Calendar date | Date of birth: 2008-05-15 |
| **Time** | Time of day | Arrival time: 08:30 |
| **Date/Time** | Combined date and time | Transaction: 2024-03-15 14:32:05 |
| **Currency** | Monetary value (formatted) | Price: R299.99 |
| **Auto-number** | Automatically incremented integer | StudentID: 1001, 1002, 1003... |
| **OLE Object / BLOB** | Binary large objects (images, files) | Student photo |
| **Memo / Long Text** | Long text fields | Notes, descriptions |

---

## Sources of Data

| Source | Examples |
|---|---|
| **Surveys / forms** | Questionnaires, registration forms |
| **Transactions** | Purchase records, bank statements |
| **Sensors / IoT** | Temperature readings, GPS data |
| **Web activity** | Clicks, page views, searches |
| **Social media** | Posts, comments, likes |
| **Public records** | Census data, government databases |

---

## Data Collection Methods

| Method | Description | Advantages | Disadvantages |
|---|---|---|---|
| **Online forms** | Web-based input | Wide reach, automatic validation | Requires internet access |
| **Paper forms** | Physical forms | No technology required | Must be manually captured |
| **Barcode/QR scanning** | Automated reading | Fast, accurate | Requires equipment |
| **RFID** | Radio frequency identification | Passive (no action needed) | Cost of tags and readers |
| **Biometrics** | Fingerprint, face recognition | Unique, hard to fake | Privacy concerns, cost |
| **API / data feeds** | Automated transfer from other systems | Real-time, no manual entry | Technical setup required |

---

## Data Storage

| Storage Method | Description | Examples |
|---|---|---|
| **Flat file** | Simple text/CSV — one table, no relationships | Spreadsheet, CSV export |
| **Relational database** | Multiple related tables with keys | MS Access, MySQL, PostgreSQL |
| **NoSQL database** | Non-tabular storage — documents, graphs | MongoDB, Firebase |
| **Data warehouse** | Large-scale analytics storage | For business intelligence |
| **Cloud database** | Database hosted in cloud | AWS RDS, Google Cloud SQL |

---

## File Types and Data Storage

| Format | Use | Can store relationships? |
|---|---|---|
| `.csv` | Comma-separated values — simple tabular data | No |
| `.xlsx` | Excel spreadsheet | No (without complex workarounds) |
| `.accdb` | Microsoft Access database | Yes |
| `.sql` | SQL database dump | Yes |
| `.json` | Data exchange format | Partial (nested structures) |
| `.xml` | Data exchange format | Partial |
| `.db` | SQLite database | Yes |

---

## Data Lifecycle

```
Collection → Storage → Processing → Analysis → Distribution → Archiving/Deletion
```

| Stage | What happens |
|---|---|
| **Collection** | Data gathered from various sources |
| **Storage** | Saved in a database or file system |
| **Processing** | Cleaned, validated, transformed |
| **Analysis** | Queries, reports, and summaries produced |
| **Distribution** | Information shared with users who need it |
| **Archiving** | Old data stored long-term |
| **Deletion** | Data that is no longer needed is securely removed |

---

## Metadata

**Metadata** is data about data — it describes the properties of other data.

| Example | Metadata |
|---|---|
| A photo | Date taken, camera settings, GPS location, file size |
| An email | Sender, recipient, timestamp, subject |
| A document | Author, creation date, file size, word count |
| A database record | Last modified, created by which user |

---

## Primary vs Secondary Data

| | Primary Data | Secondary Data |
|---|---|---|
| Source | Collected firsthand for this purpose | Collected previously for another purpose |
| Relevance | Highly relevant to your needs | May not perfectly fit your needs |
| Cost | Expensive (time, resources) | Cheap (already exists) |
| Currency | Fresh and current | May be outdated |
| Examples | Survey you conduct | Government census, published studies |

---

## Key Terms

| Term | Definition |
|---|---|
| **Data** | Raw, unprocessed facts |
| **Information** | Processed data that has meaning and context |
| **Knowledge** | Information applied with experience and understanding |
| **Data type** | Category of value a field can store (Integer, String, etc.) |
| **Metadata** | Data describing properties of other data |
| **Flat file** | Single-table data storage (e.g. CSV) |
| **Relational database** | Multiple related tables linked by keys |
| **Data quality** | How accurate, complete, consistent, and valid data is |
| **Primary data** | Data collected firsthand for a specific purpose |
| **Secondary data** | Data collected previously for another purpose |

---

## Exam Focus

> [!IMPORTANT] High-Frequency Questions
>
> 1. **"What is the difference between data and information?"** — Data is raw unprocessed facts (e.g. "85"); information is data that has been processed and given context (e.g. "Ayden scored 85% in the March test")
>
> 2. **"Give FOUR characteristics of quality data"** — accurate, complete, consistent, relevant, timely, valid, unique
>
> 3. **"Name THREE data types used in a database"** — Text/String, Integer, Real/Float, Boolean, Date, Currency, Auto-number
>
> 4. **"What is metadata? Give ONE example."** — Data that describes other data; example: a photo's metadata includes the date taken, GPS location, and camera settings
>
> 5. **"Explain the difference between primary and secondary data"** — Primary: collected firsthand for the specific purpose (your survey); Secondary: collected previously for a different purpose (government census)
