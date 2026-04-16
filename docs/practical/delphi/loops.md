# Loops — FOR, WHILE, and REPEAT-UNTIL

Loops let your program repeat a block of code multiple times without you writing the same code over and over. They are fundamental to almost every Paper 1 question — especially those involving arrays.

> [!NOTE] Grade 10+
> All three loop types are introduced in Grade 10. Nested loops are extended in Grade 11 and are critical for 2D array questions.

---

## Choosing the Right Loop

| Loop | Use when… | Condition checked | Minimum runs |
|---|---|---|---|
| `FOR` | You know exactly how many times to repeat | Before (implicit in counter) | 1 (if start ≤ end) |
| `WHILE` | You don't know how many times — condition checked first | Before | 0 (may never run) |
| `REPEAT...UNTIL` | You don't know how many times — must run at least once | After | 1 (always) |

---

## The FOR Loop

### Counting Up (TO)

```pascal
FOR iCounter := iStart TO iEnd DO
BEGIN
  // body — runs once for each value from iStart to iEnd
END;
```

**Example — print 1 to 10:**
```pascal
procedure TForm1.btnCountClick(Sender: TObject);
var
  i : Integer;
begin
  redOutput.Lines.Clear;
  FOR i := 1 TO 10 DO
  BEGIN
    redOutput.Lines.Add(IntToStr(i));
  END;
end;
```

### Counting Down (DOWNTO)

```pascal
FOR iCounter := iEnd DOWNTO iStart DO
BEGIN
  // body — runs from iEnd down to iStart
END;
```

**Example — countdown from 10:**
```pascal
FOR i := 10 DOWNTO 1 DO
  redOutput.Lines.Add(IntToStr(i) + '...');
redOutput.Lines.Add('GO!');
```

### Sum of numbers using FOR:
```pascal
procedure TForm1.btnSumClick(Sender: TObject);
var
  i, iTotal, iN : Integer;
begin
  iN     := StrToInt(edtN.Text);  // e.g. sum from 1 to N
  iTotal := 0;

  FOR i := 1 TO iN DO
    iTotal := iTotal + i;

  lblResult.Caption := 'Sum = ' + IntToStr(iTotal);
end;
```

> [!WARNING] Common Mistake — Semicolon After DO
> A semicolon directly after `DO` creates an **empty loop body**. Your loop runs the correct number of times but does nothing:
> ```pascal
> // WRONG — loop body is the empty statement after the semicolon ❌
> FOR i := 1 TO 10 DO;
>   redOutput.Lines.Add('Hello');   // only runs ONCE after the loop
>
> // CORRECT ✓
> FOR i := 1 TO 10 DO
>   redOutput.Lines.Add('Hello');   // runs 10 times
> ```

---

## The WHILE Loop

Use when the number of repetitions is **unknown** and you might need to repeat **zero times** (if the condition is already false at the start).

```pascal
WHILE <condition> DO
BEGIN
  // body — runs only while condition is TRUE
  // IMPORTANT: something inside must eventually make condition FALSE
END;
```

**Example — keep doubling a number until it exceeds 1000:**
```pascal
procedure TForm1.btnDoubleClick(Sender: TObject);
var
  iNum : Integer;
begin
  iNum := 1;
  redOutput.Lines.Clear;

  WHILE iNum <= 1000 DO
  BEGIN
    redOutput.Lines.Add(IntToStr(iNum));
    iNum := iNum * 2;
  END;
end;
```

**Example — validate input (accept only positive numbers):**
```pascal
// In a console-style scenario:
WHILE iNum <= 0 DO
BEGIN
  ShowMessage('Enter a POSITIVE number.');
  iNum := StrToInt(InputBox('Input', 'Number:', ''));
END;
```

> [!WARNING] Infinite Loop Risk
> If the condition in a WHILE loop **never becomes false**, the loop runs forever and freezes the application. Always make sure something inside the loop changes the variable that the condition checks.

---

## The REPEAT...UNTIL Loop

Use when the body **must run at least once** — the condition is checked at the END of each iteration (not the start).

```pascal
REPEAT
  // body — always runs at least once
UNTIL <condition>;  // loop STOPS when this is TRUE
```

> [!NOTE] UNTIL Stops — Not Continues
> This is the opposite of WHILE. WHILE loops while the condition is TRUE. REPEAT loops UNTIL the condition becomes TRUE (then stops).

**Example — menu that repeats until user quits:**
```pascal
procedure TForm1.btnMenuClick(Sender: TObject);
var
  iChoice : Integer;
begin
  REPEAT
    iChoice := StrToInt(InputBox('Menu', '1=Add  2=Delete  0=Quit', ''));

    CASE iChoice OF
      1 : ShowMessage('Add selected');
      2 : ShowMessage('Delete selected');
      0 : ShowMessage('Goodbye!');
    ELSE
      ShowMessage('Invalid option');
    END;
  UNTIL iChoice = 0;
end;
```

**Example — sum numbers until user enters 0:**
```pascal
procedure TForm1.btnSumClick(Sender: TObject);
var
  iNum, iTotal : Integer;
begin
  iTotal := 0;

  REPEAT
    iNum   := StrToInt(InputBox('Sum', 'Enter a number (0 to stop):', ''));
    iTotal := iTotal + iNum;
  UNTIL iNum = 0;

  lblTotal.Caption := 'Total = ' + IntToStr(iTotal);
end;
```

---

## Nested Loops

> [!TIP] Grade 11 — Extension
> Nested loops are essential for 2D arrays and multiplication tables. A loop inside another loop multiplies the number of iterations.

A nested loop has one loop entirely inside another:

```pascal
FOR iOuter := 1 TO rows DO
BEGIN
  FOR iInner := 1 TO cols DO
  BEGIN
    // this body runs rows × cols times total
  END;
END;
```

**Example — multiplication table (times table):**
```pascal
procedure TForm1.btnTableClick(Sender: TObject);
var
  i, j : Integer;
  sRow : String;
begin
  redOutput.Lines.Clear;

  FOR i := 1 TO 10 DO
  BEGIN
    sRow := '';
    FOR j := 1 TO 10 DO
    BEGIN
      sRow := sRow + Format('%4d', [i * j]);
    END;
    redOutput.Lines.Add(sRow);
  END;
end;
```

This produces a 10×10 times table grid.

**Counting nested loop iterations:**

If the outer loop runs 5 times and the inner loop runs 3 times:
```
Total iterations of the inner body = 5 × 3 = 15
```

---

## Loop Summary with Exam Examples

### "Count how many values in an array are above average"
Requires: (1) FOR loop to calculate sum, (2) Calculate average, (3) FOR loop to count items above average.

```pascal
procedure TForm1.btnAnalyseClick(Sender: TObject);
const
  MAX = 10;
var
  aScores         : array[1..MAX] of Integer;
  i, iSum, iCount : Integer;
  rAvg            : Real;
begin
  // Load array (in real exam, these would be filled already)
  iSum := 0;
  FOR i := 1 TO MAX DO
    iSum := iSum + aScores[i];

  rAvg   := iSum / MAX;
  iCount := 0;

  FOR i := 1 TO MAX DO
    IF aScores[i] > rAvg THEN
      iCount := iCount + 1;

  lblResult.Caption := IntToStr(iCount) + ' scores above average';
end;
```

---

## Common Mistakes Summary

> [!WARNING] Common Mistakes
> 1. **Semicolon after `DO`** in FOR loop — creates an empty loop body
> 2. **Forgetting to update the counter** in WHILE — causes infinite loop
> 3. **UNTIL condition is wrong way around** — remember: UNTIL stops the loop (condition = TRUE to stop)
> 4. **Off-by-one errors** — e.g. looping `FOR i := 0 TO MAX` when array is `[1..MAX]` causes access violations
> 5. **Modifying the FOR loop counter** inside the loop — undefined behaviour in Delphi; never do this
> 6. **Nested loop variable names reused** — use different counter names (i and j, not i and i)

---

## Practice Exercises

**Exercise 1 — Sum of even numbers**

Use a FOR loop to sum all even numbers from 1 to 100 and display the result in `lblSum`.

<details>
<summary>Show solution</summary>

```pascal
procedure TForm1.btnSumEvenClick(Sender: TObject);
var
  i, iSum : Integer;
begin
  iSum := 0;
  FOR i := 2 TO 100 DO
  BEGIN
    IF i MOD 2 = 0 THEN
      iSum := iSum + i;
  END;
  lblSum.Caption := 'Sum of evens = ' + IntToStr(iSum);
end;
```
</details>

---

**Exercise 2 — Factorial using WHILE**

Calculate n! (factorial) for a number entered in `edtN` and show in `lblResult`.
*(Remember: 5! = 5 × 4 × 3 × 2 × 1 = 120)*

<details>
<summary>Show solution</summary>

```pascal
procedure TForm1.btnFactClick(Sender: TObject);
var
  iN, iCounter, iResult : Integer;
begin
  iN       := StrToInt(edtN.Text);
  iResult  := 1;
  iCounter := iN;

  WHILE iCounter >= 1 DO
  BEGIN
    iResult  := iResult * iCounter;
    iCounter := iCounter - 1;
  END;

  lblResult.Caption := IntToStr(iN) + '! = ' + IntToStr(iResult);
end;
```
</details>

---

**Exercise 3 — Repeat until valid**

Use REPEAT...UNTIL to keep asking the user for a number between 1 and 10 (using InputBox) until they enter a valid one.

<details>
<summary>Show solution</summary>

```pascal
procedure TForm1.btnValidClick(Sender: TObject);
var
  iNum : Integer;
begin
  REPEAT
    iNum := StrToInt(InputBox('Input', 'Enter a number between 1 and 10:', ''));
    IF (iNum < 1) OR (iNum > 10) THEN
      ShowMessage('Invalid! Must be between 1 and 10.');
  UNTIL (iNum >= 1) AND (iNum <= 10);

  ShowMessage('Valid number entered: ' + IntToStr(iNum));
end;
```
</details>

---

> [!TIP] Exam Tip
> FOR loops are used in ~80% of array questions. WHILE and REPEAT are usually standalone or used for validation. In exam scenarios where you see "keep asking until valid input is received", that is always REPEAT...UNTIL. When you see "process every element in an array", that is always FOR.
