---
title: Database Programming with TADOTable (Grade 11)
description: Connect to an Access database in Delphi and read, add, change, delete and search records with TADOTable — no SQL.
---

# Database Programming with TADOTable

::: info 📌 Key Points
- In Grade 11 you work with a database **through Delphi code**, not SQL. You move through the table one record at a time with `First`, `Next` and `Eof`.
- Read and write fields with **bracket notation**: `tblBooks['Title']`.
- To change data: `Insert` (new record) or `Edit` (existing record) → assign the fields → `Post`.
- Searching and counting are done **from first principles**: a loop, an `if`, a counter or a Boolean flag.
:::

A school library keeps the details of its books in an Access database. The librarian asks: *"Which books are on the shelf right now? How many poetry books still need a barcode? Do we have Night Sky?"* You could open Access and look, but a program can answer all three questions with a single click. All it needs to do is walk through the table, one record at a time, and test each record.

---

## See it working

The table **tblBooks** in **LibraryDB.mdb**:

| BookID | Title | Genre | Pages | Barcoded | OnLoan |
|---|---|---|---|---|---|
| 1 | River Songs | Poetry | 96 | True | False |
| 2 | Night Sky | Science | 240 | True | False |
| 3 | Long Road | Fiction | 310 | True | True |
| 4 | Tide Pools | Science | 128 | False | False |

This button displays every book that is **not** on loan:

```pascal
procedure TfrmLibrary.btnOnShelfClick(Sender: TObject);
begin
  redOutput.Clear;
  redOutput.Lines.Add('Title' + #9 + 'Genre' + #9 + 'Pages');
  tblBooks.First;                          // 1. go to the first record
  while not tblBooks.Eof do                // 2. until we pass the last record
  begin
    if not tblBooks['OnLoan'] then          // 3. test the current record
      redOutput.Lines.Add(tblBooks['Title'] + #9 + tblBooks['Genre'] +
        #9 + IntToStr(tblBooks['Pages']));
    tblBooks.Next;                         // 4. move to the next record
  end;
end;
```

```text
Title         Genre     Pages
River Songs   Poetry    96
Night Sky     Science   240
Tide Pools    Science   128
```

---

## Understand it — the record pointer

A `TADOTable` always points at **one record**: the *current record*. Everything you read or write applies to that record only.

```text
             tblBooks
   ┌──────────────────────────────┐
   │ 1  River Songs  Poetry  ...  │ ◄── First puts the pointer here
   │ 2  Night Sky    Science ...  │ ◄── Next moves it down one record
   │ 3  Long Road    Fiction ...  │
   │ 4  Tide Pools   Science ...  │
   └──────────────────────────────┘
     (after the last record)        ◄── Eof becomes True
```

| Method / property | What it does |
|---|---|
| `tblX.First` | Moves to the first record |
| `tblX.Next` | Moves to the next record |
| `tblX.Eof` | `True` once the pointer has moved past the last record |
| `tblX.RecordCount` | Number of records in the table |
| `tblX['FieldName']` | Reads (or writes) a field of the current record |

::: danger 🚨 Watch Out For
1. **Forgetting `Next`** creates an endless loop because the pointer never moves. Delphi freezes.
2. **Forgetting `First`** means the loop starts wherever the pointer was left by a previous button, so you may get no output at all.
3. **Misspelling a field name** (`tblBooks['Name']` instead of `['Title']`) causes a runtime error: *Field not found*.
:::

---

## How the connection is set up

In exams and PATs the connection code is usually **given** in a data module. You need to recognise it, not memorise it.

```pascal
// ConnectDB_U.pas — provided code
adoC.ConnectionString := 'Provider=Microsoft.Jet.OLEDB.4.0; ' +
  'Data Source=LibraryDB.mdb; Persist Security Info=False';
adoC.LoginPrompt := False;
adoC.Connected := True;

tblBooks.Connection := adoC;
tblBooks.TableName := 'tblBooks';
tblBooks.Active := True;
dsBooks.DataSet := tblBooks;       // the DBGrid shows dsBooks
```

```mermaid
flowchart LR
  A[(LibraryDB.mdb)] --> B[TADOConnection<br/>adoC]
  B --> C[TADOTable<br/>tblBooks]
  C --> D[TDataSource<br/>dsBooks]
  D --> E[TDBGrid<br/>on the form]
```

::: tip 💡 Why This Matters
Every app you use, from a banking app to Takealot to your school's admin system, sits on top of a database. The loop *"go to the first record, test it, move to the next"* is the same idea those systems use, just hidden behind SQL. Once you understand the record pointer, Grade 12 SQL makes a lot more sense.
:::

---

## Reading fields — bracket notation

```pascal
sName := tblBooks['Title'];                  // Short Text  → String
iAge  := tblBooks['Pages'];                   // Number      → Integer
bDone := tblBooks['OnLoan'];                     // Yes/No      → Boolean
dDate := tblBooks['DateAdded'];                 // Date/Time   → TDateTime
rCost := tblBooks['Price'];                         // Currency    → Real

redOutput.Lines.Add(tblBooks['Title']);       // a text field can be added directly
redOutput.Lines.Add(IntToStr(tblBooks['Pages']));            // numbers must be converted
redOutput.Lines.Add(FormatDateTime('dd/mm/yyyy', tblBooks['DateAdded']));
```

::: warning ⚠️ Common Misconception
Learners often think that `tblBooks['Pages']` is a string because it comes "from the table". The field has the **data type of the database field**, so it is a number. Use `IntToStr`/`FloatToStrF` to display it and compare it directly with numbers: `if tblBooks['Pages'] > 200 then`.
:::

---

## Changing data

All three operations follow the same shape: **put the table in a mode → assign fields → `Post`**.

### Add a new record — `Insert` (or `Append`)

```pascal
tblBooks.Insert;                            // a new, empty record
tblBooks['Title']     := 'Code Club';
tblBooks['Genre']     := 'Science';
tblBooks['Pages']     := 180;
tblBooks['DateAdded'] := Date;                // today's date
tblBooks['Barcoded']  := False;
tblBooks['OnLoan']    := False;
tblBooks.Post;                                // save it
ShowMessage('Code Club has been added');
```

::: info 📝 AutoNumber fields
Never assign a value to an **AutoNumber** primary key (e.g. `BookID`). Access generates it when you `Post`.
:::

### Change existing records — `Edit`

Loop through the table and edit only the records that meet a condition:

```pascal
iCount := 0;
tblBooks.First;
while not tblBooks.Eof do
begin
  if (tblBooks['Genre'] = 'Poetry') and (tblBooks['Pages'] < 150) and
     (not tblBooks['Barcoded']) then
  begin
    tblBooks.Edit;                            // 1. edit mode
    tblBooks['Barcoded'] := True;             // 2. change the field
    tblBooks.Post;                            // 3. save
    Inc(iCount);
  end;
  tblBooks.Next;
end;
redOutput.Lines.Add('Books barcoded: ' + IntToStr(iCount));
```

### Remove a record — `Delete`

```pascal
tblBooks.First;
while not tblBooks.Eof do
begin
  if tblBooks['BookID'] = 15 then
    tblBooks.Delete                         // pointer moves to the next record automatically
  else
    tblBooks.Next;
end;
```

::: danger 🚨 Watch Out For
After `Delete`, the **next** record becomes the current record. If you also call `Next`, you skip a record. That is why `Next` is in the `else`.
:::

---

## Searching — the Boolean flag pattern

Built-in shortcuts like `Locate` are **not** accepted when a question says *"from first principles"*. Use a flag that stops the loop as soon as the record is found:

```pascal
sSearch := InputBox('Search', 'Enter the title of the book:', '');
bFound := False;
tblBooks.First;
while (not tblBooks.Eof) and (not bFound) do
begin
  if UpperCase(tblBooks['Title']) = UpperCase(sSearch) then
  begin
    bFound := True;                           // stop the loop, stay on this record
    redOutput.Lines.Add('Genre: ' + tblBooks['Genre']);
    redOutput.Lines.Add('Added: ' + FormatDateTime('d mmm yyyy', tblBooks['DateAdded']));
  end
  else
    tblBooks.Next;
end;
if not bFound then
  redOutput.Lines.Add(sSearch + ' was not found');
```

Making **both sides** uppercase makes the search *case-insensitive*, so "night sky", "NIGHT SKY" and "Night Sky" all match.

---

## Counting, totals and averages

```pascal
iCount := 0;
iTotal := 0;
tblBooks.First;
while not tblBooks.Eof do
begin
  if tblBooks['Genre'] = 'Fiction' then
  begin
    Inc(iCount);
    iTotal := iTotal + tblBooks['Pages'];
  end;
  tblBooks.Next;
end;
if iCount > 0 then
  redOutput.Lines.Add('Average length: ' + FloatToStrF(iTotal / iCount, ffFixed, 6, 1) + ' pages');
```

### Grouping with an outer loop

To report on **every** genre, put the table loop *inside* a loop over the groups. Go back to `First` and reset the counters for each group:

```pascal
for I := 1 to 3 do                            // arrGenres = ('Fiction', 'Poetry', 'Science')
begin
  iCount := 0;
  tblBooks.First;                           // start at the top for EACH genre
  while not tblBooks.Eof do
  begin
    if tblBooks['Genre'] = arrGenres[I] then
      Inc(iCount);
    tblBooks.Next;
  end;
  redOutput.Lines.Add(arrGenres[I] + ': ' + IntToStr(iCount));
end;
```

### Finding the maximum

```pascal
iMaxDays := -1;
tblBooks.First;
while not tblBooks.Eof do
begin
  if tblBooks['OnLoan'] then
  begin
    iDays := Trunc(Date - tblBooks['DateAdded']);       // days in the library
    if iDays > iMaxDays then
    begin
      iMaxDays := iDays;
      sOldest := tblBooks['Title'];
    end;
  end;
  tblBooks.Next;
end;
```

---

## 📋 Summary

| Task | Pattern |
|---|---|
| Visit every record | `First` → `while not Eof` → … → `Next` |
| Read a field | `tblX['FieldName']` (convert numbers/dates to display them) |
| Add a record | `Insert` → assign fields → `Post` |
| Change a record | `Edit` → assign fields → `Post` (inside the loop, inside an `if`) |
| Delete a record | `Delete` — and **don't** call `Next` for that record |
| Search | Boolean flag; loop `while (not Eof) and (not bFound)` |
| Group report | Outer loop over the groups; `First` and reset counters inside it |

::: tip 🎯 Exam Tip
Marks are given for the **loop structure** (`First`, `while not Eof`, `Next`) on almost every database question, and that is separate from the logic inside the loop. Write those three lines first, even if you are unsure of the condition. Always click **Restore DB** before testing again, because your earlier test runs changed the data.
:::

## ✏️ Check Your Understanding

**Question 1:** A learner's loop never ends and the program freezes. Which line is most likely missing?

**Question 2:** Explain why `tblBooks.Next` is placed in the `else` part when deleting records.

**Question 3:** Write the code to increase `Pages` by 2 for every book in the table (a notice page has been added to each book). (5)

::: details Check your answers
**Q1:** `tblBooks.Next;` Without it, the record pointer never moves, so `Eof` never becomes True.

**Q2:** `Delete` already moves the pointer to the next record. Calling `Next` as well would skip the record straight after the deleted one.

**Q3:**
```pascal
tblBooks.First;                                          // ✓
while not tblBooks.Eof do                                // ✓
begin
  tblBooks.Edit;                                         // ✓
  tblBooks['Pages'] := tblBooks['Pages'] + 2;              // ✓
  tblBooks.Post;
  tblBooks.Next;                                         // ✓
end;
```
:::

---

*Previous: [← Text Files](./text-files) | Next: [Date & Time →](./date-time)*
