# Mathematical Methods

Delphi comes with built-in mathematical functions you can call without writing them yourself. These are **predefined methods** and are heavily tested in Paper 1.

> [!NOTE] Grade 10+
> Basic math methods (Round, Trunc, Sqrt, Random) introduced in Grade 10. Ceil, Floor, Power, RandomRange need the **Math unit** — extended in Grade 11.

---

## Adding the Math Unit

Some functions require the **Math unit** in your `uses` clause:

```pascal
uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics,
  Controls, Forms, Dialogs, StdCtrls, Math;  // ← add Math here
```

Functions that need Math: `Ceil`, `Floor`, `Power`, `RandomRange`

---

## Round — Nearest integer (Banker's Rounding)

```pascal
iResult := Round(rValue);
```

| Statement | Result | Reason |
|---|---|---|
| `Round(12.4)` | `12` | Normal round down |
| `Round(12.5)` | `12` | Exactly halfway → **nearest even** (12 is even) |
| `Round(12.6)` | `13` | Normal round up |
| `Round(13.5)` | `14` | Exactly halfway → **nearest even** (14 is even) |

> [!WARNING] Banker's Rounding Surprise
> Delphi does NOT always round .5 up. It rounds .5 to the nearest **even** number. `Round(2.5) = 2`, but `Round(3.5) = 4`. If you need always-round-up, use `Trunc(x + 0.5)`.

---

## RoundTo — Round to a specific power of ten *(Math unit)*

```pascal
rResult := RoundTo(rValue, iPlace);
```

`iPlace` is the number of decimal places. Use **negative** values for decimal places, **positive** for rounding to tens/hundreds.

| Statement | Result | Meaning |
|---|---|---|
| `RoundTo(247.93816, -3)` | `247.938` | 3 decimal places |
| `RoundTo(247.93816, -1)` | `247.9` | 1 decimal place |
| `RoundTo(247.93816, 2)` | `300.0` | Nearest hundred |

> [!NOTE]
> `RoundTo` uses Banker's rounding at .5, just like `Round`. For display purposes, `FloatToStrF` with `ffFixed` is usually simpler.

---

## Trunc — Remove the decimal part

```pascal
iResult := Trunc(rValue);
```

Simply chops off everything after the decimal. Always moves toward zero.

| Statement | Result |
|---|---|
| `Trunc(12.9)` | `12` |
| `Trunc(-12.9)` | `-12` |

---

## Frac — Return the decimal part only

```pascal
rResult := Frac(rValue);
```

| Statement | Result |
|---|---|
| `Frac(12.75)` | `0.75` |
| `Frac(100.0)` | `0.0` |

---

## Ceil — Round UP always *(Math unit)*

```pascal
iResult := Ceil(rValue);
```

| Statement | Result |
|---|---|
| `Ceil(12.1)` | `13` |
| `Ceil(-12.8)` | `-12` (−12 > −13) |

---

## Floor — Round DOWN always *(Math unit)*

```pascal
iResult := Floor(rValue);
```

| Statement | Result |
|---|---|
| `Floor(12.9)` | `12` |
| `Floor(-12.8)` | `-13` (−13 < −12) |

---

## Sqr — Square a number (x²)

```pascal
iResult := Sqr(iValue);
rResult := Sqr(rValue);
```

| Statement | Result |
|---|---|
| `Sqr(12)` | `144` |
| `Sqr(5.5)` | `30.25` |

---

## Sqrt — Square root

```pascal
rResult := Sqrt(rValue);
```

Always returns Real. Square root of negative number → runtime error (validate first).

| Statement | Result |
|---|---|
| `Sqrt(144)` | `12.0` |
| `Sqrt(25)` | `5.0` |

**Pythagoras example:**
```pascal
rC := Sqrt(Sqr(rA) + Sqr(rB));
```

---

## Abs — Absolute value

```pascal
rResult := Abs(rValue);   // works with Real
iResult := Abs(iValue);   // works with Integer
```

Returns the positive (non-negative) value of a number. Negative numbers become positive; positive numbers are unchanged.

| Statement | Result |
|---|---|
| `Abs(-45)` | `45` |
| `Abs(45)` | `45` |
| `Abs(-7.3)` | `7.3` |

Useful for calculating differences when you don't know which value is larger:
```pascal
rDiff := Abs(rScore1 - rScore2);
```

---

## Odd — Test if a number is odd

```pascal
bResult := Odd(iValue);
```

Returns `True` if the integer is odd, `False` if even. Argument must be **Integer**.

| Statement | Result |
|---|---|
| `Odd(9)` | `True` |
| `Odd(4)` | `False` |
| `Odd(0)` | `False` |

```pascal
IF Odd(iNumber) THEN
  lblResult.Caption := 'Odd'
ELSE
  lblResult.Caption := 'Even';
```

---

## Pi — The constant π

```pascal
rArea := Pi * Sqr(rRadius);           // area of circle
rCirc := 2 * Pi * rRadius;            // circumference
```

`Pi = 3.14159265358979`

---

## Power — Raise to a power *(Math unit)*

```pascal
rResult := Power(rBase, rExponent);
```

| Statement | Result |
|---|---|
| `Power(2, 10)` | `1024.0` |
| `Power(3, 4)` | `81.0` |

**Compound interest:**
```pascal
rFinal := rPrincipal * Power(1 + rRate/100, iYears);
```

---

## Random — Generate random numbers

```pascal
rNum := Random;           // Real: 0 to < 1
iNum := Random(n);        // Integer: 0 to n-1

// Formula for range a to b:
iNum := Random(b - a + 1) + a;
```

**Examples:**
```pascal
iNum := Random(90) + 10;  // 10 to 99
iDice := Random(6) + 1;   // 1 to 6
```

> [!WARNING] Call Randomize in FormCreate
> ```pascal
> procedure TForm1.FormCreate(Sender: TObject);
> begin
>   Randomize;  // seeds the random number generator
> end;
> ```
> Without this, the same sequence repeats every run.

---

## RandomRange *(Math unit)*

```pascal
iResult := RandomRange(iLow, iHigh);
// produces: iLow to iHigh - 1
```

| Statement | Range |
|---|---|
| `RandomRange(1, 7)` | 1 to 6 |
| `RandomRange(10, 101)` | 10 to 100 |

---

## Inc and Dec — Increment / Decrement

```pascal
Inc(iVar);       // iVar := iVar + 1
Inc(iVar, n);    // iVar := iVar + n
Dec(iVar);       // iVar := iVar - 1
Dec(iVar, n);    // iVar := iVar - n
```

Works with Integer and Char:
```pascal
iCount := 6;
Inc(iCount);      // iCount = 7
Inc(iCount, 5);   // iCount = 12

cLetter := 'A';
Inc(cLetter);     // cLetter = 'B'
Inc(cLetter, 2);  // cLetter = 'D'
```

---

## Quick Reference Table

| Function | Unit | Returns | What it does |
|---|---|---|---|
| `Round(x)` | System | Integer | Nearest integer (Banker's rounding) |
| `RoundTo(x, n)` | **Math** | Real | Rounds to n decimal places (negative n) or powers of 10 (positive n) |
| `Trunc(x)` | System | Integer | Drops decimal part (no rounding) |
| `Frac(x)` | System | Real | Decimal portion only |
| `Ceil(x)` | **Math** | Integer | Always rounds up |
| `Floor(x)` | **Math** | Integer | Always rounds down |
| `Abs(x)` | System | same as input | Positive value of x |
| `Odd(x)` | System | Boolean | True if x is odd |
| `Sqr(x)` | System | same as input | x squared (x²) |
| `Sqrt(x)` | System | Real | Square root of x |
| `Pi` | System | Real | 3.14159... |
| `Power(b, e)` | **Math** | Real | b raised to power e |
| `Random` | System | Real | 0 to < 1 |
| `Random(n)` | System | Integer | 0 to n−1 |
| `RandomRange(a, b)` | **Math** | Integer | a to b−1 |
| `Inc(v)` | System | — | v := v + 1 (modifies in place) |
| `Inc(v, n)` | System | — | v := v + n (modifies in place) |
| `Dec(v)` | System | — | v := v − 1 (modifies in place) |
| `Dec(v, n)` | System | — | v := v − n (modifies in place) |

---

## Date Functions

Delphi has built-in support for working with dates. Use `TDate` (or just `TDateTime`) to store date values. The `DatePicker` (TDateTimePicker) component lets users select a date visually.

### Required units

```pascal
uses
  ..., SysUtils, DateUtils;   // DateUtils needed for YearOf, MonthOf, DayOf etc.
```

> The `FormatSettings` prefix is needed in Delphi 10+ for `LongMonthNames` and `LongDayNames`. In older Delphi versions these are global arrays.

---

### Basic date functions

| Function | Returns | Example | Result |
|---|---|---|---|
| `Date` | TDate | `dToday := Date` | Today's date |
| `CurrentYear` | Integer | `iYear := CurrentYear` | `2026` |
| `IsLeapYear(iYear)` | Boolean | `IsLeapYear(2024)` | `True` |
| `IsLeapYear(iYear)` | Boolean | `IsLeapYear(2026)` | `False` |
| `DayOfWeek(dDate)` | Integer | `DayOfWeek(Date)` | 1 = Sunday … 7 = Saturday |

```pascal
// Display today's date as a string
lblDate.Caption := DateToStr(Date);

// Check if a year is a leap year
IF IsLeapYear(StrToInt(edtYear.Text)) THEN
  lblResult.Caption := 'Leap year'
ELSE
  lblResult.Caption := 'Not a leap year';

// Show the name of the current day
lblDay.Caption := FormatSettings.LongDayNames[DayOfWeek(Date)];
```

---

### Day / month name arrays

These arrays let you look up month and day names by number.

| Array | Index | Example | Result |
|---|---|---|---|
| `FormatSettings.LongMonthNames[k]` | 1–12 | `LongMonthNames[9]` | `'September'` |
| `FormatSettings.ShortMonthNames[k]` | 1–12 | `ShortMonthNames[9]` | `'Sep'` |
| `FormatSettings.LongDayNames[k]` | 1–7 | `LongDayNames[1]` | `'Sunday'` |
| `FormatSettings.ShortDayNames[k]` | 1–7 | `ShortDayNames[2]` | `'Mon'` |

```pascal
// Display "Wednesday, 23 April 2026"
lblDate.Caption := FormatSettings.LongDayNames[DayOfWeek(Date)]
                   + ', ' + DateToStr(Date);
```

---

### DateUtils functions *(add DateUtils to uses)*

| Function | Returns | Example | Result |
|---|---|---|---|
| `YearOf(dDate)` | Integer | `YearOf(dDOB)` | `2008` |
| `MonthOf(dDate)` | Integer | `MonthOf(dDOB)` | `11` |
| `DayOf(dDate)` | Integer | `DayOf(dDOB)` | `3` |
| `YearsBetween(d1, d2)` | Integer | `YearsBetween(dDOB, Date)` | `17` (age) |
| `DaysBetween(d1, d2)` | Integer | `DaysBetween(dStart, Date)` | `230` |
| `DaysInAMonth(iYear, iMonth)` | Integer | `DaysInAMonth(2026, 2)` | `28` |
| `DaysInMonth(dDate)` | Integer | `DaysInMonth(Date)` | `30` |
| `IsValidDate(iY, iM, iD)` | Boolean | `IsValidDate(2026, 2, 30)` | `False` |
| `IsValidDate(iY, iM, iD)` | Boolean | `IsValidDate(2024, 2, 29)` | `True` |

```pascal
// Calculate age from a DateTimePicker
iAge := YearsBetween(dtpDOB.Date, Date);
lblAge.Caption := IntToStr(iAge) + ' years old';

// Validate a date before using it
iY := StrToInt(edtYear.Text);
iM := StrToInt(edtMonth.Text);
iD := StrToInt(edtDay.Text);
IF IsValidDate(iY, iM, iD) THEN
  dDate := EncodeDate(iY, iM, iD)
ELSE
  ShowMessage('Invalid date entered');

// How many days are in February this year?
lblDays.Caption := IntToStr(DaysInAMonth(CurrentYear, 2)) + ' days in Feb';
```

---

## Practice Exercise

Generate 10 random integers between 1 and 100. Display them in a RichEdit and show the largest value found.

<details>
<summary>Show solution</summary>

```pascal
procedure TForm1.FormCreate(Sender: TObject);
begin
  Randomize;
end;

procedure TForm1.btnGenClick(Sender: TObject);
var
  i, iNum, iMax : Integer;
begin
  iMax := 0;
  redOutput.Lines.Clear;

  FOR i := 1 TO 10 DO
  BEGIN
    iNum := Random(100) + 1;
    redOutput.Lines.Add(IntToStr(i) + ': ' + IntToStr(iNum));
    IF iNum > iMax THEN
      iMax := iNum;
  END;

  redOutput.Lines.Add('Largest: ' + IntToStr(iMax));
end;
```
</details>

> [!TIP] Exam Tip
> Round vs Trunc is tested almost every year. Remember: `Trunc(12.9) = 12` always. `Round(12.5) = 12` (Banker's — rounds to even). If asked "what does `Round(13.5)` return?" the answer is `14` (14 is even).
