# 2D Arrays

A 1D array is a list. A **2D array** is a table — it has rows and columns. Think of a spreadsheet, a seating plan, a grid of pixels, or a mark book: rows for students, columns for subjects.

> [!NOTE] Grade 11+
> 2D arrays are introduced in Grade 11 and appear in Paper 1. They are always processed with nested loops.

---

## What is a 2D Array?

A 2D array stores data in a **grid** — you access each element using **two indexes**: row and column.

```
          Col 1  Col 2  Col 3  Col 4
Row 1:      78     85     91     67
Row 2:      92     88     76     95
Row 3:      65     71     83     89
```

- `aGrid[2][3]` = 76 (row 2, column 3)
- `aGrid[1][4]` = 67 (row 1, column 4)

---

## Declaring a 2D Array

```pascal
const
  ROWS = 3;
  COLS = 4;

var
  aGrid   : array[1..ROWS, 1..COLS] of Integer;
  aMarks  : array[1..5, 1..6] of Real;    // 5 students, 6 subjects
  aBoard  : array[1..8, 1..8] of Char;    // 8×8 chessboard
```

Syntax: `array[rowStart..rowEnd, colStart..colEnd] of DataType`

---

## Accessing Elements

```pascal
// Assign
aGrid[1][1] := 78;
aGrid[2][3] := 76;

// Read
iScore := aGrid[iRow][iCol];

// Using variables
FOR iRow := 1 TO ROWS DO
  FOR iCol := 1 TO COLS DO
    aGrid[iRow][iCol] := 0;   // initialise all to 0
```

---

## Traversing with Nested Loops

**Always use nested loops to process a 2D array.**

### Display all elements

```pascal
procedure TForm1.btnDisplayClick(Sender: TObject);
const
  ROWS = 3;
  COLS = 4;
var
  aGrid        : array[1..ROWS, 1..COLS] of Integer;
  iRow, iCol   : Integer;
  sLine        : String;
begin
  // Assume aGrid is already populated
  redOutput.Lines.Clear;

  FOR iRow := 1 TO ROWS DO
  BEGIN
    sLine := '';
    FOR iCol := 1 TO COLS DO
    BEGIN
      sLine := sLine + Format('%5d', [aGrid[iRow][iCol]]);
    END;
    redOutput.Lines.Add(sLine);
  END;
end;
```

### Sum of all elements

```pascal
iTotal := 0;
FOR iRow := 1 TO ROWS DO
  FOR iCol := 1 TO COLS DO
    iTotal := iTotal + aGrid[iRow][iCol];

rAverage := iTotal / (ROWS * COLS);
```

### Sum of each row separately

```pascal
FOR iRow := 1 TO ROWS DO
BEGIN
  iRowSum := 0;
  FOR iCol := 1 TO COLS DO
    iRowSum := iRowSum + aGrid[iRow][iCol];

  redOutput.Lines.Add('Row ' + IntToStr(iRow) + ' sum: ' + IntToStr(iRowSum));
END;
```

### Sum of each column separately

```pascal
FOR iCol := 1 TO COLS DO
BEGIN
  iColSum := 0;
  FOR iRow := 1 TO ROWS DO
    iColSum := iColSum + aGrid[iRow][iCol];

  redOutput.Lines.Add('Col ' + IntToStr(iCol) + ' sum: ' + IntToStr(iColSum));
END;
```

### Find maximum in entire array

```pascal
iMax := aGrid[1][1];   // assume first element is max

FOR iRow := 1 TO ROWS DO
  FOR iCol := 1 TO COLS DO
    IF aGrid[iRow][iCol] > iMax THEN
      iMax := aGrid[iRow][iCol];

redOutput.Lines.Add('Maximum: ' + IntToStr(iMax));
```

---

## Worked Example — Mark Book

A class has 4 students and 3 test marks each. Find:
a) Each student's average
b) The class average (average of all marks)
c) The highest mark in the entire grid

```pascal
procedure TForm1.btnAnalyseClick(Sender: TObject);
const
  STUDENTS = 4;
  TESTS    = 3;
var
  aMarks          : array[1..STUDENTS, 1..TESTS] of Integer;
  iRow, iCol      : Integer;
  iRowSum, iTotal : Integer;
  iMax            : Integer;
  rStudentAvg     : Real;
begin
  // Assume aMarks is already filled (or fill with InputBox)

  redOutput.Lines.Clear;
  iTotal := 0;
  iMax   := aMarks[1][1];

  FOR iRow := 1 TO STUDENTS DO
  BEGIN
    iRowSum := 0;

    FOR iCol := 1 TO TESTS DO
    BEGIN
      iRowSum := iRowSum + aMarks[iRow][iCol];
      IF aMarks[iRow][iCol] > iMax THEN
        iMax := aMarks[iRow][iCol];
    END;

    iTotal      := iTotal + iRowSum;
    rStudentAvg := iRowSum / TESTS;

    redOutput.Lines.Add('Student ' + IntToStr(iRow) +
                        ' average: ' + FloatToStrF(rStudentAvg, ffFixed, 8, 1));
  END;

  redOutput.Lines.Add('');
  redOutput.Lines.Add('Class average: ' +
                       FloatToStrF(iTotal / (STUDENTS * TESTS), ffFixed, 8, 1));
  redOutput.Lines.Add('Highest mark: ' + IntToStr(iMax));
end;
```

---

## Filling a 2D Array

### With nested loops and InputBox

```pascal
FOR iRow := 1 TO ROWS DO
  FOR iCol := 1 TO COLS DO
    aGrid[iRow][iCol] := StrToInt(
      InputBox('Input', 'Row ' + IntToStr(iRow) + ', Col ' + IntToStr(iCol) + ':', ''));
```

### Pre-filled (exam scenario — given to you)

In most exam questions: "The 2D array `aMarks` has already been populated." You only write the processing code.

---

## Row vs Column — Mental Model

```pascal
// OUTER loop = rows (go down)
// INNER loop = cols (go across)

FOR iRow := 1 TO ROWS DO      // ← controls which row
BEGIN
  FOR iCol := 1 TO COLS DO   // ← controls which column within that row
  BEGIN
    // aGrid[iRow][iCol]
  END;
END;
```

To process **column by column**, swap the loop order:

```pascal
FOR iCol := 1 TO COLS DO      // outer = column
  FOR iRow := 1 TO ROWS DO   // inner = row within that column
    // process aGrid[iRow][iCol]
```

---

## Common Mistakes

> [!WARNING] Watch Out For
> 1. **Mixing up row and column indexes** — `aGrid[row][col]`, not `aGrid[col][row]`
> 2. **Single loop for 2D array** — you always need nested loops to cover all elements
> 3. **Wrong bounds in inner loop** — inner loop goes to `COLS`, not `ROWS`
> 4. **Not initialising max/min** — set to `aGrid[1][1]` before the nested loops
> 5. **Confusing total elements** — a 3×4 array has 12 elements total (3 × 4); average denominator is `ROWS * COLS`

---

## Practice Exercises

**Exercise 1 — Grid sum and diagonal**

A 4×4 integer grid. Write code to:
a) Find the sum of all elements
b) Find the sum of the main diagonal (top-left to bottom-right: `aGrid[i][i]`)

<details>
<summary>Show solution</summary>

```pascal
const SIDE = 4;
var
  aGrid       : array[1..SIDE, 1..SIDE] of Integer;
  i, j        : Integer;
  iTotal      : Integer;
  iDiagSum    : Integer;
begin
  // a) Sum of all
  iTotal := 0;
  FOR i := 1 TO SIDE DO
    FOR j := 1 TO SIDE DO
      iTotal := iTotal + aGrid[i][j];

  redOutput.Lines.Add('Total: ' + IntToStr(iTotal));

  // b) Main diagonal (where row = col)
  iDiagSum := 0;
  FOR i := 1 TO SIDE DO
    iDiagSum := iDiagSum + aGrid[i][i];

  redOutput.Lines.Add('Diagonal sum: ' + IntToStr(iDiagSum));
end;
```
</details>

---

**Exercise 2 — Count values meeting a condition**

A 3×5 array of integer marks. Count how many marks are above 60, and display them row by row.

<details>
<summary>Show solution</summary>

```pascal
const ROWS = 3; COLS = 5;
var
  aMarks : array[1..ROWS, 1..COLS] of Integer;
  i, j, iCount : Integer;
begin
  iCount := 0;
  redOutput.Lines.Clear;
  redOutput.Lines.Add('Marks above 60:');

  FOR i := 1 TO ROWS DO
    FOR j := 1 TO COLS DO
      IF aMarks[i][j] > 60 THEN
      BEGIN
        redOutput.Lines.Add('  [' + IntToStr(i) + '][' + IntToStr(j) + '] = ' +
                             IntToStr(aMarks[i][j]));
        Inc(iCount);
      END;

  redOutput.Lines.Add('Count: ' + IntToStr(iCount));
end;
```
</details>

---

> [!TIP] Exam Tip
> In 2D array questions, always start by identifying what the rows and columns represent (e.g. rows = students, columns = subjects). Then the question becomes obvious: "sum of row 2" = sum of one student's marks; "sum of column 3" = all marks for subject 3. Drawing a small table on paper before coding saves significant time and prevents index errors.
