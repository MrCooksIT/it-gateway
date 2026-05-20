---
title: Setting Up & Practising in Delphi
---

# Setting Up & Practising in Delphi

Delphi Community Edition is **free** for students and personal use. If you have a Windows PC at home, installing it gives you the exact same environment you will use in the exam — which means any time you spend practising in it directly transfers to the real thing.

::: warning Windows only
Delphi Community Edition only runs on Windows. If you don't have a Windows PC, see the [Studying Without Delphi](./study-without-delphi) guide instead.

**Linux users:** Install **Lazarus IDE** (free, open-source, nearly identical to Delphi). See the note at the bottom of this page.
:::

---

## System requirements

| Requirement | Minimum | Recommended |
|---|---|---|
| Operating system | Windows 10 (64-bit) | Windows 11 |
| RAM | 4 GB | 8 GB |
| Free disk space | 10 GB | 15 GB |
| Internet | Required for download and registration | — |

---

## Step 1: Download Delphi Community Edition

1. Open a browser and go to **embarcadero.com**
2. Navigate to **Products → Delphi** and look for **Community Edition** (it is free)
3. Click **Download Free** — you will need to create a free Embarcadero account
4. Use your school email address when registering
5. Download the installer (approximately 2–3 GB — use a good Wi-Fi connection)

::: tip Free for students
The Community Edition licence is completely free for students, learners, and non-commercial use. You will need to log in with your Embarcadero account when you first open Delphi, but after that it works offline.
:::

---

## Step 2: Install Delphi

1. Run the downloaded `.exe` installer (right-click → Run as administrator)
2. Accept the licence agreement
3. When asked which platforms to install, select **VCL (Windows)** — this is what the exam uses
4. Leave other options at their defaults and click Install
5. Installation takes 15–30 minutes depending on your PC
6. Restart your computer when prompted

::: warning Disk space
Check that you have at least 10 GB free before starting. The installer will warn you if there isn't enough space, but it's better to check first.
:::

---

## Step 3: Know the IDE layout

When you open Delphi and create a new **VCL Forms Application** (File → New → VCL Forms Application), you will see:

```
┌─────────────────────────────────────────────────────────────────┐
│  Menu bar:  File  Edit  Search  View  Project  Run  Tools       │
├──────────────┬──────────────────────────────┬───────────────────┤
│              │                              │                   │
│  Object      │   Form Designer              │   Tool Palette    │
│  Inspector   │   (drag components here)     │   (components     │
│              │                              │    to place)      │
│  Properties  ├──────────────────────────────┤                   │
│  tab         │                              │                   │
│              │   Code Editor                │                   │
│  Events      │   (Unit1.pas)                │                   │
│  tab         │                              │                   │
└──────────────┴──────────────────────────────┴───────────────────┘
```

| Area | What it does |
|------|-------------|
| **Form Designer** | Visual layout — drag components onto the form here |
| **Object Inspector → Properties** | Change how a component looks or behaves (`Name`, `Caption`, `Text`, `Color`) |
| **Object Inspector → Events** | Wire up event handlers — double-click `OnClick` to create a button click procedure |
| **Code Editor** | Write your Pascal code |
| **Tool Palette** | All the components you can place — grouped by category |

---

## Step 4: Components you must know

These components appear in almost every Paper 1 question. Know their names, their key properties, and how to read from and write to them in code.

### Input components

| Component | Palette section | Key properties | Code example |
|-----------|----------------|----------------|-------------|
| `TEdit` | Standard | `Name`, `Text` | `sInput := edtName.Text;` |
| `TMemo` | Standard | `Name`, `Lines`, `Text` | `mmoNotes.Lines.Add('Hello');` |
| `TListBox` | Standard | `Name`, `Items` | `lstNames.Items.Add(sName);` |
| `TComboBox` | Standard | `Name`, `Items`, `Text` | `sChoice := cmbGrade.Text;` |
| `TRadioButton` | Standard | `Name`, `Caption`, `Checked` | `if rdoBtnMale.Checked then ...` |
| `TCheckBox` | Standard | `Name`, `Caption`, `Checked` | `if chkAgree.Checked then ...` |

### Output components

| Component | Palette section | Key properties | Code example |
|-----------|----------------|----------------|-------------|
| `TLabel` | Standard | `Name`, `Caption` | `lblResult.Caption := 'Done';` |
| `TStringGrid` | Additional | `Name`, `Cells`, `ColCount`, `RowCount` | `sgData.Cells[col, row] := sValue;` |

### Action components

| Component | Key properties | How to create the event |
|-----------|----------------|------------------------|
| `TButton` | `Name`, `Caption`, `OnClick` | Double-click the button on the form |

### Database components (Grade 12)

| Component | Purpose |
|-----------|---------|
| `TADOConnection` | Connect to the Access `.mdb` or `.accdb` file |
| `TADOQuery` | Run SQL queries against the database |
| `TDataSource` | Link a query to display components |
| `TDBGrid` | Display query results in a table |

---

## Step 5: Naming conventions

The exam uses standard Hungarian-style prefixes. Use them consistently — it makes your code readable and matches the style expected.

| Prefix | Data type | Example names |
|--------|-----------|--------------|
| `n` | Integer | `nScore`, `nCount`, `nTotal` |
| `r` | Real / Double | `rAverage`, `rPrice` |
| `s` | String | `sName`, `sResult`, `sSurname` |
| `b` | Boolean | `bFound`, `bValid` |
| `c` | Char | `cChoice`, `cGrade` |
| `arr` | Array | `arrScores`, `arrNames` |
| `edt` | TEdit | `edtUsername`, `edtScore` |
| `lbl` | TLabel | `lblResult`, `lblStatus` |
| `btn` | TButton | `btnSearch`, `btnClear` |
| `lst` | TListBox | `lstOutput`, `lstStudents` |
| `mmo` | TMemo | `mmoNotes`, `mmoReport` |
| `cmb` | TComboBox | `cmbGrade`, `cmbSubject` |
| `sg` | TStringGrid | `sgResults` |

---

## Step 6: Essential keyboard shortcuts

Learning these shortcuts will save you significant time in the exam. Practise using them from day one.

| Shortcut | Action |
|----------|--------|
| `F9` | Run the application |
| `F8` | Step through code one line at a time (debugging) |
| `F5` | Toggle breakpoint on the current line |
| `F2` | Save current file |
| `Ctrl + S` | Save |
| `Ctrl + Space` | Code completion — shows available options |
| `Ctrl + F` | Find text |
| `Ctrl + Z` | Undo |
| `Ctrl + Shift + C` | Complete class (auto-generate method bodies) |
| `Alt + F9` | Compile without running (check for errors) |

---

## Step 7: Common mistakes to fix early

::: danger These errors cost marks — fix the habit now

**1. Forgetting to convert between String and Integer**
```pascal
// Wrong — won't compile:
nTotal := edtScore.Text + 10;

// Correct:
nTotal := StrToInt(edtScore.Text) + 10;
```

**2. Using `=` instead of `:=` for assignment**
```pascal
// Wrong:
nScore = 75;

// Correct:
nScore := 75;
```

**3. Off-by-one errors in loops**
```pascal
// Array declared as array[1..10] — loop must match:
for i := 1 to 11 do  // Wrong — crashes on i = 11
for i := 1 to 10 do  // Correct
```

**4. Not initialising counters and totals before a loop**
```pascal
// Always do this before the loop:
nTotal := 0;
nCount := 0;
for i := 1 to nSize do
  ...
```

**5. Missing `begin...end` when a loop body has more than one line**
```pascal
// Wrong — only the first line is inside the if:
if nScore >= 50 then
  lblGrade.Caption := 'Pass';
  lblColour.Font.Color := clGreen;  // This always runs!

// Correct:
if nScore >= 50 then
begin
  lblGrade.Caption := 'Pass';
  lblColour.Font.Color := clGreen;
end;
```

**6. Comparing strings with the wrong case**
```pascal
// Wrong — 'pass' ≠ 'Pass':
if sInput = 'pass' then ...

// Correct — normalise first:
if LowerCase(sInput) = 'pass' then ...
```
:::

---

## Step 8: Using the debugger

The debugger is one of the most useful tools in Delphi. Use it to understand what your code is actually doing, not what you think it is doing.

### Setting a breakpoint
1. Click in the grey margin next to any line of code — a red dot appears
2. Press `F9` to run
3. The program pauses at that line before executing it
4. Hover over any variable name to see its current value in a tooltip

### Stepping through code
Once paused at a breakpoint:
- `F8` — execute the current line and move to the next
- `F7` — step *into* a procedure or function call
- `F9` — continue running until the next breakpoint

### The Watch window
1. While paused, right-click a variable → **Add Watch**
2. The Watch list shows the variable's live value as you step through

This is especially useful for:
- Checking what value is in an array at each loop iteration
- Verifying that string functions are producing what you expect
- Tracking a boolean flag through a search

---

## Step 9: Practise exercises — by grade

Work through these in order. Each one builds on the previous. Do them without looking at notes once you have studied the relevant topic.

### Grade 10 — Foundations

**Exercise 1: Temperature converter**
- `TEdit`: temperature in Celsius
- `TLabel`: shows the Fahrenheit result
- `TButton`: "Convert"
- Formula: `F = (C × 9/5) + 32`

**Exercise 2: Grade classifier**
Read a mark (0–100). Display the grade symbol:
- 80–100 → `Distinction`
- 70–79 → `Merit`
- 60–69 → `Achievement`
- 50–59 → `Pass`
- Below 50 → `Fail`

**Exercise 3: Simple loop display**
Read a start and end number. Display all numbers between them in a `TListBox`. Show how many numbers were displayed in a label.

**Exercise 4: Times table**
Read a number. Display its full times table (1 × n to 12 × n) in a `TMemo`.

---

### Grade 11 — Arrays and strings

**Exercise 5: Array of marks**
Read 10 marks into a 1D array using a loop. Display in a `TListBox`:
- All marks
- The highest and lowest mark
- The average (formatted to 2 decimal places)
- How many are above the average

**Exercise 6: String analyser**
Read a sentence from a `TEdit`. Display:
- Number of characters (including spaces)
- Number of vowels (a, e, i, o, u)
- Number of words (count spaces + 1)
- The sentence reversed
- The sentence with all spaces removed

**Exercise 7: Bubble sort**
Read 8 numbers into an array. Sort them in ascending order using bubble sort. Display the unsorted array, then the sorted array side by side.

**Exercise 8: 2D array — class marks**
Create a 4×5 array of random marks. Display in a `TStringGrid`. Show:
- The average per row (student average)
- The average per column (subject average)
- The highest mark in the entire grid

---

### Grade 12 — Files, OOP, and databases

**Exercise 9: Text file reader**
Read a text file containing names and scores (`Dlamini,78` format, one per line). Store in parallel arrays. Display in a `TStringGrid`. Show the average score.

**Exercise 10: OOP — Student class**

Create a `TStudent` class with:
- Private fields: `FSurname`, `FName`, `FScore` (all strings/integers)
- Constructor: `Create(sSurname, sName : String; nScore : Integer)`
- Read-only properties: `Surname`, `Name`, `Score`
- Method `GetGrade`: returns the grade symbol (`'A'`–`'F'`) for the score
- Method `GetDetails`: returns a formatted string: `'Dlamini, Sipho — 78 (B)'`

Create 5 `TStudent` objects and display them in a `TListBox`.

**Exercise 11: Database search**
Connect to an Access database. Display all records in a `TDBGrid`. Add:
- A search `TEdit` and button that filters by surname (`LIKE '%..%'`)
- A label showing how many records are currently displayed
- A Clear button that resets the filter

---

## Step 10: Weekly practice plan

Use this as a guide once Delphi is set up:

| Week | Focus area | Exercise to complete |
|------|-----------|---------------------|
| 1 | IDE setup, components, basic I/O | Exercises 1–2 |
| 2 | Selection (`if`/`case`) | Exercise 2 (extend), Exercise 3 |
| 3 | Loops (`for`/`while`/`repeat`) | Exercises 3–4 |
| 4 | 1D arrays | Exercise 5 |
| 5 | String functions | Exercise 6 |
| 6 | Sorting and searching | Exercise 7 |
| 7 | 2D arrays | Exercise 8 |
| 8 | Text files and procedures | Exercise 9 |
| 9 | OOP | Exercise 10 |
| 10 | Databases and SQL in Delphi | Exercise 11 |
| 11–12 | Past papers under timed conditions | One full paper per week |

::: tip Timed practice
From week 4 onwards, time yourself: 45 minutes per question, no pausing. This builds the speed and pressure management you need for the real exam.
:::

---

## Lazarus IDE — for Linux users

If you have a Linux PC (including an older laptop, a Raspberry Pi, or a converted Chromebook running Linux), **Lazarus IDE** is a free, open-source alternative to Delphi that is nearly identical in layout and syntax.

**What's the same:**
- The visual form designer
- Object Pascal language (same syntax as Delphi)
- All programming logic, string functions, arrays, OOP, and file handling
- The `TEdit`, `TLabel`, `TButton`, `TListBox`, `TMemo` components

**What's different:**
- Database components use a different set (`TSQLite3Connection` instead of `TADOConnection`)
- Some component names and properties differ slightly

For Grades 10–11, Lazarus is effectively identical to Delphi. For Grade 12 database work, there are small differences in how database connections are set up — but the SQL and logic are the same.

**Download:** Search for "Lazarus IDE download" at `lazarus-ide.org`
