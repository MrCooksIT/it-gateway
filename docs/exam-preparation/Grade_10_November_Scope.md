---
title: Grade 10 November Exam Scope
description: What is examined in the Grade 10 IT November final examination — Paper 1 (practical) and Paper 2 (theory), with mark allocations and study links.
---

# Grade 10 November Exam Scope

::: info 📌 Exam overview
| Paper | Type | Time | Marks |
|---|---|---|---|
| Paper 1 | Practical (Delphi) | 3 hours | 120 |
| Paper 2 | Theory (written) | 3 hours | 120 |

**All work from Terms 1 to 4 is examinable.** Use the checklists below: tick each item when you can do it **without looking at notes**.
:::

---

## Paper 1 — Practical (120 marks)

You get one Delphi project per question, with the form already designed. You write the code for each button.

### Question 1: Properties, debugging, formulae and formatting (40)

- [ ] Set component properties **in code**: `Caption`, `Text`, `Color` (with `ParentBackground := False` on panels), `Font.Name`, `Font.Size`, `Font.Color`, `Font.Style := [fsBold, fsItalic]`, `Visible`, `Enabled`
- [ ] Code in the `FormShow` / `FormCreate` event as well as button `OnClick` events
- [ ] **Debugging:** find and correct **syntax, runtime and logic errors** in given code (code may be inside comment braces `{ }`)
- [ ] Declare and use variables and **constants** of type Integer, Real, String, Char and Boolean
- [ ] Convert between types: `StrToInt`, `StrToFloat`, `IntToStr`, `FloatToStr`
- [ ] Translate a mathematical **formula** into Delphi: operator precedence, brackets, `Pi`, `Sqr`, `Sqrt`, `Power`, `Round`, `Trunc`
- [ ] Integer arithmetic with **`div` and `mod`**, e.g. splitting an amount into units
- [ ] **Formatting** output: `FloatToStrF(x, ffFixed, 8, 2)`, `FloatToStrF(x, ffCurrency, 8, 2)`, `FormatFloat`
- [ ] Output to a **label, panel, edit box, memo/rich edit** (`Lines.Add`, `Clear`) and `ShowMessage`
- [ ] Line up output with tabs (`#9`) and use multiple lines (`#13`)

📖 [Components](../practical/delphi/components) · [Variables](../practical/delphi/variables) · [Operators](../practical/delphi/operators) · [Math Methods](../practical/delphi/math-methods) · [Debugging](../practical/delphi/debugging)

### Question 2: Decision making and repetition (40)

- [ ] `if … then … else`, **nested** ifs and `else if` chains
- [ ] Compound conditions with **`and`, `or`, `not`**, with the brackets correct
- [ ] **`case`** statements, including ranges (`50..69:`) and the `else` part
- [ ] Read input from a **radio group** (`ItemIndex`, check for `-1`), **check box** (`Checked`), **spin edit** (`Value`), edit box and combo box
- [ ] Change a **TShape** (`Brush.Color`) or other component based on a decision
- [ ] **`for`** loops (`to` and `downto`) that build output line by line
- [ ] **`while`** loops: repeat while a condition is true; counters and running totals
- [ ] Choose the right loop for the problem

📖 [Selection — IF & CASE](../practical/delphi/selection) · [Loops](../practical/delphi/loops) · [Input Validation](../practical/delphi/validation)

### Question 3: General problem-solving (40)

- [ ] **`repeat … until`** loops, e.g. keep asking with an `InputBox` until a stop value is entered
- [ ] Counters, totals, **highest/lowest** values, averages, all inside loops
- [ ] **String handling from first principles:** loop through a string character by character (`sWord[i]`), `Length`, test characters with sets (`in ['A'..'Z']`, `in ['0'..'9']`)
- [ ] String functions: `Copy`, `Pos`, `Delete`, `Insert`, `UpperCase`, `LowerCase`, `Trim`
- [ ] **Validation** with a Boolean flag and helpful messages
- [ ] Random numbers: `Randomize`, `Random(n)`, `RandomRange(a, b)`, and getting the range right
- [ ] Separate the digits of a number with `div` and `mod`
- [ ] Display results in a rich edit in the **exact format** asked for

📖 [String Functions](../practical/delphi/strings) · [Loops](../practical/delphi/loops) · [Classic Problems](../practical/algorithms/classic-problems)

::: danger 🚨 Not in the Grade 10 exam
Arrays, text files, procedures/functions with parameters, databases, SQL and OOP. These start in Grade 11 and 12.
:::

---

## Paper 2 — Theory (120 marks)

| Section | Content | Marks |
|---|---|---|
| A | Short questions: multiple choice, matching columns, true/false with correction | ±20 |
| B | Systems Technologies | ±20 |
| C | Communication and Network Technologies | ±20 |
| D | Data and Information Management | ±20 |
| E | Solution Development | ±20 |
| F | Integrated scenario (any topic, including social implications) | ±20 |

Sections B–F are each based on a **scenario**. Always relate your answer to the scenario.

### Section B: Systems Technologies
- [ ] The general model of a computer: input, processing, output, storage, communication
- [ ] Types of computers and their uses: desktop, laptop, tablet, smartphone, server
- [ ] Input, output and storage devices; categorise devices and compare a desktop with a mobile device
- [ ] **Primary memory** (RAM, ROM, cache) vs **secondary storage** (HDD, SSD, flash, optical, cloud)
- [ ] CPU basics and clock speed; motherboard, ports and connectors (USB, HDMI)
- [ ] **System software** (operating system, utilities, drivers) vs **application software**
- [ ] Functions of the operating system; utility programs (antivirus, backup, compression, disk clean-up)
- [ ] Software licences: proprietary, open source, freeware, shareware; product keys

📖 [Hardware](../theory/systems/hardware) · [Peripherals](../theory/systems/peripherals) · [Software](../theory/systems/software) · [OS & File Management](../theory/systems/os-management)

### Section C: Communication and Network Technologies
- [ ] What a network is; advantages and disadvantages of networks
- [ ] Network types: **PAN, HAN, LAN/WLAN, WAN**; the Internet as a WAN
- [ ] Basic network components: NIC, switch, router, modem, access point, cables
- [ ] Communication media: UTP, fibre, Wi-Fi, Bluetooth; compare speed, distance and cost
- [ ] **Client-server vs peer-to-peer** networks
- [ ] E-communication and **e-mail best practices** (To / Cc / Bcc, subject lines, attachments, netiquette)
- [ ] Internet vs WWW; browsers vs search engines; **parts of a URL**; ISPs; Internet services

📖 [Network Concepts](../theory/networks/network-concepts) · [Types of Networks](../theory/networks/network-types) · [E-Communication](../theory/networks/e-communication) · [Internet & WWW](../theory/internet/internet-www)

### Section D: Data and Information Management
- [ ] **Data vs information vs knowledge**, with examples from a scenario
- [ ] **Number systems:** convert between binary, decimal and **hexadecimal** (show working)
- [ ] Bits, bytes and storage units (KB, MB, GB, TB); storage calculations
- [ ] Character representation: **ASCII and Unicode**
- [ ] Data types for given data (Integer, Real, String, Char, Boolean)
- [ ] File types and extensions; file paths and folder structures

📖 [Binary](../practical/number-systems/binary) · [Hexadecimal](../practical/number-systems/hexadecimal) · [Data Sizes](../practical/number-systems/data-sizes) · [Data Representation](../theory/systems/data-representation)

### Section E: Solution Development
- [ ] What an algorithm is; **IPO** tables; flowcharts and pseudocode
- [ ] **Trace tables:** trace given pseudocode or Delphi code and state its purpose
- [ ] Read Delphi code: identify **syntax, runtime and logic errors** and correct them
- [ ] Predict the output of given code
- [ ] Control structures: sequence, selection (if, case), repetition (for, while, repeat); compare the loops
- [ ] Basic validation techniques

📖 [Programming Concepts](../theory/programming/programming-concepts) · [Algorithms](../theory/programming/algorithms-theory) · [Debugging](../practical/delphi/debugging)

### Section F: Integrated scenario — social implications
- [ ] **POPIA** basics: collecting and protecting personal information
- [ ] E-mail threats: **phishing**, spam, social engineering, malware; safe Internet use
- [ ] Strong passwords and **two-factor authentication**
- [ ] **Copyright**, piracy, plagiarism, licences, Creative Commons
- [ ] **Ergonomics** and health (RSI, eye strain, posture)
- [ ] **Green computing** and e-waste
- [ ] The **digital divide**; advantages and disadvantages of using computers

📖 [Cybercrime](../theory/social/cybercrime) · [Copyright](../theory/social/copyright) · [Online Safety](../theory/social/online-safety) · [Environment & Society](../theory/social/environment-society) · [Digital Divide](../theory/social/digital-divide)

---

::: tip 🎯 Exam Tips
- **Paper 1:** Read the whole question first. Marks go to every correct step, so a half-working answer still earns marks, but code that doesn't compile can cost you everything in that project. Comment out (`{ }`) anything that breaks compilation.
- **Paper 2:** The mark allocation tells you how many facts to give: **(2) = two separate points**. Use the scenario in your answers. "Explain" and "discuss" need a reason, not just a name.
- Practise with past papers, but remember that each year's paper uses a **new scenario**.
:::

*Also see: [Grade 10 Practical Notes](./Grade_10_IT_Practical_Notes) · [Grade 10 Theory Notes](./Grade_10_IT_Theory_Notes)*
