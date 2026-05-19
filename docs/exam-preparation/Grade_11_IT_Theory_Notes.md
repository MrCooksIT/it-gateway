# Grade 11 Information Technology — Theory Study Notes

*A topic-by-topic reference for CAPS Information Technology theory.*

These notes follow the CAPS topic order: System Technologies → Communication and Network Technologies → Data and Information Management → Solution Development → Social Implications and Integrated Topics. Each topic is explained in full so the notes can be used as standalone study material for any examination.

---

# SECTION 1: SYSTEM TECHNOLOGIES

## 1.1 The Motherboard

The **motherboard** is the main printed circuit board inside the computer. It is the foundation that everything else connects to. Two of its most important roles are:

* It physically holds and connects the major components of the computer — the CPU, the RAM modules, the storage drives, the graphics card, the power supply and all the peripheral devices plug into the motherboard.
* It provides the **buses** (the electrical pathways) that allow data to be transferred between these components. The CPU, RAM and storage devices cannot send data to each other without the motherboard's buses.

### Buses

A **bus** is a set of electrical wires (or tracks on the motherboard) that carry data between components. Without buses, the CPU would have no way to fetch instructions from RAM or send results to storage. The width and speed of a bus has a direct impact on the overall speed of the computer — a faster bus moves more data per second.

### Expansion cards

An **expansion card** (also called an "add-in card") is a printed circuit board that can be plugged into a slot on the motherboard to add or upgrade a specific capability of the computer. Common examples include a dedicated graphics card (GPU), a sound card, a network card (NIC) and a Wi-Fi card.

The purpose of an expansion card is to give the computer functionality that the motherboard does not provide on its own, or to *replace* a built-in component with a much more powerful one (for example, replacing weak integrated graphics with a powerful gaming GPU).

### Modular design

**Modular design** means that a computer is built out of standardised, separate, replaceable parts (modules) — the CPU, the RAM, the storage drive, the graphics card, the power supply, and so on. Each part fits into a standard socket or slot on the motherboard.

Advantages of modular design for maintenance include:

* **Easy repair** — if one component fails, only that component needs to be replaced. The whole computer does not have to be thrown away.
* **Easy upgrades** — components can be swapped out for faster or larger versions (e.g. more RAM, a bigger SSD, a better GPU) without replacing the whole machine. This extends the useful life of the computer and saves money.

## 1.2 Memory

### Volatile vs non-volatile memory

* **Volatile memory** loses its contents as soon as the power is switched off. RAM and cache memory are volatile.
* **Non-volatile memory** keeps its contents even with no power. Examples include SSDs, HDDs, USB flash drives, and ROM (where the BIOS is stored).

### RAM (Random Access Memory)

RAM is the computer's **main working memory**. While a program is running, both the program code and the data it is working on must be loaded into RAM so the CPU can access them quickly. RAM is **volatile** — when the computer is switched off, everything in RAM is lost. That is why work must be saved to a non-volatile drive before shutting down.

### Cache memory

**Cache memory** is a very small, very fast type of memory built directly into (or right next to) the CPU. Its purpose is to **speed up access to frequently used data and instructions**.

When the CPU needs data, RAM is too slow to keep up with the CPU's speed. The cache acts as a "holding zone" between the CPU and RAM — recently used and frequently used data is kept in the cache where the CPU can grab it almost instantly, instead of having to fetch it from RAM every time. This dramatically reduces "wait time" for the CPU and makes the computer feel faster.

### Cache memory vs RAM

| Aspect | Cache memory | RAM |
|---|---|---|
| **Location** | Built into or directly next to the CPU | Plugs into slots on the motherboard, further from the CPU |
| **Speed** | Much faster — closest in speed to the CPU itself | Slower than cache, but much faster than storage |
| **Size** | Very small (measured in MB) | Much larger (measured in GB) |
| **Cost** | Very expensive per MB | Relatively affordable per GB |
| **Purpose** | Hold the most frequently used data for the CPU | Hold all currently running programs and their data |

### Virtual memory

**Virtual memory** is a technique used by the operating system to use a portion of the storage device (SSD or HDD) as if it were extra RAM. When the actual RAM is full and a program needs more memory, the operating system moves blocks of data that are not currently being used from RAM to a special file on the drive (called the "swap file" or "page file"). When that data is needed again, it is moved back into RAM.

Virtual memory allows the computer to run more programs at the same time than the physical RAM would normally allow. However, because the storage drive is much slower than RAM, heavy use of virtual memory will slow the system down — this is sometimes called "thrashing".

## 1.3 BIOS

The **BIOS (Basic Input/Output System)** is a small program built into a chip on the motherboard. It is the very first piece of software that runs when the computer is switched on, before the operating system even starts.

The purpose of the BIOS during start-up is to:

* **Perform the POST (Power-On Self Test)** — check that essential hardware (CPU, RAM, keyboard, storage) is present and working correctly.
* **Initialise the hardware** — set up the basic settings so the CPU and motherboard can communicate with the hardware.
* **Locate and load the operating system** — find the bootable storage device, load the start-up code, and hand control over to the operating system.

The BIOS is stored on **non-volatile memory** (specifically a flash ROM chip) because its instructions must still be there even after the computer has been switched off and unplugged. If the BIOS were stored on volatile memory like RAM, it would be wiped out every time the power was disconnected and the computer would never be able to start up again.

## 1.4 Storage

### SSD vs HDD

A **HDD (Hard Disk Drive)** stores data on spinning magnetic platters, while an **SSD (Solid State Drive)** stores data on flash memory chips with no moving parts.

Advantages of an SSD over an HDD:

* **Much faster** — boot times, file copying and program loading happen in seconds rather than minutes. This is because there is no need to wait for a disk to spin to the right position.
* **More durable** — SSDs have no moving parts, so they survive being knocked, bumped or dropped (important for laptops).
* **Silent** — no spinning motor, no clicking read/write head.
* **Less power-hungry** — extends laptop battery life and reduces heat.
* **Smaller and lighter** — allows for thinner laptops.

The main disadvantage is that SSDs are more expensive per gigabyte than HDDs, so a typical computer might use an SSD for the operating system and programs (for speed) and a larger HDD for bulk storage of files.

## 1.5 Virtualisation and Virtual Machines

### Definition

**Virtualisation** is the creation of a virtual (software-based) version of something physical. In computing, it most often refers to creating a virtual computer — called a **virtual machine (VM)** — that runs as a program on top of an existing physical computer.

A virtual machine behaves as if it were a separate physical computer with its own CPU, RAM, storage and network connection. It runs its own operating system and its own application software. The physical computer that hosts a VM is called the **host**, and the VM is called the **guest**.

Examples of virtualisation software include VirtualBox (free), VMware Workstation and Parallels.

### Why use a virtual machine?

Common reasons include:

* **Testing software safely** — if a developer wants to test a program that *might* contain a virus, they can run it inside a virtual machine. If the program causes damage, only the VM is harmed. The host operating system and all the user's files stay safe. The infected VM can be deleted and a fresh one created.
* **Trying out a different operating system** — a Windows user can install Ubuntu Linux in a VM to learn how to use it, without removing Windows from their computer.
* **Software development and testing** — a developer can test their app on Windows 10, Windows 11, Linux and various Android versions all on one physical machine.
* **Running old software** — software that only runs on older operating systems can be kept alive inside a VM long after the host has been upgraded.

### Server virtualisation

In a corporate or data-centre environment, **server virtualisation** allows a single powerful physical server to run many virtual servers at the same time. A company that used to need ten separate physical servers can instead buy one large server and run ten virtual machines on it.

This is more cost-effective for two main reasons:

* **Hardware savings** — buying one big server is cheaper than buying ten smaller ones, and it uses far less electricity, cooling and physical space.
* **Better resource utilisation** — most physical servers sit at 10–20% CPU usage most of the day, wasting capacity. Virtualisation lets many virtual servers share that capacity efficiently, so the hardware that has been bought is actually used.

## 1.6 Server Operating Systems

A **server operating system** is a special operating system designed to run on a server — a computer whose main job is to provide services to other computers (called "clients") on a network.

Functions of a server operating system include:

* **User management** — creating, managing and authenticating user accounts; controlling who is allowed to log in.
* **Resource management** — managing shared resources like printers, storage and applications, and controlling who is allowed to use them.
* **File storage and sharing** — providing a central place where users save files, with permissions controlling who can read or edit them.
* **Security** — enforcing password policies, encrypting connections, and protecting the server from unauthorised access.
* **Hosting services** — running services like email servers, web servers, database servers and backup services.

## 1.7 Cloud vs Locally Installed Software

Modern users often have a choice between **cloud-based software** (e.g. Google Docs, Microsoft 365 online, Canva) and **locally installed software** (programs installed on the actual computer).

**Cloud-based software**:

* Runs on a remote server and is used through a web browser.
* Requires a working internet connection.
* Files are saved online and can be accessed from any device.
* Less demanding on the computer's hardware — even an older laptop can run it.
* Is usually paid for on a subscription basis.

**Locally installed software**:

* Runs directly on the computer's own hardware.
* Works without an internet connection.
* Files are saved on the computer's own drive (unless deliberately uploaded).
* Needs the computer to meet the software's system requirements.
* Is usually paid for once (a perpetual licence) or comes with a one-off purchase.

**Recommendation for a learner doing schoolwork, research and general office tasks**:
Cloud-based software is generally a good choice because schoolwork rarely needs heavy software, the cost can be lower (free options like Google Docs exist), files are backed up automatically and can be accessed from school, home or a mobile phone, and the computer does not need to be top-of-the-range. The trade-off is that an internet connection is required.

---

# SECTION 2: COMMUNICATION AND NETWORK TECHNOLOGIES

## 2.1 Bandwidth and Data Transmission

**Bandwidth** is the maximum amount of data that can be transferred over a network connection in a fixed period of time. It is measured in **bits per second** — typically Mbps (megabits per second) or Gbps (gigabits per second). Think of bandwidth as the *width* of the pipe: a wider pipe lets more water through per second.

**Data transmission** is the actual process of moving data from one device to another over a network. The data is broken up into small **packets**, each packet is addressed, the packets travel separately across the network, and they are reassembled at the destination. Data transmission depends on cables (or wireless signals), networking devices like switches and routers, and a shared set of rules called protocols.

## 2.2 Wired vs Wireless Networks

### Wireless connections

A **wireless connection** uses radio waves (most often **Wi-Fi**) to connect devices without cables.

**Advantage**: Mobility and convenience — devices can connect from anywhere within the signal range without the need to run cables. Adding a new device is as simple as entering the password.

**Disadvantage**: Wireless signals are typically slower and less stable than a wired connection, the signal can be blocked or weakened by walls, and a wireless network is much easier for an outsider to intercept or attack than a cable that is physically inside the building.

### Recommending wired, wireless, or a combination

For most schools and offices, a **combination of wired and wireless networking** is the best choice. Desktop computers, servers and printers (which never move) are wired for speed and reliability. Laptops, tablets and phones (which do move) connect over Wi-Fi for convenience. This combines the strengths of both technologies.

## 2.3 Network Hardware

### Router vs Access Point

These two devices are often confused but do different jobs:

* A **router** is the device that connects two different networks and directs traffic between them. The most common job of a home/school router is to connect the internal network (LAN) to the internet (WAN). It looks at the destination IP address of each packet and forwards it correctly.
* A **wireless access point (WAP)** is a device that allows wireless devices to connect to a wired network. It converts Wi-Fi signals into wired signals (and vice versa) so that a laptop or phone can join the network without a cable.

Many home "routers" are actually combined devices — they are a router, a switch and a wireless access point all in one box.

## 2.4 Protocols

A **protocol** is a set of rules that governs how data is formatted, transmitted and received over a network. Devices can only communicate successfully if they both use the same protocol — in the same way that a phone conversation only works if both people speak the same language.

The purpose of protocols is to:

* **Standardise communication** so that devices from different manufacturers can talk to each other.
* **Ensure error-free transmission** by including rules for checking and re-sending lost data.
* **Define the meaning of the data** so that the receiving device knows what to do with it (e.g. "this is an email" vs "this is a web page").

### Common protocols

| Protocol | Used for |
|---|---|
| **HTTP** | Browsing web pages (unencrypted) |
| **HTTPS** | Browsing web pages (encrypted, secure) |
| **SMTP** | **Sending** email |
| **POP3** | **Receiving** email from a mail server (downloads it to one device) |
| **IMAP** | **Receiving** email from a mail server (keeps it on the server so multiple devices can see the same inbox) |
| **FTP** | Transferring files between computers |
| **TCP/IP** | The fundamental protocol that the internet itself uses |

A common exam trick is to mix up **SMTP** (Send Mail Transfer Protocol) for **sending** and **POP3/IMAP** for **receiving** email.

## 2.5 Mobile Technology and Wireless Communication

**Mobile technology** (smartphones, tablets, laptops with cellular data) improves communication between staff who work from different locations because:

* Staff can send and receive emails, instant messages and files **from anywhere**, not just from the office.
* **Video calls and online meetings** allow remote staff to attend the same meeting as office staff.
* Cloud-based apps on a phone let staff **update shared documents in real time** from a coffee shop, a client's office or a hotel room.
* Staff can be **contacted immediately** rather than waiting until they are back at a desk.

## 2.6 Wireless Network Security

A wireless network is more exposed to attack than a wired one because the signal travels through the air and can be picked up by anyone in range. Important security measures include:

* **A strong wireless password (WPA3 encryption)** — ensures that only people who know the password can connect to the Wi-Fi, and that data travelling over the air is encrypted. Without this, anyone in range can join the network and read traffic.
* **Changing the default router/admin password** — every router ships with a default admin password (often printed in the manual). If this is not changed, an attacker who connects can simply log into the router and take over the whole network.
* **Hiding the SSID (network name)** so casual outsiders cannot easily see that the network exists.
* **MAC address filtering** to allow only known devices on the network.
* **Keeping the router firmware updated** to fix newly discovered security flaws.

### Why a strong password alone is not enough

Even a very strong password can be:

* **Stolen by phishing** — a fake email tricks the user into typing their password into a fake login page.
* **Stolen by malware/keyloggers** that record what the user types.
* **Leaked in a data breach** at the company that owns the website.
* **Cracked through brute-force attacks** if given enough time.

That is why important accounts need **multi-factor authentication (MFA)** — a second proof of identity (an SMS code, an authentication app, a fingerprint) on top of the password.

## 2.7 Cloud Storage

**Cloud storage** is online storage provided by a third party (Google Drive, OneDrive, Dropbox). For staff who work from different locations, the main advantage is that **files are accessible from any device with internet access**. A document edited at the office in the morning can be opened on a phone at a client meeting that afternoon, with no need to remember to copy it onto a USB drive.

Other advantages: automatic backup, easy file sharing with colleagues, version history, and no need to invest in expensive servers in the office.

## 2.8 Email vs Instant Messaging

For **quick day-to-day communication** between staff, **instant messaging** is more suitable than email. IM messages are short, arrive immediately, get an immediate reply, and are good for quick questions and decisions. Email is better for longer, more formal messages, for messages with attachments, and for messages that need to be kept as a record. Most workplaces use both — IM for quick chat and email for formal correspondence.

---

*Continues with Data Management, Solution Development, and Social Implications…*

# SECTION 3: DATA AND INFORMATION MANAGEMENT

## 3.1 Database Management Systems (DBMS)

A **Database Management System (DBMS)** is a software package that allows users to **create, store, organise, retrieve, update and manage data in a database**. It sits between the user (or the user's application) and the actual database file, hiding the complicated details of how the data is physically stored and giving the user a simple way to work with the data.

### What a DBMS allows the user to do

A DBMS allows the user to:

* **Create** databases, tables and the structure (fields) inside them.
* **Add, edit and delete records** in the tables.
* **Search and sort** records to find specific information quickly.
* **Build queries** that combine data from several tables to answer business questions.
* **Control who has access** to which parts of the database (user permissions).
* **Back up and restore** the database to prevent data loss.
* **Enforce data integrity** by validating data before it is stored.

### Categories of DBMS

There are two main categories:

* **Flat-file DBMS** — stores all the data in a single table. Microsoft Excel used as a database is the typical example. It is simple to set up and easy for one user to understand, but it cannot handle large amounts of related data and tends to suffer from a lot of **data redundancy** (the same information repeated in many rows). Flat-file systems are only suitable for small, simple jobs.
* **Relational DBMS (RDBMS)** — stores the data in multiple linked tables, with the tables connected to each other through **keys** (primary keys and foreign keys). Examples include Microsoft Access, MySQL, PostgreSQL and Oracle. A relational DBMS avoids duplicating data, enforces strong data integrity, supports many users at the same time, and can be queried in powerful ways using SQL.

**Choosing between the two**: A **flat-file** system is suitable only when the data is small, simple, and concerns one kind of entity that is not linked to anything else (e.g. a single list of contacts). For almost any real application — a library catalogue, a stock-control system, a school administration system, a hospital record system — a **relational DBMS** is the right choice. As soon as the data involves more than one kind of entity (books *and* members *and* loans, or products *and* customers *and* orders), a relational system avoids the duplication that a flat-file system would force, supports proper queries that link the tables, and keeps the data consistent.

## 3.2 Keys in a Database

### Primary key

A **primary key** is a field (or combination of fields) in a database table whose value **uniquely identifies each record** in that table. No two records may have the same primary key value, and the primary key may not be empty (null).

Examples:

* In a learner table, the learner number is a good primary key.
* In a book table, the ISBN number is a good primary key.
* In a member table, the member number (or ID number) is a good primary key.

The primary key gives every record a unique "name" that the DBMS can use to find that exact record instantly, and that other tables can refer to.

**Important**: a primary key **may not contain duplicate values**. If duplicates were allowed, the field could not be used to uniquely identify a record.

## 3.3 Data Validation

**Data validation** is the process of checking that the data entered into a system is **reasonable, complete and in the correct format** *before* it is stored. Validation cannot tell whether the data is *correct* (only the user knows that), but it can stop nonsense data from being entered.

Examples of data validation:

* **Range check** — making sure a learner's mark is between 0 and 100.
* **Length check** — making sure a South African ID number is exactly 13 digits.
* **Type check** — making sure a number field does not contain letters.
* **Presence check** — making sure a compulsory field has been filled in.
* **Format check** — making sure an email address contains an `@` symbol.

The opposite of validation is **verification**, which is checking that the data captured matches the original source (e.g. double-entry, where the data is typed in twice and the system checks that the two entries match).

## 3.4 Data Mining

**Data mining** is the process of analysing very large sets of data to **discover useful patterns, relationships and trends** that would not be obvious if the data were looked at by hand. Businesses use data mining to learn things like which products are often bought together, which customers are likely to leave, or when sales of certain items peak during the year.

## 3.5 Database Roles and Careers

A real-world database project is not run by one person — it has several specialist roles:

* **Database Administrator (DBA)** — responsible for the **day-to-day operation and security** of the database. The DBA installs the DBMS, manages user accounts and permissions, schedules backups, monitors performance, and restores the database if something goes wrong. They are the technical "owner" of the live database.
* **Database Analyst** — responsible for the **design and analysis** of the database. The analyst studies what the organisation needs, designs the structure of the tables (the data model), decides which fields go in which table, and works out how the tables relate to each other. They focus on *what* the database should look like, not on the running of it.
* **Database Programmer** — responsible for **writing the code** that interacts with the database. The programmer writes the SQL queries, the stored procedures and the application code that lets users add, edit and view the data through a friendly interface.

The three roles overlap in some organisations, but in larger projects they are very distinct: the analyst designs it, the programmer builds it, and the DBA runs it.

---

# SECTION 4: SOLUTION DEVELOPMENT

## 4.1 Modular Programming — Procedures and Functions

Instead of writing one enormous block of code, a program should be broken up into smaller, named pieces called **methods**. In Delphi (and Pascal) there are two kinds of methods:

* A **procedure** is a named block of code that performs a task but **does not return a value**. You call a procedure to make something happen — for example, `ClearForm`, `DisplayMenu`, `SaveToFile`.
* A **function** is a named block of code that performs a task and **returns a single value** to the place that called it. You call a function to get something back — for example, `CalculateArea(r)` returns a real number, `IsAdult(age)` returns a Boolean.

### Why use procedures and functions (modular programming)?

* **Readability** — a program made of short, well-named methods is much easier to read and understand than a single 500-line block.
* **Testing** — each method can be tested on its own, in isolation, which makes finding bugs much easier.
* **Reuse** — a method can be called from many different places in the program (and even from other programs), so the code is written once but used many times.
* **Maintenance** — if the way something is done needs to change, the change is made in one place (inside the method) and automatically applies everywhere that method is called.

## 4.2 Local vs Global Variables

The **scope** of a variable refers to which parts of the program can see and use it.

* A **local variable** is declared inside a procedure or function. It exists only while that procedure runs and is invisible to the rest of the program. Two different procedures can have local variables with the same name without interfering with each other.
* A **global variable** is declared outside of all the procedures (usually near the top of the unit) and is visible to *every* procedure and function in the program. Any part of the program can read or change it.

Local variables are preferred because they make the program more predictable: a procedure's behaviour cannot be broken by something elsewhere in the program accidentally changing one of its variables. Global variables should be used sparingly.

## 4.3 Algorithms Revisited

An **algorithm** is a step-by-step set of instructions for solving a problem. Two essential properties that a well-designed algorithm must have are:

* **Finiteness** — the algorithm must always end after a finite number of steps. An algorithm must never get stuck in an endless loop.
* **Definiteness** — every step must be precisely and unambiguously defined. There must be no doubt about what to do at any step.

(Other properties include: it must have clear inputs, it must produce clear outputs, and every step must be effectively executable.)

## 4.4 Loops

A **loop** is a control structure that repeats a block of code more than once. The three main kinds of loop used in Delphi are:

* **for loop** — used when the number of repetitions is **known in advance**. For example, "do this exactly 5 times" or "do this for each item in a list of 100 names".
* **while…do loop** — a *pre-test* loop. It checks the condition **before** the loop body runs. If the condition is false at the start, the body never runs at all. Example: `while (count < 10) do …`
* **repeat…until loop** — a *post-test* loop. It runs the body first, **then** checks the condition. The body always runs **at least once**, regardless of the condition. Example: `repeat … until iAnswer = 'Y'`

### `while…do` vs `repeat…until`

The key difference is **when the condition is checked**:

| Aspect | `while…do` | `repeat…until` |
|---|---|---|
| When is the condition checked? | Before the loop body runs (pre-test) | After the loop body runs (post-test) |
| Minimum number of times the body runs | Zero | One |
| Loop continues while the condition is… | True | False (i.e. loops *until* the condition becomes true) |
| Body needs `begin…end`? | Yes, if more than one statement | No — the `repeat…until` itself acts as the block |

### Choosing the right loop

For a task like "display a message exactly 5 times", a **for loop** is the most suitable, because the number of repetitions is known in advance:

```pascal
for i := 1 to 5 do
   ShowMessage('Hello');
```

If the loop must continue until the user types a specific value (where you don't know how many tries it will take), `while…do` or `repeat…until` is more appropriate.

## 4.5 Validation in Programming

In a program, **validation** is checking that the user's input is acceptable before the program tries to use it. If the program asks the user to enter the number of books borrowed, the most appropriate validation is a **range check**, for example: "the value must be a whole number greater than or equal to 0 and less than or equal to some sensible maximum (e.g. 50)".

This stops the user from entering nonsense like `-3`, `1000` or `abc`. The program either rejects the input and asks again, or displays an error message.

## 4.6 Text Files in Delphi

A **text file** is a way to store information permanently on the disk so that the program can read it later, even after the program has been closed and re-opened. Text files store data as plain readable text — they can be opened in Notepad.

To work with a text file in Delphi, you declare a variable of type `TextFile`:

```pascal
var
   tfReport : TextFile;
   sFileName : String;
   sLine : String;
```

### The four key commands

| Step | Delphi command | Purpose |
|---|---|---|
| **1. Link** the variable to the actual file on disk | `AssignFile(tfReport, sFileName);` | Tells the program which physical file the variable refers to. Does not open the file yet. |
| **2a. Open for reading** | `Reset(tfReport);` | Opens an *existing* file so that data can be read from it. The file must already exist. |
| **2b. Open for writing (new)** | `Rewrite(tfReport);` | Creates a new (empty) file, or overwrites any existing file of the same name. |
| **2c. Open for appending** | `Append(tfReport);` | Opens an existing file and positions the pointer at the end, so that new data is added to what is already there. |
| **3a. Write one line** | `WriteLn(tfReport, sLine);` | Writes the contents of `sLine` to the file, followed by a new-line character. |
| **3b. Read one line** | `ReadLn(tfReport, sLine);` | Reads the next line from the file into `sLine`. |
| **4. Close** | `CloseFile(tfReport);` | Flushes any buffered data to disk and releases the file so other programs can use it. |

### Why `CloseFile` is essential

Forgetting to call `CloseFile` is a common bug with serious consequences:

* **Data loss** — Delphi buffers data in memory before actually writing it to disk. If the file is not closed, the last writes may never reach the disk and will be lost when the program ends.
* **The file remains locked** — other programs (and even the same program) may not be able to open the file again until it is closed.
* **Corruption** — if the program crashes with the file still open, the file may be left in an inconsistent or corrupted state.

**Example**: A program writes a report to a text file using `WriteLn`, but the programmer forgets to call `CloseFile`. When the user later opens the file in Notepad, the last several entries are missing because they were still sitting in the buffer in memory when the program ended.

### Text file vs in-memory storage — recommendation

For any system that must keep data between sessions, a **text file (or better, a database) is the right choice**. Keeping data only in memory means everything is lost the moment the program is closed. Persistent storage is essential whenever the user expects to come back to their work later.

## 4.7 Compiler

A **compiler** is a translator program. It **converts source code (the code written by the programmer in a language like Delphi) into machine code (the binary instructions the CPU can execute directly) before the program is run**. The compiler produces an executable file (e.g. an `.exe`). Once compiled, the program runs without needing the compiler.

A compiler is different from an **interpreter**, which translates and executes source code one line at a time, every time the program is run.

---

# SECTION 5: SOCIAL IMPLICATIONS AND INTEGRATED TOPICS

## 5.1 Social Networking Sites

A **social networking site** is a website or app that allows users to **create a personal profile, connect with other users (friends, followers, contacts), and share content** such as posts, photos, videos and messages. Examples include Facebook, Instagram, X (Twitter), TikTok and LinkedIn.

### Benefits for organisations

* **Wide reach** — events and announcements can be seen by many community members at no advertising cost.
* **Two-way communication** — followers can comment, ask questions, and give feedback instantly.
* **Targeting** — modern social platforms allow posts to be targeted by location, age and interest, so the right people see the right message.
* **Building community** — photos and videos of past activities make new followers feel that the organisation is active and welcoming.

### Risks of oversharing on social media

Sharing personal information publicly (location, daily routines, valuable possessions) exposes a person to:

* **Burglary and theft** — criminals see when you are not at home and where the expensive equipment is.
* **Stalking and harassment** — strangers can build a detailed profile of where you go and when.
* **Identity theft** — small pieces of personal information (school name, pet's name, date of birth) can be combined to guess passwords or answer security questions.
* **Social engineering and phishing** — an attacker who knows what you do and what you own can craft a very convincing scam targeting you specifically.

## 5.2 Social Engineering

**Social engineering** is the use of **psychological manipulation** to trick people into revealing confidential information (passwords, ID numbers, banking details) or doing something they would not normally do (like clicking a malicious link). Instead of "hacking" the computer, the attacker "hacks" the *human*.

Examples include phishing emails, fake phone calls pretending to be IT support, and scammers pretending to be from a bank.

## 5.3 Online Safety — Practical Measures

When an organisation or individual has limited time and money, the two most effective measures to reduce online risk are:

* **Enable multi-factor authentication (MFA)** on every important account. Even if a password is stolen, the attacker still cannot get in.
* **Educate users** about phishing and social engineering. The user is the weakest link — a well-trained user will not click suspicious links, will check the sender of an email, and will report anything unusual.

Other useful measures include strong unique passwords (using a password manager), keeping software up to date, using an antivirus, and not oversharing personal information online.

## 5.4 Online Communication Tools

**Online communication tools** (email, video conferencing, instant messaging, collaborative documents) allow staff to work effectively even when they are not in the same building.

Advantages include:

* **Real-time collaboration** — multiple people can edit the same document at the same time and see each other's changes immediately.
* **Cost savings** — meetings can be held over Zoom or Teams instead of flying staff to a central office.
* **Faster decisions** — a quick chat or video call replaces a long email thread.
* **Written record** — chats and emails are searchable later, unlike spoken phone conversations.

## 5.5 E-Commerce

**E-commerce (electronic commerce)** is the buying and selling of goods and services over the internet. Customers visit an online store, choose products, pay online (by card, EFT, mobile payment) and have the goods delivered or downloaded.

### Advantages and disadvantages for the customer

| Advantages | Disadvantages |
|---|---|
| Shop from anywhere, at any time of day | Cannot physically see or try the product before buying |
| Easy to compare prices between many stores | Must wait for delivery |
| Wider product selection than any local shop | Risk of online fraud, fake stores and credit card theft |
| Customer reviews help decision-making | Delivery costs may add to the price |

### Advantages and disadvantages for the business

| Advantages | Disadvantages |
|---|---|
| Sell to customers anywhere in the country (or world), 24/7 | Setup and maintenance of the website and payment system costs money |
| No need for a physical shop, so lower running costs | Strong competition from other online sellers — easy for customers to switch |
| Easy to gather data on customer preferences | Vulnerable to hacking and online fraud |
| Easy to run promotions and update the catalogue | Reliable delivery (couriers) must be arranged |

## 5.6 Cloud Storage for Organisations

For an organisation deciding whether to use **cloud storage** instead of a single office computer:

Cloud storage is generally a good idea because files become accessible from anywhere, multiple staff can access shared documents at the same time, the cloud provider handles backups automatically, and a single office computer breaking down does not mean all the files are lost. The trade-off is that a working internet connection becomes essential, and the organisation must trust the cloud provider with its data.

## 5.7 Impact of Social Media on Learners

Social media has both positive and negative effects on learners. On the positive side, learners can join study groups, share notes, watch educational content, and stay connected with classmates. On the negative side, social media is a major source of **distraction** during study time, can lead to **cyberbullying**, can damage self-esteem through unrealistic comparisons, and excessive use is linked to anxiety and reduced sleep. Schools, parents and other organisations that support learners should encourage healthy, purposeful use of social media — not a complete ban, but boundaries and awareness.

---

*End of Grade 11 Theory Notes*
