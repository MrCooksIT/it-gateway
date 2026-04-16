# Binary Numbers

Computers store and process everything — text, images, sound, programs — as binary: sequences of 0s and 1s. Understanding binary is essential for number conversion questions in both Paper 1 and Paper 2.

> [!NOTE] Grade 10+
> Binary is introduced in Grade 10. Conversions between binary, decimal, and hexadecimal are examined every year.

---

## What is Binary?

**Binary** is a **base-2** number system. It uses only two digits: **0** and **1** (called **bits**).

Compare with our everyday decimal (base-10) system, which uses 10 digits (0–9).

| System | Base | Digits Used | Example |
|---|---|---|---|
| Decimal | 10 | 0 1 2 3 4 5 6 7 8 9 | 347 |
| Binary | 2 | 0 1 | 101011011 |
| Hexadecimal | 16 | 0–9 and A–F | 15B |

Each position in a binary number represents a **power of 2**:

```
Position:  8    7    6    5    4    3    2    1
Value:    2⁷  2⁶  2⁵  2⁴  2³  2²  2¹  2⁰
        = 128   64   32   16    8    4    2    1
```

---

## Binary → Decimal Conversion

**Method:** Multiply each bit by its place value, then add them up.

### Worked Example: Convert `10110101` to decimal

| Bit | 1 | 0 | 1 | 1 | 0 | 1 | 0 | 1 |
|---|---|---|---|---|---|---|---|---|
| Place value | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| × Bit | 128 | 0 | 32 | 16 | 0 | 4 | 0 | 1 |

Sum = 128 + 32 + 16 + 4 + 1 = **181**

So `10110101₂ = 181₁₀`

### Step-by-Step Method

1. Write the binary number with its place values above
2. Keep only the place values where the bit is **1**
3. Add those values

### Quick Practice

| Binary | Working | Decimal |
|---|---|---|
| `0101` | 4 + 1 | 5 |
| `1010` | 8 + 2 | 10 |
| `1111` | 8 + 4 + 2 + 1 | 15 |
| `10000000` | 128 | 128 |
| `11001100` | 128 + 64 + 8 + 4 | 204 |

---

## Decimal → Binary Conversion

**Method: Repeated Division by 2** (divide and record remainders)

### Worked Example: Convert `45` to binary

| Step | Calculation | Quotient | Remainder |
|---|---|---|---|
| 1 | 45 ÷ 2 | 22 | **1** |
| 2 | 22 ÷ 2 | 11 | **0** |
| 3 | 11 ÷ 2 | 5 | **1** |
| 4 | 5 ÷ 2 | 2 | **1** |
| 5 | 2 ÷ 2 | 1 | **0** |
| 6 | 1 ÷ 2 | 0 | **1** |

Read remainders **bottom to top**: **101101**

So `45₁₀ = 101101₂`

**Verify:** 32 + 8 + 4 + 1 = 45 ✓

### Alternative Method: Subtraction (Place Values)

1. Find the largest power of 2 that fits into the number
2. Write a 1, subtract that value
3. Repeat with the remainder

**Example: Convert `93`**

```
93 - 64 = 29  → bit 6 = 1
29 - 16 = 13  → bit 4 = 1
13 - 8  =  5  → bit 3 = 1
 5 - 4  =  1  → bit 2 = 1
 1 - 1  =  0  → bit 0 = 1

Result: 1011101
```

Check: 64 + 16 + 8 + 4 + 1 = 93 ✓

---

## Binary Arithmetic

### Binary Addition Rules

| A | B | Carry In | Sum | Carry Out |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 0 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 | **1** |
| 1 | 1 | 1 | 1 | **1** |

**Key rule: 1 + 1 = 10 (write 0, carry 1)**

### Worked Example: 1011 + 0110

```
  1 0 1 1
+ 0 1 1 0
---------
  Bit 1 (rightmost): 1 + 0 = 1           → write 1, carry 0
  Bit 2: 1 + 1 = 10                       → write 0, carry 1
  Bit 3: 0 + 1 + 1(carry) = 10            → write 0, carry 1
  Bit 4: 1 + 0 + 1(carry) = 10            → write 0, carry 1
  Bit 5 (new): carry = 1                  → write 1

Result: 10001
```

Check: 11 + 6 = 17 = `10001₂` ✓

---

## Important Powers of 2

Memorise these:

| Power | Value |
|---|---|
| 2⁰ | 1 |
| 2¹ | 2 |
| 2² | 4 |
| 2³ | 8 |
| 2⁴ | 16 |
| 2⁵ | 32 |
| 2⁶ | 64 |
| 2⁷ | 128 |
| 2⁸ | 256 |
| 2⁹ | 512 |
| 2¹⁰ | 1 024 |

---

## Bits, Bytes, and Storage Units

| Unit | Size | Notes |
|---|---|---|
| **Bit** | 1 binary digit (0 or 1) | Smallest unit |
| **Nibble** | 4 bits | Half a byte |
| **Byte** | 8 bits | Stores one character (ASCII) |
| **Kilobyte (KB)** | 1 024 bytes | 2¹⁰ |
| **Megabyte (MB)** | 1 024 KB = 1 048 576 bytes | 2²⁰ |
| **Gigabyte (GB)** | 1 024 MB | 2³⁰ |
| **Terabyte (TB)** | 1 024 GB | 2⁴⁰ |

> [!NOTE] 1 KB = 1 024, not 1 000
> In computing, kilobyte = 2¹⁰ = 1 024 bytes, NOT 1 000 bytes. Storage manufacturers sometimes use 1 000 (which is why your 500 GB drive shows as 465 GB in Windows).

### Storage Calculation Example

How many bytes needed to store a plain text file with 5 000 characters?

```
5 000 characters × 1 byte/character (ASCII) = 5 000 bytes = 4.88 KB
```

How many bits?

```
5 000 bytes × 8 bits/byte = 40 000 bits
```

---

## Binary and Computers

- A transistor in a CPU can be ON (1) or OFF (0) → one bit
- A byte (8 bits) can represent 256 different values (0–255)
- ASCII uses 7 bits → 128 characters; Extended ASCII uses 8 bits → 256 characters
- Unicode (UTF-8/16/32) uses multiple bytes per character for international character sets
- An image's colour depth: 8-bit = 256 colours, 24-bit = 16.7 million colours

---

## Practice Exercises

**Exercise 1 — Convert to decimal**

Convert each binary number to decimal. Show your working.

a) `1101`  
b) `10101010`  
c) `11111111`

<details>
<summary>Show solution</summary>

a) `1101`:  
8 + 4 + 0 + 1 = **13**

b) `10101010`:  
128 + 0 + 32 + 0 + 8 + 0 + 2 + 0 = **170**

c) `11111111`:  
128 + 64 + 32 + 16 + 8 + 4 + 2 + 1 = **255**
(This is the maximum value for 1 byte — 2⁸ − 1)
</details>

---

**Exercise 2 — Convert to binary**

Convert each decimal to binary using repeated division.

a) `23`  
b) `100`  
c) `200`

<details>
<summary>Show solution</summary>

a) 23 → `10111` (16 + 4 + 2 + 1 = 23 ✓)

b) 100 → `1100100` (64 + 32 + 4 = 100 ✓)

c) 200 → `11001000` (128 + 64 + 8 = 200 ✓)
</details>

---

**Exercise 3 — Binary addition**

Add: `10110111 + 01001101`

<details>
<summary>Show solution</summary>

```
  1 0 1 1 0 1 1 1   (= 183)
+ 0 1 0 0 1 1 0 1   (= 77)
-----------
  1 0 0 0 0 1 0 0   (= 260)
```

Check: 183 + 77 = 260 = `100000100₂` ✓
</details>

---

> [!TIP] Exam Tip
> The two most common binary exam questions are: (1) convert decimal to binary, and (2) convert binary to decimal. For decimal → binary, practise the repeated-division method until it's automatic. For binary → decimal, write the place values (128, 64, 32, 16, 8, 4, 2, 1) above each bit and add the ones where the bit is 1. Always verify your answer by converting back.
