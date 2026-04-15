---
title: Hardware
parent: Systems Technologies
grand_parent: Theory (Paper 2)
nav_order: 2
---

# Hardware

Your phone processes millions of instructions every second just to display your social media feed — but which physical components make that happen? Understanding hardware means understanding *how* a computer actually works inside, not just what it does on screen.

**Hardware** is any physical component of a computer system that you can see and touch.

---

## The Computer Model

Every computer — from a smartwatch to a supercomputer — follows the same fundamental processing model:

```
INPUT → PROCESS → OUTPUT
            ↕
         STORAGE
            ↕
       COMMUNICATION
```

| Stage | What happens | Examples |
|---|---|---|
| **Input** | Data enters the system from the outside world | Keyboard, mouse, microphone, scanner, webcam |
| **Process** | The CPU manipulates and transforms the data | Calculations, comparisons, logical decisions |
| **Output** | Results are presented to the user | Monitor, printer, speakers, projector |
| **Storage** | Data is saved permanently or temporarily | HDD, SSD, USB drive, SD card, cloud |
| **Communication** | Data is sent or received over a network | NIC, Wi-Fi card, modem, Bluetooth adapter |

> [!NOTE] Grade 10 — Foundation
> You need to know the full computer model (Input → Process → Output → Storage → Communication) and be able to give a real example of a device for each stage. This is one of the most reliable questions in Paper 2 — it appears almost every year. Make sure you can also explain the role of each stage, not just name a device.

---

## The Central Processing Unit (CPU)

The CPU is the **brain of the computer** — it carries out every instruction given to it by software. Every calculation, every comparison, every decision you see on screen was first processed here.

### The Fetch-Decode-Execute Cycle

The CPU works by continuously repeating three steps:

1. **Fetch** — retrieve the next instruction from RAM
2. **Decode** — interpret what the instruction means
3. **Execute** — carry out the instruction (arithmetic, logic, or control action)

This cycle happens billions of times per second in a modern CPU.

### CPU Performance Factors

| Factor | What it means | Effect on performance |
|---|---|---|
| **Clock speed** | How many cycles the CPU completes per second (MHz/GHz) | Higher clock speed = faster processing per core |
| **Number of cores** | Independent processing units built into one CPU chip | More cores = better multitasking and parallel work |
| **Cache size** | Fast on-chip memory (L1/L2/L3) for frequently used data | Larger cache = less time waiting for data from RAM |
| **Generation** | How new the CPU architecture is (e.g. Intel 13th Gen) | Newer = more instructions processed per clock cycle |
| **Multi-threading** | One physical core handling two instruction threads at once | Better utilisation of each core's resources |

### Clock Speed Explained

Clock speed is measured in **MHz** (megahertz) or **GHz** (gigahertz):

| Unit | Meaning |
|---|---|
| 1 Hz | 1 cycle per second |
| 1 MHz | 1 000 000 cycles per second |
| 1 GHz | 1 000 000 000 cycles per second |

A modern 3.6 GHz CPU completes **3.6 billion processing cycles every second**.

### Cores and Multi-threading

| Configuration | Description | Real-world analogy |
|---|---|---|
| Single-core | One processing unit; one task at a time | One cashier serving one queue |
| Dual-core | Two processing units working simultaneously | Two cashiers, two queues |
| Quad-core | Four processing units | Four cashiers |
| Octa-core | Eight processing units | Eight cashiers |
| Multi-threading | One core processes two lightweight threads simultaneously | One cashier handles card payment and packing at once |

> [!TIP] Grade 11 — Extension
> At Grade 11 you need to explain the difference between multi-core processing and multi-threading, and understand that more cores primarily benefit tasks like video editing, 3D rendering, and gaming — not simple tasks like word processing. You must also know all three cache levels (L1, L2, L3) and their roles.

> [!IMPORTANT] Grade 12 — Mastery
> Grade 12 questions ask you to **motivate** a CPU recommendation for a specific user type. A video editor needs many cores AND high clock speed. A basic home user doing word processing and browsing needs neither. You must name the specific performance factor and link it directly to the user's needs to earn full marks.

---

## Memory: RAM, ROM, and Cache

The word "memory" is used for several very different components. They differ in speed, capacity, and whether they keep their data when power is removed.

---

### RAM — Random Access Memory

**RAM is the computer's short-term working memory.** When you open any program, it is loaded from storage (HDD/SSD) into RAM so the CPU can access it quickly.

Key characteristics of RAM:
- **Volatile** — all information is cleared from RAM once the computer is restarted or switched off
- Holds the operating system, open applications, and any data currently being worked on
- The more RAM you have, the more programs you can run simultaneously without slowdown
- Measured in **GB** (gigabytes) — typical range: 4 GB (basic) to 64 GB+ (professional)

#### RAM Types (DDR = Double Data Rate)

| Type | Generation | Typical use |
|---|---|---|
| DDR3 | Older (2007–2015) | Budget and legacy systems |
| DDR4 | Current mainstream (2014–present) | Most modern desktops and laptops |
| DDR5 | Latest generation (2020–present) | High-end new builds |

DDR RAM transfers data **twice per clock cycle** (once on the rising edge, once on the falling edge) — that is what "Double Data Rate" means.

> [!NOTE] Grade 10 — Foundation
> Know that RAM is volatile (temporary storage). Know that more RAM = better multitasking. Be able to explain what happens when RAM is full: the system begins using **virtual memory** — a section of the HDD/SSD used as overflow RAM — which is dramatically slower and causes noticeable lag.

---

### ROM — Read-Only Memory

**ROM stores the computer's BIOS (Basic Input/Output System).** The BIOS is the first program that runs when you switch on a computer — it checks that hardware is present and working, then loads the operating system from storage.

Key characteristics of ROM:
- **Non-volatile** — data is permanently stored and is **not** cleared when the computer is switched off
- Read-only memory can only be retrieved, but **not overwritten or deleted** during normal operation
- Contains **firmware** — low-level software burned into the chip during manufacturing
- The **CMOS battery** (a small coin-cell battery on the motherboard) keeps BIOS settings such as date, time, and boot order alive when the computer is unplugged from the wall

> [!NOTE] Grade 10 — Foundation
> The most tested ROM fact is: ROM is non-volatile and stores the BIOS. Know that if the CMOS battery dies, the computer will lose its date and time settings and may struggle to boot. ROM cannot be changed during normal use — that is the key distinction from RAM.

---

### Cache Memory

**Cache memory is also called CPU memory.** It is extremely fast and works directly with the CPU to store small amounts of information that may be needed by the CPU in the immediate future.

Think of cache as the CPU's own private notepad: instead of walking all the way to the filing cabinet (RAM) every time it needs something, the CPU keeps the most frequently used items right on its desk.

#### Cache Levels

| Level | Location | Speed | Typical Size | Role |
|---|---|---|---|---|
| **L1** | Inside each CPU core | Fastest of all | 32 KB – 512 KB | Stores the instructions and data the core is using right now |
| **L2** | Inside the CPU (per core or shared) | Very fast | 256 KB – 4 MB | Second-level lookup before going wider |
| **L3** | On the CPU die (shared by all cores) | Fast | 4 MB – 64 MB | Shared pool available to all cores |

When the CPU needs data, it checks in order:

```
L1 cache → L2 cache → L3 cache → RAM → Storage
(fastest)                                (slowest)
```

- **Cache hit** — the required data is found in cache. Fast!
- **Cache miss** — the data is not in cache; the CPU must fetch it from RAM. Slow.

> [!TIP] Grade 11 — Extension
> You need to know all three cache levels by name and explain the cache hit vs cache miss concept. A larger L3 cache is particularly beneficial for gaming (large game assets) and video editing (large media files). Exam questions often ask you to explain why L1 is faster than L3, and why cache is faster than RAM.

---

## Memory Comparison Table

This comparison table is tested almost every year — learn every cell.

| Memory | Capacity | Speed | Volatile? | Can be written? | Purpose |
|---|---|---|---|---|---|
| **RAM** | 4 GB – 64 GB (typical) | Very high | Yes — cleared on restart | Yes — constantly | Active programs and working data |
| **ROM** | A few MB | Very slow | No — permanent | No — read only | Stores BIOS firmware |
| **Cache** | KB to tens of MB | Extremely fast | Yes — cleared on restart | CPU manages it | CPU's immediate data store |
| **HDD** | 500 GB – several TB | Normal/slow | No — permanent | Yes | Long-term file storage |
| **SSD** | 256 GB – several TB | High | No — permanent | Yes | Long-term file storage (faster than HDD) |

---

## The Motherboard

The motherboard is the **main circuit board** of a computer. Every other component either plugs into it or connects to it. It is the backbone that allows all parts to communicate with each other.

### Key Motherboard Components

| Component | Purpose |
|---|---|
| **CPU socket** | Physically holds the CPU — must match the CPU's brand and socket type (e.g. Intel LGA1700) |
| **RAM slots (DIMM slots)** | Hold the RAM sticks — the number of slots determines how much RAM can be installed |
| **Chipset** | A set of chips that manages data flow between the CPU, RAM, and other components |
| **BIOS/UEFI chip** | Contains the ROM with startup firmware — the first thing that runs at boot |
| **CMOS battery** | Keeps date/time and BIOS settings alive when the PC is unplugged |
| **Power connector** | Receives power from the PSU (Power Supply Unit) |
| **PCI-e slots** | Expansion slots for GPUs, sound cards, NIC cards, and other add-in cards |
| **SATA connectors** | Connect internal HDD and SSD drives via data cables |
| **USB headers** | Internal connectors for front-panel USB ports |
| **Buses** | Printed electrical pathways carrying data between all components |

### Expansion Cards and PCI-e Slots

**PCI-e (Peripheral Component Interconnect Express)** is the standard interface for expansion cards:

| Expansion card | What it adds |
|---|---|
| **Graphics card (GPU)** | Dedicated graphics processing for gaming, video editing, and AI |
| **Sound card** | High-quality audio for music production studios |
| **Network Interface Card (NIC)** | Adds an ethernet port or Wi-Fi capability |
| **Capture card** | Records or streams gameplay footage |

> [!TIP] Grade 11 — Extension
> You must know the major motherboard components and their roles for Grade 11. A common exam question is: "Why can't you install any CPU into any motherboard?" — the answer is that the CPU must match the motherboard's socket type. Know what PCI-e slots are used for and why the chipset matters for bus speeds.

---

## Buses

A **bus** is an electrical pathway printed onto the motherboard that carries signals between components. Think of it like a highway system — different types of data travel on different roads.

### The Three Types of Bus

| Bus type | What it carries | Direction of travel |
|---|---|---|
| **Data bus** | The actual data being transferred | Bidirectional (both directions) |
| **Address bus** | The memory address specifying where data should be read from or written to | Unidirectional (CPU → memory) |
| **Control bus** | Control signals: read, write, interrupt, clock signals | Bidirectional |

### Bus Width

The **width** of a bus determines how much data can travel simultaneously:

| Bus width | Data per cycle |
|---|---|
| 8-bit bus | 8 bits at once |
| 32-bit bus | 32 bits at once |
| 64-bit bus | 64 bits at once (modern standard) |

A wider bus moves more data per cycle — like having a 6-lane highway instead of a 2-lane road.

> [!TIP] Grade 11 — Extension
> The three bus types are a very common Paper 2 question. You must know: (1) what each bus carries, (2) the direction of travel for each, and (3) why the address bus is unidirectional while the data bus is bidirectional. The address bus tells the system *where* data is — it only ever travels from the CPU outward.

---

## Key Terms

| Term | Definition |
|---|---|
| **Hardware** | Any physical component of a computer that you can touch |
| **CPU** | Central Processing Unit — the component that executes all instructions |
| **Clock speed** | The number of processing cycles a CPU completes per second, measured in GHz |
| **Core** | An independent processing unit within a single CPU chip |
| **Multi-threading** | A technique where one CPU core handles two instruction threads simultaneously |
| **RAM** | Random Access Memory — volatile, high-speed temporary working memory |
| **Volatile** | Data is lost when electrical power is removed |
| **Non-volatile** | Data is retained when electrical power is removed |
| **ROM** | Read-Only Memory — non-volatile memory that stores BIOS firmware |
| **BIOS** | Basic Input/Output System — firmware that initialises hardware at startup |
| **Firmware** | Low-level software permanently stored in ROM or flash memory |
| **CMOS battery** | Coin-cell battery that keeps BIOS settings (clock, date, boot order) alive when unplugged |
| **Cache memory** | Ultra-fast CPU memory (L1/L2/L3) that stores frequently needed data close to the CPU |
| **Cache hit** | The required data is found in cache — fast result |
| **Cache miss** | The required data is not in cache — CPU must fetch from slower RAM |
| **Virtual memory** | A section of HDD/SSD used as overflow RAM when actual RAM is full — very slow |
| **Motherboard** | The main circuit board that connects and enables communication between all components |
| **PCI-e** | Peripheral Component Interconnect Express — expansion slot standard for GPUs, NICs, and other cards |
| **Bus** | An electrical pathway on the motherboard that carries data, addresses, or control signals |
| **Data bus** | Bus that carries actual data — bidirectional |
| **Address bus** | Bus that carries memory addresses — unidirectional (CPU to memory) |
| **Control bus** | Bus that carries control and command signals — bidirectional |
| **DDR** | Double Data Rate — RAM that transfers data twice per clock cycle |
| **Chipset** | Chips on the motherboard that manage data flow between the CPU and other components |
| **SATA** | Serial ATA — the connector standard used for internal HDD and SSD drives |

---

## Exam Focus — Paper 2

> [!IMPORTANT] What Examiners Test
> Hardware is examined almost every year in Paper 2. These are the question patterns you must be ready for:

**1. Define and distinguish RAM vs ROM** (3–4 marks)

A strong answer contrasts: volatility, capacity, speed, purpose, and whether it can be written.

| | RAM | ROM |
|---|---|---|
| Volatile? | Yes — data lost on shutdown | No — data is permanent |
| Capacity | GBs | A few MB |
| Speed | Very fast | Very slow |
| Can be written? | Yes | No |
| Stores | Running programs and data | BIOS firmware |

**2. Explain why RAM is described as volatile** (2 marks)
> RAM is volatile because all data stored in it is lost/erased when the computer is switched off or restarted. It requires continuous electrical power to maintain its contents.

**3. Explain the role of cache memory / distinguish L1, L2, L3** (3–6 marks)
- Cache is very fast memory that sits between the CPU and RAM
- L1 is the fastest and smallest — stores what the current core is actively using
- L2 is larger and slightly slower — a second-level store per core
- L3 is the largest and shared by all cores — last stop before RAM

**4. Name and describe THREE types of bus** (6 marks)
- **Data bus**: carries actual data; bidirectional
- **Address bus**: carries memory addresses; unidirectional (CPU → memory)
- **Control bus**: carries control signals (read/write/interrupt); bidirectional

**5. List FOUR factors that affect CPU performance** (4 marks)
- Clock speed (GHz), number of cores, cache size (L1/L2/L3), CPU generation

**6. Complete or draw the computer model with examples** (5 marks)
- Input (keyboard), Process (CPU), Output (monitor), Storage (HDD/SSD), Communication (NIC/modem)

**Command words to watch:**
- *Define* — give the exact technical meaning
- *Describe* — explain in detail with context
- *Distinguish / Differentiate* — explain the differences between two things
- *Motivate* — give reasons backed by evidence
- *List* — give items without explanation (unless the question says "and explain")
