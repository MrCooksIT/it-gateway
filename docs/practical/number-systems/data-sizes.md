# Data Sizes & Storage Calculations

Understanding data sizes lets you answer questions like: "How much storage does this image need?" or "How long will this file take to download?" These calculations appear in both Paper 1 and Paper 2.

> [!NOTE] Grade 10+
> Data sizes and storage calculations are introduced in Grade 10. The calculation method is the same every time — practise it until it is automatic.

---

## The Units

| Unit | Abbreviation | Size | Power of 2 |
|---|---|---|---|
| Bit | b | 1 binary digit (0 or 1) | — |
| Nibble | — | 4 bits | 2² |
| Byte | B | 8 bits | 2³ |
| Kilobyte | KB | 1 024 bytes | 2¹⁰ |
| Megabyte | MB | 1 024 KB | 2²⁰ |
| Gigabyte | GB | 1 024 MB | 2³⁰ |
| Terabyte | TB | 1 024 GB | 2⁴⁰ |
| Petabyte | PB | 1 024 TB | 2⁵⁰ |

> [!WARNING] 1 KB = 1 024, NOT 1 000
> In computing, prefixes are powers of 2. Manufacturers sometimes use 1 000 (metric), which is why a "500 GB" hard drive shows as ~465 GB in Windows. In IT exams, always use 1 024.

### Quick Scale

```
8 bits = 1 byte
1 024 bytes = 1 KB
1 024 KB    = 1 MB
1 024 MB    = 1 GB
1 024 GB    = 1 TB
```

---

## Converting Between Units

### Larger → Smaller (multiply)

```
GB → MB: × 1 024
MB → KB: × 1 024
KB → B:  × 1 024
B  → bits: × 8
```

**Example:** Convert 2.5 MB to bytes:  
2.5 × 1 024 = 2 560 KB  
2 560 × 1 024 = 2 621 440 bytes

### Smaller → Larger (divide)

```
bytes → KB: ÷ 1 024
KB → MB: ÷ 1 024
MB → GB: ÷ 1 024
bits → bytes: ÷ 8
```

**Example:** Convert 5 120 bytes to KB:  
5 120 ÷ 1 024 = **5 KB**

---

## Storage Calculation Method

The general method for finding how much storage a file needs:

```
1. Find the number of items (characters, pixels, samples, etc.)
2. Find how many bits each item needs
3. Multiply: total bits = items × bits per item
4. Convert to bytes: total bits ÷ 8
5. Convert to KB/MB as required: ÷ 1 024 per step
```

---

## Text Files

**Rule:** In ASCII, 1 character = 1 byte (8 bits).

### Example 1 — Plain text file
A text file contains 8 000 characters. How much storage (in KB)?

```
8 000 characters × 1 byte = 8 000 bytes
8 000 ÷ 1 024 = 7.81 KB ≈ 7.8 KB
```

### Example 2 — Word document
A book has 350 pages. Each page has 40 lines, each line has 70 characters. Storage needed (in MB)?

```
350 × 40 × 70 = 980 000 characters
980 000 × 1 byte = 980 000 bytes
980 000 ÷ 1 024 = 957.03 KB
957.03 ÷ 1 024 = 0.935 MB ≈ 0.9 MB
```

---

## Images (Uncompressed/Bitmap)

**Key variables:**
- **Resolution** = width × height (in pixels)
- **Colour depth** = bits per pixel

**Formula:**
```
Storage = width × height × colour_depth_bits ÷ 8 (for bytes)
```

### Colour Depth Reference

| Colour depth | Colours possible | Storage per pixel |
|---|---|---|
| 1-bit | 2 (black & white) | 1 bit |
| 4-bit | 16 | 4 bits = 0.5 byte |
| 8-bit | 256 | 1 byte |
| 16-bit | 65 536 | 2 bytes |
| 24-bit | 16 777 216 (True colour) | 3 bytes |
| 32-bit | 16 777 216 + transparency | 4 bytes |

### Example — Bitmap Image
A 24-bit colour photograph is 1920 × 1080 pixels. What is the file size in MB?

```
Pixels = 1 920 × 1 080 = 2 073 600
Bits = 2 073 600 × 24 = 49 766 400 bits
Bytes = 49 766 400 ÷ 8 = 6 220 800 bytes
KB = 6 220 800 ÷ 1 024 = 6 075 KB
MB = 6 075 ÷ 1 024 = 5.93 MB ≈ 5.9 MB
```

> [!NOTE] Compression Reduces This
> A JPEG of the same photograph might be 500 KB after compression. The uncompressed calculation gives the raw/bitmap size — the question will specify whether to calculate uncompressed or account for compression.

---

## Audio Files (Uncompressed)

**Key variables:**
- **Sample rate** = samples per second (Hz or kHz): CD quality = 44 100 Hz
- **Bit depth** = bits per sample: CD quality = 16 bits
- **Channels**: mono = 1, stereo = 2
- **Duration**: in seconds

**Formula:**
```
Storage = sample_rate × bit_depth × channels × duration_seconds ÷ 8
```

### Example — Audio Recording
A 3-minute stereo recording at 44 100 Hz, 16-bit. Size in MB?

```
Duration = 3 × 60 = 180 seconds
Bits = 44 100 × 16 × 2 × 180 = 254 016 000 bits
Bytes = 254 016 000 ÷ 8 = 31 752 000 bytes
KB = 31 752 000 ÷ 1 024 = 31 007.8 KB
MB = 31 007.8 ÷ 1 024 = 30.3 MB
```

---

## Video Files (Uncompressed)

**Formula:**
```
Storage = frame_rate × duration × frame_size
frame_size = width × height × colour_depth_bits ÷ 8
```

### Example — Short Video Clip
A 30-second video at 30 fps, 1280 × 720 resolution, 24-bit colour. Size in MB?

```
Frame size = 1280 × 720 × 24 ÷ 8 = 2 764 800 bytes
Total frames = 30 × 30 = 900 frames
Total = 2 764 800 × 900 = 2 488 320 000 bytes
MB = 2 488 320 000 ÷ 1 024 ÷ 1 024 = 2 373 MB ≈ 2.3 GB
```

This is why video compression (MP4, HEVC) is essential.

---

## Data Transmission

**Bandwidth** is typically measured in **bits per second** (bps, Kbps, Mbps, Gbps).  
Note: bandwidth uses lowercase 'b' for bits; storage uses uppercase 'B' for bytes.

**Formula:**
```
Transfer time = file_size_in_bits ÷ bandwidth_in_bps
```

### Example — Download Time
How long to download a 50 MB file on a 10 Mbps connection?

```
File size in bits = 50 × 1 024 × 1 024 × 8 = 419 430 400 bits
Bandwidth = 10 × 1 000 000 = 10 000 000 bps  (note: Mbps uses 1 000 000)
Time = 419 430 400 ÷ 10 000 000 = 41.9 seconds
```

> [!NOTE] Mbps Uses 1 000 000, not 1 048 576
> Network speeds use SI prefixes (1 Mbps = 1 000 000 bps), not binary prefixes. Storage uses binary (1 MB = 1 048 576 bytes). This is a deliberate difference — don't mix them up.

---

## Quick Reference — Steps Summary

| File Type | Items | × Per Item | ÷ 8 | ÷ 1024 per level |
|---|---|---|---|---|
| Text (ASCII) | characters | 8 bits | → bytes | → KB → MB |
| Image | width × height pixels | colour depth bits | → bytes | → KB → MB |
| Audio | sample_rate × channels × seconds | bit depth | → bytes | → KB → MB |
| Video | fps × seconds × pixels | colour depth bits | → bytes | → KB → MB → GB |

---

## Practice Exercises

**Exercise 1**

A school database stores 2 000 student records. Each record contains:
- 30 characters for name
- 13 characters for ID number
- 3 characters for grade

What is the total storage required in KB?

<details>
<summary>Show solution</summary>

Characters per record = 30 + 13 + 3 = 46 characters  
Total characters = 2 000 × 46 = 92 000 characters  
Bytes = 92 000 × 1 = 92 000 bytes (ASCII: 1 char = 1 byte)  
KB = 92 000 ÷ 1 024 = **89.8 KB ≈ 90 KB**
</details>

---

**Exercise 2**

An 8-bit grayscale image is 800 × 600 pixels. What is its uncompressed file size in KB?

<details>
<summary>Show solution</summary>

Pixels = 800 × 600 = 480 000  
Bits per pixel = 8 (8-bit colour depth)  
Total bits = 480 000 × 8 = 3 840 000 bits  
Bytes = 3 840 000 ÷ 8 = 480 000 bytes  
KB = 480 000 ÷ 1 024 = **468.75 KB ≈ 469 KB**
</details>

---

**Exercise 3**

A podcast is recorded in mono at 22 050 Hz with 16-bit audio. The episode is 45 minutes long. Calculate the file size in MB.

<details>
<summary>Show solution</summary>

Duration = 45 × 60 = 2 700 seconds  
Bits = 22 050 × 16 × 1 × 2 700 = 952 560 000 bits  
Bytes = 952 560 000 ÷ 8 = 119 070 000 bytes  
KB = 119 070 000 ÷ 1 024 = 116 279 KB  
MB = 116 279 ÷ 1 024 = **113.6 MB**
</details>

---

> [!TIP] Exam Tip
> Always show all your working in data-size questions — method marks are awarded even if you get the final answer wrong. Write each step clearly: total items, × bits per item, ÷ 8 for bytes, then ÷ 1024 for each level up. The formula is always the same — the question just changes which file type you're calculating.
