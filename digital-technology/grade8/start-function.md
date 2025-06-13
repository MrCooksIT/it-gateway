---
layout: page
title: The Start Function
parent: Introduction to Coding (JavaScript with Karel)
grand_parent: Grade 8 Digital Technology
nav_order: 5
---

# The Start Function
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Where Does Our Program Start?

As you've learned to create functions, you might be wondering: "When I have multiple functions in my program, how does Karel know which commands to do and in what order?"

This is an excellent question that gets to the heart of program organization and execution.

You might think Karel starts at the top of the file and reads down through it. This is almost correct, but there's an important detail that makes programs organized and predictable.

## The Problem with Disorganized Code

Imagine if you could put commands anywhere in your program, mixed in with function definitions:

```
function turnRight() {
    turnLeft();
    turnLeft();
    turnLeft();
}

move();  // Random command here?
move();

function turnAround() {
    turnLeft();
    turnLeft();
}

putBall();  // Another random command?
```

This would be terribly confusing! Where should Karel start? From the top? From the bottom? What if commands are scattered throughout the file? This approach makes programs impossible to understand and debug.

**This is never the way to write code.**

## Introducing the start() Function

The solution is a special function called `start()`. This function serves as the official starting point for every Karel program.

### What Makes start() Special?

The `start()` function is different from other functions because:
- **It's the program's entry point** - Karel always begins by executing start()
- **It's automatically called** - You don't need to call start() yourself
- **It's required** - Every Karel program must have a start() function
- **There can only be one** - You cannot have multiple start() functions

### The start() Function Structure

```
function start() {
    // All of your main program commands go here
}
```

All the commands you want Karel to execute must go inside the start function, between the curly braces. The commands will be executed in the order they appear.

## Rules for Using start()

### 1. There Can Only Be One start() Function

Each program needs exactly one start() function - no more, no less.

**Correct:**
```
function start() {
    move();
    putBall();
}
```

**Incorrect (multiple start functions):**
```
function start() {
    move();
}

function start() {  // Error! Can't have two start functions
    putBall();
}
```

### 2. You Must Have a start() Function

Every Karel program requires a start() function to run properly.

### 3. All Program Commands Go Inside start() or Other Functions

Commands should never be floating loose in your program file.

**Correct Organization:**
```
function start() {
    move();           // Commands go here
    turnRight();
    putBall();
}

function turnRight() {  // Function definitions go here
    turnLeft();
    turnLeft();
    turnLeft();
}
```

**Incorrect Organization:**
```
move();  // Wrong! Commands shouldn't be here

function start() {
    turnRight();
    putBall();
}

move();  // Wrong! Commands shouldn't be here either
```

### 4. Function Definitions Go Outside start()

Define your custom functions outside the start() function, but call them from inside start().

```
function start() {
    buildTower();     // Function call (inside start)
    moveToCorner();   // Function call (inside start)
}

function buildTower() {     // Function definition (outside start)
    putBall();
    putBall();
    putBall();
}

function moveToCorner() {   // Function definition (outside start)
    move();
    move();
    turnRight();
    move();
}
```

![Function organization showing definitions outside start() and calls inside](./images/function-organization-diagram.jpg)

## Program Readability: Writing Code Like a Story

The start() function is the first step in making programs easy to understand by both humans and computers. Good programs read like stories that clearly describe what happens.

### Example: A Story-Like Program

```
function start() {
    goToStore();
    buyChocolate();
    comeHomeAndCelebrate();
}

function goToStore() {
    move();
    move();
    move();
    turnRight();
    move();
}

function buyChocolate() {
    putBall();  // Chocolate represented by tennis ball
    takeBall(); // "Buying" the chocolate
}

function comeHomeAndCelebrate() {
    turnAround();
    move();
    move();
    move();
    turnLeft();
    move();
    putBall();  // Celebration!
}
```

### Why This Approach Works

**Clear Narrative**: Reading the start() function tells you exactly what the program does - it's like reading the outline of a story.

**Organized Structure**: Function definitions are separated from the main program logic.

**Easy to Understand**: Anyone can read `goToStore()` and understand what that part of the program accomplishes.

**Easy to Debug**: If something goes wrong with buying chocolate, you know exactly which function to check.

## The Flow of Program Execution

Understanding how Karel executes your program helps you write better code:

### Step 1: Karel Finds start()
When you run your program, Karel automatically looks for the start() function.

### Step 2: Karel Executes start() Commands
Karel reads through the commands inside start() from top to bottom.

### Step 3: Karel Calls Other Functions
When Karel encounters a function call like `goToStore()`, Karel jumps to that function definition and executes its commands.

### Step 4: Karel Returns to start()
After completing a function, Karel returns to start() and continues with the next command.

![Program execution flow showing start function calling other functions and returning](./images/program-execution-flow.jpg)

## Example: Building a Complete Program

Let's create a complete program that demonstrates proper organization:

```
function start() {
    prepareForWork();
    buildSquare();
    returnHome();
}

function prepareForWork() {
    move();
    move();
    turnRight();
}

function buildSquare() {
    buildOneSide();
    buildOneSide();
    buildOneSide();
    buildOneSide();
}

function buildOneSide() {
    putBall();
    move();
    putBall();
    move();
    turnRight();
}

function returnHome() {
    move();
    move();
    turnLeft();
    move();
    move();
}

function turnRight() {
    turnLeft();
    turnLeft();
    turnLeft();
}
```

### Why This Organization Works

**Clear Main Program**: The start() function shows the three main phases of the program.

**Logical Grouping**: Related commands are grouped into functions with descriptive names.

**Reusable Components**: Functions like `buildOneSide()` and `turnRight()` can be used multiple times.

**Easy Maintenance**: If you need to change how Karel builds one side of the square, you only modify the `buildOneSide()` function.

## Common Mistakes and How to Avoid Them

### Mistake 1: Forgetting the start() Function
```
// Wrong - no start() function
move();
putBall();

// Correct - commands inside start()
function start() {
    move();
    putBall();
}
```

### Mistake 2: Multiple start() Functions
```
// Wrong - multiple start functions
function start() {
    move();
}

function start() {  // Error!
    putBall();
}

// Correct - one start function
function start() {
    move();
    putBall();
}
```

### Mistake 3: Commands Outside Functions
```
// Wrong - loose commands
move();

function start() {
    putBall();
}

turnLeft();  // This command is lost!

// Correct - all commands in functions
function start() {
    move();
    putBall();
    turnLeft();
}
```

### Mistake 4: Function Definitions Inside start()
```
// Wrong - function defined inside start()
function start() {
    function turnRight() {  // Error!
        turnLeft();
        turnLeft();
        turnLeft();
    }
    turnRight();
}

// Correct - function defined outside start()
function start() {
    turnRight();
}

function turnRight() {
    turnLeft();
    turnLeft();
    turnLeft();
}
```

## Benefits of Proper Program Organization

### 1. Predictable Execution
Everyone knows the program starts with the start() function.

### 2. Clear Structure
The separation between main program logic and function definitions makes code easier to follow.

### 3. Better Debugging
When something goes wrong, you can quickly identify which function contains the problem.

### 4. Easier Collaboration
Other programmers can quickly understand your code structure.

### 5. Professional Standards
This organization matches how real programming languages work.

## Key Takeaways

1. **The start() function is the entry point** for every Karel program
2. **There must be exactly one start() function** in each program
3. **All program commands go inside start() or other functions** - never loose in the file
4. **Function definitions belong outside the start() function**
5. **Programs should read like stories** with descriptive function names
6. **Proper organization makes code easier to understand and debug**
7. **This structure prepares you for real programming languages** that work similarly

The start() function represents a major step in learning to write professional, organized code. This structure - having a main function that calls other functions - is fundamental to programming in all languages. You're now writing code that follows the same organizational principles used by professional software developers.

Next, you'll learn about breaking down complex problems into even smaller, more manageable functions using top-down design principles!