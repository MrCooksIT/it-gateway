---
title: How to Practice & Study Code
nav_order: 5
has_children: true
---

# How to Practice & Study Code

Preparing for Paper 1 is different from studying for Paper 2. You can't just read notes — you need to **think like a programmer**. This section shows you how to do that, whether or not you have Delphi at home.

## Choose your path

| My situation | Where to start |
|---|---|
| I don't have a Windows PC at home | [Studying Without Delphi →](./study-without-delphi) |
| I have Windows and can install software | [Setting Up & Practising in Delphi →](./setup-delphi) |

::: tip Both paths matter
Even if you have Delphi at home, **start with the "Studying Without Delphi" guide**. The thinking and tracing skills there are what Paper 1 actually tests — Delphi is just where you type the answers.
:::

---

## What the exam really tests

Paper 1 is not testing whether you can drag a button onto a form. It tests whether you can **read a problem, think through a solution, and write correct code**.

The Delphi form is just a container. Everything that matters happens **inside the event handler**:

```pascal
procedure TForm1.btnCalculateClick(Sender: TObject);
begin
  // ← This is what the exam tests.
  //    This logic works the same in any Pascal program.
  //    You can study it without ever opening Delphi.
end;
```

The implication: you can study the vast majority of Paper 1 content with **nothing more than a pen and paper**.

---

## Core skills — what's "inside the container"

These are the skills Paper 1 tests. They are the same whether you study them on paper, in an online compiler, or in Delphi.

### Grade 10 foundations
- [ ] Declaring variables with the correct data type (`Integer`, `Real`, `String`, `Boolean`, `Char`)
- [ ] Assignments and arithmetic operators (`+`, `-`, `*`, `/`, `div`, `mod`)
- [ ] `if / else if / else` selection
- [ ] `case` statements
- [ ] `for` loops (counting up and down)
- [ ] `while` and `repeat...until` loops
- [ ] Reading from and writing to components (`edtInput.Text`, `lblOutput.Caption`)

### Grade 11 skills
- [ ] 1D arrays — declaring, filling, searching, sorting
- [ ] 2D arrays — rows and columns, nested loops
- [ ] String functions: `Length`, `Copy`, `Pos`, `UpCase`, `LowerCase`, `Trim`, `IntToStr`, `StrToInt`
- [ ] Math functions: `Round`, `Trunc`, `Abs`, `Sqr`, `Sqrt`
- [ ] Input validation (while loops checking conditions)
- [ ] SQL `SELECT` with `WHERE`, `ORDER BY`, `GROUP BY`, `HAVING`

### Grade 12 skills
- [ ] Procedures with parameters (`var` and value parameters)
- [ ] Functions with return values (`Result :=`)
- [ ] Text file operations (`AssignFile`, `Reset`, `Rewrite`, `ReadLn`, `WriteLn`, `CloseFile`)
- [ ] OOP: classes, constructors, properties, methods
- [ ] Inheritance and method overriding
- [ ] SQL `INSERT`, `UPDATE`, `DELETE`
- [ ] Connecting Delphi to a database (`TADOConnection`, `TADOQuery`)

---

## How to use this section

1. Work through [Studying Without Delphi](./study-without-delphi) to build logic, tracing, and reading skills
2. If you have Windows, follow [Setting Up Delphi](./setup-delphi) to practice in the real environment
3. Use [Quick Study](../quick-study/) cheat sheets as a reference while practising
4. Practice past papers under timed conditions — one question per 45 minutes
