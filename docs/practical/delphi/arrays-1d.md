# 1D Arrays

When you need to store and process a **collection of values of the same type**, an array is the tool. Instead of declaring 10 separate variables, you declare one array with 10 slots.

> [!NOTE] Grade 11+
> 1D arrays are introduced in Grade 11 (CAPS) and are one of the highest-weighted topics in Paper 1. Every year there is at least one significant array question. Grade 11 must know **bubble sort**, **selection sort**, **linear search** and **binary search**.

---

## What is an Array?

An **array** is a fixed-size collection of variables of the **same data type**, stored under one name and accessed by a numbered index.

<div>
  <div class="itg-array-name">aScores</div>
  <div class="itg-array-vis">
    <div class="itg-array-cell"><div class="itg-array-box">78</div><div class="itg-array-idx">[1]</div></div>
    <div class="itg-array-cell"><div class="itg-array-box">85</div><div class="itg-array-idx">[2]</div></div>
    <div class="itg-array-cell"><div class="itg-array-box">91</div><div class="itg-array-idx">[3]</div></div>
    <div class="itg-array-cell"><div class="itg-array-box">67</div><div class="itg-array-idx">[4]</div></div>
    <div class="itg-array-cell"><div class="itg-array-box">88</div><div class="itg-array-idx">[5]</div></div>
  </div>
</div>

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

## Sorting: Bubble Sort

Bubble sort compares **adjacent elements** and swaps them if they are in the wrong order. After each full pass, the largest unsorted value "bubbles" to its correct position at the end.

**Bubble sort pass-by-pass** — Array: `[5, 3, 8, 1, 9]` sorting ascending:

<div class="itg-sort-wrap">
  <div class="itg-sort-title">Bubble Sort — [5, 3, 8, 1, 9]</div>

  <div class="itg-sort-row">
    <span class="itg-sort-lbl">Start</span>
    <span class="itg-sort-cell">5</span>
    <span class="itg-sort-cell">3</span>
    <span class="itg-sort-cell">8</span>
    <span class="itg-sort-cell">1</span>
    <span class="itg-sort-cell">9</span>
  </div>

  <div class="itg-sort-row">
    <span class="itg-sort-lbl">Pass 1</span>
    <span class="itg-sort-cell swapped">3</span>
    <span class="itg-sort-cell swapped">5</span>
    <span class="itg-sort-cell swapped">1</span>
    <span class="itg-sort-cell swapped">8</span>
    <span class="itg-sort-cell locked">9</span>
    <span class="itg-sort-note">9 locked in</span>
  </div>

  <div class="itg-sort-row">
    <span class="itg-sort-lbl">Pass 2</span>
    <span class="itg-sort-cell">3</span>
    <span class="itg-sort-cell swapped">1</span>
    <span class="itg-sort-cell swapped">5</span>
    <span class="itg-sort-cell locked">8</span>
    <span class="itg-sort-cell locked">9</span>
    <span class="itg-sort-note">8, 9 locked</span>
  </div>

  <div class="itg-sort-row">
    <span class="itg-sort-lbl">Pass 3</span>
    <span class="itg-sort-cell swapped">1</span>
    <span class="itg-sort-cell swapped">3</span>
    <span class="itg-sort-cell locked">5</span>
    <span class="itg-sort-cell locked">8</span>
    <span class="itg-sort-cell locked">9</span>
    <span class="itg-sort-note">5, 8, 9 locked</span>
  </div>

  <div class="itg-sort-row">
    <span class="itg-sort-lbl">Pass 4</span>
    <span class="itg-sort-cell locked">1</span>
    <span class="itg-sort-cell locked">3</span>
    <span class="itg-sort-cell locked">5</span>
    <span class="itg-sort-cell locked">8</span>
    <span class="itg-sort-cell locked">9</span>
  </div>

  <div class="itg-sort-row">
    <span class="itg-sort-lbl done">Sorted</span>
    <span class="itg-sort-cell locked">1</span>
    <span class="itg-sort-cell locked">3</span>
    <span class="itg-sort-cell locked">5</span>
    <span class="itg-sort-cell locked">8</span>
    <span class="itg-sort-cell locked">9</span>
  </div>

  <div class="itg-sort-legend">
    <span class="itg-sort-legend-item"><span class="itg-sort-legend-swatch itg-swatch-swap"></span> swapped this pass</span>
    <span class="itg-sort-legend-item"><span class="itg-sort-legend-swatch itg-swatch-lock"></span> locked in final position</span>
  </div>
</div>

**Delphi implementation:**

```pascal
procedure BubbleSort(var aScores: TArray; iSize: Integer);
var
  i, j, iTemp : Integer;
begin
  FOR i := 1 TO iSize - 1 DO          // number of passes
  BEGIN
    FOR j := 1 TO iSize - i DO        // compare adjacent pairs
    BEGIN
      IF aScores[j] > aScores[j + 1] THEN
      BEGIN
        iTemp          := aScores[j];
        aScores[j]     := aScores[j + 1];
        aScores[j + 1] := iTemp;
      END;
    END;
  END;
end;
```

> [!TIP] Why `iSize - i` in the inner loop?
> After each pass, the last `i` elements are already in their final position — no need to compare them again. This makes bubble sort slightly more efficient.


### Sorting in descending order

Change **only the comparison**: `>` sorts ascending and `<` sorts descending.

```pascal
IF aScores[j] < aScores[j + 1] THEN     // descending: bigger values move to the front
```

---

## Sorting: Selection Sort

Selection sort finds the **smallest** (or largest) value in the unsorted part and swaps it into the next position, one position at a time.

```text
Start:   [ 5 | 9 | 1 | 8 | 3 ]
Pass 1:  [ 1 | 9 | 5 | 8 | 3 ]   smallest (1) swapped into position 1
Pass 2:  [ 1 | 3 | 5 | 8 | 9 ]   smallest of the rest (3) into position 2
Pass 3:  [ 1 | 3 | 5 | 8 | 9 ]   5 already in place
Pass 4:  [ 1 | 3 | 5 | 8 | 9 ]   done
```

```pascal
FOR i := 1 TO MAX - 1 DO
BEGIN
  iMin := i;                              // assume position i holds the smallest
  FOR j := i + 1 TO MAX DO
    IF aScores[j] < aScores[iMin] THEN    // use > for descending
      iMin := j;                          // remember where the smallest is
  IF iMin <> i THEN
  BEGIN
    iTemp := aScores[i];                  // one swap per pass
    aScores[i] := aScores[iMin];
    aScores[iMin] := iTemp;
  END;
END;
```

> [!TIP] Bubble vs selection
> **Bubble sort** compares neighbours and may swap many times per pass. **Selection sort** searches the whole unsorted part and swaps **at most once** per pass. Both use two nested loops. Learn both: CAPS expects Grade 11 learners to know each one.

A common exam alternative that is also accepted as a selection-style sort compares position `i` with every later position `j` and swaps immediately:

```pascal
FOR i := 1 TO MAX - 1 DO
  FOR j := i + 1 TO MAX DO
    IF aScores[j] < aScores[i] THEN
    BEGIN
      iTemp := aScores[i];
      aScores[i] := aScores[j];
      aScores[j] := iTemp;
    END;
```

---

## Sorting Parallel Arrays

When two arrays belong together (e.g. `aNames[3]` is the learner who scored `aScores[3]`), **every swap must be done in both arrays**. Otherwise the names end up next to the wrong scores.

```pascal
// Sort by score, highest first, keeping names linked
FOR i := 1 TO MAX - 1 DO
  FOR j := i + 1 TO MAX DO
    IF aScores[j] > aScores[i] THEN
    BEGIN
      iTemp := aScores[i];  aScores[i] := aScores[j];  aScores[j] := iTemp;   // swap scores
      sTemp := aNames[i];   aNames[i]  := aNames[j];   aNames[j]  := sTemp;   // swap names too
    END;
```

> [!WARNING] Two temp variables
> The temporary variable must have the **same type** as the array it swaps, so you need an Integer `iTemp` for the scores and a String `sTemp` for the names.

---

## Searching: Binary Search

A **linear search** checks every element one by one. A **binary search** only works on a **sorted** array. It checks the **middle** element and throws away the half that cannot contain the value, again and again.

```text
Find 30 in:  [3 | 8 | 12 | 17 | 21 | 26 | 30 | 35 | 41 | 47]
               1   2    3    4    5    6    7    8    9   10
Low=1  High=10 Mid=5  → 21 < 30, search the right half: Low = 6
Low=6  High=10 Mid=8  → 35 > 30, search the left half:  High = 7
Low=6  High=7  Mid=6  → 26 < 30, Low = 7
Low=7  High=7  Mid=7  → 30 = 30, FOUND at position 7
```

```pascal
iLow := 1;
iHigh := MAX;
bFound := False;
WHILE (iLow <= iHigh) AND (NOT bFound) DO
BEGIN
  iMid := (iLow + iHigh) DIV 2;
  IF aKennels[iMid] = iSearch THEN
    bFound := True
  ELSE IF aKennels[iMid] < iSearch THEN
    iLow := iMid + 1                      // value is in the right half
  ELSE
    iHigh := iMid - 1;                    // value is in the left half
END;
IF bFound THEN
  ShowMessage('Found at position ' + IntToStr(iMid))
ELSE
  ShowMessage('Not found');
```

| | Linear search | Binary search |
|---|---|---|
| Array must be sorted? | No | **Yes** |
| How it works | Checks every element in order | Halves the search area each time |
| Max comparisons for 1 000 items | 1 000 | 10 (2¹⁰ = 1 024) |
| Best for | Small or unsorted arrays | Large sorted arrays |

> [!WARNING] Common misconception
> Binary search on an **unsorted** array does not crash, but it often says "not found" for values that are in the array. Always sort first.


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
