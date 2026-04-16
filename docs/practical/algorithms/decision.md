# Decision Structures in Algorithms

Programs rarely follow a single path. Based on conditions — whether a number is positive, whether a password is correct, whether stock is available — the algorithm branches in different directions. Decision structures are what make programs intelligent.

---

## What is a Decision Structure?

A **decision structure** allows an algorithm to choose between different paths based on a condition.

```
Condition TRUE → execute path A
Condition FALSE → execute path B
```

---

## IF Statement (Flowchart)

The simplest decision — take an action if a condition is true; skip it if false.

```
        ┌──────────────┐
        │  Condition?  │
        └──────┬───────┘
          YES  │   NO
         ┌─────┘   └────┐
         ▼              │
   ┌──────────┐          │
   │  Action  │          │
   └────┬─────┘          │
        └────────────────┘
                ▼
```

**Pseudocode:**
```
IF condition THEN
    statements
END IF
```

**Delphi:**
```pascal
if iMark >= 50 then
  ShowMessage('Pass');
```

---

## IF-ELSE Statement

Take one of two possible actions based on the condition.

```
        ┌──────────────┐
        │  Condition?  │
        └──────┬───────┘
          YES  │   NO
         ┌─────┘   └────────┐
         ▼                  ▼
   ┌──────────┐       ┌──────────┐
   │ Action A │       │ Action B │
   └────┬─────┘       └────┬─────┘
        └─────────┬─────────┘
                  ▼
```

**Pseudocode:**
```
IF condition THEN
    statements A
ELSE
    statements B
END IF
```

**Delphi:**
```pascal
if iMark >= 50 then
  ShowMessage('Pass')
else
  ShowMessage('Fail');
```

---

## Nested IF Statements

IF statements inside other IF statements — for multiple conditions.

**Pseudocode:**
```
IF mark >= 80 THEN
    symbol ← 'A'
ELSE IF mark >= 70 THEN
    symbol ← 'B'
ELSE IF mark >= 60 THEN
    symbol ← 'C'
ELSE IF mark >= 50 THEN
    symbol ← 'D'
ELSE
    symbol ← 'F'
END IF
```

**Delphi:**
```pascal
if iMark >= 80 then
  sSymbol := 'A'
else if iMark >= 70 then
  sSymbol := 'B'
else if iMark >= 60 then
  sSymbol := 'C'
else if iMark >= 50 then
  sSymbol := 'D'
else
  sSymbol := 'F';
```

---

## CASE Statement

When comparing one variable against many possible values, CASE is cleaner than nested IF.

**Pseudocode:**
```
CASE variable OF
    value1: statements
    value2: statements
    value3: statements
    ELSE: default statements
END CASE
```

**Delphi:**
```pascal
case iDay of
  1: lblDay.Caption := 'Monday';
  2: lblDay.Caption := 'Tuesday';
  3: lblDay.Caption := 'Wednesday';
  4: lblDay.Caption := 'Thursday';
  5: lblDay.Caption := 'Friday';
  6: lblDay.Caption := 'Saturday';
  7: lblDay.Caption := 'Sunday';
else
  lblDay.Caption := 'Invalid';
end;
```

> [!TIP] When to use CASE vs IF
> Use CASE when testing one variable against multiple **discrete** values.  
> Use IF when testing **conditions** or **ranges** (CASE cannot test `> 50`).

---

## Flowchart Worked Examples

### Example 1: Classify a mark

**Problem:** Input a mark (0–100). Output whether it is a Pass (≥50) or Fail.

**Flowchart:**
```
START
  ↓
Input mark
  ↓
┌─────────────┐
│ mark >= 50? │
└──────┬──────┘
 YES   │   NO
 ↓         ↓
Output   Output
"Pass"   "Fail"
  ↓         ↓
  └────┬────┘
       ↓
      END
```

**Delphi code:**
```pascal
procedure TForm1.btnCheckClick(Sender: TObject);
var
  iMark: Integer;
begin
  iMark := StrToInt(edtMark.Text);
  if iMark >= 50 then
    lblResult.Caption := 'Pass'
  else
    lblResult.Caption := 'Fail';
end;
```

---

### Example 2: Tax calculator

**Problem:** Income tax rates:
- Income ≤ R100,000: 18% tax
- Income ≤ R200,000: 26% tax  
- Income > R200,000: 31% tax

**Pseudocode:**
```
INPUT income
IF income <= 100000 THEN
    tax ← income × 0.18
ELSE IF income <= 200000 THEN
    tax ← income × 0.26
ELSE
    tax ← income × 0.31
END IF
OUTPUT 'Tax due: R' + tax
```

**Delphi code:**
```pascal
procedure TForm1.btnCalculateClick(Sender: TObject);
var
  rIncome, rTax: Real;
begin
  rIncome := StrToFloat(edtIncome.Text);
  if rIncome <= 100000 then
    rTax := rIncome * 0.18
  else if rIncome <= 200000 then
    rTax := rIncome * 0.26
  else
    rTax := rIncome * 0.31;
  lblTax.Caption := 'Tax due: R' + FloatToStrF(rTax, ffFixed, 10, 2);
end;
```

---

### Example 3: Grade symbol (CASE)

**Problem:** A quiz has scores 1–5. Display the corresponding grade.

**Delphi:**
```pascal
procedure TForm1.btnGradeClick(Sender: TObject);
var
  iScore: Integer;
  sGrade: String;
begin
  iScore := StrToInt(edtScore.Text);
  case iScore of
    5: sGrade := 'Outstanding';
    4: sGrade := 'Merit';
    3: sGrade := 'Achieved';
    2: sGrade := 'Elementary';
    1: sGrade := 'Not achieved';
  else
    sGrade := 'Invalid score';
  end;
  lblGrade.Caption := sGrade;
end;
```

---

## Common Decision Problems

### Is a number positive, negative, or zero?
```pascal
if iNum > 0 then
  lblSign.Caption := 'Positive'
else if iNum < 0 then
  lblSign.Caption := 'Negative'
else
  lblSign.Caption := 'Zero';
```

### Is a number even or odd?
```pascal
if iNum mod 2 = 0 then
  lblResult.Caption := 'Even'
else
  lblResult.Caption := 'Odd';
```

### Is a year a leap year?
A year is a leap year if:
- Divisible by 4 **AND** NOT divisible by 100, **OR**
- Divisible by 400

```pascal
if (iYear mod 400 = 0) or ((iYear mod 4 = 0) and (iYear mod 100 <> 0)) then
  lblLeap.Caption := 'Leap year'
else
  lblLeap.Caption := 'Not a leap year';
```

### Maximum of two numbers:
```pascal
if iA > iB then
  iMax := iA
else
  iMax := iB;
```

### Maximum of three numbers:
```pascal
if (iA >= iB) and (iA >= iC) then
  iMax := iA
else if iB >= iC then
  iMax := iB
else
  iMax := iC;
```

---

## Practice Exercises

### Exercise 1 — BMI Classifier
Write an algorithm that inputs a BMI value and outputs the category:
- BMI < 18.5: Underweight
- BMI 18.5–24.9: Normal weight
- BMI 25–29.9: Overweight
- BMI ≥ 30: Obese

<details>
<summary>Solution</summary>

```pascal
procedure TForm1.btnClassifyClick(Sender: TObject);
var
  rBMI: Real;
  sCategory: String;
begin
  rBMI := StrToFloat(edtBMI.Text);
  if rBMI < 18.5 then
    sCategory := 'Underweight'
  else if rBMI < 25 then
    sCategory := 'Normal weight'
  else if rBMI < 30 then
    sCategory := 'Overweight'
  else
    sCategory := 'Obese';
  lblCategory.Caption := sCategory;
end;
```
</details>

---

### Exercise 2 — Day type
Input a day number (1–7) where 1=Monday. Display whether it is a Weekday or Weekend.

<details>
<summary>Solution</summary>

```pascal
var
  iDay: Integer;
begin
  iDay := StrToInt(edtDay.Text);
  case iDay of
    1..5: lblType.Caption := 'Weekday';
    6, 7: lblType.Caption := 'Weekend';
  else
    lblType.Caption := 'Invalid';
  end;
end;
```
</details>

---

### Exercise 3 — Electricity tariff
Input units used. Calculate cost:
- First 50 units: R0.50/unit
- Next 100 units (51–150): R0.80/unit
- Above 150 units: R1.20/unit

<details>
<summary>Solution</summary>

```pascal
var
  iUnits: Integer;
  rCost: Real;
begin
  iUnits := StrToInt(edtUnits.Text);
  if iUnits <= 50 then
    rCost := iUnits * 0.50
  else if iUnits <= 150 then
    rCost := 50 * 0.50 + (iUnits - 50) * 0.80
  else
    rCost := 50 * 0.50 + 100 * 0.80 + (iUnits - 150) * 1.20;
  lblCost.Caption := 'R' + FloatToStrF(rCost, ffFixed, 10, 2);
end;
```
</details>
