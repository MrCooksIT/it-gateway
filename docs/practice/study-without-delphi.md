---
title: Studying Without Delphi
---

# Studying Without Delphi

You don't need Delphi installed to study for Paper 1. The exam tests your ability to **think through problems and write correct code** — skills you build with nothing more than a pen, paper, and focus.

This guide walks you through the techniques that work without a computer, plus some free browser-based tools for those with internet access.

---

## 1. Understand what the exam is really asking

Before studying any code, understand how Paper 1 questions are structured. Every question gives you:

1. **A context** — a scenario (school system, shop inventory, sports results, etc.)
2. **A Delphi project** — partially written code already on the computer
3. **Specific tasks** — "write code to...", "complete the procedure...", "fix the error in..."

You are **never** building an app from scratch. You are reading existing code and adding to it correctly.

This means the single most important skill is: **reading and understanding code you have never seen before**.

---

## 2. The "inside the container" concept

Every Delphi answer lives inside an event handler or procedure. The form, button, and label are just the visual wrapper. What the exam marks is the logic you write inside.

**What the examiner sees in Delphi:**
```pascal
procedure TForm1.btnCalculateClick(Sender: TObject);
var
  iScore : Integer;
  sGrade : String;
begin
  iScore := StrToInt(edtScore.Text);
  if iScore >= 75 then
    sGrade := 'Distinction'
  else if iScore >= 50 then
    sGrade := 'Pass'
  else
    sGrade := 'Fail';
  lblResult.Caption := sGrade;
end;
```

**What the logic actually is (no GUI needed):**
```
INPUT iScore
IF iScore >= 75 THEN
    sGrade = 'Distinction'
ELSE IF iScore >= 50 THEN
    sGrade = 'Pass'
ELSE
    sGrade = 'Fail'
OUTPUT sGrade
```

These are identical in meaning. You can study, trace, and write the second form with no computer at all. Once you understand the logic, translating it into Delphi syntax is the easy part.

---

## 3. Code Tracing (Dry Running)

**Code tracing** means reading code line by line and manually tracking what each variable contains at each step. This is the single most powerful study technique for Paper 1 — and it requires no computer.

### How to trace code

1. List all variables and write their starting values (usually `0`, `''`, or `False`)
2. Read each line in order, exactly as the computer would
3. Update variable values when assignments (`:-`) happen
4. For loops: track the counter, check the condition, execute the body

### Worked example 1 — Simple loop

```pascal
var
  i, iTotal : Integer;
begin
  iTotal := 0;
  for i := 1 to 5 do
    iTotal := iTotal + i;
  ShowMessage(IntToStr(iTotal));
end;
```

**Trace table — track each variable after each step:**

| Step | Code executed | `i` | `iTotal` |
|------|--------------|-----|---------|
| 1 | `iTotal := 0` | — | **0** |
| 2 | Loop: `i := 1` | **1** | 0 |
| 3 | `iTotal := 0 + 1` | 1 | **1** |
| 4 | Loop: `i := 2` | **2** | 1 |
| 5 | `iTotal := 1 + 2` | 2 | **3** |
| 6 | Loop: `i := 3` | **3** | 3 |
| 7 | `iTotal := 3 + 3` | 3 | **6** |
| 8 | Loop: `i := 4` | **4** | 6 |
| 9 | `iTotal := 6 + 4` | 4 | **10** |
| 10 | Loop: `i := 5` | **5** | 10 |
| 11 | `iTotal := 10 + 5` | 5 | **15** |
| 12 | `ShowMessage('15')` | — | — |

**Output: `15`** — The code adds the numbers 1 to 5 together.

---

### Worked example 2 — String functions

```pascal
var
  sWord, sResult : String;
begin
  sWord := 'Gateway';
  sResult := Copy(sWord, 1, 4);
  sResult := UpCase(sResult[1]) + LowerCase(Copy(sResult, 2, Length(sResult)));
  lblOutput.Caption := sResult + ' - ' + IntToStr(Length(sWord));
end;
```

**Trace each expression step by step:**

| Step | Expression | Value |
|------|-----------|-------|
| `sWord := 'Gateway'` | — | `'Gateway'` |
| `Copy(sWord, 1, 4)` | Characters 1–4 of `'Gateway'` | `'Gate'` |
| `sResult := 'Gate'` | — | `'Gate'` |
| `sResult[1]` | First character of `'Gate'` | `'G'` |
| `UpCase('G')` | Already uppercase | `'G'` |
| `Copy(sResult, 2, Length(sResult))` | Characters 2 to end of `'Gate'` | `'ate'` |
| `LowerCase('ate')` | — | `'ate'` |
| `'G' + 'ate'` | Concatenate | `'Gate'` |
| `Length(sWord)` | Length of `'Gateway'` | `7` |
| `IntToStr(7)` | — | `'7'` |
| `'Gate' + ' - ' + '7'` | — | `'Gate - 7'` |

**Output label shows: `Gate - 7`**

---

### Worked example 3 — Array search

```pascal
var
  arrScores : array[1..5] of Integer;
  i, iHighest : Integer;
begin
  arrScores[1] := 65;  arrScores[2] := 82;
  arrScores[3] := 71;  arrScores[4] := 90;
  arrScores[5] := 58;

  iHighest := arrScores[1];
  for i := 2 to 5 do
    if arrScores[i] > iHighest then
      iHighest := arrScores[i];

  ShowMessage('Highest: ' + IntToStr(iHighest));
end;
```

**Array contents:**

| Index | [1] | [2] | [3] | [4] | [5] |
|-------|-----|-----|-----|-----|-----|
| Value | 65  | 82  | 71  | 90  | 58  |

**Trace the search:**

| `i` | `arrScores[i]` | `> iHighest`? | `iHighest` |
|-----|---------------|---------------|-----------|
| Start | — | — | **65** |
| 2 | 82 | 82 > 65 → Yes | **82** |
| 3 | 71 | 71 > 82 → No | 82 |
| 4 | 90 | 90 > 82 → Yes | **90** |
| 5 | 58 | 58 > 90 → No | 90 |

**Output: `Highest: 90`**

---

### Practice trace exercise

Try this one yourself before looking at the answer. What does this function return when `sText = 'Hello World'`?

```pascal
function Mystery(sText : String) : Integer;
var
  i, iCount : Integer;
begin
  iCount := 0;
  for i := 1 to Length(sText) do
    if sText[i] = ' ' then
      Inc(iCount);
  Result := iCount + 1;
end;
```

<details>
<summary>Show trace and answer →</summary>

`sText = 'Hello World'`, `Length('Hello World') = 11`

| `i` | `sText[i]` | Is it `' '`? | `iCount` |
|-----|-----------|------------|---------|
| 1 | 'H' | No | 0 |
| 2 | 'e' | No | 0 |
| 3 | 'l' | No | 0 |
| 4 | 'l' | No | 0 |
| 5 | 'o' | No | 0 |
| 6 | ' ' | **Yes** | **1** |
| 7 | 'W' | No | 1 |
| 8 | 'o' | No | 1 |
| 9 | 'r' | No | 1 |
| 10 | 'l' | No | 1 |
| 11 | 'd' | No | 1 |

`Result := 1 + 1 = 2`

**The function counts spaces and adds 1 — it counts the number of words.** For `'Hello World'` (1 space), it returns `2`.

</details>

::: tip Make your own trace tables
Take any code example from the [Delphi section](../practical/delphi/) and trace it on paper before checking what it does. This directly mirrors what you need to do in the exam.
:::

---

## 4. Reading Unfamiliar Code

When you open a Paper 1 question file, you will see code you have never seen before. Here is how to approach it:

### Step 1: Read the component names
The names tell you what each component is for.
- `edtUsername` → an edit box for a username
- `btnSearch` → a search button
- `lstResults` → a list box showing results
- `lblStatus` → a label showing a status message

### Step 2: Read each procedure/function name
Before reading the code inside, ask: *what is this supposed to do?*
- `btnSearchClick` → fires when Search is clicked
- `FormCreate` → runs when the form loads
- `ValidateInput` → checks whether input is acceptable
- `CalculateAverage` → calculates an average — of what?

### Step 3: Trace the logic for each task
For each task in the question, find the relevant procedure and trace through it line by line.

### Step 4: Identify what is missing
The exam will leave gaps. After tracing what's there, ask: *what would need to be added to make this work correctly?*

---

## 5. Pseudocode — Plan Before You Code

Pseudocode is your solution written in plain English logic — no Delphi syntax, no compiler, just the steps. It forces you to think through the problem before worrying about semicolons and `begin...end` blocks.

### CAPS pseudocode conventions

```
INPUT value
OUTPUT value
variable ← expression          (assignment)

IF condition THEN
    ...
ELSE IF condition THEN
    ...
ELSE
    ...
ENDIF

FOR counter ← start TO end DO
    ...
ENDFOR

WHILE condition DO
    ...
ENDWHILE

REPEAT
    ...
UNTIL condition
```

### From question to pseudocode to Delphi

**The question:** Read a number. If it is divisible by both 3 and 5, display "FizzBuzz". If by 3 only, display "Fizz". If by 5 only, display "Buzz". Otherwise display the number.

**Step 1 — Pseudocode:**
```
INPUT iNum
IF iNum MOD 3 = 0 AND iNum MOD 5 = 0 THEN
    OUTPUT 'FizzBuzz'
ELSE IF iNum MOD 3 = 0 THEN
    OUTPUT 'Fizz'
ELSE IF iNum MOD 5 = 0 THEN
    OUTPUT 'Buzz'
ELSE
    OUTPUT iNum
ENDIF
```

**Step 2 — Translate to Delphi:**
```pascal
var iNum : Integer;
begin
  iNum := StrToInt(edtNumber.Text);
  if (iNum mod 3 = 0) and (iNum mod 5 = 0) then
    lblResult.Caption := 'FizzBuzz'
  else if iNum mod 3 = 0 then
    lblResult.Caption := 'Fizz'
  else if iNum mod 5 = 0 then
    lblResult.Caption := 'Buzz'
  else
    lblResult.Caption := IntToStr(iNum);
end;
```

Notice: every pseudocode line maps directly to one or two Delphi lines. The logic is identical.

---

## 6. Writing Code on Paper

Writing Delphi code by hand — without autocomplete, without syntax highlighting, without the IDE catching your errors — is harder than typing it. That is exactly why it is effective. It forces you to actively recall every keyword, data type, and structure.

### How to practice

1. Pick a task (e.g. "search an array for the smallest value")
2. Close all notes
3. Write the full solution by hand in your notebook
4. Check your syntax against the [Delphi Syntax cheat sheet](../quick-study/delphi-syntax)
5. Circle every mistake and understand *why* it was wrong

### Tasks to write from memory (start here)

- [ ] A `for` loop that adds all numbers in an array and calculates the average
- [ ] An `if` statement that assigns a grade symbol based on a percentage
- [ ] A `while` loop that validates that a number is between 1 and 100
- [ ] A function that takes a string and returns `True` if it contains only digits
- [ ] A procedure that reads a text file into an array line by line
- [ ] A class declaration with a constructor, two properties, and one method

---

## 7. Pattern Recognition

Expert programmers don't solve problems from scratch every time — they recognise familiar **patterns** and adapt them. Learn these patterns until you can write them without thinking.

### Pattern 1 — Sum and average of an array

```pascal
iTotal := 0;
for i := 1 to iSize do
  iTotal := iTotal + arrData[i];
rAverage := iTotal / iSize;
```

### Pattern 2 — Find the maximum value

```pascal
iMax := arrData[1];           // assume first is largest
for i := 2 to iSize do
  if arrData[i] > iMax then
    iMax := arrData[i];
```

### Pattern 3 — Count items meeting a condition

```pascal
iCount := 0;
for i := 1 to iSize do
  if arrData[i] > 50 then    // change condition as needed
    Inc(iCount);
```

### Pattern 4 — Linear search

```pascal
bFound := False;
iIndex := 0;
for i := 1 to iSize do
  if arrNames[i] = sSearch then
  begin
    bFound := True;
    iIndex := i;
  end;
```

### Pattern 5 — Input validation (while loop)

```pascal
while (StrToIntDef(edtInput.Text, -1) < 0) or
      (StrToIntDef(edtInput.Text, -1) > 100) do
begin
  ShowMessage('Enter a value between 0 and 100');
  edtInput.SetFocus;
  edtInput.Clear;
end;
iValue := StrToInt(edtInput.Text);
```

### Pattern 6 — Read a text file into an array

```pascal
AssignFile(f, 'data.txt');
Reset(f);
iCount := 0;
while not EOF(f) do
begin
  Inc(iCount);
  ReadLn(f, arrData[iCount]);
end;
CloseFile(f);
```

### Pattern 7 — Build a filtered list

```pascal
lstResults.Items.Clear;
for i := 1 to iCount do
  if arrScores[i] >= 50 then
    lstResults.Items.Add(arrNames[i] + ' — ' + IntToStr(arrScores[i]));
```

### Pattern 8 — Bubble sort (ascending)

```pascal
for i := 1 to iSize - 1 do
  for j := 1 to iSize - i do
    if arrData[j] > arrData[j + 1] then
    begin
      iTemp := arrData[j];
      arrData[j] := arrData[j + 1];
      arrData[j + 1] := iTemp;
    end;
```

::: tip How to learn patterns
Don't just read these. Cover the code, write each pattern from memory, then check. Repeat until you can write any pattern without looking. This is the difference between recognising code and being able to produce it.
:::

---

## 8. SQL Practice Without Access

::: info Grade 12 content
SQL queries are a Grade 12 topic. If you are in Grade 10 or 11, focus on the Delphi programming patterns above first.
:::

SQL can be practised in any web browser — no Windows, no Access, no installation needed.

### Free browser tools

| Tool | URL | Best for |
|------|-----|----------|
| W3Schools SQL Tryit | `w3schools.com/sql/trysql.asp` | Quick SELECT practice with built-in sample data |
| DB Fiddle | `db-fiddle.com` | Create your own tables and test any SQL |
| SQLiteOnline | `sqliteonline.com` | Import a CSV file and query it |

### SQL patterns to know

**Basic SELECT with filtering:**
```sql
SELECT Surname, Name, Score
FROM Students
WHERE Score >= 50
ORDER BY Surname ASC;
```

**Aggregate functions:**
```sql
SELECT Grade, COUNT(*) AS Total, AVG(Score) AS Average
FROM Students
GROUP BY Grade
HAVING AVG(Score) > 60;
```

**JOIN two tables:**
```sql
SELECT Students.Surname, Subjects.SubjectName, Results.Mark
FROM Students
INNER JOIN Results ON Students.StudentID = Results.StudentID
INNER JOIN Subjects ON Results.SubjectID = Subjects.SubjectID
WHERE Results.Mark > 50
ORDER BY Students.Surname;
```

**Data manipulation:**
```sql
INSERT INTO Students (StudentID, Surname, Name, Score)
VALUES (101, 'Dlamini', 'Sipho', 78);

UPDATE Students
SET Score = 82
WHERE StudentID = 101;

DELETE FROM Students
WHERE Score < 30;
```

::: warning SQL case sensitivity
SQL keywords like `SELECT`, `WHERE`, `ORDER BY` are not case sensitive, but values like `'Dlamini'` must match exactly, including capitals.
:::

---

## 9. Online Pascal Compiler

If you have internet access but no Windows PC, you can write and run Pascal code in a browser. The logic is identical to Delphi — only the input/output changes (no GUI form: you use text instead).

### Recommended tools

| Tool | URL | Notes |
|------|-----|-------|
| OnlineGDB | `onlinegdb.com` | Select "Pascal" from the language dropdown |
| Ideone | `ideone.com` | Select "Pascal (fpc)" |

### Translating Delphi to console Pascal

The logic inside a button click is identical to console Pascal. Only the input/output lines change:

| In Delphi (GUI) | In Console Pascal |
|---|---|
| `edtName.Text` | `ReadLn(sName)` |
| `lblResult.Caption := ...` | `WriteLn(...)` |
| `ShowMessage(...)` | `WriteLn(...)` |
| `StrToInt(edtNum.Text)` | `ReadLn(iNum)` (declare as `Integer`) |

**Delphi button click version:**
```pascal
procedure TForm1.btnGreetClick(Sender: TObject);
var
  sName : String;
  iAge  : Integer;
begin
  sName := edtName.Text;
  iAge  := StrToInt(edtAge.Text);
  if iAge >= 18 then
    lblResult.Caption := sName + ' is an adult.'
  else
    lblResult.Caption := sName + ' is a minor.';
end;
```

**Same logic in console Pascal (paste this into OnlineGDB):**
```pascal
program AgeCheck;
var
  sName : String;
  iAge  : Integer;
begin
  Write('Enter name: ');  ReadLn(sName);
  Write('Enter age: ');   ReadLn(iAge);
  if iAge >= 18 then
    WriteLn(sName + ' is an adult.')
  else
    WriteLn(sName + ' is a minor.');
end.
```

If you can write the console version correctly, you can write the Delphi version — just swap the `ReadLn`/`WriteLn` lines for the component equivalents.

---

## 10. A Study Routine That Works

### Without any computer access

| Day | Activity | Time |
|-----|----------|------|
| Monday | Trace 2–3 code examples by hand (use this site's Practical pages) | 30 min |
| Tuesday | Write 2 patterns from memory — check after each one | 30 min |
| Wednesday | Read a worked example, write the pseudocode for it | 30 min |
| Thursday | Write a full solution on paper for one past paper question | 45 min |
| Friday | SQL: write 5 queries on paper (no looking at notes first) | 20 min |
| Weekend | Review everything you got wrong during the week | 30 min |

### With internet access (phone, tablet, or laptop)

Do the above, plus:
- Verify your SQL queries using W3Schools Tryit or DB Fiddle
- Test logic-heavy procedures by translating them to console Pascal on OnlineGDB
- Search YouTube for specific topics you find difficult (search: "Delphi arrays tutorial", "Pascal loops explained", "SQL JOIN explained")

### In the weeks before the exam

- Focus on tracing — not learning new content
- Redo past paper questions you found difficult
- Practise under timed conditions: 45 minutes per question, no pauses
- Use the [Quick Study](../quick-study/) cheat sheets for last-minute revision, not as a crutch during practice
