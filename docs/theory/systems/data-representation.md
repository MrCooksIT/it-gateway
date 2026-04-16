# Data Representation

Inside a computer, everything is stored as binary — sequences of 0s and 1s. Letters, images, sounds, and instructions are all represented this way. Understanding how data is encoded into binary is fundamental to understanding how computers work.

> [!NOTE] Grade 10+
> Binary and ASCII are introduced in Grade 10. Hexadecimal and Unicode extend into Grade 11. Number conversions are examined in both Paper 1 and Paper 2.

---

## Why Binary?

Computers are built from transistors — electronic switches that are either ON (1) or OFF (0). Binary (base-2) maps perfectly to this: 1 = ON, 0 = OFF.

Every piece of data in a computer — text, images, audio, video, program instructions — is ultimately stored as a sequence of 0s and 1s.

---

## Number Systems Overview

| System | Base | Digits | Used for |
|---|---|---|---|
| **Decimal** | 10 | 0–9 | Human everyday counting |
| **Binary** | 2 | 0, 1 | Computer storage and processing |
| **Hexadecimal** | 16 | 0–9, A–F | Compact representation of binary; memory addresses, colours |

---

## Binary (Base-2)

Each position represents a power of 2:

```
Position:  8    7    6    5    4    3    2    1
Power:    2⁷  2⁶  2⁵  2⁴  2³  2²  2¹  2⁰
Value:    128   64   32   16    8    4    2    1
```

**Key powers of 2 to memorise:**

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
| 2¹⁰ | 1 024 |

### Binary → Decimal

Multiply each bit by its place value and add:

`10110101` = 128 + 32 + 16 + 4 + 1 = **181**

### Decimal → Binary

Divide by 2 repeatedly; read remainders bottom to top:

45 ÷ 2 = 22 r **1**  
22 ÷ 2 = 11 r **0**  
11 ÷ 2 = 5 r **1**  
5 ÷ 2 = 2 r **1**  
2 ÷ 2 = 1 r **0**  
1 ÷ 2 = 0 r **1**

Read bottom to top: **101101**

Verify: 32 + 8 + 4 + 1 = 45 ✓

---

## Hexadecimal (Base-16)

16 digits: 0–9 and A (10), B (11), C (12), D (13), E (14), F (15)

Each hex digit = exactly **4 binary bits** (one nibble).

**Hex → Binary shortcut:**

```
A      F      3
1010  1111  0011
```

So `AF3₁₆ = 101011110011₂`

**Binary → Hex shortcut:**

Group bits into 4 from the right, convert each group:

```
1101  0110
  D     6
```

So `11010110₂ = D6₁₆`

### Hex → Decimal

Multiply each digit by its place value (power of 16):

`2B₁₆` = (2 × 16) + (11 × 1) = 32 + 11 = **43**

`FF₁₆` = (15 × 16) + (15 × 1) = 240 + 15 = **255**

### Decimal → Hex

Divide by 16 repeatedly:

255 ÷ 16 = 15 r **15 (F)**  
15 ÷ 16 = 0 r **15 (F)**

Bottom to top: **FF**

---

## ASCII — Encoding Text

**ASCII** (American Standard Code for Information Interchange) assigns a number to each character. The computer stores that number in binary.

**Key ASCII values:**

| Decimal | Hex | Character |
|---|---|---|
| 32 | 20 | Space |
| 48 | 30 | '0' |
| 57 | 39 | '9' |
| 65 | 41 | 'A' |
| 90 | 5A | 'Z' |
| 97 | 61 | 'a' |
| 122 | 7A | 'z' |

**Important patterns:**
- `'A'` = 65, `'Z'` = 90 (uppercase)
- `'a'` = 97, `'z'` = 122 (lowercase)
- Difference between uppercase and lowercase = 32
- `'0'` = 48, `'9'` = 57 (digit characters)

**Standard ASCII:** 7 bits → 128 characters (0–127)  
**Extended ASCII:** 8 bits → 256 characters (0–255) — adds special characters

**Example — storing 'Hi' in ASCII:**
- 'H' = 72 = `01001000`
- 'i' = 105 = `01101001`

So 'Hi' = `01001000 01101001` (2 bytes)

---

## Unicode

ASCII only covers English and basic symbols — it cannot represent Chinese, Arabic, Hindi, emoji, or thousands of other characters.

**Unicode** is a universal standard that assigns a unique code point to every character in every writing system.

| Encoding | Bits per character | Characters possible | Notes |
|---|---|---|---|
| ASCII | 7 bits | 128 | English only |
| Extended ASCII | 8 bits | 256 | Some European chars |
| Unicode (UTF-8) | 1–4 bytes | 1 112 064 | Backwards compatible with ASCII |
| Unicode (UTF-16) | 2–4 bytes | 1 112 064 | Used in Windows internally |
| Unicode (UTF-32) | 4 bytes fixed | 1 112 064 | Fixed width, easier processing |

**Why Unicode matters:**
- Globalisation — websites need to display any language
- Emoji are Unicode characters (`😀` = U+1F600)
- Modern systems use UTF-8 by default

---

## Encoding Images

Images are stored as pixels. Each pixel's colour is stored as a binary number.

**Key terms:**
- **Resolution** — width × height in pixels (e.g. 1920 × 1080)
- **Colour depth** — how many bits per pixel

| Colour depth | Colours possible | Storage per pixel |
|---|---|---|
| 1-bit | 2 (B&W) | 1 bit |
| 4-bit | 16 | 0.5 byte |
| 8-bit | 256 | 1 byte |
| 16-bit | 65 536 | 2 bytes |
| **24-bit** | **16 777 216** | **3 bytes** |
| 32-bit | 16 777 216 + transparency | 4 bytes |

**True colour = 24-bit** — 8 bits each for Red, Green, Blue (RGB).

**Storage calculation:**

Uncompressed image size = width × height × colour_depth_bits ÷ 8 (bytes)

Example: 1920 × 1080, 24-bit  
= 1 920 × 1 080 × 24 ÷ 8 = 6 220 800 bytes ≈ 5.93 MB

---

## Encoding Audio

Audio is captured by **sampling** the analogue sound wave at regular intervals.

| Parameter | Meaning | CD quality |
|---|---|---|
| **Sample rate** | Samples per second (Hz) | 44 100 Hz |
| **Bit depth** | Bits per sample | 16 bits |
| **Channels** | Mono (1) or stereo (2) | 2 (stereo) |

**Storage = sample_rate × bit_depth × channels × seconds ÷ 8**

---

## Data Compression

Raw data is often much larger than necessary. Compression reduces file size.

| Type | Method | Quality change | Examples |
|---|---|---|---|
| **Lossless** | Removes redundant data; fully recoverable | None — exact original | ZIP, PNG, FLAC |
| **Lossy** | Permanently removes detail human senses won't notice | Reduced (but usually acceptable) | JPEG, MP3, MP4 |

**Why lossless for some files:**
- Text/programs: even one changed bit breaks the file — must be lossless
- Medical images: can't lose any detail — lossless required

**Why lossy is acceptable for media:**
- Human eyes/ears don't detect small quality reductions
- File size reduction can be 10× to 100×

---

## Data Representation Summary Table

| Data Type | Encoding Standard | Key Unit |
|---|---|---|
| Text (English) | ASCII | 1 byte per character |
| Text (international) | Unicode (UTF-8) | 1–4 bytes per character |
| Integers | Binary (two's complement for negatives) | 4 bytes (32-bit integer) |
| Images | RGB / colour depth | Bits per pixel |
| Audio | PCM sampling | Sample rate × bit depth × channels |
| Video | Frames × image encoding | Frame rate × frame size |
| Colour codes | Hexadecimal RGB | `#RRGGBB` |

---

## Key Terms

| Term | Definition |
|---|---|
| **Bit** | Single binary digit (0 or 1) |
| **Byte** | 8 bits — basic unit of storage |
| **ASCII** | Standard 7-bit encoding for English characters |
| **Unicode** | Universal encoding standard for all world characters |
| **UTF-8** | Variable-width Unicode encoding; most common on the web |
| **Colour depth** | Number of bits used to represent one pixel's colour |
| **Resolution** | Number of pixels in an image (width × height) |
| **Sample rate** | Number of audio samples taken per second (Hz) |
| **Lossless compression** | Reduces size without losing any data |
| **Lossy compression** | Reduces size by permanently removing some data |
| **Pixel** | Smallest element of a digital image |
| **Hexadecimal** | Base-16 number system — compact binary representation |

---

## Exam Focus

> [!IMPORTANT] High-Frequency Questions
>
> 1. **Convert decimal ↔ binary / hex** — show all working; verify by converting back
>
> 2. **"Give the ASCII value of [character]"** — memorise A=65, a=97, 0=48; calculate others by offset
>
> 3. **"Calculate the uncompressed file size of an image"** — width × height × colour depth ÷ 8 for bytes
>
> 4. **"Explain the difference between lossless and lossy compression. Give an example of each."** — lossless = no quality loss (ZIP/PNG), lossy = some quality lost (JPEG/MP3)
>
> 5. **"Why do we need Unicode when we have ASCII?"** — ASCII only covers 128 characters (English); Unicode supports all world languages + emoji + special characters
