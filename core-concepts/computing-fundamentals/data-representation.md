---
layout: page
title: Data Representation
parent: Computing Fundamentals
grand_parent: Core Concepts
nav_order: 2
---

# Data Representation

{: .note }
This topic appears in Grade 10 CAPS and is built upon in Grade 11 and 12. It's frequently tested in Paper 2.

## Number Systems

Computers store all data as binary digits (bits), but humans typically work with decimal numbers. Understanding different number systems is essential for computing.

### Binary (Base 2)

Binary uses only two digits: 0 and 1.

#### Example:
The binary number `1011` equals:
- 1 × 2³ + 0 × 2² + 1 × 2¹ + 1 × 2⁰
- 8 + 0 + 2 + 1 = 11 in decimal

### Hexadecimal (Base 16)

Hexadecimal uses sixteen digits: 0-9 and A-F.

#### Example:
The hexadecimal number `1A` equals:
- 1 × 16¹ + 10 × 16⁰ 
- 16 + 10 = 26 in decimal

## Conversion Between Number Systems

### Decimal to Binary Conversion

To convert decimal to binary:
1. Divide the number by 2
2. Record the remainder
3. Repeat with the quotient until it becomes 0
4. Read the remainders from bottom to top

#### Example: Converting 13 to binary

13 ÷ 2 = 6 remainder 1
6 ÷ 2 = 3 remainder 0
3 ÷ 2 = 1 remainder 1
1 ÷ 2 = 0 remainder 1

Reading from bottom to top: 1101

### Binary to Decimal Conversion

Multiply each bit by its position value (power of 2) and sum.

#### Example: Converting 1101 to decimal
1 × 2³ + 1 × 2² + 0 × 2¹ + 1 × 2⁰
= 8 + 4 + 0 + 1
= 13

## Character Representation

Computers store text as numeric codes. Two common encoding systems are:

### ASCII

American Standard Code for Information Interchange:
- 7-bit code representing 128 characters
- Includes uppercase letters, lowercase letters, digits, and special characters

### Unicode

An extension of ASCII that includes characters from all world languages:
- UTF-8: Variable-length encoding (1-4 bytes)
- Can represent over 1 million characters

## Practice Questions

1. Convert the decimal number 25 to binary.
2. Convert the binary number 10110 to decimal.
3. Why do we use hexadecimal in computing?
4. What is the difference between ASCII and Unicode?

## Code Connection

How binary representation appears in programming:

```java
// Binary literals in Java
int binaryValue = 0b1011; // Binary for 11
System.out.println(binaryValue); // Outputs: 11

// Hexadecimal literals
int hexValue = 0x1A; // Hex for 26
System.out.println(hexValue); // Outputs: 26

##Exam Tips
In Paper 2, you might need to:

Convert between number systems
Explain the purpose of different number systems
Calculate storage requirements for different data types