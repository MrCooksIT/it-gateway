---
title: Software
---

# Topic 3: Software

## Introduction

Hardware on its own does nothing — it is just metal and silicon sitting there. **Software** is what brings a computer to life. Software contains the instructions that tell the computer exactly what to do and how to do it. Without software, hardware is useless.

:::tip Key Term
**Software** (also called programs or applications) — instructions that run on a computer and tell it what to do. Software is how the computer does the useful things we want it to do.
:::

There are two main types of software: **user application software** and **system software**. Understanding the difference between them, and how they relate to each other, is key to understanding how computers work.

---

## 1. The Software Hierarchy

There is a clear hierarchy inside your computer — each layer depends on the layer below it:

1. **Hardware** — the physical machine (the CPU, discs, mouse, printer, etc.). Hardware does not do anything on its own; it needs instructions.
2. **System software** — programs installed on the hardware that help the computer perform its own internal tasks. System software sits between the hardware and everything else.
3. **Application software** — programs that you install and use to do cool things like play games, write papers, or browse the internet. Application software depends on the system software to do its job.

:::info
The user interacts directly only with **application software**. System software works behind the scenes — the user does not directly interact with it. But without system software, application software cannot function.
:::

---

## 2. User Application Software

**User application software** (often just called "apps") are programs that you install on your computer to accomplish tasks. You go out, find them, install them, and then use them.

:::tip Key Term
**User application software** — programs installed by the user that allow them to accomplish specific tasks, such as writing, gaming, browsing the web, or sending messages.
:::

Application software enables you to do things like:
- Send a message or write an email
- Write a paper for class
- Play a game
- Browse the internet

These programs are written by programmers and published so that anyone can install them on their own computers.

### Examples of User Application Software

| Category | Examples |
|----------|---------|
| **Games** | Minecraft, FIFA, Fortnite |
| **Office applications** | Word processors, spreadsheets |
| **Web browsers** | Chrome, Firefox, Edge |
| **File explorers** | Windows Explorer, Finder (macOS) |
| **Communication apps** | WhatsApp, Gmail |

---

## 3. System Software

**System software** are programs that run on the computer to help the computer itself perform its tasks — not to help you directly, but to help the machine operate correctly.

:::tip Key Term
**System software** — programs that help the computer perform its own internal tasks. System software acts as a layer between the hardware and the user application software.
:::

System software handles tasks like:
- Helping the computer access memory
- Saving and loading files
- Handling multiple tasks running at the same time
- Turning the computer on and off properly

### Examples of System Software

| System Software | What It Does |
|----------------|-------------|
| **Boot program** | Loads the operating system into main memory when the computer is first turned on |
| **BIOS** (Basic Input/Output System) | Manages communication between the input/output devices and the operating system |
| **Device drivers** | Software for a specific input or output device that tells it how to function |

---

## 4. Operating Systems

The most important example of system software is the **operating system**. The operating system makes your computer usable — it makes the computer *operate*.

:::tip Key Term
**Operating system (OS)** — the most important piece of system software. It sits between the user applications and the hardware, managing all the computer's resources and making the hardware usable by applications and the user.
:::

The operating system sits between the user applications and the hardware. User applications cannot directly access the printer, the mouse, or other hardware devices — they must ask the operating system for permission, and the OS handles communication with the hardware.

### What the Operating System Does

| Task | Description |
|------|-------------|
| **Manages user applications** | Controls which programs can run and gives each one the resources it needs |
| **Memory allocation** | Divides RAM between different applications so they can all run without interfering with each other |
| **Multitasking** | Allows multiple applications to run on your computer at the same time |
| **Graphical user interface (GUI)** | Provides the visual desktop — icons, windows, and menus — so you can interact with the computer using a mouse instead of typing text commands |

:::info
Before graphical user interfaces existed, users had to type commands into a text-based console to give the computer instructions. The GUI, provided by the operating system, is what allows you to click on icons, drag windows around, and interact with the computer visually.
:::

### Common Operating Systems

| Operating System | Notes |
|-----------------|-------|
| **Microsoft Windows** | The most widely used desktop operating system |
| **Apple macOS (OS X)** | Used on Apple Mac computers |
| **Linux** | Free, open-source; popular on servers and among developers |
| **UNIX** | An older, powerful OS that influenced both Linux and macOS |

---

## 5. Programs

In addition to user application software and system software, there is a third way we use the word "software" — **programs**.

A **program** is a small piece of code that a user writes to perform a very specific task. It is not necessarily published for others to install; it is simply instructions written to solve a particular problem.

:::tip Key Term
**Program** — a set of specific instructions for the computer, written by a programmer using a programming language to perform a particular task.
:::

Examples of things a user might write as a program:
- Visualise music
- Send a reminder at a certain time
- Process a large dataset and find the biggest number in it

### Programming Languages

Programs are written in a **programming language** — a human-readable way to write computer instructions.

:::tip Key Term
**Programming language** — a formal language that programmers use to write instructions for a computer. It is human-readable and gets translated into instructions the computer can follow.
:::

Examples of programming languages include:
- **C**
- **Java**
- **JavaScript**
- **Python**

There are many, many programming languages, and new ones are created every year. In this course, you will learn to use a programming language to write your own programs — you will actually make your own software.

---

## 6. How Software Layers Work Together

The diagram below shows how hardware, system software, and application software depend on each other:

```
┌────────────────────────────────┐
│      USER APPLICATION          │  ← What you interact with (games, browsers, etc.)
│         SOFTWARE               │
├────────────────────────────────┤
│        SYSTEM SOFTWARE         │  ← Manages the hardware for applications
│    (Operating System, BIOS,    │
│       device drivers)          │
├────────────────────────────────┤
│          HARDWARE              │  ← The physical machine
│   (CPU, RAM, printer, mouse)   │
└────────────────────────────────┘
```

- The **hardware** is the foundation — it cannot do anything without instructions.
- The **system software** runs directly on the hardware and manages it, acting as a bridge.
- The **user application software** runs on top of the system software and uses it to access the hardware indirectly.

---

## Check Your Understanding

1. What is software? Explain why hardware cannot do anything useful without software.

2. Describe the three layers of the software hierarchy. What does each layer do, and what does it depend on?

3. What is user application software? Give **three** examples of user applications and describe what each one does.

4. What is system software? Explain how it is different from user application software.

5. Why does a user application need to ask the operating system to do things with the hardware, rather than accessing the hardware directly?

6. What is the BIOS? What role does it play when you first turn on your computer?

7. What is a device driver? Give an example of a device that would need a driver and explain why.

8. Name **four** things an operating system is responsible for managing on your computer.

9. What is a graphical user interface (GUI)? How was interacting with a computer different before GUIs existed?

10. Name the **four** most common operating systems mentioned in this chapter. On what type of computer would you typically find each one?

11. What is a programming language? Why do programmers use high-level programming languages rather than writing directly in the computer's own language?
