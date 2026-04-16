# Delphi Syntax — Quick Reference Card

Fast-scan reference for all core Delphi syntax. No prose — just syntax patterns and examples.

---

## Variable Declaration

```pascal
var
  iCount   : Integer;
  rTotal   : Real;
  sName    : String;
  cGrade   : Char;
  bPassed  : Boolean;
  aScores  : array[1..10] of Integer;
  i, j     : Integer;       // multiple on one line

const
  MAX = 10;
  RATE = 0.15;
```

---

## Naming Conventions (Hungarian Notation)

| Prefix | Type | Example |
|---|---|---|
| `i` | Integer | `iScore`, `iCount`, `iMax` |
| `r` | Real | `rAvg`, `rTotal`, `rPrice` |
| `s` | String | `sName`, `sCode` |
| `c` | Char | `cGrade`, `cChoice` |
| `b` | Boolean | `bFound`, `bPassed` |
| `a` | Array | `aScores`, `aNames` |
| `btn` | TButton | `btnCalc` |
| `lbl` | TLabel | `lblResult` |
| `edt` | TEdit | `edtName` |
| `red` | TRichEdit | `redOutput` |

---

## Assignment

```pascal
iAge   := 16;
rPrice := 49.99;
sName  := 'Ayden';
bFlag  := True;
iTotal := iTotal + iValue;     // accumulate
```

---

## Arithmetic Operators

| Op | Meaning | Types | Example |
|---|---|---|---|
| `+` | Add | Int, Real | `5 + 3 = 8` |
| `-` | Subtract | Int, Real | `10 - 4 = 6` |
| `*` | Multiply | Int, Real | `6 * 7 = 42` |
| `/` | Divide (Real) | Int, Real | `7 / 2 = 3.5` |
| `DIV` | Integer divide | Integer | `7 DIV 2 = 3` |
| `MOD` | Remainder | Integer | `7 MOD 2 = 1` |

---

## Relational Operators

| Op | Meaning | Example |
|---|---|---|
| `=` | Equal | `iMark = 50` |
| `<>` | Not equal | `sName <> 'Admin'` |
| `<` | Less than | `iScore < 50` |
| `>` | Greater than | `rPrice > 100` |
| `<=` | Less or equal | `iAge <= 17` |
| `>=` | Greater or equal | `iMark >= 50` |

---

## Logical Operators

```pascal
(iAge >= 18) AND (iMark >= 50)   // both must be true
(iDay = 6)   OR  (iDay = 7)      // either is enough
NOT bFound                         // reverses boolean
```

Always bracket each sub-condition when using AND/OR.

---

## IF Statement

```pascal
// Basic
IF iNum > 0 THEN
  lblResult.Caption := 'Positive';

// IF...ELSE
IF iMark >= 50 THEN
BEGIN
  lblResult.Caption := 'Pass';
END
ELSE                         // NO semicolon before ELSE
BEGIN
  lblResult.Caption := 'Fail';
END;

// Chained
IF iMark >= 80 THEN     sGrade := 'A'
ELSE IF iMark >= 70 THEN sGrade := 'B'
ELSE IF iMark >= 60 THEN sGrade := 'C'
ELSE IF iMark >= 50 THEN sGrade := 'D'
ELSE                     sGrade := 'F';
```

---

## CASE Statement

```pascal
CASE iDay OF
  1 : lblDay.Caption := 'Monday';
  2 : lblDay.Caption := 'Tuesday';
  6, 7 : lblDay.Caption := 'Weekend';     // comma = multiple values
  8..14 : ShowMessage('Out of range');    // .. = range
ELSE
  ShowMessage('Invalid');
END;
```

> CASE only works with Integer, Char, Boolean — **not** String.

---

## FOR Loop

```pascal
// Count up
FOR i := 1 TO MAX DO
BEGIN
  redOutput.Lines.Add(IntToStr(aScores[i]));
END;

// Count down
FOR i := MAX DOWNTO 1 DO
BEGIN
  redOutput.Lines.Add(IntToStr(i));
END;
```

> Never put a semicolon directly after `DO` — it creates an empty loop body.

---

## WHILE Loop

```pascal
WHILE iNum > 0 DO
BEGIN
  iNum := iNum DIV 2;
  iCount := iCount + 1;
END;
// Condition checked BEFORE each iteration — may run 0 times
```

---

## REPEAT...UNTIL Loop

```pascal
REPEAT
  iChoice := StrToInt(InputBox('Menu', '1-3 or 0 to quit:', ''));
UNTIL iChoice = 0;
// Condition checked AFTER — runs AT LEAST once
// Loop STOPS when condition is TRUE
```

---

## Arrays

```pascal
// Declaration
var
  aScores : array[1..MAX] of Integer;

// Assign
aScores[1] := 78;
aScores[i] := StrToInt(InputBox('Score', 'Enter:', ''));

// Traverse
FOR i := 1 TO MAX DO
  redOutput.Lines.Add(IntToStr(aScores[i]));

// Sum + Average
iSum := 0;
FOR i := 1 TO MAX DO
  iSum := iSum + aScores[i];
rAvg := iSum / MAX;

// Max
iMax := aScores[1];
FOR i := 2 TO MAX DO
  IF aScores[i] > iMax THEN iMax := aScores[i];

// Min
iMin := aScores[1];
FOR i := 2 TO MAX DO
  IF aScores[i] < iMin THEN iMin := aScores[i];

// Linear search
bFound := False;
FOR i := 1 TO MAX DO
  IF aScores[i] = iTarget THEN BEGIN bFound := True; iPos := i; END;

// Swap
iTemp := aScores[i];
aScores[i] := aScores[j];
aScores[j] := iTemp;
```

---

## 2D Arrays

```pascal
var
  aGrid : array[1..ROWS, 1..COLS] of Integer;

// Access
aGrid[iRow][iCol] := 5;

// Traverse all elements
FOR iRow := 1 TO ROWS DO
  FOR iCol := 1 TO COLS DO
    redOutput.Lines.Add(IntToStr(aGrid[iRow][iCol]));
```

---

## Procedures & Functions

```pascal
// Procedure (no return value)
procedure ShowGreeting(sName : String);
begin
  ShowMessage('Hello, ' + sName);
end;

// Function (returns a value)
function Square(iNum : Integer) : Integer;
begin
  Result := iNum * iNum;
end;

// VAR parameter (modifies original)
procedure Swap(var iA, iB : Integer);
var iTemp : Integer;
begin
  iTemp := iA;
  iA    := iB;
  iB    := iTemp;
end;
```

---

## Text Files

```pascal
var
  f : TextFile;
  sLine : String;

// Write to file
AssignFile(f, 'output.txt');
Rewrite(f);
WriteLn(f, 'Hello');
WriteLn(f, IntToStr(iScore));
CloseFile(f);

// Read from file
AssignFile(f, 'data.txt');
Reset(f);
WHILE NOT EOF(f) DO
BEGIN
  ReadLn(f, sLine);
  redOutput.Lines.Add(sLine);
END;
CloseFile(f);
```

---

## Dialogs

```pascal
ShowMessage('Operation complete!');

sInput := InputBox('Title', 'Prompt message:', 'default');
iNum   := StrToInt(InputBox('Input', 'Enter number:', ''));
```

---

## Math Functions

| Function | Returns | Notes |
|---|---|---|
| `Round(x)` | Integer | Banker's rounding (.5 → nearest even) |
| `Trunc(x)` | Integer | Chops decimal part |
| `Frac(x)` | Real | Decimal portion only |
| `Ceil(x)` | Integer | Always rounds UP *(Math unit)* |
| `Floor(x)` | Integer | Always rounds DOWN *(Math unit)* |
| `Sqr(x)` | same | x squared |
| `Sqrt(x)` | Real | Square root |
| `Power(b,e)` | Real | b^e *(Math unit)* |
| `Random(n)` | Integer | 0 to n−1 |
| `Inc(v)` | — | v := v + 1 |
| `Dec(v)` | — | v := v − 1 |

---

## Type Conversion

| Function | From → To | Example |
|---|---|---|
| `IntToStr(i)` | Int → String | `IntToStr(42)` = `'42'` |
| `StrToInt(s)` | String → Int | `StrToInt('42')` = `42` |
| `FloatToStr(r)` | Real → String | `FloatToStr(3.14)` = `'3.14'` |
| `StrToFloat(s)` | String → Real | `StrToFloat('3.14')` = `3.14` |
| `FloatToStrF(r,ffFixed,8,2)` | Real → String | 2 decimal places |
| `Chr(i)` | Int → Char | `Chr(65)` = `'A'` |
| `Ord(c)` | Char → Int | `Ord('A')` = `65` |

---

## Common Runtime Errors and Fixes

| Error | Cause | Fix |
|---|---|---|
| Index out of range | Accessing array beyond its bounds | Check loop bounds match array declaration |
| Division by zero | `x / 0` or `x MOD 0` | Validate divisor ≠ 0 before dividing |
| Invalid integer | `StrToInt` on non-numeric text | Validate input or use try/except |
| Stack overflow | Infinite recursion | Ensure recursion has a base case |
| Access violation | Using unassigned object/pointer | Initialise before use |
