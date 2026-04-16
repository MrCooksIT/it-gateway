# Repetition Structures in Algorithms

Doing the same task over and over is what computers excel at. Adding 1,000 numbers, checking every email in a folder, processing every pixel in an image — repetition structures make this possible without writing the same code a thousand times.

---

## Types of Loops

| Loop | Use when | Condition checked |
|---|---|---|
| **FOR** | You know exactly how many times to repeat | Before each iteration |
| **WHILE** | Repeat while condition is true; may execute 0 times | Before each iteration |
| **REPEAT-UNTIL** | Repeat until condition becomes true; always executes at least once | After each iteration |

---

## FOR Loop

Use when the number of repetitions is **known in advance**.

**Flowchart:**
```
counter ← start
    ↓
┌──────────────────┐
│ counter <= end?  │
└──────┬───────────┘
 YES   │   NO
  ↓         ↓
body       EXIT
  ↓
counter ← counter + 1
  ↑________________________|
```

**Pseudocode:**
```
FOR counter ← 1 TO 10 DO
    statements
END FOR
```

**Delphi (counting up):**
```pascal
var
  i: Integer;
begin
  for i := 1 to 10 do
  begin
    // body executes for i = 1, 2, 3, ... 10
    lbOutput.Items.Add(IntToStr(i));
  end;
end;
```

**Delphi (counting down):**
```pascal
for i := 10 downto 1 do
  lbOutput.Items.Add(IntToStr(i));
```

---

## WHILE Loop

Use when you want to repeat **while a condition is true** — and you're not sure in advance how many times.

The condition is checked **before** the body executes. If false at the start, body never executes.

**Flowchart:**
```
    ↓
┌──────────────┐
│  Condition?  │
└──────┬───────┘
 TRUE  │   FALSE
  ↓         ↓
body       EXIT
  ↑________________________|
```

**Pseudocode:**
```
WHILE condition DO
    statements
END WHILE
```

**Delphi:**
```pascal
var
  iNum, iSum: Integer;
begin
  iSum := 0;
  iNum := StrToInt(edtStart.Text);
  while iNum > 0 do
  begin
    iSum := iSum + iNum;
    iNum := iNum - 1;
  end;
  lblSum.Caption := IntToStr(iSum);
end;
```

---

## REPEAT-UNTIL Loop

Use when the body must execute **at least once**, and you repeat until the condition becomes true.

The condition is checked **after** the body executes.

**Flowchart:**
```
    ↓
  body
    ↓
┌──────────────┐
│  Condition?  │
└──────┬───────┘
 TRUE  │   FALSE
  ↓         ↑
EXIT    (repeat)
```

**Pseudocode:**
```
REPEAT
    statements
UNTIL condition
```

**Delphi:**
```pascal
var
  sInput: String;
  iNum: Integer;
begin
  repeat
    sInput := InputBox('Input', 'Enter a number between 1 and 10:', '');
    iNum := StrToInt(sInput);
  until (iNum >= 1) and (iNum <= 10);
  ShowMessage('You entered: ' + IntToStr(iNum));
end;
```

---

## Loop Comparison

| Feature | FOR | WHILE | REPEAT-UNTIL |
|---|---|---|---|
| Iterations known? | Yes | No | No |
| Condition checked | Before (pre-test) | Before (pre-test) | After (post-test) |
| Min executions | 0 (if end < start) | 0 | 1 (always) |
| Use case | Fixed count | Unknown count | Input validation, menu |

---

## Accumulator Pattern

Very common pattern: accumulate a total inside a loop.

```pascal
// Sum of 1 to n
var
  i, iN, iSum: Integer;
begin
  iN := StrToInt(edtN.Text);
  iSum := 0;                    // initialise accumulator
  for i := 1 to iN do
    iSum := iSum + i;           // accumulate
  lblSum.Caption := IntToStr(iSum);
end;
```

---

## Counter Pattern

Count how many values satisfy a condition.

```pascal
// Count even numbers entered
var
  i, iNum, iCount: Integer;
begin
  iCount := 0;                  // initialise counter
  for i := 1 to 10 do
  begin
    iNum := StrToInt(InputBox('Input', 'Enter number ' + IntToStr(i) + ':', ''));
    if iNum mod 2 = 0 then
      Inc(iCount);              // count this one
  end;
  lblCount.Caption := 'Even numbers: ' + IntToStr(iCount);
end;
```

---

## Finding Minimum and Maximum

```pascal
// Find the largest of 5 numbers entered
var
  i, iNum, iMax: Integer;
begin
  // First input becomes initial max
  iMax := StrToInt(InputBox('Input', 'Enter number 1:', ''));
  
  for i := 2 to 5 do
  begin
    iNum := StrToInt(InputBox('Input', 'Enter number ' + IntToStr(i) + ':', ''));
    if iNum > iMax then
      iMax := iNum;             // new maximum found
  end;
  lblMax.Caption := 'Maximum: ' + IntToStr(iMax);
end;
```

---

## Nested Loops

A loop inside another loop. Inner loop completes fully for each iteration of the outer loop.

**Use case:** multiplication table, 2D arrays, patterns

```pascal
// Multiplication table 1–5
var
  i, j: Integer;
begin
  lbOutput.Clear;
  for i := 1 to 5 do
  begin
    for j := 1 to 5 do
    begin
      lbOutput.Items.Add(IntToStr(i) + ' × ' + IntToStr(j) + ' = ' + IntToStr(i * j));
    end;
  end;
end;
```

**Total iterations** = outer iterations × inner iterations = 5 × 5 = 25

---

## Worked Examples

### Example 1 — Sum of digits

**Problem:** Input a positive integer. Sum all its digits.  
`123 → 1+2+3 = 6`

**Algorithm:**
```
INPUT number
sum ← 0
WHILE number > 0 DO
    digit ← number MOD 10
    sum ← sum + digit
    number ← number DIV 10
END WHILE
OUTPUT sum
```

**Delphi:**
```pascal
procedure TForm1.btnSumDigitsClick(Sender: TObject);
var
  iNum, iSum, iDigit: Integer;
begin
  iNum := StrToInt(edtNumber.Text);
  iSum := 0;
  while iNum > 0 do
  begin
    iDigit := iNum mod 10;
    iSum := iSum + iDigit;
    iNum := iNum div 10;
  end;
  lblSum.Caption := 'Sum of digits: ' + IntToStr(iSum);
end;
```

---

### Example 2 — Fibonacci sequence

**Problem:** Display the first 10 Fibonacci numbers (1, 1, 2, 3, 5, 8, 13, 21, 34, 55).

```pascal
procedure TForm1.btnFibClick(Sender: TObject);
var
  i, iA, iB, iTemp: Integer;
begin
  lbOutput.Clear;
  iA := 1;
  iB := 1;
  lbOutput.Items.Add(IntToStr(iA));
  lbOutput.Items.Add(IntToStr(iB));
  for i := 3 to 10 do
  begin
    iTemp := iA + iB;
    lbOutput.Items.Add(IntToStr(iTemp));
    iA := iB;
    iB := iTemp;
  end;
end;
```

---

### Example 3 — Input validation loop

**Problem:** Keep asking for input until a valid mark (0–100) is entered.

```pascal
procedure TForm1.btnGetMarkClick(Sender: TObject);
var
  iMark: Integer;
begin
  repeat
    iMark := StrToInt(InputBox('Mark', 'Enter mark (0-100):', ''));
    if (iMark < 0) or (iMark > 100) then
      ShowMessage('Invalid! Mark must be between 0 and 100.');
  until (iMark >= 0) and (iMark <= 100);
  lblMark.Caption := 'Mark accepted: ' + IntToStr(iMark);
end;
```

---

## Practice Exercises

### Exercise 1 — Factorial
Calculate n! (e.g. 5! = 5×4×3×2×1 = 120). Input n from user.

<details>
<summary>Solution</summary>

```pascal
var
  i, iN: Integer;
  iFactorial: Int64;
begin
  iN := StrToInt(edtN.Text);
  iFactorial := 1;
  for i := 1 to iN do
    iFactorial := iFactorial * i;
  lblResult.Caption := IntToStr(iN) + '! = ' + IntToStr(iFactorial);
end;
```
</details>

---

### Exercise 2 — Count numbers above average
Input 10 numbers. Calculate the average, then count how many are above the average.

<details>
<summary>Solution</summary>

```pascal
var
  aNumbers: array[1..10] of Integer;
  i, iSum, iCount: Integer;
  rAvg: Real;
begin
  iSum := 0;
  for i := 1 to 10 do
  begin
    aNumbers[i] := StrToInt(InputBox('Input', 'Number ' + IntToStr(i) + ':', ''));
    iSum := iSum + aNumbers[i];
  end;
  rAvg := iSum / 10;
  iCount := 0;
  for i := 1 to 10 do
    if aNumbers[i] > rAvg then
      Inc(iCount);
  lblResult.Caption := 'Average: ' + FloatToStrF(rAvg, ffFixed, 5, 1)
                     + ', Above average: ' + IntToStr(iCount);
end;
```
</details>

---

### Exercise 3 — Reverse a number
Input a positive integer and output its digits in reverse order.  
Example: 1234 → 4321

<details>
<summary>Solution</summary>

```pascal
var
  iNum, iReversed, iDigit: Integer;
begin
  iNum := StrToInt(edtNumber.Text);
  iReversed := 0;
  while iNum > 0 do
  begin
    iDigit := iNum mod 10;
    iReversed := iReversed * 10 + iDigit;
    iNum := iNum div 10;
  end;
  lblResult.Caption := 'Reversed: ' + IntToStr(iReversed);
end;
```
</details>
