# Operators

Operators are symbols that perform operations on values. Every calculation, comparison, and logical test in Delphi uses an operator. Knowing which operator to use — and the exact Delphi syntax — is essential.

> [!NOTE] Grade 10+
> All operators are introduced in Grade 10. DIV and MOD are particularly common in exam questions and are frequently tested.

---

## Arithmetic Operators

Used for mathematical calculations on numbers.

| Operator | Operation | Types | Example | Result |
|---|---|---|---|---|
| `+` | Addition | Integer, Real | `5 + 3` | `8` |
| `-` | Subtraction | Integer, Real | `10 - 4` | `6` |
| `*` | Multiplication | Integer, Real | `6 * 7` | `42` |
| `/` | Division (Real result) | Integer, Real | `7 / 2` | `3.5` |
| `DIV` | Integer division (quotient) | Integer only | `7 DIV 2` | `3` |
| `MOD` | Modulus (remainder) | Integer only | `7 MOD 2` | `1` |

> [!WARNING] / Always Returns Real
> Even `4 / 2` returns `2.0` (Real), not `2` (Integer). If you need an integer result, use `DIV`.

### DIV and MOD — Explained

`DIV` gives the **whole number** part of division. `MOD` gives the **remainder**.

```
17 DIV 5 = 3      because 5 goes into 17 three times
17 MOD 5 = 2      because 17 - (3 × 5) = 2 remainder
```

**Common uses of MOD:**

```pascal
// Check if a number is even (remainder when divided by 2 is 0)
IF iNum MOD 2 = 0 THEN
  lblResult.Caption := 'Even'
ELSE
  lblResult.Caption := 'Odd';

// Check if a number is divisible by 3
IF iNum MOD 3 = 0 THEN
  ShowMessage('Divisible by 3');

// Extract last digit of a number
iLastDigit := iNum MOD 10;   // e.g. 347 MOD 10 = 7

// Extract first two digits of a 3-digit number
iFirstTwo := iNum DIV 10;    // e.g. 347 DIV 10 = 34
```

### Operator Precedence (Order of Operations)

Delphi follows standard mathematical precedence:

1. Brackets `( )` — evaluated first
2. `*`, `/`, `DIV`, `MOD` — multiplication/division
3. `+`, `-` — addition/subtraction

```pascal
// Without brackets
iResult := 2 + 3 * 4;      // = 14 (3*4 first, then +2)

// With brackets
iResult := (2 + 3) * 4;    // = 20 (2+3 first, then *4)
```

> [!WARNING] Always Use Brackets When in Doubt
> Bracket your calculations explicitly. It avoids errors and makes code easier to read:
> ```pascal
> rAvg := (iScore1 + iScore2 + iScore3) / 3;  // clear ✓
> rAvg := iScore1 + iScore2 + iScore3 / 3;    // WRONG — divides only score3 ❌
> ```

---

## Relational Operators (Comparison)

Used in conditions (IF, WHILE, REPEAT-UNTIL). Always return a Boolean (`True` or `False`).

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `=` | Equal to | `iAge = 18` | True if iAge is 18 |
| `<>` | Not equal to | `sName <> 'Admin'` | True if sName is not 'Admin' |
| `<` | Less than | `iScore < 50` | True if iScore is below 50 |
| `>` | Greater than | `rPrice > 100.0` | True if rPrice exceeds 100 |
| `<=` | Less than or equal | `iAge <= 17` | True if iAge is 17 or younger |
| `>=` | Greater than or equal | `iMark >= 50` | True if iMark is 50 or above |

```pascal
IF iMark >= 50 THEN
  lblResult.Caption := 'Pass'
ELSE
  lblResult.Caption := 'Fail';

WHILE iNum <> 0 DO
BEGIN
  // process until user enters 0
END;
```

---

## Logical (Boolean) Operators

Used to combine multiple conditions.

| Operator | Meaning | Result |
|---|---|---|
| `AND` | Both conditions must be True | True only if **both** are True |
| `OR` | At least one condition must be True | True if **either** is True |
| `NOT` | Reverses the boolean value | True becomes False, False becomes True |

### Truth Tables

**AND:**
| A | B | A AND B |
|---|---|---|
| True | True | **True** |
| True | False | False |
| False | True | False |
| False | False | False |

**OR:**
| A | B | A OR B |
|---|---|---|
| True | True | **True** |
| True | False | **True** |
| False | True | **True** |
| False | False | False |

**NOT:**
| A | NOT A |
|---|---|
| True | False |
| False | True |

### Examples

```pascal
// AND — both conditions must hold
IF (iAge >= 18) AND (iMark >= 50) THEN
  lblResult.Caption := 'Eligible';

// OR — either condition is enough
IF (iDay = 6) OR (iDay = 7) THEN
  lblDay.Caption := 'Weekend';

// NOT — reverse a condition
IF NOT bFound THEN
  lblResult.Caption := 'Not found in array';

// Combined
IF (iScore >= 0) AND (iScore <= 100) THEN
  lblValid.Caption := 'Valid score'
ELSE
  lblValid.Caption := 'Invalid — must be 0 to 100';
```

> [!WARNING] Always Bracket Each Sub-Condition
> Delphi evaluates `NOT` before `AND` before `OR`. Without brackets, compound conditions can behave unexpectedly:
> ```pascal
> // WRONG — unpredictable ❌
> IF iAge >= 18 AND iMark >= 50 THEN
>
> // CORRECT ✓
> IF (iAge >= 18) AND (iMark >= 50) THEN
> ```

---

## String Operator

| Operator | Operation | Example | Result |
|---|---|---|---|
| `+` | Concatenation (join strings) | `'Hello' + ' ' + 'World'` | `'Hello World'` |

```pascal
sFullName := sFirst + ' ' + sSurname;
lblGreet.Caption := 'Welcome, ' + sName + '!';
redOutput.Lines.Add('Score: ' + IntToStr(iScore));
```

> [!NOTE] Only + Works for Strings
> `*`, `-`, `/` etc. are **not** valid for strings. To repeat a character, use `StringOfChar('*', 5)`.

---

## Compound Assignment (Common Pattern)

Delphi has no `+=` shorthand. You must write the full statement:

```pascal
// Accumulate a total
iTotal := iTotal + iValue;   // NOT iTotal += iValue

// Double a value
iNum := iNum * 2;

// Append to a string
sOutput := sOutput + sLine;
```

---

## Complete Worked Examples

**Example 1 — Body Mass Index (BMI)**

```pascal
procedure TForm1.btnBMIClick(Sender: TObject);
var
  rWeight, rHeight, rBMI : Real;
begin
  rWeight := StrToFloat(edtWeight.Text);  // kg
  rHeight := StrToFloat(edtHeight.Text);  // metres

  rBMI := rWeight / (rHeight * rHeight);

  lblBMI.Caption := 'BMI: ' + FloatToStrF(rBMI, ffFixed, 8, 1);

  IF rBMI < 18.5 THEN
    lblCat.Caption := 'Underweight'
  ELSE IF rBMI < 25.0 THEN
    lblCat.Caption := 'Normal'
  ELSE IF rBMI < 30.0 THEN
    lblCat.Caption := 'Overweight'
  ELSE
    lblCat.Caption := 'Obese';
end;
```

**Example 2 — Digit extraction using DIV and MOD**

```pascal
procedure TForm1.btnDigitsClick(Sender: TObject);
var
  iNum, iHundreds, iTens, iUnits : Integer;
begin
  iNum := StrToInt(edtNum.Text);  // assume 3-digit number

  iHundreds := iNum DIV 100;           // e.g. 347 → 3
  iTens     := (iNum MOD 100) DIV 10;  // e.g. 347 → 4
  iUnits    := iNum MOD 10;            // e.g. 347 → 7

  redOutput.Lines.Clear;
  redOutput.Lines.Add('Hundreds: ' + IntToStr(iHundreds));
  redOutput.Lines.Add('Tens:     ' + IntToStr(iTens));
  redOutput.Lines.Add('Units:    ' + IntToStr(iUnits));
end;
```

**Example 3 — Leap year check**

```pascal
// A year is a leap year if:
// divisible by 4 AND (not divisible by 100 OR divisible by 400)
IF (iYear MOD 4 = 0) AND ((iYear MOD 100 <> 0) OR (iYear MOD 400 = 0)) THEN
  lblResult.Caption := IntToStr(iYear) + ' is a leap year'
ELSE
  lblResult.Caption := IntToStr(iYear) + ' is NOT a leap year';
```

---

## Common Mistakes

> [!WARNING] Watch Out For
> 1. **Using `=` instead of `:=`** for assignment — will not compile
> 2. **Dividing integers with `/`** when you want integer result — use `DIV`
> 3. **Missing brackets in AND/OR conditions** — incorrect precedence
> 4. **`7 MOD 0`** — division by zero runtime error; validate the divisor first
> 5. **Order of precedence** — `2 + 3 * 4 = 14` not `20`; use brackets to be explicit

---

## Practice Exercises

**Exercise 1 — Even or Odd**

Read a number from `edtNum`. Display whether it is even or odd, and also display the remainder when divided by 3.

<details>
<summary>Show solution</summary>

```pascal
procedure TForm1.btnEvenOddClick(Sender: TObject);
var
  iNum : Integer;
begin
  iNum := StrToInt(edtNum.Text);

  IF iNum MOD 2 = 0 THEN
    lblEven.Caption := IntToStr(iNum) + ' is EVEN'
  ELSE
    lblEven.Caption := IntToStr(iNum) + ' is ODD';

  lblRemainder.Caption := 'Remainder ÷ 3: ' + IntToStr(iNum MOD 3);
end;
```
</details>

---

**Exercise 2 — Time converter**

Read a number of seconds from `edtSeconds`. Display the equivalent hours, minutes, and remaining seconds.
e.g. `3725 seconds` → `1 hour, 2 minutes, 5 seconds`

<details>
<summary>Show solution</summary>

```pascal
procedure TForm1.btnConvertClick(Sender: TObject);
var
  iTotalSec, iHours, iMins, iSecs : Integer;
begin
  iTotalSec := StrToInt(edtSeconds.Text);

  iHours := iTotalSec DIV 3600;
  iMins  := (iTotalSec MOD 3600) DIV 60;
  iSecs  := iTotalSec MOD 60;

  lblResult.Caption := IntToStr(iHours) + 'h ' +
                       IntToStr(iMins)  + 'm ' +
                       IntToStr(iSecs)  + 's';
end;
```
</details>

---

> [!TIP] Exam Tip
> `MOD` and `DIV` questions appear almost every year. Classic scenarios: check if a number is even/odd, check divisibility, extract individual digits from a number, convert seconds to hours/minutes/seconds. Practice these patterns — they are mechanical once you know them.
