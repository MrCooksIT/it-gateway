---
title: Algorithms (Theory)
parent: Solution Development (Theory)
grand_parent: Theory (Paper 2)
nav_order: 2
---

# Algorithms — Theory

> [!NOTE] Grade 10 — Foundation
> Algorithms are covered in **8 hours** of the Grade 10 theory section. Expect exam questions on drawing flowcharts, tracing algorithms, writing pseudocode, and identifying algorithm types.

---

## 1. What Is an Algorithm?

An **algorithm** is a step-by-step procedure used to solve a problem. Computer programs are simply lists of instructions — which means every program you write is, at its core, an algorithm. If an algorithm is not correct, it will cause errors in the resulting program.

> [!TIP] Exam Tip
> Always define an algorithm as: *a finite, ordered set of unambiguous steps that solves a problem and produces at least one result.*

### Everyday Example — Making Hot Chocolate

Consider the steps to make a cup of hot chocolate:

```
1. Boil water in the kettle.
2. Place a mug on the counter.
3. Add two teaspoons of hot chocolate powder to the mug.
4. Pour the boiling water into the mug.
5. Stir until the powder is dissolved.
6. Add milk or sugar if desired.
7. Serve.
```

This is an algorithm — it is a finite, ordered list of clear steps that ends with a result (a cup of hot chocolate). Each step is simple, specific, and cannot be misunderstood.

---

## 2. Properties of a Good Algorithm

For an algorithm to be considered correct and usable, it must meet all of the following criteria:

| # | Criterion | Explanation |
|---|---|---|
| 1 | **Finite number of steps** | The algorithm must eventually end — it cannot run forever. |
| 2 | **Easy to understand** | Steps must be written so any person (or computer) can follow them without guessing. |
| 3 | **Detailed and specific** | Vague instructions like "make it work" are not acceptable. |
| 4 | **Clear and unambiguous** | Each step must have only one possible interpretation. |
| 5 | **Single task per step** | Each step should do exactly one thing — not bundle several actions together. |
| 6 | **Most basic level** | Steps should not require prior expert knowledge to interpret. |
| 7 | **Repetitions have clear endings** | Any loop must have a condition that will eventually stop it. |
| 8 | **At least one result** | Every algorithm must produce some output or result. |

---

## 3. Precision vs Order — Evaluating Algorithm Quality

Two key criteria are used to evaluate how well an algorithm works:

### Precision

**Precision** measures how accurately and reliably an algorithm solves a problem. A precise algorithm always produces the correct result for all valid inputs.

### Order

**Order** measures the total number of steps needed — including repeated steps — to complete the algorithm. A lower order (fewer steps) is generally more efficient.

### Example: Baking a Cake

**Imprecise algorithm:**
```
1. Mix some ingredients together.
2. Bake for a while.
3. Take the cake out when it looks done.
```
This algorithm is **imprecise** — "some ingredients", "a while", and "looks done" are vague and will produce different (possibly wrong) results every time.

**Precise algorithm:**
```
1. Preheat the oven to 180°C.
2. Measure 200 g of flour and sift into a bowl.
3. Add 100 g of sugar, 2 eggs, 100 ml of milk, and 5 ml of baking powder.
4. Mix on medium speed for 3 minutes.
5. Pour batter into a greased 20 cm round tin.
6. Bake at 180°C for 35 minutes.
7. Insert a skewer into the centre — if it comes out clean, the cake is done.
8. Remove from the oven and allow to cool for 10 minutes before serving.
```
Every measurement, time, and condition is exact — this algorithm will produce the same correct result every time.

> [!TIP] Exam Tip
> In an exam, you may be asked to identify what makes an algorithm imprecise. Look for vague words: *"some"*, *"a bit"*, *"a while"*, *"a few"*, *"when ready"*, *"looks right"*, etc. Each vague word loses a mark.

---

## 4. How to Write an Algorithm

When writing an algorithm in the SA IT exam, follow these conventions:

- Number every step starting from 1.
- Write in plain everyday language (not code — unless pseudocode is specifically asked for).
- Use the word **READ** or **INPUT** to accept data from the user.
- Use the word **DISPLAY**, **PRINT**, or **OUTPUT** to show a result.
- Keep each step to a single action.
- Include a **START** and an **END**.

### Example: Convert Temperature from Celsius to Fahrenheit

```
1. START
2. READ celsius
3. CALCULATE fahrenheit = (celsius × 9 / 5) + 32
4. DISPLAY fahrenheit
5. END
```

---

## 5. Flowcharts

A **flowchart** is a visual (diagram) representation of an algorithm. Each step is drawn as a specific shape, and arrows show the direction of flow between steps.

### Flowchart Symbols

| Symbol | Shape | Meaning |
|---|---|---|
| **Oval / Terminator** | Rounded ends | Start or End of the algorithm |
| **Rectangle / Process** | Plain rectangle | A processing step — calculation or assignment |
| **Diamond / Decision** | Diamond (rhombus) | A YES/NO question — creates a branch |
| **Parallelogram** | Slanted rectangle | Input or Output |
| **Arrow** | Line with arrowhead | Direction of flow — connects shapes |

> [!NOTE] Grade 10 — Foundation
> You must be able to draw these shapes and label them correctly. In an exam, marks are awarded for the correct shape, the correct label inside the shape, and the correct arrows between shapes.

### Flowchart Example: Is a Number Even or Odd?

The following describes a flowchart read from top to bottom:

```
[OVAL]              START
       ↓
[PARALLELOGRAM]     INPUT number
       ↓
[DIAMOND]           Is number MOD 2 = 0?
    YES ↓                       ↓ NO
[PARALLELOGRAM]         [PARALLELOGRAM]
DISPLAY "Even"          DISPLAY "Odd"
    ↓                           ↓
    └──────────┬────────────────┘
               ↓
[OVAL]              END
```

In this flowchart:
- The **diamond** tests whether `number MOD 2 = 0` (i.e. whether the remainder when dividing by 2 is zero — meaning the number is even).
- The **YES** branch (left) displays "Even".
- The **NO** branch (right) displays "Odd".
- Both branches rejoin and lead to the **END** oval.

> [!TIP] Exam Tip
> The **MOD** operator gives the remainder after division. `7 MOD 2 = 1` (odd), `8 MOD 2 = 0` (even). This is one of the most common flowchart and pseudocode examples in CAPS papers.

---

## 6. Pseudocode Conventions (SA IT Exams)

**Pseudocode** is a structured, human-readable way of writing algorithm steps. It is closer to actual code, but not tied to any programming language. The SA CAPS IT exam uses specific keywords — you must use these exact forms.

### Input and Output

| Keyword | Meaning | Example |
|---|---|---|
| `READ` or `INPUT` | Accept a value from the user | `READ iAge` |
| `DISPLAY`, `PRINT`, or `OUTPUT` | Show a value to the user | `DISPLAY "Hello"` |

### Selection (Decision) — IF

```
IF condition THEN
    [steps if true]
ELSE
    [steps if false]
ENDIF
```

**Example:**
```
IF iMark >= 50 THEN
    DISPLAY "PASSED"
ELSE
    DISPLAY "FAILED"
ENDIF
```

### Counted Loop — FOR

```
FOR counter := start TO end DO
    [repeated steps]
ENDFOR
```

**Example — display numbers 1 to 5:**
```
FOR iCount := 1 TO 5 DO
    DISPLAY iCount
ENDFOR
```

### Condition-controlled Loop — WHILE

```
WHILE condition DO
    [repeated steps]
ENDWHILE
```

The condition is tested **before** each iteration. If the condition is false from the start, the loop body never runs.

**Example:**
```
WHILE iCount <= 10 DO
    DISPLAY iCount
    iCount := iCount + 1
ENDWHILE
```

### Post-test Loop — REPEAT...UNTIL

```
REPEAT
    [repeated steps]
UNTIL condition
```

The condition is tested **after** each iteration. The loop body always runs **at least once**.

**Example:**
```
REPEAT
    READ iNumber
UNTIL iNumber > 0
```

> [!TIP] Exam Tip
> Know the difference: **WHILE** tests the condition first (may never run); **REPEAT...UNTIL** tests the condition last (always runs at least once). Exam questions often ask you to choose the correct loop type for a given scenario.

---

## 7. Types of Algorithms (CAPS-Prescribed)

### Sequential Algorithm

Steps are executed **one after another, in a fixed order**. No decisions, no loops.

```
1. START
2. READ firstName
3. READ lastName
4. DISPLAY firstName + " " + lastName
5. END
```

### Decision Algorithm

Contains **at least one branching point** — a condition that determines which path to follow. Uses IF...THEN...ELSE or CASE structures.

```
1. START
2. READ iTemperature
3. IF iTemperature > 30 THEN
4.     DISPLAY "Hot day"
5. ELSE
6.     DISPLAY "Cool day"
7. ENDIF
8. END
```

### Repetition Algorithm

Contains **at least one loop** — a set of steps that repeats. Uses FOR, WHILE, or REPEAT...UNTIL.

```
1. START
2. iTotal := 0
3. FOR iCount := 1 TO 5 DO
4.     READ iNumber
5.     iTotal := iTotal + iNumber
6. ENDFOR
7. DISPLAY iTotal
8. END
```

> [!NOTE] Grade 10 — Foundation
> An algorithm can belong to more than one type. A loop that contains an IF statement is both a **repetition** and a **decision** algorithm. When asked to identify the type, name all that apply.

---

## 8. Tracing an Algorithm

**Tracing** means manually working through an algorithm step by step, tracking the value of each variable at each point. A **trace table** is used to record these values.

### Example: Trace the following with input `7`

```
1. START
2. READ iNumber
3. IF iNumber MOD 2 = 0 THEN
4.     DISPLAY "Even"
5. ELSE
6.     DISPLAY "Odd"
7. ENDIF
8. END
```

| Step | Action | `iNumber` | Output |
|---|---|---|---|
| 2 | READ iNumber | 7 | — |
| 3 | 7 MOD 2 = 1 → not 0 → condition is **FALSE** | 7 | — |
| 6 | DISPLAY "Odd" | 7 | Odd |
| 8 | END | — | — |

> [!TIP] Exam Tip
> In a trace table, set up one column per variable, plus an Output column. Fill in values row by row. Only write a new value in a variable's column when that variable actually changes.

---

## Summary

| Concept | Key Point |
|---|---|
| Algorithm | Finite, ordered, unambiguous steps that solve a problem |
| Precision | How accurately the algorithm produces the correct result |
| Order | Total number of steps — measures efficiency |
| Flowchart | Visual representation using standard shapes |
| Pseudocode | Human-readable code-like notation using CAPS keywords |
| Sequential | Steps in order only — no branches, no loops |
| Decision | Contains at least one IF/CASE branch |
| Repetition | Contains at least one loop (FOR, WHILE, REPEAT) |
