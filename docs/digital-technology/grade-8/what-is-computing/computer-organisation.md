---
title: Computer Organisation
---

# Topic 2: Computer Organisation

## Introduction

A computer is not one single thing — it is a carefully organised system of components that work together. Understanding how these components are organised helps you make sense of everything else about how computers work.

At the highest level, all computer parts fall into two main categories: **hardware** and **software**.

- **Hardware** is the physical components of your computer — the things you can actually touch and hold, usually made of silicon or metal.
- **Software** is the programs that run on the computer and make it do the things you want. Software is not physical — it is instructions given to the computer.

Within these two broad categories, there are several important subcategories: **output devices**, **input devices**, **storage devices**, and **network devices**. We will look at each of these in turn.

---

## 1. Output Devices

**Output devices** are how your computer tells *you* things. They allow the computer to get information from inside the computer out into the outside world.

Behind the scenes, everything inside a computer is stored as numbers — as **digital information**. This is not very useful to humans on its own. Output devices take that digital information and transform it into physical information that you can actually understand and interact with — things like light (pictures on a screen) and sound.

For example, if the computer reads the number 28, it might display a blue pixel on the screen. If it reads the number 32, it might display a yellow pixel. The output device is taking those digital numbers and turning them into something meaningful.

:::tip Key Term
**Output device** — a device that transforms digital information stored inside the computer into physical information that a human can understand, such as images, sounds, or printed text.
:::

### Types of Output Devices

| Type of Output | Examples |
|---------------|---------|
| **Visual (screen) output** | Monitors, video cards, projectors |
| **Audio output** | Speakers, sound cards, headphones |
| **Physical output (printing)** | Laser printers, inkjet printers, 3D printers |

---

## 2. Input Devices

**Input devices** are how you give your information *to* the computer. They allow information to travel from the outside world into the computer.

Input devices take messy, physical data from the real world — things like sound, light, touch, and movement — and convert it into clean, well-formed digital data (numbers) that the computer can store and work with.

:::tip Key Term
**Input device** — a device that converts physical data from the outside world into digital data that the computer can store and process.
:::

### Interactive Input Devices

These devices convert your physical actions (touch, movement, button presses) into digital signals:

- Touchpads and trackpads
- Mice
- Keyboards
- Joysticks
- Remote controls
- Touchscreens

### Sensing Input Devices

These devices constantly monitor the outside world and capture information as digital data:

- **Scanners** — convert physical documents into digital images
- **Microphones** — store audio information as digital data
- **Digital cameras and webcams** — store visual information as digital data
- **Sensors** — measure things like altitude, direction, humidity, and temperature

:::info Real-World Example
An airplane cockpit is full of sensors (input devices) constantly gathering information such as altitude, direction, and humidity. The dials on the cockpit panel are the output devices — they receive information from those sensors and display it to the pilot in a readable form.
:::

---

## 3. Storage Devices

**Storage devices** are how your computer remembers information and stores it for later. They are the computer's memory, allowing data to be saved and retrieved.

There are two categories of storage: **primary storage** and **secondary storage**.

### Primary Storage

Primary storage is the memory the computer uses to perform its normal activity while it is switched on. When the computer is running, it is doing many calculations per second and needs a place to keep track of numbers for these quick calculations.

This memory is **cleared when the power is turned off** — it needs electricity to hold its data.

This type of memory is called **RAM**, which stands for **Random Access Memory**. It is very fast to access, but it is constantly changing and only works while the computer is on.

:::tip Key Term
**RAM (Random Access Memory)** — the primary storage of a computer, used for quick calculations while the computer is running. It is very fast but loses all its data when the power is switched off.
:::

### Secondary Storage

Secondary storage is extra memory used for **persistent storage** — data that must survive whether the computer is switched on or off.

Examples of secondary storage include:
- CDs
- USB drives
- Hard drives
- Floppy discs
- Cloud storage

These devices store digital data and hold onto it permanently, even without power. You can save data to them, remove them from the computer, and retrieve the data later.

| Feature | Primary Storage (RAM) | Secondary Storage |
|---------|----------------------|------------------|
| Speed | Very fast | Slower |
| Keeps data when power is off | No | Yes |
| Examples | RAM | Hard drives, USB drives, CDs |
| Purpose | Active calculations while running | Long-term storage of files |

---

## 4. Network Devices

**Network devices** are how your computer communicates with other computers. This ability to connect computers together is one of the most important applications of computing — it is what makes the internet possible.

### How Networks Work

Computers on a network usually do not communicate directly with each other one-to-one. Instead, they connect to a central location that manages the traffic. This central machine is called a **router**.

:::tip Key Term
**Router** — the central device of a network. It receives data from computers, analyses it, and routes (forwards) it to where it needs to go. A router can also connect to other routers, linking different networks together.
:::

A router acts like a traffic controller: it receives data from computers and forwards it along to the correct destination. It can also receive data from routers on other networks, allowing different networks to be connected to each other.

### Types of Networks

**Local Area Network (LAN)**

A LAN is a small network that connects computers that are physically close to each other — for example, in the same building. A single router is usually enough to run a LAN.

:::tip Key Term
**LAN (Local Area Network)** — a network that connects computers within a small area, such as a single building, using one router.
:::

**Wide Area Network (WAN)**

A WAN connects computers that are very far apart. To do this, it uses multiple routers and special cables that can span long distances. A WAN is usually made up of several smaller LANs connected together.

:::tip Key Term
**WAN (Wide Area Network)** — a network that connects computers across large distances, using multiple routers and often made up of several connected LANs.
:::

:::info
The **internet** is the world's largest wide area network. It connects your computer to all other computers by linking together millions of smaller networks, with routers directing the data from place to place.
:::

### How Computers Connect to a Router

There are two main ways a computer connects to a router:

1. **Ethernet port** — allows an ethernet cable to be physically attached to your computer, sending information through that cable to the router.
2. **Wireless internet card (Wi-Fi card)** — allows your computer to connect to the router by sending and receiving radio waves, without any physical cable.

| Network Device | Purpose |
|---------------|---------|
| **Router** | Receives and forwards data between computers and networks |
| **Ethernet port** | Physical connection to a router using a cable |
| **Wi-Fi card** | Wireless connection to a router using radio waves |

---

## 5. Summary: Categories of Computer Components

| Category | What it does | Examples |
|----------|-------------|---------|
| **Output devices** | Turn digital information into physical information humans can use | Monitor, speakers, printer |
| **Input devices** | Convert physical data from the real world into digital data | Keyboard, mouse, microphone, camera, sensors |
| **Primary storage** | Fast, temporary memory used while the computer runs | RAM |
| **Secondary storage** | Permanent storage for long-term data | Hard drive, USB drive, CD, cloud storage |
| **Network devices** | Allow computers to communicate with each other | Router, ethernet port, Wi-Fi card |

---

## Check Your Understanding

1. What are the two main categories that all computer parts fall into? Describe the difference between them.

2. What is an output device? Give **three** examples and explain what physical information each one produces.

3. Explain what an input device does. Why is it necessary to convert physical data into digital data?

4. Give **two** examples of sensing input devices and explain what each one measures or captures.

5. What is the difference between primary storage and secondary storage? Give one example of each.

6. What does RAM stand for? Why does RAM lose its data when the computer is switched off?

7. What is a router, and what role does it play in a network?

8. Explain the difference between a LAN and a WAN. Give an example of where each type of network would be used.

9. Name **two** ways a computer can physically connect to a router, and briefly describe how each works.

10. Look at the following devices and classify each one as an input device, output device, primary storage, secondary storage, or network device:
    - A USB flash drive
    - A microphone
    - A projector
    - A Wi-Fi card
    - RAM
    - A webcam
    - A speaker
    - A hard drive
