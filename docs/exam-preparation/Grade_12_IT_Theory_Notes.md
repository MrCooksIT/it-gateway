# Grade 12 Information Technology — Theory Study Notes

*A topic-by-topic reference for CAPS Information Technology theory.*

These notes follow the CAPS topic order: System Technologies → Communication and Network Technologies → Data and Information Management → Solution Development → Social Implications, Cybersecurity and Integrated Topics. Each topic is explained in full so the notes can be used as standalone study material for any examination.

---

# SECTION 1: SYSTEM TECHNOLOGIES

## 1.1 CPU Performance Concepts

### Multiprocessing

**Multiprocessing** is when a computer has **more than one physical CPU core** and can execute multiple instructions **at the same time** — one instruction per core, truly in parallel. A specification like *"6 × Cores"* or *"hexa-core"* tells you the computer supports multiprocessing — it has six physical cores that can each run a separate task simultaneously.

This is different from one fast single-core CPU pretending to do multiple things by switching between them rapidly — that is just multitasking. With genuine multiprocessing, six things really are happening at once.

### Multithreading

**Multithreading** is the ability of a single CPU core to handle **multiple "threads" (sub-tasks) of a program at the same time**, by switching between them very rapidly or by running two threads in parallel on a single core (using hyper-threading technology).

A "thread" is one independent path of execution within a program. A web browser, for example, might have separate threads for downloading a web page, rendering it on screen, running JavaScript, and listening for the user's clicks — all at once. Multithreading makes the program feel more responsive because no single task can completely block the others.

Multiprocessing and multithreading are often combined: a 6-core CPU with hyper-threading can handle 12 threads at the same time.

## 1.2 Cache and Disk Cache

### Disk cache

**Disk cache** is a small amount of fast memory (RAM, or sometimes a dedicated chip on a storage drive) used to **temporarily hold data that has been recently read from, or is about to be written to, a storage device**. When the CPU needs the same data again, it can be fetched from the disk cache (which is fast) rather than from the much slower disk itself.

Disk cache is what makes opening the *same* file the second time so much faster than the first time — the first read pulled the data off the slow drive into the cache, and the second read got it from the cache.

### Cache memory vs RAM — two key differences

Although both are forms of memory, they differ sharply:

* **Speed and location** — Cache memory is built directly into (or right next to) the CPU and operates at almost CPU speed. RAM is on separate modules plugged into the motherboard, much further from the CPU, and is significantly slower.
* **Size and cost** — Cache memory is very small (typically a few MB) but very expensive per MB. RAM is much larger (typically 8 GB to 64 GB) and far cheaper per GB. This is why the cache cannot simply be made enormous to replace RAM.

## 1.3 Storage Hierarchy — Speed of Data Access

Inside a computer, different kinds of storage are arranged in a "hierarchy" — the fastest and most expensive at the top, the slowest and cheapest at the bottom. The CPU pulls data through this hierarchy.

From **fastest to slowest**:

1. **CPU cache** — fastest, smallest (MB), built into the CPU
2. **VRAM** — video RAM, dedicated to the graphics card, very fast
3. **RAM** — main system memory, fast, GBs in size
4. **SSD** — solid-state drive, fast for a storage device, hundreds of GBs to TBs
5. **HDD** — slowest, mechanical, often the largest, TBs

The reason for the hierarchy: faster memory is more expensive per byte, so we use a small amount of very fast memory close to the CPU, and a large amount of slow memory for the bulk storage of files.

## 1.4 Motherboard — Point-to-Point Connections

Most components on the motherboard share a **bus** — a common pathway that several devices take turns to use. A **point-to-point connection** is a private, dedicated link between two specific components, used by no one else.

A typical example is the connection between the **CPU and RAM** (via the memory controller built into modern CPUs), or the connection between the **CPU and the dedicated GPU** over a dedicated PCIe link.

**Point-to-point is faster than a shared bus** because:

* Only two devices use the link, so there is no waiting for other devices to finish.
* No "arbitration" overhead — no need to decide whose turn it is to use the bus.
* The link can be optimised for the specific traffic between those two devices.

## 1.5 The GPU (Graphics Processing Unit)

A **dedicated GPU** is a separate processor on the graphics card that is specialised for the kinds of mathematical calculations needed to draw graphics on screen — calculating where each pixel should appear, what colour it should be, and how 3D objects should be lit and rotated.

A **dedicated GPU improves general performance** by:

* **Taking the graphics workload off the CPU**, so the CPU is free to handle other tasks. The whole system feels snappier.
* **Handling 3D graphics, video editing and image processing much faster** than an integrated graphics chip could. Professional image- and video-editing software and modern games run smoothly.
* Having its own **VRAM (Video RAM)** so that images and textures don't have to share with the system RAM.

The trade-off is that a dedicated GPU is expensive and uses more power.

## 1.6 Virtual Machines (Standard Use Case)

A **virtual machine (VM)** is a software-created "computer within a computer" that runs its own operating system on top of the host computer.

A standard (non-developer) user might use a VM to:

* **Test new or unknown software safely** — install a program that might contain a virus inside the VM. If it does, the host computer is untouched and the VM can be deleted.
* **Run a different operating system** — keep Windows as the main OS but spin up an Ubuntu Linux VM to learn Linux, or run an old version of Windows to use legacy software that won't run on Windows 11.

## 1.7 Virtual Reality (VR)

**Virtual reality** is a computer-generated, **fully immersive 3D environment** that the user experiences by wearing a VR headset. The headset replaces what the user sees and hears, so they feel they are inside the virtual world instead of looking at a screen. Hand controllers (or hand tracking) let the user interact with virtual objects.

### Uses of VR

VR has applications across many industries:

* **Education and training** — simulating dangerous or expensive situations safely. Pilots can practise flying in a virtual cockpit; medical students can practise surgery on virtual patients; engineers can walk through a virtual factory before it is built.
* **Gaming and entertainment** — fully immersive games and interactive experiences.
* **Architecture and design** — clients can walk through a virtual building before construction begins, or designers can examine 3D products before any physical prototype is built.
* **Healthcare** — exposure therapy for phobias, pain management, and rehabilitation.
* **Retail** — customers can preview products in 3D (clothing on a virtual avatar, furniture in a virtual version of their home) before buying.
* **Remote collaboration** — colleagues in different cities can meet in a shared virtual environment as if they were in the same room.

### VR vs AR

VR (Virtual Reality) **replaces** the real world entirely with a virtual one. AR (Augmented Reality) **adds** computer-generated information on top of the real world that the user can still see. Examples of AR include phone-camera filters, navigation arrows overlaid on streets, and games like Pokémon GO where virtual creatures appear in real locations.

## 1.8 Beta Software

A **beta version** is a near-final version of a software product released to a limited group of users (or sometimes to the public) for **testing in real-world conditions before the official release**.

The purpose of releasing a beta is to:

* **Find bugs** that the developers' own tests missed, by exposing the software to a wide variety of computers and usage patterns.
* **Collect user feedback** about features, the interface and performance, so the final version can be improved.

The beta is not the final product — users are warned that it may be unstable, and they help the company by reporting problems.

## 1.9 UPS — Uninterruptible Power Supply

A **UPS (Uninterruptible Power Supply)** is a device that contains a battery and sits between the wall socket and the computer. When the mains power fails, the UPS instantly switches over to its battery and **keeps the computer running for a short time** — usually long enough to save open work and shut down properly. It also protects the computer from power surges and dips.

A UPS is especially valuable in **load-shedding regions and during thunderstorms**, where it prevents sudden shutdowns that can cause data loss and damage to the hardware.

## 1.10 Backups

A **backup** is a copy of the data, kept separately from the original, that can be used to restore the data if something goes wrong (hardware failure, file deletion, ransomware attack, theft, fire).

### Backup that is faster and uses less space

If full backups are taking too long and using too much space, the solution is to use **incremental backups** (or compressed backups):

* An **incremental backup** only copies the data that has *changed since the last backup*. A full backup is taken occasionally (say, once a week); in between, the daily incremental backups are tiny and quick. Much less storage is needed and the backup runs much faster.
* **Backup compression** can also be used — the backed-up data is compressed (zipped) as it is saved, so a 100 GB backup might only use 40 GB of disk space.

A combination of incremental backups + compression solves both the time problem and the storage problem.

## 1.11 Virtual Memory

**Virtual memory** is a technique used by the operating system to **use a portion of the storage device (SSD or HDD) as if it were extra RAM**. When physical RAM is full but a program needs more, the OS moves blocks of data that are not currently in active use out of RAM and onto the disk (into a special file called the **swap file** or **page file**). When that data is needed again, it is read back into RAM.

This allows the computer to run more programs at the same time than the physical RAM would normally allow.

### Negative effect on performance

The disk (even an SSD) is **vastly slower than RAM** — by a factor of hundreds or thousands. If the system has to swap data between RAM and the disk constantly (a situation called **thrashing**), the computer slows down dramatically. Programs become unresponsive, simple tasks take a long time, and the disk activity light is constantly on. The only real fix is to install more physical RAM so that virtual memory is needed less often.

## 1.12 CMOS — Storing BIOS Settings

The **CMOS** (Complementary Metal-Oxide-Semiconductor) is a small memory chip on the motherboard whose job is to **store the BIOS settings** — things like the system date and time, the boot order, and basic hardware configuration. The CMOS is kept powered by a small coin-shaped battery on the motherboard so that its contents are not lost when the computer is switched off.

When the small battery runs out, the computer "forgets" the time and boot settings each time it is unplugged.

## 1.13 System Software Quick Reference

* **System software** is software that manages and controls the computer hardware (the OS, drivers, utility programs).
* **Utility programs** are part of the system software and perform **maintenance and administrative tasks** — antivirus, backup, file compression, disk defragmenter, system clean-up tools.
* A **device driver** is software that enables an operating system to communicate with a specific hardware device.
* **Convergence** is the trend where separate technologies and functions are combined into a single multi-purpose device (the modern smartphone being the obvious example).
* **Synchronisation** in the context of online (cloud) storage means that the same files are automatically kept up to date across multiple devices. A file edited on the laptop appears in its updated form on the phone moments later — no manual copying needed.

---

# SECTION 2: COMMUNICATION AND NETWORK TECHNOLOGIES

## 2.1 Network Concepts and Hardware

### Host

A **host** is any computer or device on a network that **provides services or resources to other computers** on the network. A server is the most common example. Hosts are different from **clients**, which are the devices that *use* the services that hosts provide. The same device can act as a host and a client at different times.

### NIC — Network Interface Card

A **NIC (Network Interface Card)** is the hardware component that **physically connects a computer to a network**. It is installed inside the computer (or built into the motherboard) and provides the Ethernet port (RJ-45) for a cable, or the Wi-Fi antenna for a wireless connection. Without a NIC, a computer cannot join a network at all.

### Switch

A **switch** is a network device that connects multiple devices on the same network and forwards data only to the device it is intended for (using the device's MAC address). This is much more efficient than a "hub" (which sends all data to all devices), especially in a high-traffic environment, because:

* Each device gets the full bandwidth of its own connection to the switch — they are not sharing one pipe.
* Data is sent only where it needs to go, not flooded to every device, reducing congestion.
* The switch can handle many conversations between pairs of devices at the same time.

### Star topology

In a **star topology**, every device on the network is connected by its own cable to a **central switch** (or hub). It is the most common topology in modern LANs. Its advantages: easy to add or remove devices without affecting others; if one cable fails, only that one device is affected; easy to troubleshoot.

## 2.2 Cabling — Fibre vs UTP

For the **main backbone** of a high-traffic network, **fibre-optic cable** is preferred over copper UTP cable. Three technical advantages of fibre over copper:

* **Higher bandwidth and longer distance** — fibre can carry vastly more data per second and over much longer distances than copper, without losing signal strength.
* **Immune to electromagnetic interference (EMI)** — fibre uses pulses of light, not electrical signals, so it is not affected by nearby motors, fluorescent lights or other cables that would introduce noise on copper.
* **More secure** — fibre is extremely difficult to tap into without breaking the cable (which would cause a noticeable signal loss), so eavesdropping on the data is much harder than on copper.

The downside is that fibre is more expensive to buy and to install, and it cannot be bent sharply.

## 2.3 Signal Loss — Attenuation

**Attenuation** is the **loss of signal strength** as a signal travels along a cable, through the air, or through any other medium. Causes include the distance the signal has travelled, the quality of the cable, and external interference. Attenuation is why network cables have maximum length limits (e.g. 100 m for UTP) — beyond that distance the signal is too weak to be useful. **Repeaters** and **switches** can boost the signal back up.

Other related terms that often get confused with attenuation:

* **Electromagnetic interference (EMI)** — signal disturbance caused by external electromagnetic fields (motors, fluorescent lights, other cables).
* **Eavesdropping** — secretly listening in on the data on the network.
* **Crosstalk** — signal from one cable leaking into another nearby cable.

## 2.4 GPS and 5G

### GPS

**GPS (Global Positioning System)** is a technology that **determines the exact geographical coordinates of a device on Earth** using signals from a constellation of satellites orbiting the planet. The GPS receiver in the device picks up signals from multiple satellites at once and calculates its position from the tiny differences in the time the signals took to arrive.

### Combining GPS with 5G — real-time tracking

GPS tells a device *where it is*; 5G is a fast cellular network that allows the device to **send that information across the internet** quickly. Together they make real-time tracking possible:

* The GPS receiver in the vehicle calculates the current location every few seconds.
* The 5G connection immediately sends those coordinates to a central tracking system over the internet.
* The tracking software at headquarters displays the vehicle's position on a map in real time, updating as the vehicle moves.
* Because 5G has high bandwidth and low latency, the position can be updated with almost no delay even when the vehicle is in motion between cities.

### 5G vs fixed-line for mobile use

For research units that **travel between locations**, **5G mobile connectivity is the right choice** because fixed lines obviously cannot follow a moving vehicle.

Reasons for choosing 5G:

* **Mobility** — 5G works anywhere the cellular network reaches, so the vehicle stays connected as it moves.
* **High speed** — modern 5G easily matches or exceeds typical fixed-line broadband, so large files can be transferred while the vehicle is on the move.
* **No physical installation** — no cabling needs to be laid; the units are productive immediately.

## 2.5 Location-Based Computing

**Location-based computing** is the use of a device's geographical location (usually from GPS, but also from Wi-Fi and cell-tower triangulation) to **provide services or information that are relevant to where the user is**. Examples include Google Maps directing you to the nearest petrol station, an app showing you the weather forecast for your current city, or a security app recording where the device is.

### Ethical concern

The major ethical concern is **privacy**. Location data is extremely sensitive: it reveals where you live, where you work, where your children go to school, what time you go to gym, and where you spent last Saturday night. If this data is collected without informed consent, sold to advertisers, leaked in a data breach, or accessed by a stalker or abusive partner, it can cause real harm. Companies collecting location data have an ethical (and often legal) duty to be transparent about how it is used and to keep it secure.

## 2.6 Bandwidth Management — Shaping vs Throttling

ISPs and network administrators control how bandwidth is used through two related but different techniques:

* **Bandwidth shaping** (also called **traffic shaping**) **prioritises** certain types of traffic over others. It gives more bandwidth to important traffic (e.g. video calls, critical business apps) and less to less important traffic (e.g. file downloads, software updates). The total bandwidth available is unchanged — it is just shared more cleverly.
* **Bandwidth throttling** **deliberately limits the speed** of certain types of traffic (or of certain users) to a specific cap. The throttled traffic cannot exceed that limit even if there is plenty of unused bandwidth available.

### Which to use for a lab that prioritises video conferencing

**Shaping** is the right choice. Shaping gives video conferencing **priority** so that calls are smooth and clear, while still allowing other traffic (like software updates) to use the leftover bandwidth at whatever speed is available. Throttling would simply cap one type of traffic regardless of conditions and might still leave video calls competing for bandwidth.

## 2.7 Network Security

### Firewall

A **firewall** is a security technology that acts as a **barrier between an internal network and external traffic**, monitoring all incoming and outgoing data and **blocking anything that does not meet a defined set of security rules**. Firewalls can be hardware devices, software running on each computer, or a combination. They are the first line of defence against unauthorised external access.

### Multi-layer verification (Multi-Factor Authentication)

**Multi-layer verification** (also called **multi-factor authentication / MFA / 2FA**) is a security process that requires the user to provide **two or more independent pieces of evidence** before access is granted. Typically this is a combination of:

* **Something you know** — a password or PIN
* **Something you have** — a phone receiving an SMS code, an authentication app generating codes, a security key
* **Something you are** — a fingerprint, face scan or iris scan

### Why multi-layer is better than a simple password

A password alone can be **stolen, phished, guessed, leaked in a data breach, or cracked by brute force**. If an attacker has the password, they have full access. Multi-layer verification means that even if the password is stolen, the attacker still cannot log in — they would also need the user's actual phone (or fingerprint), which is much harder to obtain. This dramatically reduces the chance of a successful break-in.

### HTTPS / SSL — Secure Web Connections

**HTTPS** (HyperText Transfer Protocol Secure) is the protocol used to ensure that a connection between a browser and a website is **encrypted and secure**. HTTPS uses the underlying **SSL/TLS** encryption to scramble the data, so that even if an attacker intercepts it, they cannot read or modify it. HTTPS is essential for any website that handles passwords, personal information or payment details — a green padlock or "https://" in the browser address bar is the visual sign that HTTPS is in use.

### VPN — Virtual Private Network

A **VPN (Virtual Private Network)** creates a secure, encrypted "tunnel" between the user's device and a remote network (often the user's company network), with all data flowing through the tunnel. To outsiders, the connection looks like ordinary encrypted traffic; they cannot see what is being sent.

A VPN is recommended for remote workers accessing the company network because:

* All data sent over the public internet is **encrypted**, protecting it from being read or tampered with — even on insecure public Wi-Fi.
* The user appears to be **inside the company network**, so they can access internal resources (file servers, internal applications) as if they were sitting at the office desk.

## 2.8 Cloud Services

### SaaS — Software as a Service

**SaaS (Software as a Service)** is a model where the software is **hosted in the cloud and accessed through a web browser** (or thin client app), rather than installed on each user's computer. The user pays a subscription instead of buying the software outright.

Examples include Microsoft 365 (online), Google Workspace, Salesforce, Canva and many logistics tracking systems.

Benefits of SaaS over traditional desktop software include:

* **No installation or maintenance** — the provider handles updates, patches and infrastructure; the user just opens a browser.
* **Access from anywhere** — works on any device with internet access; not tied to one machine.
* **Lower upfront cost** — paid monthly instead of a large once-off licence purchase.
* **Automatic updates** — everyone is always on the latest version, so there are no compatibility headaches.

The trade-off is that an internet connection is essential and the company is dependent on the SaaS provider's reliability.

### VoIP — Voice over Internet Protocol

**VoIP** is technology that allows **voice calls to be made over the internet** instead of the traditional telephone network. Skype, WhatsApp calls, Microsoft Teams calls and most modern business phone systems use VoIP. It is much cheaper than traditional phone calls, especially internationally.

Disadvantages of relying *only* on VoIP:

* **Depends entirely on a working internet connection** — when the internet is down, the phones do not work.
* **Affected by network problems** — slow or unstable connections cause poor call quality, dropouts and echo.
* **Customers without good internet** may struggle to reach the business (older customers or rural customers may prefer a normal phone number).
* **Power dependency** — traditional phones often work during a power cut; VoIP devices need power and a working router.

## 2.9 Internet Terminology

### Intranet

An **intranet** is a **private network internal to an organisation**, used for sharing information, files and services between employees. Despite using the same technology as the internet (web pages, email, etc.), the intranet is *not* accessible to outsiders. If outsiders are given limited access, the resulting network is called an *extranet*.

A common misconception worth correcting: an intranet is *not* accessible to users outside the organisation. That is a key difference between an intranet (internal only), an extranet (internal plus selected outsiders) and the internet (open to all).

### AUP — Acceptable Use Policy

An **AUP (Acceptable Use Policy)** is a document that sets out the **rights and responsibilities of users on an organisation's network**. It explains what users are allowed to do (and not do), the consequences of misuse, and the organisation's right to monitor activity. New employees (and learners in a school) usually have to sign an AUP before being given a network account.

## 2.10 Email Protocols

* **SMTP** (Simple Mail Transfer Protocol) — used to **send** email.
* **POP3** (Post Office Protocol v3) — used to **receive** email; downloads messages to one device and (by default) removes them from the server.
* **IMAP** (Internet Message Access Protocol) — used to **receive** email; keeps the messages on the server, so the same inbox can be seen from multiple devices in sync.

A common exam trick is to claim that "POP3 is a protocol for *sending* emails" — that is **false**. POP3 receives; SMTP sends.

---

# SECTION 3: DATA AND INFORMATION MANAGEMENT

## 3.1 Source Code vs Machine Code

* **Source code** is the human-readable code written by a programmer in a programming language like Delphi, Python, Java or C++. It is plain text — programmers can read and edit it.
* **Machine code** is the **binary instructions in 0s and 1s that the CPU can execute directly**. The CPU does not understand source code at all.

A **compiler** translates the source code into machine code so the CPU can run it. A common exam trick is to claim "source code is in binary format that the CPU can execute directly" — that is **false**. Source code is in a human-readable programming language; *machine code* is the binary version.

## 3.2 The Machine Cycle

The **machine cycle** is the **specific sequence of steps the CPU follows when carrying out an instruction**. The four steps are usually called:

1. **Fetch** — get the next instruction from memory.
2. **Decode** — work out what the instruction is telling the CPU to do.
3. **Execute** — perform the instruction (e.g. perform a calculation, move data).
4. **Store** — save the result back to memory or to a register.

The CPU repeats this cycle billions of times per second.

## 3.3 GIGO — Garbage In, Garbage Out

**GIGO** is the principle that the **quality of the output of any computer system is directly related to the quality of the input**. If the data put into the system is wrong, incomplete or nonsense ("garbage"), the system can only produce wrong, incomplete or nonsense results — no matter how well-written the program is. GIGO is the reason why data validation and verification matter so much.

## 3.4 Database Keys

### Primary key

A **primary key** is a field (or combination of fields) whose value **uniquely identifies each record in a table**. It cannot be null and cannot have duplicate values.

### Composite key

A **composite key** is a primary key made up of **a combination of two or more fields** — used when no single field on its own is unique enough to identify a record. For example, in a "MarksObtained" table, neither the LearnerID nor the SubjectID alone identifies a record uniquely (one learner has many subjects, and many learners take the same subject), but the *combination* of LearnerID + SubjectID is unique.

### Foreign key

A **foreign key** is a field in one table whose value matches the primary key of another table. It is the mechanism that creates **relationships** between tables in a relational database. For example, in a Loans table, the `MemberID` field is a foreign key linking to the Members table.

## 3.5 Data Types in a Database

When designing a database, each field needs an appropriate data type:

| Use | Data type |
|---|---|
| Money values like a total cost | **Currency** |
| Whole numbers (counts, quantities) | **Integer / Number** |
| Numbers with decimals (measurements) | **Real / Double** |
| Yes/No, True/False values | **Boolean / Yes/No** |
| Text (names, addresses, descriptions) | **String / Text** |
| Dates of birth, transaction dates | **Date/Time** |

A field that stores a monetary value (e.g. `TotalAmount`, `Price`, `Salary`) should be of type **Currency**. A field that stores a count or quantity (e.g. `NumberOfItems`, `Age`) should be **Integer**. A field that stores a true/false condition (e.g. `IsActive`, `HasPaid`) should be **Boolean**.

## 3.6 Normalisation

**Normalisation** is the process of **organising the fields and tables of a relational database to reduce redundancy and improve data integrity**. The aim is to ensure that each piece of information is stored in **one place only**, and that each table contains data about only one "thing" (one entity).

Normalisation is essential for good database design because:

* **It eliminates data redundancy** — information is not repeated across many records, saving storage and avoiding inconsistencies (where the same fact is updated in one place but not in another).
* **It protects data integrity** — when there is only one copy of a piece of data, there is no risk of two copies disagreeing.
* **It makes the database easier to maintain** — fields and tables have clear responsibilities, and the structure can grow without becoming a tangled mess.

### A field violating normalisation

A field that stores a **calculated or derived value** violates normalisation. The classic example is a `Total` field that stores the sum of several other fields in the same record — say `Total = Price + Tax + Delivery`. Storing the total duplicates information that already exists in the other fields. If one of the underlying values changes (the tax rate goes up) but the stored total is not also manually updated, the database becomes inconsistent — the `Total` no longer equals `Price + Tax + Delivery`.

The correct approach is to **calculate the value whenever it is needed** (using a query or a calculated field in the form) instead of storing it. Other examples of derived values that violate normalisation: storing an age (calculate from date of birth), storing an average (calculate from the underlying values), storing a person's full name when first name and surname already exist.

## 3.7 Database Relationships

A **one-to-many relationship** is the most common kind of relationship in a relational database: one record in Table A is related to many records in Table B. Some everyday examples:

* One **Author** writes many **Books**.
* One **Customer** places many **Orders**.
* One **Department** employs many **Staff** members.

To create a one-to-many relationship between two tables (let's call them `tblParent` and `tblChild`):

* `tblParent` has a primary key — e.g. `ParentID`.
* `tblChild` includes a field that stores the ID of the parent that the child record belongs to. In `tblChild`, that field is a **foreign key** that links to the primary key in `tblParent`.
* In the DBMS the relationship is then defined between the foreign key and the primary key, and **referential integrity** is enforced — meaning the system will not allow a child record to refer to a parent that does not exist, and will not allow a parent to be deleted while children still reference it.

## 3.8 Centralised vs Distributed Databases

* In a **centralised database** model, all the data is stored on **one central server**, and every user (no matter where they are) connects to that one location to read and write data.
* In a **distributed database** model, the data is **spread across multiple servers in different locations**, often kept in sync with each other. A user typically connects to the nearest server.

### Advantages of a centralised database

A centralised database makes it **easy to manage, back up and secure the data** because everything is in one place. The IT team controls one server, applies one set of security policies and runs one backup process. Data consistency is also easier to enforce — there is only one "version of the truth", so the same record cannot exist in slightly different forms in different places.

### Advantages of a distributed database

A distributed database is most useful when an organisation has multiple sites in different locations (typically different cities or countries). Its advantages are:

* **Faster local access** — each site reads from a nearby server, with no long delays caused by data having to travel across continents.
* **Resilience** — if one site's server fails or its internet link goes down, the other sites are not affected and can continue working.
* **Bandwidth efficiency** — less data has to travel between sites because most queries are answered locally.

However, distributed systems are **more complex and expensive**, and keeping the copies of the data in sync requires careful design.

## 3.9 RFID

**RFID (Radio Frequency Identification)** is a wireless technology in which a small tag (containing a microchip and antenna) transmits identifying information to a nearby reader using radio waves. RFID tags do not need line-of-sight (unlike barcodes), can be read from a short distance, and many tags can be read at the same time.

### Uses of RFID

RFID is used wherever many items need to be tracked or identified automatically. Common applications include:

* **Stock and asset tracking** — every item in a warehouse, library or laboratory is tagged so its current location can be checked instantly.
* **Access control** — staff use RFID cards or badges to unlock doors to secure or restricted areas.
* **Toll roads and public transport** — vehicles fitted with tags pass through gates without stopping; commuters tap pre-loaded RFID cards on a reader.
* **Animal identification** — pets and livestock can be implanted with tiny RFID tags carrying their unique ID and owner details.
* **Retail anti-theft** — clothing items are tagged; the tag triggers an alarm at the exit if not deactivated at the till.
* **Contactless payment** — bank cards and phones use a short-range form of RFID (NFC) to pay without inserting the card.

## 3.10 Invisible Online Data Collection

**Invisible (or covert) online data collection** is the gathering of information about users by websites and online services **without the user being directly aware that the data is being collected**. The user is focused on the page content; the data collection happens silently in the background.

Examples include:

* **Cookies** that record which pages you visited and for how long.
* **Browser fingerprinting** — recording details of your device, OS, screen size and installed fonts to identify you uniquely.
* **Tracking pixels** in emails and on web pages.
* **Click and scroll tracking** that records where you click and how far down a page you scroll.
* **IP address logging** and approximate geolocation.

This kind of data is used for targeted advertising, analytics and sometimes for profiling — and it is a major privacy concern.

## 3.11 Data Integrity Controls

### Logging changes (audit log)

**Logging changes** is the process of **recording every change made to the data in the database** so that there is a permanent record of who did what and when. The log allows changes to be traced, audited and (if necessary) undone.

Details that must be recorded in such a log include:

* **The user who made the change** (which account performed the action).
* **The date and time** of the change.
* **What changed** — the field, the old value and the new value.
* The **table and record** that was affected.

### Access rights and permissions

**User access rights** control **whether** a user can access a particular part of the database; **permissions** control **what** they can do (read, write, edit, delete) once they have access.

Used together, they prevent unauthorised personnel from altering sensitive data. For example, only staff who actually need to capture results into a specific table are given **write/edit access** to that table; everyone else is either denied access entirely or given **read-only access** (so they can see the data but not change it). The DBA configures these rights for each user account.

### Logical integrity

**Logical integrity** means that the data stored in the database **makes sense in the real world** — values fall within acceptable ranges and follow the rules of the application area. For example, a date of birth cannot be in the future, a person's age cannot be negative, and an event's end date cannot fall before its start date. Logical integrity is enforced by **validation rules** in the database design.

A common validation technique to ensure a date field is valid is a **range check** — the date must fall within a specified range (e.g. between an official start date and end date), or simply must not be in the future.

## 3.12 Transaction Rollback

A **transaction rollback** is a database mechanism that **undoes (rolls back) all changes made during a transaction if the transaction does not complete successfully**. Its purpose is to keep the database in a consistent state — either *all* the steps of a transaction happen, or *none* of them do.

If the system is updating a table during a power surge and the update is interrupted halfway through, a rollback undoes any partial changes that were made, returning the database to exactly the state it was in before the failed transaction started. This prevents corrupted, half-finished data from being left behind.

## 3.13 Data Warehousing and Data Mining

These two terms are often confused but mean very different things:

* A **data warehouse** is a **large central store of data**, often combined from many different sources (sales systems, customer systems, production systems), kept over a long period of time. Its purpose is to **gather, organise and store historical data** in a way that makes large-scale analysis possible. It is essentially a giant, well-organised database optimised for analysis rather than day-to-day operations.
* **Data mining** is the **process of analysing the data in a warehouse** to **discover useful patterns, trends and relationships** that were not previously known. Its purpose is to *extract* knowledge from the data.

A simple analogy: the data warehouse is the library; data mining is the act of reading through the library to find a story no one had noticed before.

## 3.14 SQL

**SQL (Structured Query Language)** is the **standard language used for querying and manipulating data in a relational database**. Almost every relational DBMS — MySQL, PostgreSQL, Oracle, Microsoft SQL Server, Microsoft Access — supports SQL. With SQL the programmer can create tables, insert records, update records, delete records and run powerful queries to extract exactly the information needed.

## 3.15 Database-Related Careers

Two careers involved in the day-to-day maintenance and security of databases:

* **Database Administrator (DBA)** — installs the DBMS, manages user accounts and permissions, schedules and verifies backups, monitors performance, applies security patches, and restores the database after failures.
* **Database Security Specialist** — focuses specifically on protecting the database from unauthorised access and cyberattack, including encryption, access controls, intrusion detection and vulnerability assessment.

Other careers in the database field include **Database Analyst** (designs the data model) and **Database Programmer / Developer** (writes the queries and application code).

## 3.16 Binary Conversion (8-bit)

To convert a decimal number to its 8-bit binary equivalent, use the place values:

| Place value | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
|---|---|---|---|---|---|---|---|---|

Start with the largest place value that fits in the number, write a 1 in that position, subtract the place value, and repeat with the remainder.

**Example: Convert 53 to 8-bit binary**

* 53 − 32 = 21 → put a 1 in the 32 position
* 21 − 16 = 5 → put a 1 in the 16 position
* 5 − 4 = 1 → put a 1 in the 4 position
* 1 − 1 = 0 → put a 1 in the 1 position

| Place value | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
|---|---|---|---|---|---|---|---|---|
| Binary digit | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 1 |

**Answer: 00110101₂**

(Always check: 32 + 16 + 4 + 1 = 53 ✓)

---

# SECTION 4: SOLUTION DEVELOPMENT

## 4.1 Algorithms and Programming Concepts

An **algorithm** is a **step-by-step approach followed to solve a problem**. Every program begins as an algorithm before any code is written.

## 4.2 Integer Division Operators in Delphi

Delphi provides several operators for working with whole-number division. The four to know:

| Expression | Meaning | Result of example |
|---|---|---|
| `64 div 6` | Integer division — the whole-number quotient | 10 (because 6 × 10 = 60, and the .67 part is discarded) |
| `64 mod 6` | Modulus — the remainder after integer division | **4** (because 64 − 60 = 4) |
| `Floor(64/6)` | Rounds the real division *down* to the nearest whole number | 10 |
| `Trunc(64/6)` | Truncates the real division (chops off the decimals) | 10 |
| `Round(64/6)` | Rounds to the nearest whole number | 11 |

So among `div`, `Floor` and `Trunc`, all three give 10 for `64 ÷ 6`. **`64 mod 6` is the odd one out — it gives 4**, the remainder, not 10.

(Note: for **negative** numbers, `Trunc` and `Floor` behave differently — `Trunc(-2.5)` is −2, while `Floor(-2.5)` is −3. For positive numbers, they agree.)

## 4.3 UML Class Diagrams (OOP)

A **UML (Unified Modeling Language) class diagram** is a visual blueprint of an object class. It shows the class's **attributes** (the data each object will store) and its **methods** (the actions each object can perform). A UML class diagram is split into three sections from top to bottom: the class name, the attributes, and the methods.

### Naming conventions

* Class names begin with **T**: `TPerson`, `TBook`, `TVehicle`.
* Attribute names use Hungarian notation prefixes: `s` for string, `i` for integer, `r` for real, `b` for Boolean, `c` for char, `arr` for array. For example: `sName`, `iAge`, `rPrice`, `bIsActive`.
* Methods are named clearly to describe what they do.

### Three kinds of methods

* A **constructor** is a special method called **Create** that runs once when the object is created, and is used to **set up the initial values of all the attributes** (usually by receiving them as parameters). For example, a `Create(sName : String; iAge : Integer)` constructor takes the name and age and stores them in the matching attributes.
* A **mutator (setter)** is a method that **changes the value of an attribute** after the object has been created. By convention it is named `SetSomething(newValue)`. For example, `SetAge(iNewAge : Integer)` updates the `iAge` attribute.
* An **accessor (getter)** is a method that **returns the value of an attribute** to the outside world. By convention it is named `GetSomething` (or `IsSomething` for booleans). For example, `GetName : String` returns the stored name; `IsActive : Boolean` returns the active flag.

### How a UML class diagram is laid out

A UML class diagram is divided into three horizontal sections:

```
┌──────────────────────────────────────────────┐
│ TClassName                                   │   <- Section 1: class name
├──────────────────────────────────────────────┤
│ - fAttribute1 : Type                         │
│ - fAttribute2 : Type                         │   <- Section 2: attributes
│ - fAttribute3 : Type                         │
├──────────────────────────────────────────────┤
│ + Create(p1 : Type; p2 : Type)               │
│ + GetAttribute1 : Type                       │   <- Section 3: methods
│ + SetAttribute2(pNew : Type)                 │
│ + SomeAction : Type                          │
└──────────────────────────────────────────────┘
```

* **Minus signs (`-`)** indicate **private** members — only methods of this class can access them.
* **Plus signs (`+`)** indicate **public** members — accessible from outside the class.
* Each attribute line shows the attribute name and its data type, separated by a colon.
* Each method line shows the method name, the parameters in brackets, and (for functions) the return type after a colon.

Reading the diagram in this order — class name first, then attributes, then methods — gives a complete summary of what the class can do and what data each object holds.

## 4.4 Validation Types

Different types of validation suit different kinds of input:

* **Range check** — confirms the value falls within an allowed range. *Most appropriate for attributes that must lie between two limits, such as a percentage (0–100) or a rating (1–5).*
* **Length check** — confirms the input has the required number of characters. *Most appropriate for fixed-length fields, such as an SA ID number (exactly 13 digits) or a country code (exactly 3 letters).*
* **Type check** — confirms the value is the right data type (no letters in a number field, no symbols where only digits are allowed).
* **Presence check** — confirms a compulsory field has been filled in.
* **Format check** — confirms the input matches a required pattern (e.g. an email address contains an `@`, a phone number contains only digits and spaces).

For a value that must be one of a small fixed set of options (e.g. a number from 1 to 5, or one of three categories), the appropriate **input component** is a **SpinEdit** or a **ComboBox / RadioGroup** with the valid options pre-loaded — both restrict the user to valid input from the start, so validation only has to confirm that *something* was selected.

## 4.5 Boolean Logic

A complex condition can be built using **AND**, **OR** and **NOT** combined with parentheses to control the order of evaluation. Each part must be evaluated true or false, then combined according to the standard rules:

* `AND` is true only when **both** sides are true.
* `OR` is true when **at least one** side is true.
* `NOT` inverts the value (turns True into False and False into True).

### Truth tables

| A | B | A AND B | A OR B | NOT A |
|---|---|---|---|---|
| True  | True  | True  | True  | False |
| True  | False | False | True  | False |
| False | True  | False | True  | True  |
| False | False | False | False | True  |

### Combining conditions with parentheses

When a condition mixes AND and OR, parentheses are essential to make the intended grouping clear. Without parentheses, AND has higher precedence than OR (just like multiplication has higher precedence than addition in arithmetic) — so the meaning can change unexpectedly.

For example, the condition "A is true, **and** either B or C is true" must be written:

```
A AND (B OR C)
```

Without the brackets, `A AND B OR C` is read as `(A AND B) OR C`, which has a completely different meaning.

### Working through a compound condition

A typical compound condition combines two or three simple tests:

```
(iAge >= 18) AND (rHeight >= 150) AND (bHasLicence OR iYearsExperience >= 5)
```

This says: the person qualifies if **all three** of the following are true:

1. They are **at least 18 years old**.
2. They are **at least 150 cm tall**.
3. **Either** they have a licence (`bHasLicence = True`) **or** they have **at least 5 years of experience**.

If `iAge = 25`, `rHeight = 160`, `bHasLicence = False`, `iYearsExperience = 7`, then:

* Test 1: `25 >= 18` is **True**.
* Test 2: `160 >= 150` is **True**.
* Test 3: `bHasLicence OR iYearsExperience >= 5` → `False OR True` → **True**.
* All three are True → the overall expression is **True**.

**Common trap**: pay close attention to whether the operator is `>` (strict) or `>=` (inclusive). A value of `18` satisfies `iAge >= 18` but does *not* satisfy `iAge > 18`.

## 4.6 Types of Errors

Programs can fail in three different ways:

* **Syntax errors** — the code breaks the rules of the language (e.g. missing semicolon, misspelled keyword). The compiler catches these *before* the program can run.
* **Runtime errors** — the program is syntactically fine but crashes while running (e.g. division by zero, trying to access an item past the end of an array). The program stops with an error message at the point of failure.
* **Logical errors** — the program compiles, runs to completion without crashing, but **produces the wrong result** because the logic is incorrect. The computer does exactly what the programmer told it to do — but what the programmer told it to do was wrong.

### Worked example — a logical error

Consider a piece of code where the programmer wanted to use random letters A–Z, but wrote:

```pascal
sLetters[RandomRange(1,26)]
```

`RandomRange(1,26)` in Delphi returns a random integer from 1 up to but **not including** 26 — in other words, 1 to 25. So the letter at position 26 (which is 'Z') is **never** selected, and the output never contains the letter Z.

This is a **logical error**: the program runs fine and prints output, but the output is subtly wrong. The correct call would have been `RandomRange(1,27)` to include 26, or `Random(26)+1`.

## 4.7 Arrays

### One-dimensional array

A **one-dimensional array** is a numbered list of values, all of the same data type, accessed by an index. Example declaration:

```pascal
var
   arrColours : array [1..6] of String;
   arrMarks   : array [1..30] of Integer;
   arrPrices  : array [1..100] of Real;
```

Each element is accessed by writing the array name and the index in square brackets — `arrColours[1]` is the first item, `arrColours[2]` the second, and so on.

### Two-dimensional array

A **two-dimensional array** is a grid (rows × columns) of values of the same type — like a spreadsheet. It is accessed with two indexes: `arr[row, col]`.

Example: a 10 × 20 grid of single characters (for example, a word-search puzzle, a Sudoku board, a tile map, or a pixelated image) can be stored in:

```pascal
var
   arrGrid : array [1..10, 1..20] of Char;
```

A 2D array of integers, useful for a numeric grid such as a class register:

```pascal
var
   arrMarks : array [1..30, 1..5] of Integer;       // 30 learners × 5 subjects
```

### Storing each character of a string into a row of a 2D array

To store the contents of `sLine` (an N-character string) into row `k` of a 2D character array:

```pascal
for j := 1 to N do
   arrGrid[k, j] := sLine[j];
```

### Advantages of a 2D array over a string of strings

* **Individual cells can be read or changed by row and column directly** — `arrGrid[3, 5]` gives the character at row 3, column 5 instantly. Doing the same with rows stored as separate strings would mean working out the right string and the right position inside it every time. A 2D array makes grid-style algorithms (e.g. checking if a word fits horizontally at row R, column C) much cleaner.
* The structure mirrors the real-world grid, making the code easier to read.
* Each cell stores exactly one character of the correct type (`Char`), rather than the whole row as a less precise `String`.

## 4.8 Permanent Storage of Program Data

When data must be kept **after the program ends and even after the computer is switched off**, the program must save it to a non-volatile data structure. Options include:

* **Text file** — the simplest option, good for plain readable data, easy to inspect with Notepad.
* **Binary file / structured file** — more efficient for large amounts of typed data.
* **Database** — best when the data is structured, large, related and must support queries and multiple users.

For permanently storing readable data such as reports, logs, generated content, or simple lists, a **text file** is usually the most appropriate choice — it is simple, can be opened in any text editor or printer, and is easy for the program to write and read back later.

### Note on loop placement

A common bug to look out for: if a `Lines.Add(sLine)` call is moved to **after** the end of the loop that builds the value of `sLine`, then `sLine` is added only **once** — and only the *last* value will appear in the output, instead of every value the loop produced. Each iteration's result must be added **inside** the loop, after the value for that iteration has been built.

---

# SECTION 5: SOCIAL IMPLICATIONS, CYBERSECURITY AND INTEGRATED TOPICS

## 5.1 Cybercrime — Common Threats

### Ransomware

**Ransomware** is a type of malicious software (malware) that **encrypts the victim's files and then demands a ransom payment** (usually in cryptocurrency) in exchange for the decryption key that would unlock the files. Until the ransom is paid (or the files are restored from a clean backup), the victim cannot access their own data.

Ransomware typically enters a system through a phishing email attachment, a malicious download, or by exploiting a security vulnerability in unpatched software. Defences include keeping software up to date, training users to recognise phishing, restricting permissions on file servers, and (most importantly) maintaining **separate, offline backups** so that files can be restored without paying the criminals.

### Social engineering

**Social engineering** is the use of **psychological manipulation to trick people into revealing confidential information or doing something they would not normally do**. Instead of attacking the *computer*, the attacker attacks the *user*. Examples include phishing emails, fake "IT support" phone calls and impersonation scams.

**Possible consequence of falling victim to social engineering**: financial loss (stolen banking details, fraudulent transactions), identity theft, unauthorised access to accounts (the attacker now has the user's password), exposure of confidential company data, or installation of malware on the company network. A single successful social engineering attack against one employee can lead to a major data breach affecting the whole organisation.

### Spam

**Spam** is **unsolicited email sent in bulk to many recipients**, usually advertising products or services that the recipient did not ask to be told about. Most spam is harmless but annoying; some spam is part of phishing or malware-delivery campaigns.

### Worm vs Trojan

These two terms are often confused:

* A **worm** is a malicious program that **copies itself and spreads automatically from computer to computer across a network**, without needing a user to run it.
* A **Trojan (Trojan horse)** is a malicious program **disguised as something useful** — a game, a free utility, a video file — that the user is tricked into running. Once running, it performs harmful actions in the background.

A common exam trick is to claim "a worm is a malicious program disguised as something useful" — that is **false**. A *Trojan* is disguised as something useful; a *worm* spreads through a network on its own.

## 5.2 Internet of Things (IoT)

The **Internet of Things (IoT)** is the network of everyday physical objects that have been fitted with sensors, software and internet connectivity, so that they can **collect data and exchange it with each other and with central systems**. Examples include smart watches, smart fridges, smart light bulbs, wearable medical devices, and industrial sensors in factories and warehouses.

### A technology that enables IoT

Several technologies enable IoT — for example:

* **Wireless connectivity** (Wi-Fi, 5G, Bluetooth, LoRaWAN) — allows devices to talk to each other and to the cloud without cables.
* **Cloud computing** — provides the storage and processing power to handle the enormous amount of data IoT devices generate.
* **Embedded sensors** — temperature, humidity, motion, location, pressure sensors that collect the real-world data.

**Impact on supply chains and logistics**: IoT sensors allow goods to be monitored in real time as they move through warehouses, factories, transport vehicles and shops. Typical sensors include temperature sensors on refrigerated cargo (to confirm the cold chain is unbroken), humidity sensors on moisture-sensitive products, GPS trackers on shipping containers, vibration sensors on fragile loads, and RFID readers at every checkpoint. Problems — a freezer warming up, a delayed truck, a load that has been dropped — are detected the moment they happen instead of when the goods arrive damaged. This **reduces waste, improves quality, lowers costs and speeds up decision-making**.

## 5.3 Augmented Reality (AR)

**Augmented reality** is technology that **overlays computer-generated information (images, sound, text) onto the user's view of the real world**. Unlike virtual reality (which replaces reality entirely), AR enhances it. The user sees the real environment through a phone camera, tablet or AR glasses, with digital content added on top.

### How AR works in practice

A typical AR application captures the real world through the device's camera, identifies surfaces or markers in that view, and then renders computer-generated content (images, 3D objects, text, navigation arrows) on top — aligned with the real world. As the user moves the device, the overlay stays "stuck" to the real-world surface or position.

Common AR uses include:

* **Retail "virtual try-on"** — customers point a phone at themselves to see how clothing, glasses, makeup or hair colour would look on them, or at a room to see how a piece of furniture would fit.
* **Navigation** — directional arrows drawn over a live camera view of the street, guiding the user.
* **Education and training** — anatomy textbooks where a model of the human heart can be viewed and rotated in 3D over the page, or repair manuals that highlight which part to remove next.
* **Industry and design** — engineers and architects can place virtual prototypes in real environments to check fit, scale and appearance before manufacturing.
* **Gaming** — virtual creatures or objects appear in the player's real environment.

### Sensors needed for AR (besides the camera)

For AR to align digital content correctly with the real world, the device must know exactly how it is moving and where it is pointing. The key sensors apart from the camera include:

* **Accelerometer** — detects movement and direction of acceleration of the device.
* **Gyroscope** — detects rotation and orientation (tilt, pitch, yaw).
* **Magnetometer (digital compass)** — detects the direction the device is facing relative to magnetic north.
* **GPS** — needed for location-based AR (e.g. games where digital objects appear in specific real-world locations).
* **Proximity sensor** — detects how close the device is to other objects.

The accelerometer + gyroscope combination is the most important: without them, the digital overlay would not stay locked onto the real surface as the phone moves.

## 5.4 Central Server Storage — Advantages

For any system that generates a large volume of data — sensor readings in a factory, transaction logs in a shop, learner records in a school — storing the data on a **central server** has several advantages over keeping it on individual machines:

* **Centralised access** — anyone with permission can access the same data from anywhere on the network. There is one "version of the truth".
* **Easier backup and security** — one server can be backed up and secured properly. Each individual device does not need its own backup system.
* **Better processing** — a server has more storage and processing power than individual workstations, so it can handle the enormous volume of data and run analysis tasks on it.
* **Consistency** — all data is stored in one format, in one place, making reporting and analysis straightforward.

---

*End of Grade 12 Theory Notes*
