---
title: Grade 11 November Exam Scope
description: What is examined in the Grade 11 IT November final examination — Paper 1 (practical) and Paper 2 (theory), with mark allocations and study links.
---

# Grade 11 November Exam Scope

::: info 📌 Exam overview
| Paper | Type | Time | Marks |
|---|---|---|---|
| Paper 1 | Practical (Delphi) | 3 hours | 150 |
| Paper 2 | Theory (written) | 3 hours | 150 |

**All work from Terms 1 to 4 is examinable**, plus the Grade 10 foundations it builds on. This paper uses the same mark totals and time as the Grade 12 final exam, so treat it as your dress rehearsal for matric.
:::

---

## Paper 1 — Practical (150 marks)

### Question 1: General programming skills — conditionals, loops, built-in functions (40)

- [ ] Set component properties in code, including `Font.Name/Size/Color/Style`; load an image (`imgX.Picture.LoadFromFile`, `Stretch`, `Proportional`)
- [ ] Translate a **formula** into code with `Power`, `Sqrt`, `Sqr`, `Round`, `Trunc` and constants
- [ ] String functions: `Copy`, `Pos`, `Delete`, `Insert`, `Length`, `UpperCase`, `LowerCase`, and accessing characters (`s[i]`)
- [ ] Remove or replace characters with a loop and `Pos`/`Delete`
- [ ] `for`, `while` and `repeat` loops, including loops that build a table of output
- [ ] Nested `if` / `else if` and `case`; compound conditions
- [ ] Formatting: `FloatToStrF` (ffFixed, ffCurrency), tabs (`#9`), rich edit output

📖 [String Functions](../practical/delphi/strings) · [Math Methods](../practical/delphi/math-methods) · [Loops](../practical/delphi/loops) · [Selection](../practical/delphi/selection)

### Question 2: Functions and procedures (40)

- [ ] Write **functions** that receive parameters and **return** a value (Real, Integer, String, Boolean)
- [ ] Write **procedures** that receive parameters and update components or global variables
- [ ] **Declare** your methods in the form class (`private` section) and implement them with the class name (`TfrmX.calcFee`)
- [ ] **Value vs `var` (reference) parameters**
- [ ] **Boolean validation functions** (e.g. check the format of a name or code character by character)
- [ ] Functions that use `Random` / `RandomRange` to generate codes
- [ ] **Call** your methods correctly from a button with the right arguments; use the returned value
- [ ] Local vs global variables
- [ ] Read input from combo boxes, spin edits, check boxes and radio groups; output to list boxes and labels

📖 [Procedures & Functions](../practical/delphi/procedures-functions) · [Input Validation](../practical/delphi/validation)

### Question 3: Database (40)

The connection code and a `Restore DB` button are given. **No SQL**: everything is done with `TADOTable` and code.

- [ ] Loop through a table: `First` → `while not Eof` → `Next`
- [ ] Read fields with **bracket notation** `tblX['FieldName']` and display them (convert numbers and dates)
- [ ] **Filter** records with an `if` inside the loop; display headings and tab-separated columns
- [ ] **Add** a record: `Insert` → assign fields (including `Date` for today) → `Post`
- [ ] **Change** records that meet a condition: `Edit` → assign → `Post`; count the changes
- [ ] **Delete** a record (and don't skip the record that follows it)
- [ ] **Search** with a Boolean flag, case-insensitive (`UpperCase` on both sides)
- [ ] **Counts, totals, averages and maximum/minimum** over the table, including **grouped reports** (outer loop over groups, `First` inside)
- [ ] Date calculations on date fields (`Date - tblX['DateField']`, `FormatDateTime`)

📖 [Database Programming with TADOTable](../practical/delphi/database-navigation) · [Date & Time](../practical/delphi/date-time)

### Question 4: General problem-solving — arrays and text files (30)

- [ ] **1D arrays** and **parallel arrays**: declare, fill, traverse, count, total, average, max/min
- [ ] **Text files:** `FileExists`, `AssignFile`, `Reset`, `ReadLn`, `Eof`, `Rewrite`, `Append`, `WriteLn`, `CloseFile`
- [ ] **Parse delimited lines** (e.g. `Name#Amount#Month`) with `Pos`, `Copy`, `Delete` and load them into parallel arrays
- [ ] **Sort** from first principles: **bubble sort** and **selection sort**, ascending and descending, **swapping all parallel arrays**
- [ ] **Search** from first principles: linear search (with a flag) and **binary search**
- [ ] Write results to a **new text file** in the format asked for

📖 [1D Arrays (sorting & searching)](../practical/delphi/arrays-1d) · [Text Files](../practical/delphi/text-files)

::: danger 🚨 Not in the Grade 11 exam
2D arrays, SQL, and OOP (classes and objects) are Grade 12 work.
:::

---

## Paper 2 — Theory (150 marks)

| Section | Content | Marks |
|---|---|---|
| A | Short questions: multiple choice, matching, true/false with correction | ±20 |
| B | Systems Technologies | ±25 |
| C | Communication and Network Technologies | ±25 |
| D | Data and Information Management | ±25 |
| E | Solution Development | ±25 |
| F | Integrated scenario | ±30 |

### Section B: Systems Technologies
- [ ] **Motherboard** components and purpose; expansion slots and cards (e.g. graphics card, PCIe); buses and data flow between storage, RAM and the CPU
- [ ] **Cache memory** (levels L1–L3) and caching (disk caching, web caching); **virtual memory**
- [ ] **Computer performance:** CPU (clock speed, cores), RAM, SSD vs HDD, GPU; bottlenecks
- [ ] **BIOS / UEFI**, CMOS, POST and the boot process; device **drivers**
- [ ] Types of operating systems: single-user, multi-user, **real-time**, embedded, mobile
- [ ] **Multitasking, multiprocessing and multithreading**
- [ ] **Compilers vs interpreters**; high-level vs low-level languages
- [ ] **Virtualisation** and virtual machines

📖 [Computer Performance](../theory/systems/performance) · [Cloud & Virtualisation](../theory/systems/cloud-virtualisation) · [OS & File Management](../theory/systems/os-management) · [Software](../theory/systems/software)

### Section C: Communication and Network Technologies
- [ ] Network types, topologies and hardware (switch, router, access point, NIC, modem)
- [ ] **Intranet vs extranet vs Internet**; **VPN**
- [ ] **Wireless and mobile technologies:** Wi-Fi, Bluetooth, **WiMAX, LTE/4G, 5G**; bandwidth, **latency**, throttling and congestion
- [ ] **Location-based computing** (GPS, RFID) and its social implications
- [ ] **VoIP**, video conferencing, e-communication protocols (SMTP, POP3, IMAP, HTTP/HTTPS, FTP)
- [ ] **Internet and WWW (Term 4):** evolution of the Internet, multimedia and **streaming**, types of websites, Internet services, **security services** (SSL/TLS, digital certificates, HTTPS)
- [ ] **Threats and remedies:** malware (virus, worm, Trojan, ransomware, spyware), phishing, DoS; firewalls, antivirus, backups, updates, encryption, MFA

📖 [Wireless](../theory/networks/wireless) · [Protocols](../theory/networks/protocols) · [Network Security](../theory/networks/network-security) · [Internet Services](../theory/internet/internet-services) · [Multimedia](../theory/internet/multimedia)

### Section D: Data and Information Management
- [ ] **DBMS:** what it is, examples (open source and commercial), **desktop vs server** databases
- [ ] Database careers: **database administrator (DBA)**, database programmer, data analyst
- [ ] **Data, information, knowledge** and decision-making
- [ ] **Characteristics of quality data** (accurate, complete, consistent, up to date, relevant)
- [ ] **Validation vs verification**; types of validation checks (range, type, format, length, presence)
- [ ] Table structure: records, fields, **data types**, **primary keys** and **foreign keys**
- [ ] **Data redundancy** and **update, insert and delete anomalies**: why one big table causes problems
- [ ] Split a flat table into related tables and **draw an ERD** with PKs, FKs and one-to-many relationships

📖 [Data Concepts](../theory/databases/data-concepts) · [Database Concepts](../theory/databases/database-concepts) · [Database Design & ERDs](../theory/databases/database-design) · [Normalisation & Anomalies](../theory/databases/normalisation) · [DBMS & Roles](../theory/databases/dbms-software)

### Section E: Solution Development
- [ ] **Trace tables** for loops, arrays and searches, including **binary search**
- [ ] Trace a pass of **bubble sort** or **selection sort**
- [ ] Read text-file code: what each line does, `Append` vs `Rewrite`, `FileExists`
- [ ] Exception handling: runtime errors, `try … except`, validation before conversion
- [ ] **Procedures vs functions**; **value vs `var` parameters** (predict values after a call)
- [ ] Modify pseudocode / algorithms; choose suitable control structures
- [ ] **User-centred design** principles for a GUI; software development phases

📖 [Algorithms (Theory)](../theory/programming/algorithms-theory) · [Software Engineering](../theory/programming/software-engineering) · [Debugging](../practical/delphi/debugging)

### Section F: Integrated scenario
Any Grade 11 topic can appear, with the emphasis on **Term 4** content and social implications:
- [ ] **Big data** (the Vs), **digitalisation**, **globalisation** and the **Fourth Industrial Revolution (4IR)**
- [ ] Emerging technology in context: **IoT**, **AI**, cloud computing, location-based services
- [ ] **Human vs computer error**; GIGO
- [ ] **Cybercrime**, online fraud, **identity theft** and protecting your online identity
- [ ] **Privacy**, POPIA, ethical and legal use of data; network-use policies
- [ ] Internet-related careers

📖 [Big Data, Globalisation & 4IR](../theory/social/big-data-4ir) · [Privacy & Ethics](../theory/social/privacy-ethics) · [Cybercrime](../theory/social/cybercrime) · [Online Safety](../theory/social/online-safety)

---

::: tip 🎯 Exam Tips
- **Paper 1:** Write the database loop skeleton (`First` / `while not Eof` / `Next`) first. It earns marks on its own. In Question 2, a method that is declared but never called earns no marks for the button.
- **Paper 2:** Section F is worth 30 marks and is mostly "discuss" and "evaluate" questions. Give **one point per mark** and link each point to the scenario.
- Grade 11 is the dress rehearsal for matric. The structure of these papers is the structure you will write next year.
:::

*Also see: [Grade 11 Practical Notes](./Grade_11_IT_Practical_Notes) · [Grade 11 Theory Notes](./Grade_11_IT_Theory_Notes)*
