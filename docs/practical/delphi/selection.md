# Selection — IF and CASE Statements

Use selection when your code needs to **make a decision** and follow different paths based on a condition. It is the most common construct in any Delphi exam question.

> [!NOTE] Grade 10+
> Selection (IF and CASE) is introduced in Grade 10 and appears in every Paper 1 exam. Master this before anything else.

---

## The IF Statement

### Basic IF (no else)

Use when you only need to act if the condition is true — nothing happens otherwise.

```pascal
IF <condition> THEN
BEGIN
  // statements that run only when condition is TRUE
END;
```

**Example — check if number is positive:**
```pascal
procedure TForm1.btnCheckClick(Sender: TObject);
var
  iNum : Integer;
begin
  iNum := StrToInt(edtNumber.Text);

  IF iNum > 0 THEN
  BEGIN
    lblResult.Caption := 'The number is positive';
  END;
end;
```

---

### IF...ELSE

Use when you need to do one thing if true, a different thing if false.

```pascal
IF <condition> THEN
BEGIN
  // runs when TRUE
END
ELSE
BEGIN
  // runs when FALSE
END;
```

> [!WARNING] Common Mistake — Semicolon Before ELSE
> **NEVER** put a semicolon after the `END` that precedes `ELSE`. A semicolon ends the IF statement — Delphi then sees a dangling `ELSE` and throws a compiler error.
> ```pascal
> // WRONG ❌
> END;       ← semicolon kills the ELSE
> ELSE
> 
> // CORRECT ✓
> END
> ELSE
> ```

**Example — pass or fail:**
```pascal
procedure TForm1.btnCheckClick(Sender: TObject);
var
  iMark : Integer;
begin
  iMark := StrToInt(edtMark.Text);

  IF iMark >= 50 THEN
  BEGIN
    lblResult.Caption := 'PASSED';
  END
  ELSE
  BEGIN
    lblResult.Caption := 'FAILED';
  END;
end;
```

---

### IF...ELSE IF...ELSE (Nested / Chained)

Use when you have more than two possible outcomes. Think of it as a ladder — Delphi checks each condition from top to bottom and **stops at the first true one**.

```pascal
IF <condition1> THEN
BEGIN
  // runs when condition1 is TRUE
END
ELSE IF <condition2> THEN
BEGIN
  // runs when condition2 is TRUE
END
ELSE IF <condition3> THEN
BEGIN
  // runs when condition3 is TRUE
END
ELSE
BEGIN
  // runs when ALL conditions are FALSE
END;
```

**Example — grade classification:**
```pascal
procedure TForm1.btnGradeClick(Sender: TObject);
var
  iMark : Integer;
  sGrade : String;
begin
  iMark := StrToInt(edtMark.Text);

  IF iMark >= 80 THEN
    sGrade := 'Distinction (Level 7)'
  ELSE IF iMark >= 70 THEN
    sGrade := 'Merit (Level 6)'
  ELSE IF iMark >= 60 THEN
    sGrade := 'Substantial Achievement (Level 5)'
  ELSE IF iMark >= 50 THEN
    sGrade := 'Adequate Achievement (Level 4)'
  ELSE IF iMark >= 40 THEN
    sGrade := 'Moderate Achievement (Level 3)'
  ELSE IF iMark >= 30 THEN
    sGrade := 'Elementary Achievement (Level 2)'
  ELSE
    sGrade := 'Not Achieved (Level 1)';

  lblGrade.Caption := sGrade;
end;
```

> [!TIP] Single Statement — No BEGIN/END Needed
> If there is only ONE statement after THEN or ELSE, BEGIN/END is optional. For readability and safety, many teachers still recommend using it. In exams, both styles are accepted — but single-statement form saves time.

---

## Logical Operators

Combine multiple conditions in one IF using **AND**, **OR**, and **NOT**.

| Operator | Meaning | Both/Either must be true? |
|---|---|---|
| `AND` | Both conditions must be true | Both |
| `OR` | At least one condition must be true | Either |
| `NOT` | Reverses the condition | — |

> [!WARNING] Always Use Brackets with AND / OR
> Delphi's operator precedence can cause bugs if you don't bracket compound conditions.
> ```pascal
> // WRONG — unpredictable results ❌
> IF x > 0 AND y > 0 THEN
> 
> // CORRECT — bracket each sub-condition ✓
> IF (x > 0) AND (y > 0) THEN
> ```

**Example — valid age and pass:**
```pascal
IF (iAge >= 18) AND (iMark >= 50) THEN
  lblResult.Caption := 'Eligible'
ELSE
  lblResult.Caption := 'Not eligible';
```

**Example — weekend check:**
```pascal
IF (iDay = 6) OR (iDay = 7) THEN
  lblDay.Caption := 'It is the weekend!'
ELSE
  lblDay.Caption := 'It is a weekday.';
```

**Example — NOT:**
```pascal
IF NOT (sPassword = 'admin123') THEN
  lblMsg.Caption := 'Incorrect password';
```

---

## The CASE Statement

Use CASE when you are comparing **one variable** against many **specific values**. It is cleaner and faster to read than a long chain of `ELSE IF` statements.

```pascal
CASE <variable or expression> OF
  value1 : <single statement>;
  value2 : BEGIN
              // multiple statements
            END;
  value3, value4 : <statement>;   // comma separates multiple matching values
  5..10 :  <statement>;           // range using ..
ELSE
  <statement>   // runs if none of the values matched
END;
```

> [!NOTE] CASE Only Works with Ordinal Types
> CASE works with Integer, Char, and Boolean — **not** with String or Real. If you need to compare strings, use IF...ELSE IF.

**Example — day of week from number:**
```pascal
procedure TForm1.btnDayClick(Sender: TObject);
var
  iDay : Integer;
begin
  iDay := StrToInt(edtDay.Text);

  CASE iDay OF
    1 : lblDay.Caption := 'Monday';
    2 : lblDay.Caption := 'Tuesday';
    3 : lblDay.Caption := 'Wednesday';
    4 : lblDay.Caption := 'Thursday';
    5 : lblDay.Caption := 'Friday';
    6, 7 : lblDay.Caption := 'Weekend';
  ELSE
    lblDay.Caption := 'Invalid day number';
  END;
end;
```

**Example — character vowel check:**
```pascal
procedure TForm1.btnVowelClick(Sender: TObject);
var
  cLetter : Char;
begin
  cLetter := UpCase(edtLetter.Text[1]);

  CASE cLetter OF
    'A', 'E', 'I', 'O', 'U' : lblResult.Caption := 'Vowel';
  ELSE
    lblResult.Caption := 'Consonant';
  END;
end;
```

**Example — menu selection with range:**
```pascal
CASE iChoice OF
  1    : // Option 1 code
  2    : // Option 2 code
  3    : // Option 3 code
  4..9 : ShowMessage('Options 4–9 not yet implemented');
ELSE
  ShowMessage('Invalid selection. Enter 1–9.');
END;
```

---

## IF vs CASE — When to Use Which

| Scenario | Use |
|---|---|
| Comparing against a range (e.g. mark >= 80) | **IF...ELSE IF** |
| Comparing a string variable | **IF...ELSE IF** |
| Comparing one integer/char against specific values | **CASE** |
| More than ~4 specific values to check | **CASE** (cleaner) |
| Complex compound conditions (AND/OR) | **IF** |

---

## Common Mistakes

> [!WARNING] Watch Out For
> 1. **Semicolon before ELSE** — removes the ELSE from the IF structure entirely
> 2. **Missing BEGIN/END** for multiple statements — only the first statement runs in the IF branch
> 3. **Wrong comparison operator** — use `=` in conditions (not `:=` which is assignment)
> 4. **No brackets on AND/OR conditions** — causes incorrect operator precedence
> 5. **CASE with a String variable** — compiler error: CASE only accepts ordinal types
> 6. **Overlapping CASE values** — if two cases could match, only the first one runs

---

## Practice Exercises

**Exercise 1 — Positive, negative, or zero**

Write a procedure that reads a number from `edtNumber` and displays whether it is positive, negative, or zero in `lblResult`.

<details>
<summary>Show solution</summary>

```pascal
procedure TForm1.btnCheckClick(Sender: TObject);
var
  iNum : Integer;
begin
  iNum := StrToInt(edtNumber.Text);

  IF iNum > 0 THEN
    lblResult.Caption := 'Positive'
  ELSE IF iNum < 0 THEN
    lblResult.Caption := 'Negative'
  ELSE
    lblResult.Caption := 'Zero';
end;
```
</details>

---

**Exercise 2 — Month name from number**

Write a CASE statement that converts a number (1–12) entered in `edtMonth` to its month name displayed in `lblMonth`. Show an error message for invalid input.

<details>
<summary>Show solution</summary>

```pascal
procedure TForm1.btnMonthClick(Sender: TObject);
var
  iMonth : Integer;
begin
  iMonth := StrToInt(edtMonth.Text);

  CASE iMonth OF
    1  : lblMonth.Caption := 'January';
    2  : lblMonth.Caption := 'February';
    3  : lblMonth.Caption := 'March';
    4  : lblMonth.Caption := 'April';
    5  : lblMonth.Caption := 'May';
    6  : lblMonth.Caption := 'June';
    7  : lblMonth.Caption := 'July';
    8  : lblMonth.Caption := 'August';
    9  : lblMonth.Caption := 'September';
    10 : lblMonth.Caption := 'October';
    11 : lblMonth.Caption := 'November';
    12 : lblMonth.Caption := 'December';
  ELSE
    lblMonth.Caption := 'Invalid month';
  END;
end;
```
</details>

---

**Exercise 3 — BMI category**

BMI value is stored in `rBMI` (Real). Display the category in `lblCategory`:
- Below 18.5 → Underweight
- 18.5 to 24.9 → Normal weight
- 25 to 29.9 → Overweight
- 30 or above → Obese

<details>
<summary>Show solution</summary>

```pascal
procedure TForm1.btnBMIClick(Sender: TObject);
var
  rBMI : Real;
begin
  rBMI := StrToFloat(edtBMI.Text);

  IF rBMI < 18.5 THEN
    lblCategory.Caption := 'Underweight'
  ELSE IF rBMI < 25.0 THEN
    lblCategory.Caption := 'Normal weight'
  ELSE IF rBMI < 30.0 THEN
    lblCategory.Caption := 'Overweight'
  ELSE
    lblCategory.Caption := 'Obese';
end;
```
</details>

---

> [!TIP] Exam Tip
> In Paper 1, selection is rarely the only construct in a question — you'll usually combine it with loops or arrays. Practise nested IF inside a FOR loop (e.g. "loop through an array and find all items above a threshold"). That is the most common combined question format.
