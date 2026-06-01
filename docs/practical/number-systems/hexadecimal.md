# Hexadecimal Numbers

Binary is efficient for computers but hard for humans to read — `11111111` requires 8 digits to express what hex writes as `FF`. Hexadecimal (base-16) is a compact shorthand for binary used throughout computing: memory addresses, colour codes, MAC addresses, and error codes all use hex.

> [!NOTE] Grade 10+
> Hexadecimal conversions are introduced in Grade 10 and appear in most Paper 1 and Paper 2 papers. The binary↔hex shortcut (groups of 4 bits) is the key skill.

---

## What is Hexadecimal?

**Hexadecimal** is a **base-16** number system using 16 symbols:

| Decimal | Hex | Binary |
|---|---|---|
| 0 | 0 | 0000 |
| 1 | 1 | 0001 |
| 2 | 2 | 0010 |
| 3 | 3 | 0011 |
| 4 | 4 | 0100 |
| 5 | 5 | 0101 |
| 6 | 6 | 0110 |
| 7 | 7 | 0111 |
| 8 | 8 | 1000 |
| 9 | 9 | 1001 |
| 10 | **A** | 1010 |
| 11 | **B** | 1011 |
| 12 | **C** | 1100 |
| 13 | **D** | 1101 |
| 14 | **E** | 1110 |
| 15 | **F** | 1111 |

> A = 10, B = 11, C = 12, D = 13, E = 14, F = 15

**One hex digit = exactly 4 binary bits (nibble)**  
This is the key relationship that makes hex ↔ binary so fast.

---

## Hex → Decimal Conversion

**Method:** Multiply each hex digit by its place value (power of 16), then add.

Place values (right to left): 16⁰ = 1, 16¹ = 16, 16² = 256, 16³ = 4096

### Worked Example: `2B₁₆` → Decimal

| Digit | B | 2 |
|---|---|---|
| Place value | 16¹ = 16 | 16⁰ = 1 |
| Value | B = 11 | 2 |
| × place | 11 × 16 = 176 | 2 × 1 = 2 |

Total = 176 + 2 = **178**

So `2B₁₆ = 178₁₀`

### Worked Example: `3F4₁₆` → Decimal

| Digit | 3 | F | 4 |
|---|---|---|---|
| Place value | 16² = 256 | 16¹ = 16 | 16⁰ = 1 |
| Value | 3 | 15 | 4 |
| × place | 3 × 256 = 768 | 15 × 16 = 240 | 4 × 1 = 4 |

Total = 768 + 240 + 4 = **1012**

---

## Decimal → Hex Conversion

**Method:** Repeated division by 16 — record remainders (convert remainders > 9 to A–F).

### Worked Example: `255₁₀` → Hex

| Step | Calculation | Quotient | Remainder |
|---|---|---|---|
| 1 | 255 ÷ 16 | 15 | **15 = F** |
| 2 | 15 ÷ 16 | 0 | **15 = F** |

Read remainders **bottom to top**: **FF**

So `255₁₀ = FF₁₆`

### Worked Example: `1012₁₀` → Hex

| Step | Calculation | Quotient | Remainder |
|---|---|---|---|
| 1 | 1012 ÷ 16 | 63 | **4** |
| 2 | 63 ÷ 16 | 3 | **15 = F** |
| 3 | 3 ÷ 16 | 0 | **3** |

Read remainders bottom to top: **3F4**

So `1012₁₀ = 3F4₁₆` ✓

---

## Binary ↔ Hex Shortcut (The Key Skill)

**Every hex digit = exactly 4 binary bits.** This makes conversion between them trivial.

### Binary → Hex

1. Group binary digits into groups of **4 from the right** (pad with leading zeros if needed)
2. Convert each group of 4 to its hex digit

### Worked Example: `10111101₂` → Hex

Split into groups of 4 bits, convert each group:

<div class="itg-nibble-row">
  <div class="itg-nibble itg-nibble-grp1">
    <div class="itg-nibble-bits">
      <div class="itg-nibble-bit">1</div><div class="itg-nibble-bit">0</div>
      <div class="itg-nibble-bit">1</div><div class="itg-nibble-bit">1</div>
    </div>
    <div class="itg-nibble-result">B</div>
  </div>
  <div class="itg-nibble-sep">→</div>
  <div class="itg-nibble itg-nibble-grp2">
    <div class="itg-nibble-bits">
      <div class="itg-nibble-bit">1</div><div class="itg-nibble-bit">1</div>
      <div class="itg-nibble-bit">0</div><div class="itg-nibble-bit">1</div>
    </div>
    <div class="itg-nibble-result">D</div>
  </div>
</div>

So `10111101₂ = BD₁₆`

### Worked Example: `1101001011₂` → Hex

Pad to a multiple of 4 bits (add leading zeros), then split:

<div class="itg-nibble-row">
  <div class="itg-nibble itg-nibble-grp1">
    <div class="itg-nibble-bits">
      <div class="itg-nibble-bit">0</div><div class="itg-nibble-bit">0</div>
      <div class="itg-nibble-bit">1</div><div class="itg-nibble-bit">1</div>
    </div>
    <div class="itg-nibble-result">3</div>
  </div>
  <div class="itg-nibble itg-nibble-grp2">
    <div class="itg-nibble-bits">
      <div class="itg-nibble-bit">0</div><div class="itg-nibble-bit">1</div>
      <div class="itg-nibble-bit">0</div><div class="itg-nibble-bit">0</div>
    </div>
    <div class="itg-nibble-result">4</div>
  </div>
  <div class="itg-nibble itg-nibble-grp3">
    <div class="itg-nibble-bits">
      <div class="itg-nibble-bit">1</div><div class="itg-nibble-bit">0</div>
      <div class="itg-nibble-bit">1</div><div class="itg-nibble-bit">1</div>
    </div>
    <div class="itg-nibble-result">B</div>
  </div>
</div>

So `1101001011₂ = 34B₁₆`

---

### Hex → Binary

Replace each hex digit with its **4-bit binary equivalent**:

### Worked Example: `A7₁₆` → Binary

```
A      7
1010  0111
```

Result: `10100111₂`

### Worked Example: `F3C₁₆` → Binary

```
F      3      C
1111  0011  1100
```

Result: `111100111100₂`

---

## Hex in Real Computing

| Where hex is used | Example |
|---|---|
| Memory addresses | `0x00FF1234` |
| RGB colours (web) | `#FF5733` (red=FF, green=57, blue=33) |
| MAC addresses | `00:1A:2B:3C:4D:5E` |
| Error codes | `0x0000004E` (Windows BSOD) |
| ASCII in hex | `41` = 'A', `20` = space |

### Colour Code Example
`#FF5733` breaks into:
- `FF` = 255 (max red)
- `57` = 87 (medium green)
- `33` = 51 (low blue)

→ A warm orange-red colour.

---

## Summary: All Three Systems

| Decimal | Binary | Hex |
|---|---|---|
| 0 | 0000 | 0 |
| 5 | 0101 | 5 |
| 10 | 1010 | A |
| 15 | 1111 | F |
| 16 | 00010000 | 10 |
| 32 | 00100000 | 20 |
| 255 | 11111111 | FF |
| 256 | 100000000 | 100 |

---

## Practice Exercises

**Exercise 1 — Hex to decimal**

Convert:
a) `1F₁₆`  
b) `C8₁₆`  
c) `2A3₁₆`

<details>
<summary>Show solution</summary>

a) `1F`:  
(1 × 16) + (15 × 1) = 16 + 15 = **31**

b) `C8`:  
(12 × 16) + (8 × 1) = 192 + 8 = **200**

c) `2A3`:  
(2 × 256) + (10 × 16) + (3 × 1) = 512 + 160 + 3 = **675**
</details>

---

**Exercise 2 — Decimal to hex**

Convert:
a) `47₁₀`  
b) `175₁₀`  
c) `1000₁₀`

<details>
<summary>Show solution</summary>

a) 47:  
47 ÷ 16 = 2 rem **15 (F)**  
2 ÷ 16 = 0 rem **2**  
Bottom to top: **2F** → verify: 2×16 + 15 = 47 ✓

b) 175:  
175 ÷ 16 = 10 rem **15 (F)**  
10 ÷ 16 = 0 rem **10 (A)**  
Bottom to top: **AF** → verify: 10×16 + 15 = 175 ✓

c) 1000:  
1000 ÷ 16 = 62 rem **8**  
62 ÷ 16 = 3 rem **14 (E)**  
3 ÷ 16 = 0 rem **3**  
Bottom to top: **3E8** → verify: 3×256 + 14×16 + 8 = 768 + 224 + 8 = 1000 ✓
</details>

---

**Exercise 3 — Binary ↔ Hex**

a) Convert `11010110₂` to hex  
b) Convert `B4₁₆` to binary

<details>
<summary>Show solution</summary>

a) `11010110`:  
Group: `1101 0110` → D = 1101, 6 = 0110 → **D6₁₆**

b) `B4`:  
B = `1011`, 4 = `0100` → **10110100₂**

Verify: 10110100 = 128 + 32 + 16 + 4 = 180 = 11×16 + 4 = **B4₁₆** ✓
</details>

---

> [!TIP] Exam Tip
> Hex ↔ binary conversion is almost instant once you memorise the 16-entry table (0–F). The binary→hex grouping trick means you never need to go binary→decimal→hex; just group into nibbles and convert directly. When an exam gives you a hex colour code or memory address and asks for binary — this shortcut saves 90 seconds.
