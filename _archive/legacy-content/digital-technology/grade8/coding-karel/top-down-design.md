---
layout: page
title: Top Down Design and Decomposition
parent: Introduction to Coding (JavaScript with Karel)
grand_parent: Grade 8 Digital Technology
nav_order: 6
---

# Top Down Design and Decomposition
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Building Better Programs with Functions

Now that you understand commands, functions, and the start() function, let's focus on how to effectively structure programs. You know that commands go inside functions, and functions make up your program - but how do you decide what functions to create and when to use them?

The key is learning to break down complex problems into smaller, manageable pieces through a process called **top-down design and decomposition**.

## When Do We Use a Function?

Recall that functions help us break down problems into smaller parts and make our programs more readable. By tucking away lists of commands inside named functions, programs become much easier to understand.

While all code must be in some function, not every command needs its own function. Here are guidelines for when to create a new function:

### 1. The Group of Commands Accomplishes a Specific Task

If several commands work together to complete one clear objective, they should be grouped into a function.

**Example:**
```
function buildTower() {
    putBall();
    move();
    turnLeft();
    putBall();
    move();
    turnLeft();
    putBall();
}
```

### 2. The Specific Task is Used More Than Once

If you need to repeat the same sequence of commands, create a function instead of copying and pasting code.

**Example:**
```
function start() {
    buildTower();  // First tower
    move();
    move();
    buildTower();  // Second tower - same function reused
}
```

### 3. The Task Solves a Smaller Problem Within the Bigger Problem

Even if a function is only used once, it's still valuable if it handles a distinct part of the overall problem. This makes your code more organized and easier to understand.

**Example:**
```
function start() {
    prepareForWork();  // Used once, but handles distinct task
    doMainWork();      // Used once, but handles distinct task
    cleanUp();         // Used once, but handles distinct task
}
```

## Top-Down Design and Decomposition

Most programming problems are large and complex, but they can be broken down into smaller, more manageable parts. This approach is called **top-down design** - starting with the big picture and working your way down to the details.

### The Process

**Step 1: Consider the Big Picture**
What is your overall goal? What does the program need to accomplish?

**Step 2: Break Down the Problem**
What are the major steps needed to reach your goal? What happens first, second, third?

**Step 3: Break Down Each Step Further**
Can each major step be broken into smaller steps? Keep breaking down until you have clear, specific tasks.

**Step 4: Define Tasks**
Each task should be small enough to describe in a single sentence, but may still require multiple commands to complete.

![Problem decomposition diagram showing big problem breaking into smaller problems](./images/problem-decomposition-diagram.jpg)

## Making a Movie: A Real-World Example

Let's use movie-making as an analogy to understand problem decomposition.

### The Big Problem
"Make a feature-length movie with big Hollywood stars, awesome special effects, that will entertain everyone who sees it."

This is clearly too big and complex to tackle all at once!

### Breaking It Down

**Level 1 - Major Components:**
- Write the Script
- Assemble Cast and Crew  
- Film the Movie
- Edit the Movie

**Level 2 - Breaking Down Further:**
- Film the Movie breaks down into:
  - Film Scene 1
  - Film Scene 2
  - Film Scene 3
  - ... and so on

**Level 3 - Even More Detail:**
- Film Scene 1 might break down into:
  - Set up lighting
  - Position cameras
  - Direct actors
  - Record dialogue

### The Key Insight

Each small problem combines with solutions to other small problems to create the solution to the overall problem. No single person needs to understand every detail - they just need to understand their piece and how it fits into the bigger picture.

## Hurdle Karel: A Programming Example

Let's apply top-down design to a Karel problem. Imagine Karel needs to go down a street and jump over all the hurdles, then stop at the end.

![Karel's starting world showing hurdles to jump over](./images/karel-hurdles-start.jpg)

![Karel's ending world after jumping all hurdles](./images/karel-hurdles-end.jpg)

### Step 1: The Big Goal

Karel needs to go down the street, jump over every hurdle, and stop at the end.

### Step 2: Break Down the Problem

What are the major steps?
1. Karel needs to go down the street until the end
2. When Karel meets a hurdle, Karel needs to jump over it
3. After the last hurdle, Karel needs to go to the end of the street

### Step 3: Identify Specific Tasks

Looking at the world, we can see:
- Karel should go to the next hurdle
- Karel should jump over the hurdle  
- Karel should stop at the wall at the end

Notice how each task is reusable - Karel will need to go to a hurdle 3 times and jump over a hurdle 2 times.

### Step 4: Design the Program Structure

```
function start() {
    runToHurdle();
    jumpHurdle();
    runToHurdle();
    jumpHurdle();
    runToFinish();
}

function jumpHurdle() {
    // Make Karel jump over a hurdle
    turnLeft();
    move();
    turnRight();
    move();
    turnRight();
    move();
    turnLeft();
}

function runToHurdle() {
    // Make Karel go to the next hurdle
    move();
    move();
    move();
}

function runToFinish() {
    // Make Karel go to the end of the street
    move();
    move();
}
```

### Why This Structure Works

**Story-Like Reading**: The start() function reads like a story - run to hurdle, jump hurdle, run to hurdle, jump hurdle, run to finish.

**Clear Responsibilities**: Each function has one clear job that can be described in a single sentence.

**Reusable Components**: Functions are used multiple times without copying code.

**Easy to Debug**: If jumping doesn't work correctly, you know exactly which function to fix.

**Easy to Modify**: If you need to change how Karel jumps, you only modify one function.

## Benefits of Top-Down Design

### 1. Makes Complex Problems Manageable

Instead of trying to solve everything at once, you focus on one small piece at a time.

### 2. Improves Code Organization

Each function has a clear purpose and fits logically into the overall program structure.

### 3. Enables Collaboration

Different people can work on different functions, as long as they understand what each function should accomplish.

### 4. Simplifies Testing and Debugging

You can test each function individually to make sure it works correctly.

### 5. Makes Programs Easier to Modify

Changes to one part of the program don't affect other parts, as long as the function interfaces remain the same.

## Applying Top-Down Design to Your Programs

### 1. Start with the End Goal

Write down what you want your program to accomplish in one or two sentences.

### 2. List Major Steps

What are the 3-5 major things that need to happen to reach your goal?

### 3. Break Down Each Step

For each major step, ask: "What smaller steps make up this larger step?"

### 4. Create Functions for Each Task

Each specific task becomes a function with a descriptive name.

### 5. Write the start() Function

The start() function should read like an outline of your program, calling the major functions in order.

## Example: Planning a Birthday Party Program

Let's practice with a non-Karel example.

### Big Goal
Plan and execute a successful birthday party for a friend.

### Major Steps (Level 1)
- Plan the party
- Prepare for the party  
- Host the party
- Clean up after the party

### Breaking Down "Plan the party" (Level 2)
- Choose a date and time
- Create guest list
- Plan activities
- Order food and drinks

### Breaking Down "Choose a date and time" (Level 3)
- Check your calendar
- Check friend's calendar
- Consider guest availability
- Confirm the date

### In Karel-Style Code
```
function start() {
    planParty();
    prepareForParty();
    hostParty();
    cleanUp();
}

function planParty() {
    chooseDateAndTime();
    createGuestList();
    planActivities();
    orderFood();
}

function chooseDateAndTime() {
    checkMyCalendar();
    checkFriendsCalendar();
    considerGuestAvailability();
    confirmDate();
}
```

## Common Mistakes in Problem Decomposition

### 1. Functions That Are Too Large

If a function tries to do too many different things, it should be broken down further.

**Too Large:**
```
function solveEverything() {
    move();
    move();
    putBall();
    turnLeft();
    move();
    move();
    takeBall();
    turnRight();
    move();
    putBall();
    // ... 20 more commands
}
```

**Better:**
```
function start() {
    goToFirstLocation();
    completFirstTask();
    goToSecondLocation();
    completeSecondTask();
}
```

### 2. Functions That Are Too Small

Creating a function for every single command makes code harder to read, not easier.

**Too Small:**
```
function moveOnce() {
    move();
}

function putOneBall() {
    putBall();
}
```

**Better:**
```
function moveToCorner() {
    move();
    move();
    move();
    turnLeft();
}
```

### 3. Poor Function Names

Functions should be named to clearly describe what they accomplish.

**Poor Names:**
```
function doStuff() { ... }
function part1() { ... }
function helper() { ... }
```

**Good Names:**
```
function jumpOverHurdle() { ... }
function returnToStart() { ... }
function buildTower() { ... }
```

## Key Takeaways

1. **Top-down design breaks complex problems into manageable pieces**
2. **Functions should accomplish specific, well-defined tasks**
3. **Programs should read like stories** with clear, descriptive function names
4. **Reusable functions reduce code duplication** and make maintenance easier
5. **Good decomposition makes programs easier to understand, test, and modify**
6. **Start with the big picture and work down to specific details**
7. **Each function should be describable in a single sentence**

Top-down design and decomposition are fundamental skills that extend far beyond Karel programming. These same principles apply to all programming languages and even to solving problems in daily life. By learning to break down complex challenges into smaller, manageable pieces, you're developing critical thinking skills that will serve you well in programming and beyond.

Next, you'll learn about commenting your code - another essential skill for writing professional, maintainable programs!