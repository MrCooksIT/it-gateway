# Software

Hardware is useless without software to run on it. Software is the set of instructions — programs — that tell a computer what to do. Every program you use, from a browser to Delphi, is software.

> [!NOTE] Grade 10+
> The software classification system (System vs Application) is introduced in Grade 10. Operating system types and utility software extend into Grade 11.

---

## Hardware vs Software

| | Hardware | Software |
|---|---|---|
| Definition | Physical components you can touch | Programs and instructions |
| Examples | CPU, RAM, hard drive, monitor | Windows, MS Word, Delphi, VLC |
| Change | Requires physical replacement | Updated or replaced via download/install |
| Stored | In circuit boards, chips, storage | On storage devices (HDD/SSD) or ROM |

---

## Software Categories

```
SOFTWARE
├── System Software
│   ├── Operating System (OS)
│   ├── Utility Software
│   └── Device Drivers
└── Application Software
    ├── General Purpose
    ├── Specific Purpose
    └── Custom-Written
```

---

## System Software

System software manages the computer's hardware and provides a platform for application software to run. Users rarely interact with it directly.

### Operating System (OS)

The **OS** is the most important piece of system software. It is the bridge between the user, the applications, and the hardware.

**Core functions of an OS:**

| Function | Description |
|---|---|
| **Process management** | Controls which programs run and when; manages CPU time |
| **Memory management** | Allocates RAM to programs; manages virtual memory |
| **File management** | Organises files in folders; handles read/write operations |
| **Device management** | Communicates with hardware via device drivers |
| **Security** | User accounts, passwords, access rights, firewalls |
| **User interface** | GUI or CLI for the user to interact with the system |

**Types of Operating System:**

| Type | Description | Examples |
|---|---|---|
| **GUI (Graphical User Interface)** | Uses icons, windows, mouse — visual interaction | Windows 11, macOS, Ubuntu |
| **CLI (Command Line Interface)** | Text commands only — no mouse | MS-DOS, Linux terminal, PowerShell |
| **Multi-user** | Multiple users can work simultaneously | Linux servers, mainframes |
| **Multi-tasking** | Multiple programs run at the same time | Windows, macOS |
| **Real-time OS (RTOS)** | Processes data instantly with no delay | Medical equipment, aircraft, factory robots |
| **Embedded OS** | Built into a device; dedicated function | Smart TV OS, washing machine controller |
| **Mobile OS** | Designed for touchscreen portable devices | Android, iOS |
| **Network OS (NOS)** | Manages network resources, shared access | Windows Server, Novell NetWare |

> [!TIP] Grade 11 — Extension
> At Grade 11, you need to compare OS types in terms of: usability (GUI easier than CLI), security (CLI can be more secure), resources needed (CLI uses less RAM), and use cases (CLI for servers, GUI for desktops).

> [!IMPORTANT] Grade 12 — Mastery
> At Grade 12, understand how OS interacts with virtualisation (running multiple OS instances on one physical machine) and cloud-based OS delivery.

---

### Utility Software

Utility programs maintain, optimise, and protect the computer system. They work in the background or on demand.

| Utility | Function | Example |
|---|---|---|
| **Antivirus** | Detect and remove malware | Avast, Windows Defender, Kaspersky |
| **Firewall** | Monitor and filter network traffic | Windows Firewall, hardware firewalls |
| **Backup software** | Create copies of data for recovery | Windows Backup, Time Machine |
| **Disk cleanup** | Remove unnecessary files to free space | Windows Disk Cleanup, CCleaner |
| **Disk defragmenter** | Rearrange fragmented files on HDD for faster access | Windows Defragmenter |
| **Compression software** | Reduce file size for storage/transfer | WinZip, 7-Zip, Windows built-in |
| **File manager** | Browse, copy, move, organise files | Windows Explorer, Finder |
| **Task manager** | Monitor and control running processes | Windows Task Manager |
| **Screensaver / Power mgmt** | Save energy when computer is idle | Windows power settings |

> [!NOTE] Disk Defragmenter vs SSD
> Defragmentation is only useful on HDDs (spinning disks). SSDs do NOT need defragmentation — it actually shortens their lifespan. Modern Windows automatically skips defrag on SSDs.

---

### Device Drivers

A **device driver** is a small program that allows the OS to communicate with a specific hardware device.

- Every hardware device needs a driver: printer, graphics card, keyboard, webcam
- When you plug in a new device, Windows searches for the correct driver
- Outdated or missing drivers cause device malfunction

---

## Application Software

Application software is designed for end users to perform specific tasks.

### General Purpose Applications

Can be used for many different tasks — not tied to one job:

| Software | Type | Use |
|---|---|---|
| Microsoft Word | Word processor | Create and edit text documents |
| Microsoft Excel | Spreadsheet | Calculations, data analysis, charts |
| Microsoft PowerPoint | Presentation | Slideshows, visual presentations |
| Google Chrome / Firefox | Web browser | Browse the internet |
| VLC Media Player | Media player | Play audio and video files |

### Specific Purpose Applications

Designed for one particular type of task:

| Software | Use |
|---|---|
| Delphi / Visual Studio | Software development / coding |
| Adobe Photoshop | Image editing |
| AutoCAD | Engineering / architectural drawing |
| Sage Accounting | Business accounting |
| MS Project | Project management |

### Custom-Written Applications

Software written specifically for ONE organisation's unique needs:

- **Example:** A hospital patient management system built exactly to that hospital's workflows
- More expensive than off-the-shelf, but perfectly suited to the organisation
- Maintained by the company or contracted developers

---

## Software Licensing

| Licence Type | Cost | Restrictions | Examples |
|---|---|---|---|
| **Proprietary / Commercial** | Paid | Cannot copy, modify, or distribute | Microsoft Office, Adobe CC |
| **Freeware** | Free | Can use freely; cannot modify source | VLC, 7-Zip |
| **Shareware** | Free trial | Pay to continue after trial | WinZip (trial) |
| **Open source** | Free | Source code available; can modify and distribute | Linux, Firefox, LibreOffice |
| **Creative Commons** | Varies | Specific conditions set by the creator | Many online images and music |

> [!NOTE] Open Source ≠ Free
> Open source means the source code is available — some open source software has commercial licences. "Free" can mean free as in cost (freeware) or free as in freedom (open source). These are different things.

---

## FOSS — Free and Open Source Software

**FOSS** combines free (no cost) and open source (modifiable source code):

- Linux operating system
- LibreOffice (alternative to MS Office)
- Firefox, Chromium
- Python, PHP, MySQL

**Advantages of FOSS:**
- No cost
- Community-supported
- Transparent — anyone can inspect the code for security flaws
- Customisable

**Disadvantages:**
- Less formal support (community forums vs paid helpdesk)
- Compatibility issues with proprietary software
- Can be less polished than commercial alternatives

---

## Key Terms

| Term | Definition |
|---|---|
| **Software** | Programs and operating information used by a computer |
| **System software** | Software that manages hardware and provides a platform for applications |
| **Operating system** | Core system software managing all computer resources |
| **GUI** | Graphical User Interface — visual icons, windows, mouse-driven |
| **CLI** | Command Line Interface — text commands only |
| **Utility software** | Programs that maintain and optimise the computer system |
| **Device driver** | Software enabling the OS to communicate with a hardware device |
| **Application software** | Software for end-user tasks |
| **Freeware** | Free-to-use software (source code not necessarily available) |
| **Open source** | Software with publicly available, modifiable source code |
| **FOSS** | Free and Open Source Software |
| **Proprietary** | Commercially licensed software — owned by a company |
| **Custom software** | Software built for one specific organisation's needs |

---

## Exam Focus

> [!IMPORTANT] High-Frequency Questions
>
> 1. **"Classify the following as system or application software and give a reason"** (2 marks each)  
>    → Know: OS + utilities = system; everything else users run = application
>
> 2. **"Name TWO types of application software and give an example of each"** (4 marks)  
>    → General purpose (Word), Specific purpose (Photoshop), Custom-written
>
> 3. **"Explain the difference between freeware and open source"** (2–3 marks)  
>    → Freeware = free to use but closed source; open source = source code available, can modify
>
> 4. **"Give TWO functions of an operating system"** (4 marks)  
>    → Always name the function AND explain what it does in that computer context
>
> 5. **"Why would a server use a CLI rather than a GUI?"** (2 marks)  
>    → CLI uses less RAM/processing power; better for remote administration; more efficient for experienced users
