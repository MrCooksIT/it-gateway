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

## 1.8 BIOS, UEFI, CMOS and POST

| Term | Meaning |
|---|---|
| **BIOS** | Older start-up firmware on the motherboard: text-based, keyboard only, limited support for large drives |
| **UEFI** | The modern replacement for BIOS: graphical interface with mouse support, faster start-up, support for large drives, and Secure Boot |
| **CMOS** | Memory that stores the BIOS/UEFI **settings** (date, time, boot order), kept alive by a small battery |
| **POST** | Power-On Self-Test: checks that the essential hardware (CPU, RAM, keyboard, storage) is present and working **before** the operating system loads. Errors are reported with beeps or a message |

**Boot process:** power on → firmware starts → POST → settings read from CMOS → bootloader found on the boot device → operating system loaded into RAM.

## 1.9 Cache levels and caching

Cache is very fast memory on or close to the CPU that keeps the instructions and data used most recently and most often, so that the CPU does not have to wait for slower RAM.

| Level | Size | Speed | Location |
|---|---|---|---|
| **L1** | Smallest | Fastest | Inside each core |
| **L2** | Larger | Slower than L1 | Per core |
| **L3** | Largest | Slowest of the three (still faster than RAM) | Shared by all cores |

**Caching** is the general idea of keeping a copy of something in a faster place: **disk caching** keeps recently read data from a drive in RAM; **web caching** keeps copies of web pages and images on your device so that a site loads faster the next time.

## 1.10 Types of operating systems

| Type | Description | Example |
|---|---|---|
| **Single-user (stand-alone)** | One user at a time on one computer | Windows on a home laptop |
| **Multi-user / network (server)** | Many users share the computer's resources at the same time; manages accounts and permissions | Windows Server, Linux server |
| **Real-time (RTOS)** | Must respond to input within a guaranteed, very short time | Car airbag controller, medical monitor, factory robot |
| **Embedded** | A small, dedicated OS built into a device that does one job | Microwave, smart TV, router |
| **Mobile** | Designed for touchscreens, batteries and sensors | Android, iOS |

Operating systems also differ in **cost** (proprietary vs open source), **size**, the **hardware** they need and the **platform** they run on.

## 1.11 Processing techniques

| Technique | Meaning |
|---|---|
| **Multitasking** | The OS runs **several programs** seemingly at once by switching the CPU between them very quickly |
| **Multithreading** | **One program** is divided into threads that run at the same time (e.g. spell-checking while you type) |
| **Multiprocessing** | **More than one core or CPU** is used, so tasks really run at the same time |

## 1.12 Compilers and interpreters

| | Compiler | Interpreter |
|---|---|---|
| How it translates | The **whole program** at once, before it runs | **One line at a time**, while the program runs |
| Result | A separate executable file (`.exe`) | No executable; the source code is needed every time |
| Speed of the program | Fast | Slower |
| Errors | All syntax errors reported after compiling | Stops at the first error it reaches |
| Example | Delphi, C++ | Python, JavaScript |

A **high-level language** (Delphi, Python) is close to English, easy to read and debug, and can be translated for different processors. A **low-level language** (machine code, assembly) is close to what the CPU executes: fast, but hard to write and specific to one type of processor.

## 1.13 Computer performance

| Component | Effect on performance |
|---|---|
| **CPU** | Higher clock speed and more cores process more instructions per second |
| **RAM** | More RAM means more programs and data stay in fast memory, so less **virtual memory** (slow storage used as if it were RAM) is needed |
| **Cache** | More cache means fewer waits for RAM |
| **Storage** | An SSD loads the OS, programs and files far faster than an HDD |
| **GPU** | A dedicated graphics card takes graphics work off the CPU (games, video editing, 3D) |

A **bottleneck** is the slowest component that holds the rest back. Upgrade that one first.

A **device driver** is the software that lets the operating system communicate with a hardware device. A new device that does not work usually needs the correct driver installed or updated.

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

A common exam trick is to mix up **SMTP** (Simple Mail Transfer Protocol) for **sending** and **POP3/IMAP** for **receiving** email.

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



## 2.9 Internet, intranet and extranet

| | Who can use it | Example |
|---|---|---|
| **Internet** | Anyone; the public worldwide network | Public websites |
| **Intranet** | Only people **inside** the organisation; a private network that uses Internet technologies (web pages, e-mail) | A staff portal with timetables and policies |
| **Extranet** | An intranet that gives **limited access to authorised outsiders** such as suppliers or clients, with a login | A supplier checks stock levels on a company's system |

A **VPN (Virtual Private Network)** creates a private, **encrypted tunnel** over the public Internet. A user at home or in another city connects as if they were on the organisation's own LAN, and data that is intercepted cannot be read.

## 2.10 Wireless technologies and data transmission

| Technology | Range | Use |
|---|---|---|
| **Bluetooth** | About 10 m | Connecting nearby devices (PAN) |
| **Wi-Fi** | Tens of metres | Wireless LAN in a home, school or office |
| **WiMAX** | Many kilometres from a tower | Fixed wireless broadband where cables are not available |
| **LTE / 4G** | Cellular coverage | Mobile broadband |
| **5G** | Cellular coverage (shorter range per tower) | Much higher speed, **lower latency**, and many more devices per area than 4G |

| Term | Meaning |
|---|---|
| **Bandwidth** | The amount of data that can be transmitted per second (Mbps) |
| **Latency** | The **delay** before data arrives. High latency causes lag in video calls and online games |
| **Throttling** | The ISP deliberately slows a user's connection, e.g. after a data limit is reached |
| **Shaping** | The ISP gives some types of traffic (e.g. browsing) priority over others (e.g. file sharing) |
| **Congestion** | Too many users at once, so everyone's connection slows down |

A **wireless access point** or range extender is added to bring Wi-Fi coverage to areas the router does not reach.

## 2.11 VoIP and location-based computing

**VoIP (Voice over Internet Protocol)** carries voice calls over the Internet instead of the telephone network (WhatsApp calls, Teams, Zoom). It is cheap or free, especially for long-distance calls, and can include video; call quality depends on bandwidth and latency, and it does not work without power and a connection.

**Location-based computing** uses the position of a device to provide a service: navigation, finding the nearest shop, tracking deliveries, tagging photos, location-based advertising.

- **GPS** uses satellite signals to work out a device's position. The receiver needs power and a clear view of the sky.
- **RFID** uses a small tag that sends its ID number when a reader is held close to it. A passive tag has no battery and **cannot report its location**; it only identifies itself to a nearby scanner.

**Social implications:** location data shows where a person lives, works and travels, and when they are away. It can be used for stalking, burglary or profiling, so it needs consent and protection.

## 2.12 The Internet and WWW (Term 4)

**Evolution of the Internet:** from static, read-only pages (Web 1.0), to interactive pages where users create content (Web 2.0: social media, blogs, wikis), to connected "things" and intelligent services (the **Internet of Things**, AI assistants).

**Multimedia:**

| | Downloading | Streaming |
|---|---|---|
| How | The whole file is saved on the device first | The media plays **while it is being received**; it is not stored permanently |
| Advantage | Can be played later without a connection | Starts almost immediately; uses no storage space |
| Disadvantage | Waiting time; uses storage | Needs a fast, stable connection; uses data every time |

**Types of websites:** e-commerce (buying and selling), social networking, blogs and video sharing, wikis, news and information, web applications, crowdfunding, search engines.

**Security services:**

- **SSL/TLS** encrypts the data sent between a browser and a web server. A site that uses it shows `https` and a padlock.
- A **digital certificate** is issued by a trusted **certificate authority**. It proves that the website really belongs to the organisation it claims to be, and it enables the encrypted connection.
- **Multi-factor authentication (MFA)** asks for a second proof of identity, such as a one-time PIN (OTP), as well as the password.

## 2.13 Threats and remedies

| Threat | What it does |
|---|---|
| **Virus** | Attaches itself to a file or program and spreads when that file is opened |
| **Worm** | Spreads by itself across a network without any user action |
| **Trojan** | Pretends to be a useful program while doing harm in the background |
| **Ransomware** | Encrypts the victim's files and demands payment for the key |
| **Spyware** | Secretly records what the user does (e.g. keystrokes and passwords) |
| **Phishing** | Fake messages that trick users into giving personal details |
| **DoS attack** | Floods a server with requests so that real users cannot reach it |

Threats can also be **physical** (theft, fire, power failure) or **hardware** failures (a drive that dies).

**Remedies:** regular **backups** kept off-site or in the cloud; up-to-date **antivirus**; a **firewall**; installing **updates**; strong passwords and MFA; **encryption**; limiting user permissions; a UPS for power failures; and training users not to open unknown attachments or links.

---

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

Validation is not the same as **verification**, which is checking that the data captured matches the original source (e.g. double-entry, where the data is typed in twice and the system checks that the two entries match).

## 3.4 Data Mining

**Data mining** is the process of analysing very large sets of data to **discover useful patterns, relationships and trends** that would not be obvious if the data were looked at by hand. Businesses use data mining to learn things like which products are often bought together, which customers are likely to leave, or when sales of certain items peak during the year.

## 3.5 Database Roles and Careers

A real-world database project is not run by one person — it has several specialist roles:

* **Database Administrator (DBA)** — responsible for the **day-to-day operation and security** of the database. The DBA installs the DBMS, manages user accounts and permissions, schedules backups, monitors performance, and restores the database if something goes wrong. They are the technical "owner" of the live database.
* **Database Analyst** — responsible for the **design and analysis** of the database. The analyst studies what the organisation needs, designs the structure of the tables (the data model), decides which fields go in which table, and works out how the tables relate to each other. They focus on *what* the database should look like, not on the running of it.
* **Database Programmer** — responsible for **writing the code** that interacts with the database. The programmer writes the SQL queries, the stored procedures and the application code that lets users add, edit and view the data through a friendly interface.

The three roles overlap in some organisations, but in larger projects they are very distinct: the analyst designs it, the programmer builds it, and the DBA runs it.

---

## 3.6 Desktop and server databases

| | Desktop database | Server (client-server) database |
|---|---|---|
| Where it runs | On one computer | On a central server that many clients connect to |
| Users | One user, or a few | Many users **at the same time**, from different places |
| Size and security | Small; limited security | Large; user access control and centralised backups |
| Examples | Microsoft Access, LibreOffice Base | MySQL, Microsoft SQL Server, Oracle, PostgreSQL |

A **distributed database** is spread over servers in different locations that work together as one.

## 3.7 Data, information, knowledge and decisions

**Data** (raw facts) is processed into **information** (meaningful results such as totals, averages and trends). Understanding that information gives **knowledge**, which is used to make a **decision**.

**Characteristics of quality data:**

| Characteristic | Meaning |
|---|---|
| **Accurate** | Correct and free of errors |
| **Complete** | Nothing that is needed is missing |
| **Consistent** | The same fact has the same value everywhere it is stored |
| **Current (up to date)** | Reflects the present situation |
| **Relevant** | Useful for the purpose |

Poor-quality data gives poor information, however good the software is (**GIGO**: garbage in, garbage out).

## 3.8 Validation and verification

| | Validation | Verification |
|---|---|---|
| Who or what checks | The **computer**, using rules | A **person** (or a second entry) |
| What it checks | That the data is **reasonable and allowed** | That the data was **captured correctly** from the source |
| Example | A mark must be from 0 to 100 | Typing a password twice; reading a number back to the customer |

Validation cannot prove that data is *true*: a mark of 56 passes a range check even if the learner really got 65.

**Validation checks:** presence (not empty), range (between limits), type (number, date), length (number of characters), format (pattern, e.g. two letters then four digits), and check digit.

## 3.9 Tables, keys and data types

A **table** holds **records** (rows), and each record is made up of **fields** (columns).

- A **primary key (PK)** is a field that uniquely identifies each record. It may not be empty or repeated.
- A **foreign key (FK)** is a field in one table that refers to the primary key of another table. It creates the **relationship** between the tables.

| Field data type | Used for |
|---|---|
| Short Text | Names, codes, and numbers that are not calculated with (phone and ID numbers keep their leading 0) |
| Number | Whole or decimal numbers used in calculations |
| Currency | Money |
| Date/Time | Dates and times |
| Yes/No | True/False values |
| AutoNumber | A unique number generated automatically, often the primary key |

## 3.10 Redundancy and anomalies

**Data redundancy** is the unnecessary repetition of the same data. When everything is kept in one big table, the same details are stored in many records. This wastes space and causes **anomalies**:

| Anomaly | Problem | Example (one table of library loans that repeats each member's details) |
|---|---|---|
| **Update anomaly** | A change must be made in many records; if one is missed, the data is inconsistent | A member's new address is changed in three loan records but not the fourth |
| **Insert anomaly** | Data cannot be added because other data does not exist yet | A new member cannot be stored until they borrow a book |
| **Delete anomaly** | Deleting one thing removes other data that is still needed | Deleting a member's only loan also deletes the member's details |

## 3.11 Splitting a table and drawing an ERD

The solution is to give each **entity** (thing you store data about) its own table and to link the tables with keys.

```
tblMembers              tblLoans                 tblBooks
MemberID (PK) 1 ----< MemberID (FK)
MemberName              LoanID (PK)
Cell                    LoanDate
                        BookID (FK) >---- 1 BookID (PK)
                                             Title
                                             Author
```

- One member can have many loans: **one-to-many** from tblMembers to tblLoans.
- One book can be lent many times: **one-to-many** from tblBooks to tblLoans.
- Each member's details are now stored **once**.

In an ERD question, show: every table with its fields, the PK of each table, the FKs in the linking table, and the relationship type on each line.

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
* **repeat…until loop** — a *post-test* loop. It runs the body first, **then** checks the condition. The body always runs **at least once**, regardless of the condition. Example: `repeat … until sAnswer = 'Y'`

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

## 4.8 Searching an array

| | Linear search | Binary search |
|---|---|---|
| How | Checks every element from the start until the value is found | Checks the **middle** element and discards the half that cannot contain the value; repeats |
| Data must be sorted? | No | **Yes** |
| Speed | Slow on large arrays | Very fast: each step halves the search area |
| Most comparisons for 100 items | 100 | 7 (because 2⁷ = 128) |

```pascal
iLow := 1;  iHigh := 8;  bFound := False;
while (iLow <= iHigh) and (not bFound) do
begin
  iMid := (iLow + iHigh) div 2;
  if arrNums[iMid] = iSearch then
    bFound := True
  else if arrNums[iMid] < iSearch then
    iLow := iMid + 1
  else
    iHigh := iMid - 1;
end;
```

**Trace** for `arrNums` = 4, 9, 15, 22, 28, 31, 40, 52 (index 1 to 8) and `iSearch` = 10:

| iLow | iHigh | iMid | arrNums[iMid] | bFound |
|---|---|---|---|---|
| 1 | 8 | 4 | 22 | False |
| 1 | 3 | 2 | 9 | False |
| 3 | 3 | 3 | 15 | False |
| 3 | 2 | | | False (loop ends: iLow > iHigh) |

The array must be sorted because the algorithm decides which half to discard by comparing with the middle value. That only works if smaller values are on one side and larger values on the other.

## 4.9 Sorting an array

**Bubble sort** compares **neighbouring** elements and swaps them if they are in the wrong order. After each pass the largest remaining value has "bubbled" to the end.

Ascending sort of `7, 3, 9, 2`:

| Pass | Comparisons | Array after the pass |
|---|---|---|
| 1 | 7,3 swap · 7,9 no swap · 9,2 swap | 3, 7, 2, 9 |
| 2 | 3,7 no swap · 7,2 swap | 3, 2, 7, 9 |
| 3 | 3,2 swap | 2, 3, 7, 9 |

**Selection sort** finds the smallest value in the unsorted part and swaps it into the first unsorted position.

| Pass | Action | Array after the pass |
|---|---|---|
| 1 | Smallest of all is 2; swap with position 1 | 2, 3, 9, 7 |
| 2 | Smallest of the rest is 3; already in place | 2, 3, 9, 7 |
| 3 | Smallest of the rest is 7; swap with position 3 | 2, 3, 7, 9 |

With **parallel arrays**, every swap must be done in **all** the arrays, or the data no longer lines up.

## 4.10 Reading text-file code

| Statement | What it does |
|---|---|
| `AssignFile(tFile, 'Data.txt')` | Links the file variable (logical name) to the file on disk (physical name) |
| `Reset(tFile)` | Opens an existing file for **reading**, from the first line |
| `Rewrite(tFile)` | Creates a new, empty file for writing. **An existing file is wiped** |
| `Append(tFile)` | Opens an existing file for writing and **adds to the end** |
| `Eof(tFile)` | True when the end of the file has been reached |
| `ReadLn(tFile, sLine)` / `WriteLn(tFile, sLine)` | Reads / writes one line |
| `CloseFile(tFile)` | Closes the file; without it, written data may be lost |
| `FileExists('Data.txt')` | True if the file exists. Test it before `Reset` or `Append` |

Splitting a line such as `Karoo#12.5`: `iPos := Pos('#', sLine)` finds the separator, `Copy(sLine, 1, iPos - 1)` gives the first part, and `Delete(sLine, 1, iPos)` leaves the rest in `sLine`.

## 4.11 Exception handling

A **runtime error (exception)** crashes the program while it runs: opening a file that does not exist, or `StrToInt` on text that is not a number. Prevent it by **checking first** (`FileExists`, validating input) or handle it with `try … except`:

```pascal
try
  iAge := StrToInt(edtAge.Text);
except
  ShowMessage('Please enter a whole number');
  Exit;
end;
```

## 4.12 Procedures, functions and parameters

A **function** returns a single value and is used in an expression. A **procedure** carries out a task and does not return a value through its name.

| | Value parameter | Variable (reference) parameter |
|---|---|---|
| Declared | `iNum: Integer` | `var iNum: Integer` |
| What is passed | A **copy** of the value | The **original variable** itself |
| Changes inside the method | Do **not** affect the caller's variable | **Do** change the caller's variable |

```pascal
procedure DoubleBoth(var iA: Integer; iB: Integer);
begin
  iA := iA * 2;
  iB := iB * 2;
end;
```

If `iX = 4` and `iY = 10`, then after `DoubleBoth(iX, iY)` the value of `iX` is **8** (`var` parameter: the original was changed) and `iY` is still **10** (value parameter: only the copy was changed).

## 4.13 User-centred design and software development

**User-centred design** puts the needs of the user first:

- a consistent layout, with the same colours and fonts throughout;
- clear labels and instructions, and a logical tab order;
- components that limit mistakes (combo box, spin edit, radio group instead of free typing);
- helpful error messages and feedback after every action;
- an uncluttered, readable screen.

**Software development phases:** analyse the problem → design the interface and the solution → code → test and debug → document → implement and maintain.

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

## 5.8 Big data

**Big data** is data sets so large and complex that ordinary software cannot process them. It is described by the **Vs**:

| V | Meaning |
|---|---|
| **Volume** | The enormous amount of data |
| **Velocity** | The speed at which new data arrives and must be processed |
| **Variety** | The many forms it takes: text, images, video, sensor readings, clicks |
| Veracity / Value | How trustworthy the data is / how useful it is (often added) |

Analysing big data reveals **patterns and trends** that support better decisions (what to stock, where to build a clinic, which adverts to show). **Social implications:** loss of privacy; data collected without informed consent; data sold or leaked; people profiled and treated differently because of it.

## 5.9 Digitalisation

**Digitalisation** is moving processes and records from paper and manual work to digital systems.

- **Benefits:** records are found and shared quickly, can be backed up, take no physical space and can be analysed.
- **Effects:** some jobs disappear or change while new ones appear; work can be done remotely; people without access or skills are left behind; organisations depend on their systems and on electricity.

## 5.10 Globalisation and the Fourth Industrial Revolution

**Globalisation** is the way technology connects people, businesses and countries into one interconnected system: people in different countries work on the same platform, buy from each other and share information in real time.

The **Fourth Industrial Revolution (4IR)** is the merging of the physical and digital worlds through technologies such as AI, robotics, the Internet of Things, 3D printing and big data.

- **Effect on work:** routine jobs (data capturing, manual record keeping, some factory work) are automated; new jobs are created (data analyst, AI specialist, IoT technician, cybersecurity specialist). Workers need to keep learning new skills.

## 5.11 The Internet of Things and artificial intelligence

The **Internet of Things (IoT)** is everyday objects fitted with sensors and connectivity that collect and exchange data over the Internet without human input: smart watches, fridges, security cameras, farm sensors. Practical concerns: battery life, network coverage, data costs, security and privacy.

**Artificial intelligence (AI)** is software that performs tasks that normally need human intelligence. In **machine learning**, a system is trained on a very large number of examples, finds patterns in them, and improves as it receives more data and feedback. Its results depend on the quality of the training data.

## 5.12 Human error and computer error

| | Human error | Computer error |
|---|---|---|
| Cause | Wrong data captured, wrong option chosen, a result accepted without checking | Hardware failure, a bug in the software, an inaccurate AI result |
| Reduce it by | Validation and verification, training, clear screens | Testing, updates, backups, human checks on important results |

**GIGO (garbage in, garbage out):** if the input is wrong, the output will be wrong, even when the program works perfectly.

## 5.13 Cybercrime and your online identity

- **Online fraud and scams:** fake websites, adverts or messages that trick people into paying for something that does not exist.
- **Identity theft:** using someone's personal details to pretend to be them, for example to open accounts.
- **Checking that a site is legitimate:** look carefully at the domain name; look for `https` and a valid certificate; search for reviews and warnings; contact the organisation on a number you already know.
- **Protecting your online identity:** strong, unique passwords and MFA; think before you post; limit what is public in your privacy settings; check what a search for your own name shows (your **digital footprint**); report fake accounts.

## 5.14 Privacy, the law and network-use policies

- **POPIA** requires organisations to collect only the personal information they need, with consent, to keep it secure, and not to share it without permission.
- An **acceptable use policy (AUP)** is the set of rules that users of an organisation's network agree to: what the network may be used for, what is not allowed (illegal downloads, bullying, sharing passwords), and the consequences.

## 5.15 Capabilities and limitations of ICT

**Capabilities:** speed, accuracy, huge storage, working without tiring, instant communication. **Limitations:** computers only follow instructions, depend on correct data and on power and connectivity, can fail or be attacked, and cannot replace human judgement and empathy.

## 5.16 Internet-related careers

Web designer, web developer, multimedia designer, network administrator, database administrator, data analyst, cybersecurity specialist, social media manager.

---

*End of Grade 11 Theory Notes*
