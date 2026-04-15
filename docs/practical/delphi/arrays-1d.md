# 1D Arrays

When you need to store and process a **collection of values of the same type**, an array is the tool. Instead of declaring 10 separate variables, you declare one array with 10 slots.

> [!NOTE] Grade 10+
> 1D arrays are introduced in Grade 10 and are one of the highest-weighted topics in Paper 1. Every year there is at least one significant array question.

---

## What is an Array?

An **array** is a fixed-size collection of variables of the **same data type**, stored under one name and accessed by a numbered index.

```
aScores[1]  aScores[2]  aScores[3]  aScores[4]  aScores[5]
   78           85           91           67           88
```

- All values are the same type (Integer here)
- Each slot has an **index** (position number)
- In Delphi, arrays can be **1-based** (starting at 1) — which is most common in SA IT exams

---

## Declaring an Array

```pascal
var
  aScores  : array[1..10] of Integer;   // 10 integers, indexed 1 to 10
  aNames   : array[1..5]  of String;    // 5 strings
  aPrices  : array[0..9]  of Real;      // 10 reals, indexed 0 to 9
  aFlags   : array[1..3]  of Boolean;   // 3 booleans
```

The syntax is: `array[startIndex..endIndex] of DataType`

> [!TIP] 1-Based vs 0-Based
> South African IT exams typically use **1-based arrays** (`array[1..n]`). This matches how we count naturally. Some textbooks use 0-based — always check what the exam question declares.

---

## Using a Constant for Array Size

Hardcoding the size everywhere is risky. Use a `const` instead:

```pascal
const
  MAX = 10;
var
  aScores : array[1..MAX] of Integer;
  i       : Integer;
```

Now if you change the size, you only change one line.

---

## Filling an Array (Input)

### Manual input from edit boxes

```pascal
aScores[1] := StrToInt(edtScore1.Text);
aScores[2] := StrToInt(edtScore2.Text);
// ...not practical for large arrays
```

### Loop input (the standard exam approach)

```pascal
procedure TForm1.btnLoadClick(Sender: TObject);
const
  MAX = 5;
var
  aScores : array[1..MAX] of Integer;
  i       : Integer;
begin
  FOR i := 1 TO MAX DO
  BEGIN
    aScores[i] := StrToInt(InputBox('Input', 'Enter score ' + IntToStr(i) + ':', ''));
  END;
end;
```

### Pre-filled array (exam scenario — already given to you)

Exams often say "the array has already been populated." You don't need input code — just write the processing part.

---

## Reading / Displaying an Array

```pascal
procedure TForm1.btnDisplayClick(Sender: TObject);
const
  MAX = 5;
var
  aScores : array[1..MAX] of Integer;
  i       : Integer;
begin
  // assume array is already filled
  redOutput.Lines.Clear;
  FOR i := 1 TO MAX DO
    redOutput.Lines.Add('Score ' + IntToStr(i) + ': ' + IntToStr(aScores[i]));
end;
```

---

## Common Array Algorithms

These five algorithms appear in almost every exam. Practise them until they are automatic.

### 1. Sum and Average

```pascal
var
  i, iSum  : Integer;
  rAverage : Real;
begin
  iSum := 0;

  FOR i := 1 TO MAX DO
    iSum := iSum + aScores[i];

  rAverage := iSum / MAX;

  lblSum.Caption := 'Sum = ' + IntToStr(iSum);
  lblAvg.Caption := 'Average = ' + FloatToStrF(rAverage, ffFixed, 8, 2);
end;
```

### 2. Find Maximum (Largest Value)

```pascal
var
  i, iMax : Integer;
begin
  iMax := aScores[1];   // assume first element is the max

  FOR i := 2 TO MAX DO   // start at 2, already set index 1
  BEGIN
    IF aScores[i] > iMax THEN
      iMax := aScores[i];
  END;

  lblMax.Caption := 'Highest score: ' + IntToStr(iMax);
end;
```

### 3. Find Minimum (Smallest Value)

```pascal
iMin := aScores[1];

FOR i := 2 TO MAX DO
BEGIN
  IF aScores[i] < iMin THEN
    iMin := aScores[i];
END;
```

### 4. Count Items Meeting a Condition

```pascal
// Count how many scores are above the average
iCount := 0;

FOR i := 1 TO MAX DO
BEGIN
  IF aScores[i] > rAverage THEN
    iCount := iCount + 1;
END;

lblCount.Caption := IntToStr(iCount) + ' scores above average';
```

### 5. Search for a Value (Linear Search)

```pascal
var
  iTarget, i  : Integer;
  bFound      : Boolean;
  iFoundIndex : Integer;
begin
  iTarget    := StrToInt(edtSearch.Text);
  bFound     := False;
  iFoundIndex := 0;

  FOR i := 1 TO MAX DO
  BEGIN
    IF aScores[i] = iTarget THEN
    BEGIN
      bFound      := True;
      iFoundIndex := i;
    END;
  END;

  IF bFound THEN
    lblResult.Caption := 'Found at index ' + IntToStr(iFoundIndex)
  ELSE
    lblResult.Caption := 'Value not found';
end;
```

---

## Combining Multiple Algorithms

Exams often ask you to do several things in one procedure. Structure your code in clear sections:

```pascal
procedure TForm1.btnAnalyseClick(Sender: TObject);
const
  MAX = 10;
var
  aScores              : array[1..MAX] of Integer;
  i, iSum, iMax, iMin  : Integer;
  iAboveAvg            : Integer;
  rAverage             : Real;
begin
  // ── Section 1: Sum and average ─────────────────────
  iSum := 0;
  FOR i := 1 TO MAX DO
    iSum := iSum + aScores[i];
  rAverage := iSum / MAX;

  // ── Section 2: Max and min ─────────────────────────
  iMax := aScores[1];
  iMin := aScores[1];
  FOR i := 2 TO MAX DO
  BEGIN
    IF aScores[i] > iMax THEN iMax := aScores[i];
    IF aScores[i] < iMin THEN iMin := aScores[i];
  END;

  // ── Section 3: Count above average ─────────────────
  iAboveAvg := 0;
  FOR i := 1 TO MAX DO
    IF aScores[i] > rAverage THEN
      Inc(iAboveAvg);

  // ── Display ────────────────────────────────────────
  redOutput.Lines.Clear;
  redOutput.Lines.Add('Sum:            ' + IntToStr(iSum));
  redOutput.Lines.Add('Average:        ' + FloatToStrF(rAverage, ffFixed, 8, 2));
  redOutput.Lines.Add('Highest:        ' + IntToStr(iMax));
  redOutput.Lines.Add('Lowest:         ' + IntToStr(iMin));
  redOutput.Lines.Add('Above average:  ' + IntToStr(iAboveAvg));
end;
```

---

## Swapping Two Values

Swapping requires a **temporary variable**:

```pascal
var
  iTemp : Integer;
begin
  // Swap aScores[3] and aScores[7]
  iTemp       := aScores[3];
  aScores[3]  := aScores[7];
  aScores[7]  := iTemp;
end;
```

> [!WARNING] Never swap without a temp variable
> Doing `aScores[3] := aScores[7]; aScores[7] := aScores[3]` doesn't work — the first line overwrites `aScores[3]` before you've saved its value.

---

## Common Mistakes

> [!WARNING] Watch Out For
> 1. **Index out of range** — accessing `aScores[0]` on a `[1..MAX]` array causes a runtime error
> 2. **Forgetting to initialise iMax/iMin** — always set them to `aScores[1]`, not to 0
> 3. **Not clearing sum variable** — `iSum` must start at 0 before the loop
> 4. **Loop from 1 to MAX when checking array already given** — don't re-fill if already loaded
> 5. **Dividing by MAX for average when MAX = 0** — validate that the array has elements

---

## Practice Exercises

**Exercise 1 — Basic array operations**

An array `aNums` of 8 integers has been filled. Write code to:
a) Display all values in a RichEdit
b) Find and display the sum
c) Find and display the maximum value

<details>
<summary>Show solution</summary>

```pascal
const
  MAX = 8;
var
  aNums : array[1..MAX] of Integer;
  i, iSum, iMax : Integer;
begin
  // Assume aNums is already populated

  redOutput.Lines.Clear;
  iSum := 0;
  iMax := aNums[1];

  FOR i := 1 TO MAX DO
  BEGIN
    redOutput.Lines.Add(IntToStr(aNums[i]));
    iSum := iSum + aNums[i];
    IF aNums[i] > iMax THEN
      iMax := aNums[i];
  END;

  redOutput.Lines.Add('Sum = ' + IntToStr(iSum));
  redOutput.Lines.Add('Max = ' + IntToStr(iMax));
end;
```
</details>

---

**Exercise 2 — Count and display**

Given an array of 10 test marks, display only the marks that are below 50 (failing), and count how many there are.

<details>
<summary>Show solution</summary>

```pascal
const
  MAX = 10;
var
  aMarks : array[1..MAX] of Integer;
  i, iCount : Integer;
begin
  iCount := 0;
  redOutput.Lines.Clear;
  redOutput.Lines.Add('Failing marks:');

  FOR i := 1 TO MAX DO
  BEGIN
    IF aMarks[i] < 50 THEN
    BEGIN
      redOutput.Lines.Add('  [' + IntToStr(i) + '] ' + IntToStr(aMarks[i]));
      Inc(iCount);
    END;
  END;

  redOutput.Lines.Add('Total failing: ' + IntToStr(iCount));
end;
```
</details>

---

> [!TIP] Exam Tip
> In Paper 1 questions involving arrays, read the question all the way through before coding. Questions often chain: fill array → process → display. Know which part you're asked for — sometimes the fill code is given and you only write the processing. Misreading the question is the most common cause of lost marks.
