# Systems Technologies — Quick Summary

Fast-scan reference for hardware, software, performance, and types of computers. No prose.

---

## Computer Model

| Component | Role | Examples |
|---|---|---|
| **Input** | Feed data into system | Keyboard, mouse, scanner, microphone |
| **Processing** | CPU executes instructions | CPU, ALU, CU, registers |
| **Memory** | Temporary storage during processing | RAM, ROM, cache |
| **Storage** | Permanent data storage | HDD, SSD, USB, optical disc |
| **Output** | Deliver results to user | Monitor, printer, speakers |
| **Communication** | Connect to other devices/networks | NIC, router, modem |

---

## CPU Internals

| Part | Function |
|---|---|
| **ALU** | Arithmetic and Logic Unit — calculations and comparisons |
| **CU** | Control Unit — coordinates all CPU operations |
| **Registers** | Tiny fastest storage inside CPU (PC, IR, MAR, MDR, AC) |
| **Cache (L1/L2/L3)** | Ultra-fast RAM buffer on/near CPU |

**Fetch-Decode-Execute cycle:**
1. Fetch instruction from RAM (using PC register)
2. Decode the instruction (CU)
3. Execute it (ALU or memory operation)
4. Store result; increment PC; repeat

---

## Memory Comparison

| Memory | Type | Volatile? | Speed | Size |
|---|---|---|---|---|
| CPU Registers | SRAM | Yes | Fastest | Bytes |
| L1 Cache | SRAM | Yes | Very fast | KB |
| L2 Cache | SRAM | Yes | Fast | KB–MB |
| L3 Cache | SRAM | Yes | Fast | MB |
| RAM | DRAM | Yes | Moderate | GB |
| ROM (BIOS) | Non-volatile ROM | No | Moderate | MB |
| SSD | Flash | No | Moderate-fast | GB–TB |
| HDD | Magnetic | No | Slow | GB–TB |

---

## CPU Performance Factors

| Factor | Effect |
|---|---|
| **Clock speed (GHz)** | More cycles per second = faster processing |
| **Number of cores** | More cores = more parallel tasks |
| **Cache size** | More cache = fewer slow RAM accesses |
| **CPU generation** | Newer = better architecture, efficiency |
| **Hyperthreading** | Each core handles 2 threads simultaneously |

---

## GPU Performance Factors

- Clock speed (GHz)
- VRAM amount (GB)
- Memory bus width
- Model/generation (RTX 4090 vs GTX 1650)

---

## RAM Performance Factors

- Generation (DDR3 < DDR4 < DDR5)
- Amount (GB) — more = less swapping to disk
- Clock speed (MHz)

---

## Storage Comparison

| | HDD | SSD |
|---|---|---|
| Technology | Spinning magnetic platters | Flash memory |
| Speed | ~100–160 MB/s | 500 MB/s–7 GB/s |
| Noise | Audible | Silent |
| Shock resistant | Low | High |
| Price/GB | Cheaper | More expensive |
| Best for | Bulk/archival storage | OS, apps, active work |

---

## Three Bus Types

| Bus | Direction | Carries |
|---|---|---|
| **Data bus** | Bidirectional | Actual data |
| **Address bus** | CPU → memory | Memory addresses |
| **Control bus** | Bidirectional | Control signals (read, write, clock) |

Bus width = number of lines = how many bits in parallel. Wider bus = more data per transfer.

---

## Software Classification

```
SOFTWARE
├── System Software
│   ├── Operating System (process, memory, file, device, security management)
│   ├── Utility (antivirus, firewall, backup, disk cleanup, compression)
│   └── Device Drivers
└── Application Software
    ├── General purpose (Word, Excel, Chrome)
    ├── Specific purpose (Photoshop, AutoCAD)
    └── Custom-written (bespoke for one organisation)
```

---

## OS Types

| Type | Description | Example |
|---|---|---|
| GUI | Graphical, mouse-driven | Windows, macOS |
| CLI | Text commands | Linux terminal |
| Multi-user | Many users simultaneously | Linux server |
| Real-time (RTOS) | Instant response | Medical device OS |
| Embedded | Dedicated device | Smart TV OS |
| Mobile | Touchscreen portable | Android, iOS |
| Network OS | Manages network resources | Windows Server |

---

## Types of Computers

| Type | Portable? | Users | Use |
|---|---|---|---|
| Desktop | ✗ | 1 | Office/home productivity |
| Laptop | ✓ | 1 | Mobile personal use |
| Tablet | ✓ | 1 | Media, education |
| Smartphone | ✓ | 1 | Communication, apps |
| Server | ✗ | Many | Network services |
| Mainframe | ✗ | Thousands | Mass transactions |
| Supercomputer | ✗ | Many | Scientific simulation |
| Embedded | Varies | 0 (invisible) | Single dedicated task |

---

## User Type Recommendations

| User | CPU | RAM | Storage | GPU |
|---|---|---|---|---|
| Home | Entry (i3/Ryzen 3) | 8 GB | Mid SSD | Integrated |
| SOHO | Mid (i5/Ryzen 5) | 16 GB | SSD | Integrated |
| Gamer | High (i7-9/Ryzen 7-9) | 16–32 GB DDR5 | Fast NVMe SSD | High-end dedicated |
| Power user | Many-core (i9/Threadripper) | 32–64 GB | Large NVMe SSD | High-end |

---

## Licence Types

| Type | Free? | Source? | Copy? |
|---|---|---|---|
| Proprietary | Paid | Closed | No |
| Freeware | Yes | Closed | Usually yes |
| Shareware | Trial | Closed | Trial only |
| Open source | Usually | Open | Yes (under conditions) |
| Public domain | Yes | Open | Yes, no restrictions |

---

## Data Sizes

```
8 bits = 1 byte
1 024 bytes = 1 KB
1 024 KB = 1 MB
1 024 MB = 1 GB
1 024 GB = 1 TB
```

**Storage calculation:**
- Text: characters × 1 byte
- Image: width × height × colour_depth_bits ÷ 8
- Audio: sample_rate × bit_depth × channels × seconds ÷ 8
