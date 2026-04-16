# OS Management Functions

The operating system doesn't just provide a desktop — it is constantly working behind the scenes managing files, memory, processes, and devices. Understanding what an OS manages is core Paper 2 content.

> [!NOTE] Grade 10+
> OS management functions are introduced in Grade 10. File management, backup, and compression are key Gr10 topics. Virtualisation links to Grade 12.

---

## OS Core Functions — Overview

| Function | What the OS does |
|---|---|
| **File management** | Organises files in folders; handles read/write/delete operations |
| **Process management** | Controls which programs run and how much CPU time they get |
| **Memory management** | Allocates RAM to programs; manages virtual memory |
| **Device management** | Communicates with hardware via drivers |
| **Security** | User accounts, passwords, access permissions, firewalls |
| **User interface** | Provides GUI or CLI for user interaction |

---

## File Management

The OS organises all data on storage devices using a **hierarchical folder structure** (directory tree).

### File System Concepts

| Concept | Explanation |
|---|---|
| **File** | A named collection of data stored on a storage device |
| **Folder/Directory** | A container that organises files |
| **Path** | Full address of a file: `C:\Users\Ayden\Documents\notes.txt` |
| **Extension** | Letters after the dot indicating file type: `.docx`, `.py`, `.txt` |
| **Root directory** | Top-level folder — `C:\` on Windows, `/` on Linux |
| **Absolute path** | Full path from root: `C:\Users\Ayden\file.txt` |
| **Relative path** | Path relative to current location: `..\file.txt` |

### Common File Extensions

| Extension | Type |
|---|---|
| `.docx` | Word document |
| `.xlsx` | Excel spreadsheet |
| `.pdf` | Portable Document Format |
| `.jpg / .jpeg` | JPEG image |
| `.png` | PNG image (lossless) |
| `.mp3` | Audio (compressed) |
| `.mp4` | Video (compressed) |
| `.exe` | Windows executable |
| `.py` | Python source code |
| `.txt` | Plain text |
| `.zip` | Compressed archive |

### File System Types

| File System | OS | Features |
|---|---|---|
| **NTFS** | Windows | Permissions, encryption, large files, journaling |
| **FAT32** | Universal | Wide compatibility, max 4 GB file size |
| **exFAT** | USB drives | Large files, cross-platform |
| **ext4** | Linux | Journaling, large files, fast |
| **APFS** | macOS | Encryption, snapshots, optimised for SSDs |

---

## Process Management

A **process** is a program that is currently being executed by the CPU.

The OS manages multiple processes via **multitasking**:
- **Time-slicing**: each process gets a tiny slice of CPU time, switching rapidly
- **Context switching**: saving one process's state while loading another
- **Process scheduler**: decides which process runs next (priority-based)

**Task Manager** (Windows) shows all running processes and their CPU/RAM usage. You can end unresponsive processes here.

---

## Memory Management

The OS allocates RAM to programs as needed and reclaims it when programs close.

### Virtual Memory

When physical RAM is full, the OS uses a portion of the hard drive as **virtual memory** (swap space / page file):
- Data from RAM is temporarily moved to a swap file on disk
- The process can continue running even with insufficient RAM
- **Significantly slower** than physical RAM (disk access vs RAM access)
- Heavy virtual memory use causes noticeable slowdowns

```
Fast RAM (8 GB) ←→ Slow Disk (swap file) — managed by OS
```

---

## Device Management

Every hardware device needs a **driver** — a small program letting the OS communicate with that specific device.

**Plug and Play process:**
1. Device is connected
2. OS detects new hardware
3. OS finds and loads the appropriate driver
4. Device is ready to use

**Driver problems:**
- Outdated → device malfunction
- Missing → device not recognised
- Wrong → system instability or BSOD (Blue Screen of Death)

---

## File Compression

**Compression** reduces file size by encoding data more efficiently.

| Type | Method | Quality | Examples |
|---|---|---|---|
| **Lossless** | Removes redundant patterns; fully reversible | No quality loss | ZIP, 7-ZIP, PNG, FLAC |
| **Lossy** | Permanently removes detail | Reduced quality | JPEG, MP3, MP4 |

**Why compress?**
- Save storage space
- Faster transfer (smaller file = less bandwidth/time)
- Bundle multiple files into one archive

---

## Backup

**Backup** is the process of copying data to a separate location so it can be restored if the original is lost or corrupted.

**Threats that make backup essential:**
- Hardware failure (HDD crash)
- Ransomware attack
- Accidental deletion
- Physical theft or damage
- Fire or flood

### Backup Types

| Type | What it backs up | Speed | Storage |
|---|---|---|---|
| **Full backup** | All selected data every time | Slowest | Most |
| **Incremental** | Only changes since last backup | Fastest | Least |
| **Differential** | Changes since last FULL backup | Medium | Medium |

### The 3-2-1 Rule
- **3** copies of data
- **2** different storage media types
- **1** copy offsite (or cloud)

### Backup Media Options
- External HDD/SSD
- USB flash drive
- Cloud backup (Google Drive, OneDrive, iCloud)
- Network-attached storage (NAS)
- Tape (large organisations, archival)

---

## Disk Defragmentation

Over time, HDD files get split into fragments scattered across the disk. **Defragmentation** rearranges fragments so files are stored contiguously, improving read speed.

> [!WARNING] SSDs Do NOT Need Defragmentation
> Defragmenting an SSD causes unnecessary writes that shorten its lifespan, with no speed benefit. Modern Windows skips defrag on SSDs automatically.

---

## User Accounts and Permissions

| Account Type | Windows | Capabilities |
|---|---|---|
| **Administrator** | Full | Install software, change settings, manage users |
| **Standard user** | Limited | Run programs, manage own files; cannot install system software |
| **Guest** | Minimal | Temporary access, no changes |

### File Permissions

| Permission | Meaning |
|---|---|
| **Read** | View file content |
| **Write** | Modify file content |
| **Execute** | Run a program |
| **Full control** | All permissions + change others' permissions |

---

## Key Terms

| Term | Definition |
|---|---|
| **Process** | Program currently executing in memory |
| **Multitasking** | OS runs multiple processes apparently simultaneously |
| **Virtual memory** | Using disk space as extra RAM when physical RAM is full |
| **Driver** | Software allowing OS to communicate with hardware |
| **Defragmentation** | Rearranging HDD file fragments for faster access |
| **Compression** | Reducing file size by encoding more efficiently |
| **Lossless** | Compression with no quality loss — file fully recoverable |
| **Lossy** | Compression that permanently removes detail |
| **Backup** | Copy of data stored separately for recovery |
| **Incremental backup** | Only backs up changes since last backup |
| **Full backup** | Backs up all selected data completely |
| **Permissions** | Access rights granted to users for files/folders |

---

## Exam Focus

> [!IMPORTANT] High-Frequency Questions
>
> 1. **"Give TWO functions of an operating system"** — name + explain each: "File management — organises files in folders and handles read/write/delete operations"
>
> 2. **"What is virtual memory?"** — uses disk space as extra RAM when physical RAM is full; slower than actual RAM
>
> 3. **"Explain the difference between full and incremental backup"** — full = all data copied every time; incremental = only changes since last backup (faster, uses less storage)
>
> 4. **"Explain lossless vs lossy compression. Give an example of each."** — lossless: no quality loss, file fully recoverable (ZIP, PNG); lossy: some quality removed permanently (JPEG, MP3)
>
> 5. **"Why should you NOT defragment an SSD?"** — no moving parts; unnecessary writes shorten lifespan; no speed benefit
