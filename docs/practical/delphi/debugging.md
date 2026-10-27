---
title: Debugging and Error Types (Grade 10)
description: Syntax, runtime and logic errors in Delphi, how to find them, and how to fix given code in an exam.
---

# Debugging and Error Types

::: info 📌 Key Points
- There are three types of errors: **syntax** (the code won't compile), **runtime** (it crashes while running) and **logic** (it runs but gives the wrong answer).
- The compiler finds syntax errors for you, but only **testing** finds logic errors.
- Use **trace tables**, **breakpoints** and **test data** (normal, boundary and invalid values) to track errors down.
- Exams give you broken code and ask you to find **and** fix the errors. Each error is usually worth 2 marks.
:::

Your program compiles, you click the button, and it shows `Change: R-26.50`. Nothing crashed and the code looks fine, but the answer is wrong. Programmers spend more time finding mistakes than writing new code, and a structured way of hunting for them is one of the most useful programming skills you can learn.

---

## See it working — broken code

This code should calculate the change for a customer. It contains **four** errors:

```pascal
procedure TfrmShop.btnChangeClick(Sender: TObject);
var
  rTotal, rPaid, rChange: Real;
begin
  rTotal := StrToFloat(edtTotal.Text)                   // ❶
  rPaid := StrToInt(edtPaid.Text);                      // ❷
  rChange := rTotal - rPaid;                            // ❸
  if rChange < 0 then
    lblChange.Caption := 'Insufficient amount paid';    // ❹
  else
    lblChange.Caption := 'Change: ' + FloatToStrF(rChange, ffCurrency, 8, 2);
end;
```

| # | Error | Type | Fix |
|---|---|---|---|
| ❶ | Missing `;` at the end of the statement | Syntax | `rTotal := StrToFloat(edtTotal.Text);` |
| ❷ | `StrToInt` crashes when the user enters 50.50 | Runtime | `rPaid := StrToFloat(edtPaid.Text);` |
| ❸ | Operands swapped, so the change is negative | Logic | `rChange := rPaid - rTotal;` |
| ❹ | `;` before `else` is not allowed | Syntax | Remove the `;` after `'Insufficient amount paid'` |

---

## The three types of errors

| | Syntax error | Runtime error | Logic error |
|---|---|---|---|
| **What it is** | The code breaks the rules of the language | The code is valid but an illegal operation happens while it runs | The code runs but produces the wrong result |
| **When found** | When you compile (F9 / Ctrl+F9) | While the program runs | Only by testing and checking output |
| **What you see** | Red error in the Messages pane: `E2066 Missing operator or semicolon` | Program stops with an error message: `'abc' is not a valid integer value` | Wrong answer, no message |
| **Examples** | Missing `;`, misspelt `begn`, missing `end`, undeclared variable | `StrToInt('')`, division by zero, array index out of range, missing file | `<` instead of `<=`, wrong formula, counter not reset, `+` instead of `-` |

::: warning ⚠️ Common Misconception
Learners often think that **"it compiled, so it works"**. Compiling only proves there are no syntax errors. A program with a logic error can compile perfectly and still give the wrong answer every time.
:::

---

## Common Delphi compiler messages

| Message | Usual cause |
|---|---|
| `Undeclared identifier: 'iTotl'` | Spelling mistake or the variable was not declared in `var` |
| `';' expected but 'END' found` | Missing semicolon on the line before |
| `';' not allowed before 'ELSE'` | Remove the semicolon before `else` |
| `Incompatible types: 'string' and 'Integer'` | Missing `IntToStr` / `StrToInt` conversion |
| `Missing operator or semicolon` | Missing `;` or a missing `+` between strings |

::: tip 💡 Why This Matters
The compiler reports the error on the line **where it noticed the problem**, which is often the line **after** the real mistake. A missing `;` at the end of line 6 is usually reported on line 7. Always check the line above.
:::

---

## Debugging techniques

### 1. Trace tables
Work through the code by hand, writing down the value of every variable after each line. This is the main technique for finding **logic errors**, and you also need it for Paper 2.

```pascal
iTotal := 0;
for i := 1 to 3 do
  iTotal := iTotal + i * 2;
```

| Line | i | iTotal |
|---|---|---|
| iTotal := 0 | | 0 |
| loop | 1 | 2 |
| loop | 2 | 6 |
| loop | 3 | 12 |

### 2. Breakpoints and watches (Delphi IDE)
- Click in the grey margin next to a line to set a **breakpoint** (red dot). The program pauses there.
- Press **F8** (step over) to run one line at a time.
- Hover over a variable or add it to the **Watch List** (Ctrl+F5) to see its value.

### 3. Temporary output
Display a variable while testing: `ShowMessage('iTotal = ' + IntToStr(iTotal));`. Remember to remove it afterwards.

### 4. Test data
Test with three kinds of data:

| Type | Example (mark out of 100) | Purpose |
|---|---|---|
| Normal | 65 | Does it work for typical values? |
| Boundary / extreme | 0, 49, 50, 100 | Does `>=` vs `>` work at the edge? |
| Invalid / erroneous | -5, 150, "abc" | Does validation catch it, or does it crash? |

---

## 📋 Summary

| Concept | Key point |
|---|---|
| Syntax error | Breaks language rules; found by the compiler |
| Runtime error | Crashes while running (bad conversion, ÷ 0, missing file) |
| Logic error | Wrong output, no message; found by testing / trace tables |
| Debugging | Trace tables, breakpoints (F8), temporary output, test data |

::: tip 🎯 Exam Tip
When a question gives you faulty code inside comment braces `{ }`, first remove the braces, then compile. The compiler finds the syntax errors for you. Then **run it with the example input** from the paper and compare the output to find the logic and runtime errors. Fix only what is wrong and don't rewrite working lines.
:::

## ✏️ Check Your Understanding

**Question 1:** Name the type of error: a loop runs 9 times instead of 10.

**Question 2:** Name the type of error and give a fix: `iAge := StrToInt(edtAge.Text);` crashes when the edit box is empty.

**Question 3:** Why can't a compiler find logic errors? (2)

::: details Check your answers
**Q1:** Logic error (probably `<` instead of `<=`, or the wrong start/end value).

**Q2:** Runtime error. Check that the edit box is not empty first (`if edtAge.Text = '' then`), use a spin edit, or use `TryStrToInt`.

**Q3:** The code obeys the rules of the language, so it is valid ✓. The compiler cannot know what the programmer *intended* the result to be ✓.
:::

---

*Previous: [← Input Validation](./validation) | Next: [Timer →](./timer)*
