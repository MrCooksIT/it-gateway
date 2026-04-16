# Classic Algorithm Problems

These are the CAPS-prescribed algorithm problems that appear regularly in Paper 1. Master these patterns and you can solve almost any exam question by recognising which pattern applies.

---

## Pattern Recognition

Before writing code, identify which pattern the problem uses:

| Pattern | Signal words | Algorithm |
|---|---|---|
| **Sum / Total** | "add up", "total", "sum" | Accumulator in a loop |
| **Count** | "how many", "count the" | Counter + condition in a loop |
| **Max / Min** | "largest", "smallest", "highest", "lowest" | Track current max/min across loop |
| **Prime check** | "is prime", "prime numbers" | Trial division |
| **Factorial** | "n!" | Multiply 1 × 2 × 3 × ... × n |
| **GCD** | "highest common factor" | Euclidean algorithm |
| **LCM** | "lowest common multiple" | LCM = (a × b) / GCD(a, b) |
| **Fibonacci** | "Fibonacci sequence" | Each = sum of two before |
| **Reverse** | "reverse digits", "backwards" | MOD 10 / DIV 10 loop |
| **Digit sum** | "sum of digits" | MOD 10 + DIV 10 loop |

---

## 1. Sum and Average

**Problem:** Calculate the sum and average of n numbers.

```pascal
procedure TForm1.btnSumClick(Sender: TObject);
var
  i, iN, iNum, iSum: Integer;
  rAvg: Real;
begin
  iN := StrToInt(edtN.Text);
  iSum := 0;
  for i := 1 to iN do
  begin
    iNum := StrToInt(InputBox('Input', 'Enter number ' + IntToStr(i) + ':', ''));
    iSum := iSum + iNum;
  end;
  rAvg := iSum / iN;
  lblResult.Caption := 'Sum: ' + IntToStr(iSum) +
                       ', Average: ' + FloatToStrF(rAvg, ffFixed, 8, 2);
end;
```

---

## 2. Maximum and Minimum

**Problem:** Find the largest and smallest of n numbers.

```pascal
procedure TForm1.btnMaxMinClick(Sender: TObject);
var
  i, iN, iNum, iMax, iMin: Integer;
begin
  iN := StrToInt(edtN.Text);
  // First number is initial max and min
  iMax := StrToInt(InputBox('Input', 'Enter number 1:', ''));
  iMin := iMax;

  for i := 2 to iN do
  begin
    iNum := StrToInt(InputBox('Input', 'Enter number ' + IntToStr(i) + ':', ''));
    if iNum > iMax then
      iMax := iNum;
    if iNum < iMin then
      iMin := iNum;
  end;
  lblResult.Caption := 'Max: ' + IntToStr(iMax) + ', Min: ' + IntToStr(iMin);
end;
```

> [!TIP] Key technique
> Always initialise max and min with the **first value**, not 0. If you initialise max to 0 and all numbers are negative, max stays 0 — which is wrong.

---

## 3. Prime Number Check

A **prime number** is only divisible by 1 and itself.  
**Examples:** 2, 3, 5, 7, 11, 13, 17, 19, 23...

**Algorithm — trial division:**
- 1 is not prime
- 2 is prime
- For any number n > 2, check if any integer from 2 to √n divides n evenly
- If any divisor found → not prime; if none found → prime

```pascal
function IsPrime(iNum: Integer): Boolean;
var
  i: Integer;
  bPrime: Boolean;
begin
  if iNum <= 1 then
    bPrime := False
  else if iNum = 2 then
    bPrime := True
  else
  begin
    bPrime := True;
    i := 2;
    while (i * i <= iNum) and bPrime do
    begin
      if iNum mod i = 0 then
        bPrime := False;
      Inc(i);
    end;
  end;
  Result := bPrime;
end;

procedure TForm1.btnPrimeClick(Sender: TObject);
var
  iNum: Integer;
begin
  iNum := StrToInt(edtNumber.Text);
  if IsPrime(iNum) then
    lblResult.Caption := IntToStr(iNum) + ' is prime'
  else
    lblResult.Caption := IntToStr(iNum) + ' is not prime';
end;
```

### List all primes up to n:

```pascal
procedure TForm1.btnListPrimesClick(Sender: TObject);
var
  i: Integer;
  sResult: String;
begin
  sResult := 'Primes: ';
  for i := 2 to StrToInt(edtN.Text) do
    if IsPrime(i) then
      sResult := sResult + IntToStr(i) + ' ';
  lblResult.Caption := sResult;
end;
```

---

## 4. Factorial

**n!** = n × (n-1) × (n-2) × ... × 2 × 1  
**Example:** 5! = 5 × 4 × 3 × 2 × 1 = 120

By definition: 0! = 1

```pascal
function Factorial(iN: Integer): Int64;
var
  i: Integer;
  iResult: Int64;
begin
  iResult := 1;
  for i := 1 to iN do
    iResult := iResult * i;
  Result := iResult;
end;

procedure TForm1.btnFactorialClick(Sender: TObject);
var
  iN: Integer;
begin
  iN := StrToInt(edtN.Text);
  if iN < 0 then
    ShowMessage('Factorial not defined for negative numbers')
  else
    lblResult.Caption := IntToStr(iN) + '! = ' + IntToStr(Factorial(iN));
end;
```

> [!WARNING] Use Int64 not Integer
> 13! = 6,227,020,800 — exceeds Integer range. Use Int64 or even larger types for large factorials.

---

## 5. GCD — Greatest Common Divisor

The **GCD** (also called HCF — Highest Common Factor) is the largest number that divides both a and b exactly.

**Example:** GCD(12, 8) = 4

**Euclidean algorithm:**
- If b = 0, then GCD = a
- Otherwise: GCD(a, b) = GCD(b, a mod b)

```pascal
function GCD(iA, iB: Integer): Integer;
begin
  while iB <> 0 do
  begin
    iA := iA mod iB;
    // swap
    iA := iA xor iB;
    iB := iA xor iB;
    iA := iA xor iB;
  end;
  Result := iA;
end;
```

**Cleaner version using a temp variable:**

```pascal
function GCD(iA, iB: Integer): Integer;
var
  iTemp: Integer;
begin
  while iB <> 0 do
  begin
    iTemp := iB;
    iB := iA mod iB;
    iA := iTemp;
  end;
  Result := iA;
end;

procedure TForm1.btnGCDClick(Sender: TObject);
var
  iA, iB: Integer;
begin
  iA := StrToInt(edtA.Text);
  iB := StrToInt(edtB.Text);
  lblResult.Caption := 'GCD(' + IntToStr(iA) + ', ' + IntToStr(iB) + ') = ' +
                       IntToStr(GCD(iA, iB));
end;
```

**Trace through GCD(12, 8):**
| iA | iB | iTemp |
|---|---|---|
| 12 | 8 | — |
| 8 | 4 | 8 |
| 4 | 0 | 4 |
| → Result = 4 | | |

---

## 6. LCM — Lowest Common Multiple

The **LCM** is the smallest positive number that is a multiple of both a and b.

**Formula:** LCM(a, b) = (a × b) / GCD(a, b)

**Example:** LCM(4, 6) = (4 × 6) / GCD(4, 6) = 24 / 2 = 12

```pascal
function LCM(iA, iB: Integer): Integer;
begin
  Result := (iA * iB) div GCD(iA, iB);
end;

procedure TForm1.btnLCMClick(Sender: TObject);
var
  iA, iB: Integer;
begin
  iA := StrToInt(edtA.Text);
  iB := StrToInt(edtB.Text);
  lblResult.Caption := 'LCM(' + IntToStr(iA) + ', ' + IntToStr(iB) + ') = ' +
                       IntToStr(LCM(iA, iB));
end;
```

---

## 7. Fibonacci Sequence

Each number is the sum of the two before it.  
**Sequence:** 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

```pascal
procedure TForm1.btnFibClick(Sender: TObject);
var
  i, iN, iA, iB, iTemp: Integer;
begin
  iN := StrToInt(edtN.Text);
  lbOutput.Clear;
  if iN >= 1 then
  begin
    iA := 1;
    lbOutput.Items.Add(IntToStr(iA));
  end;
  if iN >= 2 then
  begin
    iB := 1;
    lbOutput.Items.Add(IntToStr(iB));
  end;
  for i := 3 to iN do
  begin
    iTemp := iA + iB;
    lbOutput.Items.Add(IntToStr(iTemp));
    iA := iB;
    iB := iTemp;
  end;
end;
```

**Nth Fibonacci number (function):**

```pascal
function Fibonacci(iN: Integer): Integer;
var
  i, iA, iB, iTemp: Integer;
begin
  if iN <= 2 then
    Result := 1
  else
  begin
    iA := 1;
    iB := 1;
    for i := 3 to iN do
    begin
      iTemp := iA + iB;
      iA := iB;
      iB := iTemp;
    end;
    Result := iB;
  end;
end;
```

---

## 8. Digit Operations

### Sum of digits

`1234 → 1 + 2 + 3 + 4 = 10`

```pascal
function SumOfDigits(iNum: Integer): Integer;
var
  iSum: Integer;
begin
  iSum := 0;
  iNum := Abs(iNum);          // handle negatives
  while iNum > 0 do
  begin
    iSum := iSum + (iNum mod 10);
    iNum := iNum div 10;
  end;
  Result := iSum;
end;
```

### Count digits

`12345 → 5 digits`

```pascal
function CountDigits(iNum: Integer): Integer;
var
  iCount: Integer;
begin
  iNum := Abs(iNum);
  iCount := 0;
  if iNum = 0 then
    iCount := 1
  else
    while iNum > 0 do
    begin
      Inc(iCount);
      iNum := iNum div 10;
    end;
  Result := iCount;
end;
```

### Reverse a number

`1234 → 4321`

```pascal
function ReverseNumber(iNum: Integer): Integer;
var
  iReversed: Integer;
begin
  iReversed := 0;
  while iNum > 0 do
  begin
    iReversed := iReversed * 10 + (iNum mod 10);
    iNum := iNum div 10;
  end;
  Result := iReversed;
end;
```

### Palindrome check

A palindrome reads the same forwards and backwards: 121, 1331, 12321

```pascal
function IsPalindrome(iNum: Integer): Boolean;
begin
  Result := iNum = ReverseNumber(iNum);
end;
```

---

## 9. Even and Odd

### Count even and odd numbers in a list:

```pascal
procedure TForm1.btnEvenOddClick(Sender: TObject);
var
  i, iNum, iEven, iOdd: Integer;
begin
  iEven := 0;
  iOdd := 0;
  for i := 1 to 10 do
  begin
    iNum := StrToInt(InputBox('Input', 'Enter number ' + IntToStr(i) + ':', ''));
    if iNum mod 2 = 0 then
      Inc(iEven)
    else
      Inc(iOdd);
  end;
  lblResult.Caption := 'Even: ' + IntToStr(iEven) + ', Odd: ' + IntToStr(iOdd);
end;
```

---

## 10. Power (Exponentiation)

Calculate a^n (a to the power of n) without using the built-in `Power` function.

```pascal
function MyPower(iBase, iExp: Integer): Int64;
var
  i: Integer;
  iResult: Int64;
begin
  iResult := 1;
  for i := 1 to iExp do
    iResult := iResult * iBase;
  Result := iResult;
end;
```

---

## Practice Exercises

### Exercise 1 — Perfect Number
A **perfect number** equals the sum of its proper divisors (all divisors except itself).  
Example: 6 = 1 + 2 + 3 → perfect. 28 = 1 + 2 + 4 + 7 + 14 → perfect.

Write a function `IsPerfect(n)` that returns True if n is perfect.

<details>
<summary>Solution</summary>

```pascal
function IsPerfect(iNum: Integer): Boolean;
var
  i, iSum: Integer;
begin
  iSum := 1;                   // 1 is always a divisor (for n > 1)
  for i := 2 to iNum div 2 do
    if iNum mod i = 0 then
      iSum := iSum + i;
  Result := (iNum > 1) and (iSum = iNum);
end;
```
</details>

---

### Exercise 2 — List all primes between two numbers
Input two numbers (lower and upper bound). List all prime numbers between them inclusive.

<details>
<summary>Solution</summary>

```pascal
procedure TForm1.btnPrimeRangeClick(Sender: TObject);
var
  i, iLow, iHigh: Integer;
begin
  iLow := StrToInt(edtLow.Text);
  iHigh := StrToInt(edtHigh.Text);
  lbPrimes.Clear;
  for i := iLow to iHigh do
    if IsPrime(i) then
      lbPrimes.Items.Add(IntToStr(i));
end;
```
</details>

---

### Exercise 3 — Goldbach's Conjecture
Every even number > 2 can be written as the sum of two primes.  
Input an even number. Find ONE pair of primes that sum to it.  
Example: 28 = 5 + 23

<details>
<summary>Solution</summary>

```pascal
procedure TForm1.btnGoldbachClick(Sender: TObject);
var
  iNum, i: Integer;
  bFound: Boolean;
begin
  iNum := StrToInt(edtNumber.Text);
  bFound := False;
  i := 2;
  while (i <= iNum div 2) and not bFound do
  begin
    if IsPrime(i) and IsPrime(iNum - i) then
    begin
      lblResult.Caption := IntToStr(iNum) + ' = ' + IntToStr(i) + ' + ' + IntToStr(iNum - i);
      bFound := True;
    end;
    Inc(i);
  end;
  if not bFound then
    lblResult.Caption := 'No pair found';
end;
```
</details>
