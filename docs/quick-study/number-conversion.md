# Number Conversion — Quick Reference

Fast-scan guide for binary, decimal, and hexadecimal conversions. Steps only — no prose.

---

## Decimal → Binary

**Repeated division by 2. Read remainders bottom to top.**

```
45 ÷ 2 = 22 r 1
22 ÷ 2 = 11 r 0
11 ÷ 2 =  5 r 1
 5 ÷ 2 =  2 r 1
 2 ÷ 2 =  1 r 0
 1 ÷ 2 =  0 r 1  ← start reading here

Result: 101101  (read bottom to top)
Verify: 32+8+4+1 = 45 ✓
```

---

## Binary → Decimal

**Write place values above. Add where bit = 1.**

```
Place: 128  64  32  16   8   4   2   1
Bits:    1   0   1   1   0   1   0   1

128 + 32 + 16 + 4 + 1 = 181
```

---

## Decimal → Hex

**Repeated division by 16. Convert remainders > 9 to A–F. Read bottom to top.**

```
255 ÷ 16 = 15 r 15 (F)
 15 ÷ 16 =  0 r 15 (F)  ← start reading here

Result: FF
Verify: 15×16 + 15 = 255 ✓
```

---

## Hex → Decimal

**Multiply each digit by its place value (power of 16). Add.**

```
2B16:
B = 11 →  11 × 16 = 176
2      →   2 ×  1 =   2
               Total = 178
```

Place values: 16⁰=1, 16¹=16, 16²=256, 16³=4096

---

## Binary ↔ Hex Shortcut

**1 hex digit = exactly 4 binary bits**

### Binary → Hex

Group 4 bits from right. Convert each group.

```
1101 0110
  D    6   →  D6
```

### Hex → Binary

Replace each hex digit with 4 bits.

```
A      F
1010  1111  →  10101111
```

---

## Hex Digit Reference Table

| Dec | Hex | Binary |
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
| 10 | A | 1010 |
| 11 | B | 1011 |
| 12 | C | 1100 |
| 13 | D | 1101 |
| 14 | E | 1110 |
| 15 | F | 1111 |

---

## Powers of 2 (Memorise)

| 2⁰ | 2¹ | 2² | 2³ | 2⁴ | 2⁵ | 2⁶ | 2⁷ | 2⁸ | 2¹⁰ |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 2 | 4 | 8 | 16 | 32 | 64 | 128 | 256 | 1024 |

---

## Data Sizes (Storage)

```
8 bits     = 1 byte
1 024 bytes = 1 KB
1 024 KB   = 1 MB
1 024 MB   = 1 GB
1 024 GB   = 1 TB
```

---

## Storage Calculation Templates

**Text (ASCII — 1 char = 1 byte):**
```
characters × 1 byte = bytes → ÷ 1024 for KB
```

**Image (uncompressed):**
```
width × height (pixels) × colour_depth_bits ÷ 8 = bytes → ÷ 1024 → KB → MB
```

**Audio (uncompressed):**
```
sample_rate × bit_depth × channels × seconds ÷ 8 = bytes
```

---

## Worked Conversion Examples

| Convert | Working | Result |
|---|---|---|
| 75₁₀ → binary | 75÷2=37r**1**, 37÷2=18r**1**, 18÷2=9r**0**, 9÷2=4r**1**, 4÷2=2r**0**, 2÷2=1r**0**, 1÷2=0r**1** | **1001011** |
| 10011010₂ → decimal | 128+16+8+2 | **154** |
| 154₁₀ → hex | 154÷16=9r**10(A)**, 9÷16=0r**9** | **9A** |
| 9A₁₆ → decimal | 9×16 + 10×1 = 144+10 | **154** |
| 10011010₂ → hex | group: 1001 1010 = **9 A** | **9A** |
| B3₁₆ → binary | B=1011, 3=0011 | **10110011** |

---

## Common ASCII Values

| Char | Dec | Hex |
|---|---|---|
| '0' | 48 | 30 |
| '9' | 57 | 39 |
| 'A' | 65 | 41 |
| 'Z' | 90 | 5A |
| 'a' | 97 | 61 |
| 'z' | 122 | 7A |
| ' ' | 32 | 20 |

Key fact: lowercase = uppercase + 32
