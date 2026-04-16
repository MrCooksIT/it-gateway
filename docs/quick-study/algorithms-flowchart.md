# Algorithms & Flowchart Symbols — Quick Reference

No prose. Symbols, pseudocode patterns, and algorithm structures only.

---

## Flowchart Symbols

| Symbol | Shape | Used for |
|---|---|---|
| **Terminal** | Oval / rounded rectangle | START and END |
| **Process** | Rectangle | Assignment, calculation |
| **Decision** | Diamond | IF condition (Yes/No branches) |
| **Input/Output** | Parallelogram | Input from user or display output |
| **Connector** | Small circle | Connect flowchart across a page |
| **Arrow** | Line with arrowhead | Flow direction |
| **Subroutine** | Rectangle with double vertical lines | Call a procedure/function |

---

## Algorithm Properties

A correct algorithm must be:
- **Finite** — eventually terminates
- **Definite** — each step is precisely defined
- **Effective** — every step is doable
- **Correct** — produces the right output for all inputs

---

## Pseudocode Conventions

```
READ name
WRITE "Hello, " + name
SET total = 0

IF condition THEN
  statements
ELSE
  statements
ENDIF

FOR counter = start TO end
  statements
ENDFOR

WHILE condition DO
  statements
ENDWHILE

REPEAT
  statements
UNTIL condition
```

---

## Sequential Algorithm Pattern

```
START
  READ/CALCULATE inputs
  PROCESS (compute, assign)
  WRITE/DISPLAY outputs
END
```

**Example — Calculate VAT:**
```
START
  READ price
  SET vat = price × 0.15
  SET total = price + vat
  WRITE "Total: R" + total
END
```

---

## Decision Algorithm Patterns

### Single IF
```
IF mark >= 50 THEN
  WRITE "Pass"
ENDIF
```

### IF...ELSE
```
IF mark >= 50 THEN
  WRITE "Pass"
ELSE
  WRITE "Fail"
ENDIF
```

### Chained
```
IF mark >= 80 THEN
  grade = "A"
ELSE IF mark >= 70 THEN
  grade = "B"
ELSE IF mark >= 50 THEN
  grade = "C"
ELSE
  grade = "F"
ENDIF
```

---

## Repetition Algorithm Patterns

### FOR (known iterations)
```
FOR i = 1 TO 10
  WRITE i
ENDFOR
```

### WHILE (may not run)
```
SET n = 1
WHILE n <= 100
  WRITE n
  SET n = n × 2
ENDWHILE
```

### REPEAT...UNTIL (runs at least once)
```
REPEAT
  READ choice
UNTIL choice = 0
```

---

## Common Algorithms — Templates

### Sum and Average
```
SET sum = 0
FOR i = 1 TO n
  sum = sum + a[i]
ENDFOR
average = sum / n
```

### Find Maximum
```
SET max = a[1]
FOR i = 2 TO n
  IF a[i] > max THEN
    max = a[i]
  ENDIF
ENDFOR
```

### Find Minimum
```
SET min = a[1]
FOR i = 2 TO n
  IF a[i] < min THEN
    min = a[i]
  ENDIF
ENDFOR
```

### Linear Search
```
SET found = FALSE
SET pos = 0
FOR i = 1 TO n
  IF a[i] = target THEN
    found = TRUE
    pos = i
  ENDIF
ENDFOR
IF found THEN
  WRITE "Found at " + pos
ELSE
  WRITE "Not found"
ENDIF
```

### Count Condition
```
SET count = 0
FOR i = 1 TO n
  IF a[i] > threshold THEN
    count = count + 1
  ENDIF
ENDFOR
```

### Bubble Sort (ascending)
```
FOR i = 1 TO n-1
  FOR j = 1 TO n-i
    IF a[j] > a[j+1] THEN
      SWAP a[j] and a[j+1]
    ENDIF
  ENDFOR
ENDFOR
```

### Check Prime
```
SET isPrime = TRUE
IF n <= 1 THEN isPrime = FALSE
FOR i = 2 TO n-1
  IF n MOD i = 0 THEN
    isPrime = FALSE
  ENDIF
ENDFOR
```

---

## Tracing an Algorithm

Given:
```
SET x = 5
SET y = 2
WHILE y < x
  SET x = x - 1
  SET y = y + 1
ENDWHILE
WRITE x, y
```

| Step | x | y | Condition y < x |
|---|---|---|---|
| Start | 5 | 2 | 2 < 5 = TRUE |
| After iter 1 | 4 | 3 | 3 < 4 = TRUE |
| After iter 2 | 3 | 4 | 4 < 3 = FALSE → stop |

Output: x=3, y=4

---

## Delphi Equivalent Patterns

| Pseudocode | Delphi |
|---|---|
| `SET x = 5` | `x := 5;` |
| `READ name` | `sName := edtName.Text;` |
| `WRITE msg` | `redOutput.Lines.Add(msg);` |
| `IF x > 0 THEN` | `IF x > 0 THEN` |
| `FOR i = 1 TO n` | `FOR i := 1 TO n DO` |
| `WHILE x < 10 DO` | `WHILE x < 10 DO` |
| `REPEAT...UNTIL x = 0` | `REPEAT...UNTIL x = 0;` |
| `SWAP a, b` | `t := a; a := b; b := t;` |
