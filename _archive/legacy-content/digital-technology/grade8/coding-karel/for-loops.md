---
layout: page
title: For Loops
parent: Introduction to Coding (JavaScript with Karel)
grand_parent: Grade 8 Digital Technology
nav_order: 8
---

# For Loops in Karel
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## The Problem with Repetitive Code

You've learned that functions are a great way to reuse code and organize programs. But what happens when you need Karel to repeat the same action many times?

Imagine you want Karel to put down 100 tennis balls. Would you write this?

```
putBall();
putBall();
putBall();
putBall();
putBall();
putBall();
putBall();
putBall();
putBall();
putBall();
// ... 90 more lines of putBall();
```

This approach has serious problems:

**Extremely Tedious**: Writing the same command 100 times is boring and time-consuming.

**Error-Prone**: You might miscount and write 99 or 101 commands instead of 100.

**Hard to Modify**: If you decide you want 150 tennis balls instead, you'd need to add 50 more lines.

**Difficult to Read**: The purpose of your code gets lost in all the repetition.

**Unprofessional**: Real programmers never write repetitive code like this.

There has to be a better way!

## Introducing the For Loop

When we want to repeat any of Karel's actions for a **fixed number of times**, we can use a **for loop**. This powerful programming structure allows us to run the same code any number of times without writing it repeatedly.

![Comparison showing repetitive code versus clean for loop code](./images/repetitive-vs-loop-code.jpg)

A for loop says: "Repeat the code between the curly braces a specific number of times."

## For Loop Structure

The structure of a for loop looks like this:

```
for(var i = 0; i < count; i++) {
    /* code to execute count times */
}
```

This might look complicated at first, but let's break down each part to understand how it works:

![For loop syntax breakdown showing each component with explanations](./images/for-loop-syntax-breakdown.jpg)

### Breaking Down the For Loop

Let's examine each part of the for loop:

**`for`** - The keyword that tells Karel this is a for loop

**`var i = 0`** - Creates a counter variable named `i` that starts at 0
- Think of this as "Start counting from 0"

**`i < count`** - Continues the loop while the counter is less than count
- Think of this as "Keep going while i is less than count"
- When i reaches count, the loop stops

**`i++`** - Increases the counter by 1 after each repetition  
- Think of this as "Add 1 to the counter each time"
- This is what makes the loop eventually stop

**`{ }`** - Contains the code that gets repeated

**How it works step by step:**
1. Start: i = 0
2. Check: Is 0 < count? If yes, run the code inside { }
3. After running code: Add 1 to i (now i = 1)
4. Check: Is 1 < count? If yes, run the code again
5. Keep repeating until i is NOT less than count

For now, you only need to change the `count` value - the rest is a formula that works the same way every time.

## Simple For Loop Examples

### Example 1: Moving 5 Times

**Without a for loop (repetitive):**
```
move();
move();
move();
move();
move();
```

**With a for loop (elegant):**
```
for(var i = 0; i < 5; i++) {
    move();
}
```

Both approaches do exactly the same thing, but the for loop is much cleaner and easier to modify.

### Example 2: Putting Down 10 Tennis Balls

```
for(var i = 0; i < 10; i++) {
    putBall();
}
```

This places exactly 10 tennis balls at Karel's current location.

### Example 3: Complex Repetition

```
for(var i = 0; i < 3; i++) {
    move();
    putBall();
    move();
    turnLeft();
}
```

This repeats the entire sequence (move, put ball, move, turn left) exactly 3 times.

## When to Use For Loops

For loops are perfect when you know **exactly how many times** you want to repeat something:

### Perfect For Loop Situations

**Building Structures**: Create towers, walls, or patterns with specific dimensions
```
// Build a tower of 8 tennis balls
for(var i = 0; i < 8; i++) {
    putBall();
    move();
    turnLeft();
}
```

**Moving Fixed Distances**: Travel a specific number of spaces
```
// Move across a 12-space field
for(var i = 0; i < 12; i++) {
    move();
}
```

**Collecting Items**: Pick up a known number of tennis balls
```
// Collect 6 tennis balls
for(var i = 0; i < 6; i++) {
    takeBall();
}
```

**Creating Patterns**: Repeat decorative or functional patterns
```
// Create a zigzag pattern 4 times
for(var i = 0; i < 4; i++) {
    move();
    turnLeft();
    move();
    turnRight();
    move();
    turnRight();
    move();
    turnLeft();
}
```

## Practical For Loop Examples

### Example 1: Building a Wall

```
/*
 * Builds a wall of tennis balls that is 15 balls long
 * Precondition: Karel is at the start position, facing east
 * Postcondition: Karel has built a 15-ball wall and is at the end
 */
function buildWall() {
    for(var i = 0; i < 15; i++) {
        putBall();
        move();
    }
}
```

### Example 2: Cleaning Up a Row

```
/*
 * Picks up tennis balls from a row of 20 positions
 * Precondition: Karel is at start of row, facing east
 * Postcondition: Karel has collected all balls from 20 positions
 */
function cleanRow() {
    for(var i = 0; i < 20; i++) {
        if(ballsPresent()) {  // We'll learn about if statements soon!
            takeBall();
        }
        move();
    }
}
```

### Example 3: Creating a Square

```
/*
 * Makes Karel walk in a square pattern
 * Each side of the square is 4 steps long
 */
function walkSquare() {
    for(var i = 0; i < 4; i++) {  // Repeat for each side
        for(var j = 0; j < 4; j++) {  // Walk along each side
            move();
        }
        turnLeft();  // Turn at each corner
    }
}
```

Notice the **nested for loop** in the square example - a for loop inside another for loop! This creates more complex patterns.

## For Loops vs Functions

Students sometimes wonder when to use for loops versus when to create functions. Here's the difference:

### Use For Loops When:
- You want to repeat the **same commands** multiple times
- You know **exactly how many times** to repeat
- The repetition is the main point (like building a long wall)

### Use Functions When:
- You want to **organize related commands** into logical groups
- You want to **reuse complex behaviors** in different parts of your program
- The commands solve a **specific sub-problem** (like jumping a hurdle)

### Combining For Loops and Functions

The most powerful programs combine both approaches:

```
function start() {
    buildMultipleTowers();
}

function buildMultipleTowers() {
    for(var i = 0; i < 5; i++) {  // Build 5 towers
        buildOneTower();           // Use function for complex task
        moveToNextPosition();      // Use function for navigation
    }
}

function buildOneTower() {
    for(var j = 0; j < 3; j++) {  // Each tower is 3 balls high
        putBall();
        move();
        turnLeft();
    }
    returnToBase();
}
```

## Common For Loop Mistakes

### Mistake 1: Off-by-One Errors

```
// Wrong - this only moves 4 times, not 5
for(var i = 1; i < 5; i++) {
    move();
}

// Correct - this moves exactly 5 times
for(var i = 0; i < 5; i++) {
    move();
}
```

**Remember**: Always start with `i = 0` and use `i < count`.

### Mistake 2: Forgetting Curly Braces

```
// Wrong - only the first command is repeated
for(var i = 0; i < 3; i++)
    move();
    putBall();  // This only happens once!

// Correct - both commands are repeated
for(var i = 0; i < 3; i++) {
    move();
    putBall();  // Both commands repeat 3 times
}
```

### Mistake 3: Using For Loops When Functions Are Better

```
// Awkward - using a loop for different tasks
for(var i = 0; i < 1; i++) {
    goToStore();
}
for(var i = 0; i < 1; i++) {
    buyChocolate();
}

// Better - use functions for different tasks
function start() {
    goToStore();
    buyChocolate();
}
```

### Mistake 4: Wrong Loop Count

```
// Be careful with your counting!
// This puts down 11 balls, not 10
for(var i = 0; i <= 10; i++) {  // <= instead of <
    putBall();
}

// Correct - puts down exactly 10 balls
for(var i = 0; i < 10; i++) {
    putBall();
}
```

## For Loop Problem-Solving Strategy

When you encounter a problem that might need a for loop:

### Step 1: Identify Repetition
Ask yourself: "Am I doing the same thing multiple times?"

### Step 2: Count the Repetitions
Ask: "Exactly how many times do I need to repeat this?"

### Step 3: Identify What Repeats
Ask: "Which specific commands need to be repeated?"

### Step 4: Write the For Loop
```
for(var i = 0; i < numberOfRepetitions; i++) {
    // commands that need to repeat
}
```

### Step 5: Test and Adjust
Run your program and verify it does exactly what you intended.

## Real-World Applications

For loops aren't just for Karel - they're fundamental to all programming:

**Web Development**: Display a list of items, create navigation menus with multiple links

**Game Development**: Move characters, create multiple enemies, handle animation frames

**Data Processing**: Analyze lists of information, perform calculations on large datasets

**Art and Design**: Create patterns, generate repeated visual elements

**Robotics**: Repeat movements, scan environments, perform maintenance tasks

## Key Takeaways

1. **For loops eliminate repetitive code** by repeating commands a fixed number of times
2. **The basic syntax is `for(var i = 0; i < count; i++)`** where count is your number of repetitions
3. **For loops are perfect when you know exactly how many times to repeat** something
4. **Always use curly braces** to contain all commands that should repeat
5. **Start with `i = 0` and use `i < count`** to avoid off-by-one errors
6. **For loops and functions work together** - loops for repetition, functions for organization
7. **For loops are fundamental to all programming languages** - this skill transfers everywhere

For loops represent a major leap forward in your programming abilities. You can now write programs that would have been impossibly tedious before, and you're thinking like a professional programmer by recognizing patterns and eliminating repetition.

Next, you'll learn about if statements - another fundamental control structure that lets Karel make decisions based on the current situation!