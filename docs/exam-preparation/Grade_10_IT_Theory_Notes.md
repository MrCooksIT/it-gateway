# Grade 10 Information Technology — Theory Study Notes

*A topic-by-topic reference for CAPS Information Technology theory.*

These notes follow the CAPS topic order: System Technologies → Communication and Network Technologies → Data and Information Management → Solution Development. Each topic is explained in full so the notes can be used as standalone study material for any examination.

---

# SECTION 1: SYSTEM TECHNOLOGIES

## 1.1 Computing Devices

A **computing device** is any electronic device that can accept input, process data according to a set of instructions, store data, and produce output. The word "computer" no longer refers only to a desktop PC — it includes laptops, tablets, smartphones, smartwatches, gaming consoles, smart TVs, and even devices like ATMs and modern motor vehicles.

### Convergence devices

A **convergence device** is a single device that combines the functions of several separate devices into one. The clearest example is the modern smartphone: a single device that replaces a telephone, camera, video camera, calculator, music player, alarm clock, GPS, web browser, gaming console and torch. Other examples include smart TVs (TV + internet browser + streaming platform) and modern game consoles (gaming + streaming + web browser + media player).

### Advantages and disadvantages of using computers

Computers have transformed how people work, learn and communicate, but the benefits come with costs.

Advantages include faster processing of large amounts of data, accurate calculations, the ability to store and quickly retrieve enormous amounts of information, easy global communication, and the automation of repetitive tasks so that people can focus on more creative work.

Disadvantages include the high cost of equipment and software, the dependency that develops (when systems fail, work stops completely), health issues from prolonged use such as eye strain and repetitive strain injuries, the loss of jobs through automation, increased exposure to cybercrime, and the social impact of reduced face-to-face interaction.

## 1.2 Hardware

### Input and output devices

An **input device** allows the user (or the environment) to give data and instructions to the computer. Common examples are the keyboard, mouse, touchscreen, microphone, webcam, scanner and barcode reader.

An **output device** is used by the computer to present information to the user. Common examples are the monitor, printer, speakers and headphones.

Some devices are both input and output — a touchscreen, for example, displays output (it is a monitor) but also accepts input (you tap on it). A modem and a network card are also both input and output devices because they send and receive data.

### Storage — HDD vs SSD

Both an HDD (Hard Disk Drive) and an SSD (Solid State Drive) are used as **secondary storage** — they hold data permanently, even when the computer is switched off. The difference is in how they store data:

* An **HDD** uses spinning magnetic platters and a moving read/write head, much like an old vinyl record player. Because it has moving mechanical parts, it is slower, makes a small amount of noise, generates heat, uses more power, and is more easily damaged by being knocked or dropped.
* An **SSD** uses flash memory chips with no moving parts at all. It is much faster (boot times and program loading drop dramatically), silent, more energy-efficient, lighter, more resistant to physical shock, but is more expensive per gigabyte.

### Monitors — LCD and LED

An LCD (Liquid Crystal Display) monitor uses fluorescent (CCFL) backlighting behind the liquid crystal panel. An LED (Light Emitting Diode) monitor uses LEDs as the backlight instead.

Advantages of LED over LCD include lower power consumption, a thinner and lighter design, longer lifespan, better contrast and brighter colours, and a more environmentally friendly manufacturing process (no mercury in the backlight).

**Screen size** is measured **diagonally from corner to corner of the visible screen**. A "17.3 inch" monitor means the diagonal distance across the screen is 17.3 inches (about 44 cm). Screen size is not the same as resolution — a small screen can have a very high resolution, and a large screen can have a low resolution.

### Barcode scanners

A **barcode scanner** is an input device that reads the parallel black-and-white lines printed on product labels, book covers, packages and many other items. It works by shining a light onto the barcode and measuring the reflection — the white spaces reflect more light than the black bars. The scanner converts this pattern into the number the barcode represents and sends that number to the computer.

Benefits of using barcode scanners include:

* Speed — scanning is much faster than typing a long product/identification number.
* Accuracy — there are no typing errors, so the wrong item is never recorded.
* Automation — once an item is scanned, the database can be updated immediately (e.g. stock count reduced, item marked as sold, or item marked as out on loan).

### Upgrading for performance

When a computer is slow at running many programs at the same time, the component to upgrade is usually the **RAM**. RAM is the working memory where all open programs and their data must sit while the CPU uses them. If there is not enough RAM, the operating system has to swap data constantly between RAM and the (much slower) storage drive, which causes the computer to feel sluggish.

### Webcams and video conferencing

Most modern laptops have a small **webcam** built into the top of the screen bezel, together with a microphone. The webcam captures video and the microphone captures audio, which together allow the laptop to be used for video conferencing (Zoom, Microsoft Teams, Google Meet) without buying any extra hardware.

## 1.3 System Software and the Operating System

### What system software is

**System software** is the software that controls and manages the computer's hardware so that the user and application software (like Word or Chrome) can actually use it. It is the "middleman" between the hardware and the application programs.

System software includes:

* the **operating system** (e.g. Windows 11, macOS, Linux, Android)
* **utility programs** (antivirus, disk defragmenter, file compression, backup tools)
* **device drivers**

Examples of operating systems include Windows 11, macOS, Linux distributions like Ubuntu, Android (for phones) and iOS (for iPhones). Microsoft Word, Google Chrome and Adobe Photoshop are *not* operating systems — they are application software that runs on top of the operating system.

### The purpose of the operating system

The main purpose of an operating system is to **manage the hardware and software resources of the computer**. This includes:

* providing a user interface so the user can interact with the computer
* managing memory (deciding which programs get RAM and how much)
* managing the CPU (scheduling which program runs when)
* managing storage (organising the file system)
* managing input and output devices
* providing security (user accounts, passwords, permissions)

### Device drivers

A **device driver** is a small program that allows the operating system to communicate with a specific hardware device. Each device that the computer connects to (printer, scanner, graphics card, webcam, etc.) needs its own driver because each manufacturer designs its hardware slightly differently.

Device drivers are important because without the correct driver, the operating system simply does not know how to "talk to" the hardware. The device might be physically connected and powered on, but it will not work. A printer is a typical example — even though it is plugged in, it will not print until the driver is installed.

### Plug-and-Play and hot-swappable devices

**Plug-and-Play (PnP)** is a technology that allows the operating system to automatically detect a new hardware device when it is connected, identify it, and load the correct driver — all without the user needing to manually install anything. A printer that "just works" the moment you plug it in is using Plug-and-Play.

The advantage is that the user does not need any technical knowledge to add new hardware. The device is ready to use within seconds.

A **hot-swappable** device is one that can be safely connected to (or disconnected from) the computer while the computer is switched on and running. A USB flash drive is the classic example — you can plug it in and pull it out without restarting. Older technologies were *not* hot-swappable — adding a hard drive used to require shutting the machine down completely first.

## 1.4 Proprietary vs Open-Source Software

When choosing software, users have to decide between **proprietary software** and **open-source software**.

* **Proprietary software** (e.g. Microsoft Office, Adobe Photoshop) is owned by a company. Users must pay for a licence to use it. The source code is kept secret and may not be changed by the user.
* **Open-source software** (e.g. LibreOffice, Linux, GIMP) is software whose source code is freely available. Anyone may use, copy, study and modify the code. It is usually free of charge.

**Comparison of support:**

* Proprietary software comes with **official paid support** from the company that makes it — phone help desks, online ticket systems, official documentation. The support is usually reliable and professional, but is part of what you pay for.
* Open-source software relies mainly on **community support** — online forums, user groups, wikis and volunteers. Help is free but can be slow and inconsistent. Some open-source projects offer paid commercial support as an add-on.

---

# SECTION 2: COMMUNICATION AND NETWORK TECHNOLOGIES

## 2.1 Computer Networks

A **computer network** is a group of two or more computing devices that are connected together so that they can share data, resources (like printers and storage) and an internet connection.

**Communication media** is the physical or wireless pathway that the data travels along. Examples of wired media include UTP (twisted-pair copper) cables, coaxial cables and fibre-optic cables. The most common wireless medium is Wi-Fi, which uses radio waves; others include Bluetooth, infrared and cellular (3G/4G/5G).

### Advantages of using a computer network

* **Sharing of resources** — many users can share one printer, one internet connection, one set of files, instead of each computer needing its own.
* **Communication** — users can send each other messages, emails, files and video calls easily.
* **Centralised data** — files can be stored in one central location, making backup and access easier.
* **Cost saving** — sharing one printer between 30 computers is much cheaper than buying 30 printers.

### LAN vs WAN

A **LAN (Local Area Network)** is a network that covers a small geographic area, typically a single building or campus. The network in a school, in an office or in a home is a LAN. The owner of the network usually owns all the cables and equipment.

A **WAN (Wide Area Network)** is a network that covers a large geographic area, often connecting many LANs together across cities, countries or continents. The internet is the largest WAN in the world. A WAN typically uses cables, equipment and services that are owned and rented from telecommunications companies.

The network used **within a school building** is a LAN.

## 2.2 Network Hardware

### Routers

A **router** is a network device that connects two or more networks and routes (directs) data packets between them. In a typical home or school, the router connects the local network (LAN) to the internet (WAN). It looks at the address of every data packet and decides which network and which device it must be sent to.

### Functions of network communication

Network communication exists to allow:

* **Resource sharing** — printers, storage and internet connections can be used by many devices.
* **Data sharing** — files and information can be sent between users.
* **Centralised management** — a server can store files, manage user accounts, and enforce security policies for all the devices on the network.
* **Communication services** — email, video calls and instant messaging all rely on networks.

## 2.3 Network Security

Security is important in network communication because data travelling across a network is vulnerable to interception, theft and tampering. Without security:

* Personal information (passwords, ID numbers, banking details) can be stolen and used for fraud.
* Confidential business or organisational information can be leaked or sold.
* Attackers can install malware on devices on the network.
* The organisation's network and devices can be hijacked to attack other networks.

### Risks of using public Wi-Fi

When someone uses a public Wi-Fi network (in a coffee shop, mall, airport or hotel) to access email or any sensitive service:

* Data sent over the connection is often not encrypted, so an attacker on the same Wi-Fi can capture passwords and emails.
* Fake "hotspot" networks (named to look legitimate) can be set up by criminals to harvest user data — this is called an "evil twin" attack.
* Malware can be pushed onto the device through the open connection.

**Precautions** to reduce these risks include using a VPN to encrypt all traffic, only accessing sites that use HTTPS, turning off "automatic connection to Wi-Fi", avoiding banking and sensitive logins on public networks, and using two-factor authentication on email accounts.

## 2.4 Key Network Terms

### IP address

An **IP address (Internet Protocol address)** is a unique numerical address that identifies a device on a network. Just as every house in a street needs a unique street address so that the post office can deliver mail to the correct house, every device on a network needs a unique IP address so that data can be delivered to the correct device.

The most common form (IPv4) consists of **four sets of digits separated by dots**, for example `192.168.1.10`. Each of the four numbers can be between 0 and 255.

### Bandwidth

**Bandwidth** is the maximum amount of data that can be transferred over a network connection in a given amount of time. It is typically measured in megabits per second (Mbps) or gigabits per second (Gbps). A higher bandwidth means more data can flow at the same time — like a wider road letting more cars through at once.

A connection with low bandwidth feels slow when many people try to use it at the same time, when streaming video, or when downloading large files.

### Protocol

A **protocol** is a set of rules that governs how data is transmitted and received across a network. Two devices can only communicate if they both "speak" the same protocol — in the same way that two people can only have a conversation if they both speak the same language. Examples include HTTP and HTTPS (for web pages), SMTP (for sending email), POP3 and IMAP (for receiving email), and FTP (for file transfer).

### Modem

A **modem** (modulator-demodulator) is a device that converts the digital signals used by a computer into analogue signals that can travel over a telephone line, and then converts incoming analogue signals back into digital signals. Modems were essential when home internet was delivered over phone lines; today, most "modems" supplied by ISPs are actually combined modem-router units.

## 2.5 Internet Safety

### Phishing

**Phishing** is a type of online scam where attackers send fake emails, SMS messages or create fake websites that look like they come from a legitimate source (a bank, the school, Microsoft, etc.). The goal is to **trick users into giving personal information** — usernames, passwords, ID numbers, banking details — through fake login pages.

Phishing is *not* the same as illegally copying software (that is **piracy**) and not the same as viruses (which are malicious *programs*).

---

# SECTION 3: DATA AND INFORMATION MANAGEMENT

## 3.1 Units of Data

The smallest unit of data in a computer is the **bit** (binary digit). A bit can only have one of two values: 0 or 1.

A **byte** consists of **8 bits**. Because each bit can be either 0 or 1, a single byte can represent **2⁸ = 256** different unique combinations. A byte is large enough to store a single character of text (a letter, a digit or a symbol) using a coding system like ASCII or Unicode.

Larger units are built up from bytes:

* 1 kilobyte (KB) = 1 024 bytes
* 1 megabyte (MB) = 1 024 KB
* 1 gigabyte (GB) = 1 024 MB
* 1 terabyte (TB) = 1 024 GB

## 3.2 Number Systems

Computers use different number systems depending on the task. The three you must know are:

* **Decimal (base 10)** — the everyday system humans use, with digits 0–9.
* **Binary (base 2)** — the system computers actually use internally, with only two digits: 0 and 1.
* **Hexadecimal (base 16)** — a short-hand system used by programmers, with digits 0–9 and letters A–F (where A = 10, B = 11, C = 12, D = 13, E = 14, F = 15).

### Binary to Decimal

Each position in a binary number represents a power of 2, starting from the right. Write the place values above the bits, then add up the place values where there is a 1.

**Example: Convert 10101100₂ to decimal**

| Place value | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
|---|---|---|---|---|---|---|---|---|
| Binary digit | 1 | 0 | 1 | 0 | 1 | 1 | 0 | 0 |

Add only the place values where the binary digit is 1:
128 + 32 + 8 + 4 = **172**

### Decimal to Binary

Use the "place value subtraction" method or "successive division by 2" method.

**Example: Convert 198 to binary**

Using place value subtraction (largest power of 2 that fits, then subtract, then repeat):

| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
|---|---|---|---|---|---|---|---|
| 1 | 1 | 0 | 0 | 0 | 1 | 1 | 0 |

Working: 198 − 128 = 70 → 70 − 64 = 6 → 6 − 4 = 2 → 2 − 2 = 0
So we have 1s at the 128, 64, 4 and 2 positions.

Answer: **11000110₂**

### Hexadecimal to Decimal

Each position is a power of 16, starting from the right. Multiply each digit by its place value, then add.

**Example: Convert 1F7₁₆ to decimal**

| Place value | 256 | 16 | 1 |
|---|---|---|---|
| Hex digit | 1 | F (=15) | 7 |

(1 × 256) + (15 × 16) + (7 × 1) = 256 + 240 + 7 = **503**

### Decimal to Hexadecimal

Successively divide by 16 and record the remainders, reading them from bottom to top.

**Example: Convert 289 to hexadecimal**

* 289 ÷ 16 = 18 remainder 1
* 18 ÷ 16 = 1 remainder 2
* 1 ÷ 16 = 0 remainder 1

Reading the remainders from bottom to top: **121₁₆**

## 3.3 Data Types

A **data type** tells the computer what kind of data is being stored and how much memory to reserve for it. The main primitive data types you must know are:

* **Integer** — whole numbers (positive or negative) with no decimal part. Used for counting things. Example: number of items in a list, number of people in a group, age in completed years.
* **Real / Float** — numbers with a decimal part. Used for measurements and calculations that need fractions. Example: a temperature like 23.5 °C, a price like 15.95, a height in metres.
* **Boolean** — a value that can only be **True** or **False**. Used for yes/no questions. Example: "Is the device connected to the internet?", "Has the user accepted the terms?"
* **Char** — a single character (one letter, digit or symbol). Example: 'K', 'A', '7', '$'.
* **String** — a sequence of characters that form text. Example: "Hello123", a person's name, an address.

Selecting the right data type matters because the wrong choice wastes memory, can cause calculation errors (e.g. trying to do arithmetic on a string), or makes validation impossible.

---

# SECTION 4: SOLUTION DEVELOPMENT

## 4.1 Algorithms

An **algorithm** is a step-by-step set of instructions that solves a particular problem or completes a particular task. A recipe is an everyday example of an algorithm. In programming, every program starts as an algorithm before any code is written.

### Criteria for a well-designed algorithm

A good algorithm must meet the following criteria:

* **Finiteness** — it must always end after a finite number of steps. An algorithm must not loop forever.
* **Definiteness** — every step must be clear and unambiguous. There must be no doubt about what to do at each step.
* **Input** — it must accept zero or more clearly-defined inputs.
* **Output** — it must produce at least one clearly-defined output (the answer to the problem).
* **Effectiveness** — every step must be basic enough that it can actually be carried out.

### "Order" vs "Precision" in an algorithm

* **Order** refers to the **sequence** of the steps — they must be carried out in the correct order. Frying an egg before cracking the shell does not work.
* **Precision** refers to **how exactly** each step is described — each step must be specific and unambiguous, so that the same algorithm produces the same result every time it is followed.

## 4.2 The IPO Table

An **IPO (Input – Processing – Output) table** is a planning tool used before writing code. It forces the programmer to think clearly about three things:

* **Input** — what data the program needs from the user (or another source) to do its job.
* **Processing** — what calculations or decisions must be performed on the input.
* **Output** — what the program must show to the user as a result.

**Example: Calculate the surface area of a sphere — formula 4 × π × r²**

| Input | Processing | Output |
|---|---|---|
| The radius (r) of the sphere | Surface area = 4 × π × r × r | The surface area of the sphere |

## 4.3 Pseudocode

**Pseudocode** is a way of writing out an algorithm using a mixture of plain English and basic programming-style keywords (`IF … THEN … ELSE`, `WHILE`, `INPUT`, `OUTPUT`). It is not real code — it cannot be run on a computer — but its structure makes it easy to translate later into any actual programming language.

**Example: Profit / Loss / Break-even calculator**

A company makes a profit when income > expenses, a loss when income < expenses, and breaks even when income = expenses.

```
START
    INPUT income
    INPUT expenses
    IF income > expenses THEN
        OUTPUT "Profit"
    ELSE IF income < expenses THEN
        OUTPUT "Loss"
    ELSE
        OUTPUT "Break-even"
    END IF
END
```

The pseudocode above shows three of the most important programming concepts: **input** (getting data from the user), **selection** (the IF / ELSE structure that chooses between alternatives) and **output** (displaying results).

---

*End of Grade 10 Theory Notes*
