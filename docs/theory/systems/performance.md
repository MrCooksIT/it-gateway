# Computer Performance

You've seen two computers side by side — one flies, one crawls. The difference isn't magic: it's a combination of hardware components working together (or failing to). Understanding what drives performance lets you choose the right machine for the job — and answer the most common Paper 2 question type: *"Recommend hardware for this user and motivate your choice."*

---

> [!IMPORTANT] Grade 12 — Primary Topic
> Computer performance is primarily a Grade 12 theory topic, though the hardware components themselves are introduced in Grade 10 and 11.

---

## What is Computer Performance?

**Computer performance** is the amount of useful work accomplished by a computer system in a given time.

It is measured in terms of:
- **Speed** — how fast instructions are executed
- **Throughput** — the rate at which work is completed
- **Response time** — the time between a request and its result

High-performance computers typically achieve:
- Short response time for a given task
- High throughput
- Low utilisation of computing resources (not working too hard just to idle)
- Fast data compression/decompression
- High bandwidth
- Short data transmission time

---

## Component Performance Factors

This table is the core of the performance topic. Every cell is examinable.

| Component | Purpose | Performance Factors |
|---|---|---|
| **CPU** | Executes all general processing tasks | Clock speed (GHz), Number of cores, Cache size (L1/L2/L3), CPU generation |
| **GPU** | Handles all graphics and visual processing | Clock speed (GHz), VRAM amount, Memory clock speed, Model/generation |
| **RAM** | High-speed temporary storage for active data | Generation (DDR3 / DDR4 / DDR5), Amount in GB, Clock speed (MHz) |
| **ROM** | Stores BIOS firmware | Not a performance-critical component |
| **HDD** | Slow, mechanical long-term storage | Capacity (GB/TB), Rotational speed (RPM — e.g. 5400 or 7200 RPM) |
| **SSD** | Fast, electronic long-term storage | Capacity (GB/TB), Read/write speed (MB/s), Interface (SATA vs NVMe) |
| **Motherboard** | Connects all components | CPU socket compatibility, Bus speeds, Number of PCI-e slots |
| **Monitor** | Displays output | Resolution (1080p / 4K), Refresh rate (Hz), Panel type (IPS/OLED) |

> [!TIP] Exam Tip
> The question format is usually: *"Name TWO factors that affect the performance of the CPU."* Always name the factor AND briefly explain what it does. Two bare words ("clock speed, cores") score 2/4. Add what each factor does and you score 4/4.

---

## The Bottleneck Effect

**A bottleneck occurs when one slow component limits the performance of all other components.** The system can only run as fast as its slowest part.

> Example: A powerful R20 000 CPU paired with a slow 5400 RPM hard drive will still feel sluggish — the CPU sits idle waiting for the hard drive to load data. Upgrading the CPU further won't help. Replacing the hard drive with an SSD would dramatically improve the experience.

Storage speed matters most when:
1. Opening a program (data loaded from storage to RAM)
2. Loading the operating system at startup
3. Installing large applications
4. Saving large files (video exports, large databases)
5. Copying files between two storage devices

---

## User Types and Recommended Configurations

This is the most common exam question type. You must link each hardware choice to the user's specific needs.

### Home User
**Uses:** Internet browsing, social media, email, word processing, basic entertainment, Internet banking.

| Component | Recommendation | Why |
|---|---|---|
| CPU | Entry-level (e.g. Intel i3 or AMD Ryzen 3) | Light tasks don't require processing power |
| GPU | Integrated (built into CPU) or entry-level | No 3D gaming or video editing |
| RAM | 8 GB | Sufficient for multitasking with basic apps |
| Storage | Mid-range SSD (256–512 GB) | Fast boot and response with adequate space |
| Monitor | Entry-level (1080p) | Basic browsing and video is fine at 1080p |

### SOHO User (Small Office / Home Office)
**Uses:** Accounting, email, databases, spreadsheets, business communication, online research.

| Component | Recommendation | Why |
|---|---|---|
| CPU | Mid-range (i5 / Ryzen 5) | Business apps need reliable processing |
| GPU | Integrated | No need for graphics-intensive work |
| RAM | 16 GB | Multiple business apps running simultaneously |
| Storage | SSD | Fast load times increase productivity |
| Other | Long battery life if laptop; good display resolution | Mobility and visibility of data |

### Gamer
**Uses:** Playing modern games at high settings, recording gameplay, streaming.

| Component | Recommendation | Why |
|---|---|---|
| CPU | High-end (i7/i9 or Ryzen 7/9) | Fast single-core performance for game logic |
| GPU | High-end dedicated GPU (e.g. NVIDIA RTX) | Games are heavily GPU-dependent |
| RAM | 16–32 GB DDR5 | Large open-world games use lots of RAM |
| Storage | Fast NVMe SSD | Near-instant game loading |
| Monitor | High refresh rate (144 Hz+) | Smooth, tear-free gameplay |

> [!WARNING] Balanced Build
> Pairing a high-end GPU with a weak CPU causes a CPU bottleneck. The GPU renders frames faster than the CPU can prepare the game data. A balanced build where components are roughly matched in performance tier is always better than one ultra-fast component surrounded by weak ones.

### Power User
**Uses:** Video editing, 3D rendering, software development, graphic design, compiling large codebases.

| Component | Recommendation | Why |
|---|---|---|
| CPU | High-end, many cores (i9 / Ryzen 9 / Threadripper) | Rendering and compilation are CPU-intensive |
| GPU | High-end (also needed for GPU-accelerated rendering) | Some rendering uses GPU compute power |
| RAM | 32–64 GB | Large projects and multiple apps need it |
| Storage | Large, fast NVMe SSD | Working with large video and project files |
| Monitors | Two monitors | Multitasking across applications is essential |

---

## Storage: HDD vs SSD

| Feature | HDD | SSD |
|---|---|---|
| Mechanism | Spinning magnetic platters + read/write head | Flash memory chips (no moving parts) |
| Speed | ~80–160 MB/s | 500 MB/s (SATA) to 7000 MB/s (NVMe) |
| Noise | Audible spinning | Silent |
| Shock resistance | Low — can be damaged by drops | High — no moving parts |
| Price per GB | Cheaper | More expensive |
| Lifespan | 3–5 years typical | 5–10 years typical |
| Best for | Large, cheap long-term storage (backups, archives) | Operating system, applications, active projects |

---

## Key Terms

| Term | Definition |
|---|---|
| **Performance** | The amount of useful work a computer completes in a given time |
| **Clock speed** | How many processing cycles the CPU completes per second (GHz) |
| **Core** | An independent processing unit inside a CPU |
| **Throughput** | The rate at which a system processes work |
| **Bottleneck** | A slow component that limits the performance of all other components |
| **GPU** | Graphics Processing Unit — handles visual/graphics computation |
| **VRAM** | Video RAM — dedicated memory on the GPU for graphics data |
| **RPM** | Revolutions per minute — speed of a spinning hard drive |
| **NVMe** | Non-Volatile Memory Express — high-speed SSD interface |
| **SOHO** | Small Office / Home Office — describes a small business or home business user |
| **DDR** | Double Data Rate — RAM that transfers data twice per clock cycle |
| **Cache hit/miss** | Hit = data found in cache (fast). Miss = must fetch from RAM (slower) |
| **Bandwidth** | The rate at which data can be transferred across a connection |

---

## Exam Focus — Paper 2

> [!IMPORTANT] High-Frequency Questions
>
> 1. **"Name and explain TWO factors that affect the performance of [component]"** (4–6 marks)  
>    → Always name the factor + state its effect on performance
>
> 2. **"Recommend a computer configuration for [user type] and motivate EACH choice"** (8–10 marks)  
>    → Name the component recommendation + link it directly to that user's specific tasks
>
> 3. **"Explain what a bottleneck is. Give an example."** (3–4 marks)  
>    → Define bottleneck + give a specific component pairing example
>
> 4. **"Compare HDD and SSD. Which would you recommend for [scenario]?"** (4–6 marks)  
>    → Speed, mechanism, price, noise, shock resistance — then motivate for the scenario

> [!NOTE] Motivate = Reason + Link
> When a question says "motivate your choice", you must: (1) state what you chose, (2) give the reason, and (3) link it to the user's specific use. Just saying "fast CPU because the user needs speed" is too vague. Say: "A high-end multi-core CPU because video editing requires parallel processing of multiple video streams simultaneously."
