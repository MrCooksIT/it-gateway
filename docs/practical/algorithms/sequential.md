---
title: Sequential Structures
parent: Algorithms
grand_parent: Practical (Paper 1)
nav_order: 1
---

# Sequential Algorithms

> [!NOTE] Grade 10 — Foundation
> A sequential algorithm is the simplest type. Master this before moving to decisions and loops. Every program contains at least some sequential steps.

---

## 1. What Is a Sequential Algorithm?

A **sequential algorithm** executes steps **one after another in a fixed, top-to-bottom order**. There are no decisions (no branching) and no repetition (no loops). Every step always runs exactly once.

### Characteristics

| Feature | Detail |
|---|---|
| Order | Steps always run in the same order |
| Branches | None — no IF statements |
| Loops | None — no FOR, WHILE, or REPEAT |
| Predictability | Given the same input, always produces the same output |
| Structure | INPUT → PROCESS → OUTPUT |

---

## 2. Flowchart for a Sequential Algorithm

A sequential flowchart uses only three shapes:

```
[OVAL]              START
       ↓
[PARALLELOGRAM]     INPUT value(s)
       ↓
[RECTANGLE]         PROCESS (calculate)
       ↓
[PARALLELOGRAM]     OUTPUT result
       ↓
[OVAL]              END
```

There are no diamonds (decision symbols) in a sequential flowchart.

---

## 3. Worked Example 1 — Area of a Rectangle

### Algorithm (numbered steps)

```
1. START
2. READ length
3. READ width
4. CALCULATE area = length × width
5. DISPLAY area
6. END
```

### Pseudocode

```
INPUT rLength
INPUT rWidth
rArea := rLength * rWidth
OUTPUT rArea
```

### Delphi Code

```pascal
procedure TForm1.btnCalculateClick(Sender: TObject);
var
  rLength, rWidth, rArea : Real;
begin
  rLength := StrToFloat(edtLength.Text);
  rWidth  := StrToFloat(edtWidth.Text);
  rArea   := rLength * rWidth;
  lblArea.Caption := 'Area = ' + FloatToStr(rArea);
end;
```

### Trace Table (input: length = 5, width = 3)

| Step | `rLength` | `rWidth` | `rArea` | Output |
|---|---|---|---|---|
| 2 | 5 | — | — | — |
| 3 | 5 | 3 | — | — |
| 4 | 5 | 3 | 15 | — |
| 5 | 5 | 3 | 15 | 15 |

---

## 4. Worked Example 2 — Calculate Change

A customer pays for an item. Calculate the change they receive.

### Algorithm

```
1. START
2. READ price
3. READ amountPaid
4. CALCULATE change = amountPaid - price
5. DISPLAY change
6. END
```

### Pseudocode

```
INPUT rPrice
INPUT rAmountPaid
rChange := rAmountPaid - rPrice
OUTPUT "Change: R" + rChange
```

### Delphi Code

```pascal
procedure TForm1.btnChangeClick(Sender: TObject);
var
  rPrice, rAmountPaid, rChange : Real;
begin
  rPrice      := StrToFloat(edtPrice.Text);
  rAmountPaid := StrToFloat(edtAmountPaid.Text);
  rChange     := rAmountPaid - rPrice;
  lblChange.Caption := 'Change: R' + FloatToStrF(rChange, ffFixed, 8, 2);
end;
```

> [!TIP] Exam Tip
> Use `FloatToStrF(value, ffFixed, 8, 2)` to display currency with exactly 2 decimal places. `FloatToStr` may show many decimal digits which looks unprofessional for money.

### Trace Table (input: price = 49.99, amountPaid = 100.00)

| Step | `rPrice` | `rAmountPaid` | `rChange` | Output |
|---|---|---|---|---|
| 2 | 49.99 | — | — | — |
| 3 | 49.99 | 100.00 | — | — |
| 4 | 49.99 | 100.00 | 50.01 | — |
| 5 | 49.99 | 100.00 | 50.01 | Change: R50.01 |

---

## 5. Worked Example 3 — Average of Three Numbers

### Algorithm

```
1. START
2. READ num1
3. READ num2
4. READ num3
5. CALCULATE total = num1 + num2 + num3
6. CALCULATE average = total / 3
7. DISPLAY average
8. END
```

### Pseudocode

```
INPUT rNum1
INPUT rNum2
INPUT rNum3
rTotal   := rNum1 + rNum2 + rNum3
rAverage := rTotal / 3
OUTPUT rAverage
```

### Delphi Code

```pascal
procedure TForm1.btnAverageClick(Sender: TObject);
var
  rNum1, rNum2, rNum3 : Real;
  rTotal, rAverage    : Real;
begin
  rNum1    := StrToFloat(edtNum1.Text);
  rNum2    := StrToFloat(edtNum2.Text);
  rNum3    := StrToFloat(edtNum3.Text);
  rTotal   := rNum1 + rNum2 + rNum3;
  rAverage := rTotal / 3;
  lblAverage.Caption := 'Average = ' + FloatToStrF(rAverage, ffFixed, 8, 2);
end;
```

> [!NOTE] Grade 10 — Foundation
> Always calculate the total first, then divide. Never write `average := (num1 + num2 + num3) / 3` in pseudocode — that bundles two operations into one step. In algorithm form, keep them separate.

---

## 6. Worked Example 4 — Celsius to Fahrenheit

### Algorithm

```
1. START
2. READ celsius
3. CALCULATE fahrenheit = (celsius × 9 / 5) + 32
4. DISPLAY fahrenheit
5. END
```

### Pseudocode

```
INPUT rCelsius
rFahrenheit := (rCelsius * 9 / 5) + 32
OUTPUT "Temperature in °F: " + rFahrenheit
```

### Delphi Code

```pascal
procedure TForm1.btnConvertClick(Sender: TObject);
var
  rCelsius, rFahrenheit : Real;
begin
  rCelsius    := StrToFloat(edtCelsius.Text);
  rFahrenheit := (rCelsius * 9 / 5) + 32;
  lblResult.Caption := FloatToStrF(rCelsius, ffFixed, 8, 1)
                     + '°C = '
                     + FloatToStrF(rFahrenheit, ffFixed, 8, 1)
                     + '°F';
end;
```

### Trace Table (input: celsius = 100)

| Step | `rCelsius` | `rFahrenheit` | Output |
|---|---|---|---|
| 2 | 100 | — | — |
| 3 | 100 | 212 | — |
| 4 | 100 | 212 | 100.0°C = 212.0°F |

---

## 7. Common Mistakes to Avoid

| Mistake | Correct Approach |
|---|---|
| Forgetting `StrToFloat` / `StrToInt` | Component `.Text` is always a String — always convert before calculating |
| Using `=` instead of `:=` for assignment | In Delphi, `=` is for comparison only; `:=` assigns a value |
| Displaying a number directly | Convert back to String using `FloatToStr` or `IntToStr` |
| Putting two calculations in one step | One step = one operation |

---

## 8. Practice Exercises

Try writing the algorithm (numbered steps), pseudocode, and Delphi code for each:

1. **Simple Interest** — Read principal, rate, and time. Calculate `interest = principal × rate × time / 100`. Display the interest.

2. **Perimeter of a Circle** — Read the radius. Calculate `circumference = 2 × π × radius` (use `3.14159` for π). Display the circumference.

3. **Body Mass Index (BMI)** — Read weight (kg) and height (m). Calculate `BMI = weight / (height × height)`. Display BMI.

4. **Seconds to Hours and Minutes** — Read a number of seconds. Calculate how many complete minutes and remaining seconds it contains. Display the result.

5. **Rand to Dollar** — Read an amount in Rand. Read the exchange rate. Calculate the dollar amount. Display the result to 2 decimal places.

> [!TIP] Exam Tip
> In every sequential algorithm question: (1) identify all inputs, (2) write the formula, (3) identify what to display. That structure — READ, CALCULATE, DISPLAY — earns full marks.
