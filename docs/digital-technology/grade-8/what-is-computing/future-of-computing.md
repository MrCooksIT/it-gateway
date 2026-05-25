---
title: Future of Computing
---

# Topic 5: Future of Computing

## Introduction

We have looked at the history of computing and how computers work today. In this chapter we look ahead — at some of the directions computing might take us in the near future. Two of the most exciting areas involve completely rethinking how computers are built (new computer architectures) and rethinking what computers are used for (artificial intelligence and its applications).

---

## 1. Traditional Computer Architecture

Before exploring what is new, it helps to understand what all computers today have in common. All traditional computers use what is called the **Von Neumann architecture**.

:::tip Key Term
**Von Neumann architecture** — the design used by all traditional computers. It is built using electronic circuit boards, uses electricity to represent binary data, is mechanical in nature (metal and silicon), and is deterministic.
:::

A traditional computer is **deterministic** — meaning that a single bit is definitely a 0 or definitely a 1. It is never both, never in between. The instructions are clear and well-defined: the computer knows exactly what to do when it sees a 0 or a 1.

In the future, we might see computers with completely different architectures. Two of the most promising (though still mostly theoretical) new approaches are **DNA computers** and **quantum computers**.

---

## 2. DNA Computers

**DNA computers** use actual biological DNA to store and process information, instead of electronic circuits.

:::tip Key Term
**DNA computer** — a type of computer that uses DNA strands and enzymes to perform computations, instead of electronic circuits.
:::

DNA computers were first introduced in **1994 by Leonard Adelman**. Here is how the core idea works:

- Instead of using high and low voltages to represent 1s and 0s, DNA computers look at DNA chemicals. For example:
  - Cytosine might be interpreted as a **1**
  - Guanine might be interpreted as a **0**
- By reading down a DNA strand, the computer can store enormous amounts of data in a tiny amount of space.

### Why Are DNA Computers Exciting?

| Feature | Traditional Computer | DNA Computer |
|---------|---------------------|-------------|
| Data storage | Limited by electronic memory size | Can store **billions of times** more data in the same space |
| Parallelism | One CPU doing one operation at a time (gives the *illusion* of parallelism) | Can process multiple DNA strands with different enzymes **simultaneously** — **true** parallelism |

:::info
Traditional computers are not actually doing multiple things at the same time. They split their time between different applications to *seem* like they are multitasking, but the CPU can only do one thing at each clock cycle. DNA computers, on the other hand, can truly process multiple strands simultaneously.
:::

DNA computers would be most useful for solving **complex mathematical problems**, not for everyday casual computing. You would not use a DNA computer to browse the internet — but you might use one to solve an extremely difficult maths problem that no traditional computer could crack in a reasonable amount of time.

---

## 3. Quantum Computers

**Quantum computers** apply the principles of quantum physics to computing, making a fundamentally different kind of machine.

:::tip Key Term
**Quantum computer** — a type of computer that uses quantum bits (qubits) instead of classical bits. Unlike a classical bit (which is strictly 0 or 1), a qubit can be 0, 1, or both at the same time.
:::

Quantum computing was first theorised by **Paul Benioff in 1981**.

### The Key Difference: Qubits

In a traditional computer, a bit is always exactly 0 or exactly 1 — it is **deterministic**. In a quantum computer, a **qubit** can be 0, 1, or in a state that is *both or neither or somewhere in between*. This property is called **superposition**.

This makes quantum computers **non-deterministic** — and it is what gives them their power.

### Advantages of Quantum Computers

- **Truly parallel** — they can perform trillions of mathematical operations per second, compared to billions for a traditional computer.
- **Non-deterministic** — qubits can represent many possibilities at once, which is enormously powerful for certain types of problems.

:::warning
Quantum computing is still mostly theoretical. A practical, large-scale quantum computer has not yet been fully realised. The research is promising, but these machines are not yet commercially available in a meaningful way.
:::

### Comparison: Traditional vs DNA vs Quantum Computers

| Feature | Traditional Computer | DNA Computer | Quantum Computer |
|---------|---------------------|-------------|-----------------|
| Basic unit | Bit (0 or 1) | DNA chemical | Qubit (0, 1, or both) |
| Deterministic? | Yes | Yes | No |
| True parallelism? | No (illusion only) | Yes | Yes |
| Operations/second | Billions | Very high | Trillions |
| Current status | Widely available | Experimental | Mostly theoretical |
| Best for | General computing | Complex maths problems | Complex maths problems |

---

## 4. What Are Computers Being Used For Today and in the Near Future?

Even without new hardware architectures, computers are already being pushed into exciting new applications — and the pace is accelerating.

### Current and Near-Future Applications

| Application | Description |
|-------------|-------------|
| **Medical diagnosis** | IBM's Watson is being used to automate medical diagnosis |
| **Data analysis** | Processing huge datasets to find patterns and insights |
| **Powerful pocket computers** | Smartphones give people enormous computing power in their pockets |
| **Modelling the universe** | Computers answer questions about how our universe is expanding |
| **Games and virtual reality** | Increasingly immersive entertainment experiences |
| **Security** | Both attacking and defending against cyber threats |
| **Self-driving cars** | Computers making real-time driving decisions |
| **Human-like robots** | Robots that can navigate environments and interact naturally |
| **Automatic language translation** | Communicating with anyone in the world regardless of language |
| **Digital currency** | Replacing physical money with electronic systems |
| **Predicting behaviour** | Modelling human and social behaviour for various purposes |
| **Modelling the human brain** | Neural networks that simulate how the brain learns |

---

## 5. Artificial Intelligence

The most significant emerging area of computing is **artificial intelligence** (AI). AI is no longer science fiction — it is a real and active field of study.

:::tip Key Term
**Artificial intelligence (AI)** — a branch of computer science dealing with the simulation of intelligent behaviour in computers. It gives machines the capability to imitate intelligent behaviour, though the machine is still running a program written by humans.
:::

It is important to understand: a computer with AI is not actually intelligent. It is still just running a program that humans wrote. But when the program runs, the computer *seems* intelligent — it behaves in ways that resemble intelligent human behaviour.

### What Counts as Intelligent Behaviour?

Computers can already do many things that seem intelligent:
- Perform complex mathematical computations
- Classify pictures (e.g. "this is a picture of a face" or "this is a picture of a cat")
- Play games — and often beat humans (e.g. chess, Go, checkers)

However, some things are still very hard for computers:
- Understanding **emotions**
- Reasoning based on **context** (e.g. detecting when someone is being sarcastic or ironic)
- Reading **body language**

:::warning
As of now, computers still need instructions and algorithms to perform tasks. They cannot think on their own. But the gap between what computers can and cannot do is closing rapidly.
:::

### Real Applications of AI

AI is already producing impressive results in many areas:

| Area | Example |
|------|---------|
| **Autopilot / self-driving** | Cars, planes, and ships that drive or navigate themselves |
| **Robots** | Robot vacuums, customer service voice menus, humanlike robots |
| **Game AI** | Computer programs that can beat humans at chess, Go, and checkers |
| **Weaponry** | Unmanned drones that use AI to navigate |
| **Natural language processing** | Converting speech to text, and text to speech; assistants like Siri and Cortana |
| **Handwriting recognition** | The US Postal Service uses AI to read handwritten addresses on letters and parcels |

:::info Real-World Example
The United States Postal Service uses an artificially intelligent program to scan letters and automatically read the digits written on envelopes — even messy handwriting from different people. This allows millions of pieces of mail to be sorted quickly and accurately.
:::

### Neural Networks and Deep Learning

One of the most exciting developments in AI is the **neural network** — an algorithm that models how the human brain works at a high level. By simulating the way neurons connect and strengthen their connections through experience, a neural network can actually *simulate learning*.

This allows computers to improve at tasks over time simply by being exposed to more examples — a capability called **deep learning**. Neural networks are what power many of the AI applications mentioned above, from face recognition to language translation.

---

## 6. Summary

| Concept | Key Idea |
|---------|---------|
| **Von Neumann architecture** | How all traditional computers are built — electronic, binary, deterministic |
| **DNA computers** | Use DNA instead of circuits; store billions of times more data; truly parallel |
| **Quantum computers** | Use qubits that can be 0, 1, or both; non-deterministic; trillions of ops/second |
| **Artificial intelligence** | Simulating intelligent behaviour using programs; still needs human-written instructions |
| **Neural networks** | Algorithms modelled on the human brain; enable computers to simulate learning |

---

## Check Your Understanding

1. What does it mean for a computer to be "deterministic"? How does this apply to traditional (Von Neumann) computers?

2. Who first introduced the concept of DNA computers, and in what year?

3. Explain how a DNA computer represents binary data differently from a traditional computer.

4. What does "true parallelism" mean? Why can DNA computers achieve it while traditional computers cannot?

5. What is a qubit, and how is it different from a classical bit?

6. Explain why quantum computers are described as "non-deterministic."

7. What type of computing problem would DNA or quantum computers be most useful for? Why are they not ideal for general everyday computing?

8. Define artificial intelligence in your own words. Give **three** real-world examples of AI that you have encountered or heard about.

9. What are **two** things computers can already do well that seem intelligent, and **two** things that computers still find very difficult?

10. What is a neural network, and what human structure does it model? What ability does it give computers?

11. **Think and discuss:** If computers can beat humans at chess and Go, and can soon drive cars on their own, does that mean computers are smarter than humans? Explain your reasoning using what you have learned about AI.
