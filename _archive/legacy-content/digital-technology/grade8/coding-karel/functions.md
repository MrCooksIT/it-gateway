---
layout: page
title: Functions in Karel
parent: Introduction to Coding (JavaScript with Karel)
grand_parent: Grade 8 Digital Technology
nav_order: 4
---

# Functions in Karel
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## What Is a Function?

In the previous lesson, we introduced functions when we taught Karel how to `turnRight()`. Now let's dive deeper into understanding what functions really are and why they're so important in programming.

Think of functions as little blocks of commands that Karel knows by a single name. Just like you might tell a friend "get the newspaper" and they understand that means going outside, walking to the driveway, picking up the paper, and bringing it back - functions let us give Karel complex instructions using simple names.

![Concept showing function as a black box that takes a name and produces actions](./images/function-black-box-concept.jpg)

When we create a function, we're essentially teaching Karel a new vocabulary word that represents a series of actions.

## Why Use Functions?

Programmers really, really like to use functions for several important reasons:

### 1. Clean and Understandable Code

Functions make code read like a story. Compare these two approaches:

**Without Functions (confusing):**
```
move();
move();
move();
turnLeft();
turnLeft();
turnLeft();
move();
move();
move();
turnLeft();
turnLeft();
turnLeft();
```

**With Functions (clear):**
```
moveThreeSpaces();
turnRight();
moveThreeSpaces();
turnRight();
```

The second version immediately tells you what's happening without having to mentally process each individual command.

![Before and after code comparison showing improvement with functions](./images/code-before-after-functions.jpg)

### 2. Problem Decomposition

Functions help us break down complex problems into smaller, manageable pieces. Instead of trying to solve everything at once, we can:

- Focus on one step at a time
- Solve the parts we understand first
- Tackle the harder parts later
- Build complex solutions from simple components

**Example: Getting the Newspaper**
Instead of writing one massive program, we can break it into functions:
- `goToNewspaper()`
- `pickUpNewspaper()`
- `returnHome()`

### 3. Code Reusability

Once you create a function, you can use it as many times as needed. If you need Karel to turn around multiple times in a program, you write the `turnAround()` function once and call it whenever needed.

### 4. Time Savings

When you break problems into functions, you often discover that some parts are similar or identical. You can create functions for these common patterns and reuse them throughout your program.

## Creating Functions: The Rules

Creating functions that Karel can understand requires following specific rules. Let's explore each requirement.

## Naming is Crucial

The name of your function is extremely important for several reasons:

### Names Must Be Descriptive

**Good Function Names:**
- `buildPyramid()` - clearly describes what it does
- `climbUpTower()` - action-oriented and specific
- `pickUpThreeBalls()` - tells you exactly what and how many

**Bad Function Names:**
- `functionOne()` - doesn't tell you anything
- `doStuff()` - too vague and unhelpful
- `myFunction()` - generic and meaningless

![Examples of good vs bad function names](./images/good-bad-function-names.jpg)

### Camel Case Formatting

Function names with multiple words must use **Camel Case**:
- First word is lowercase
- All subsequent words start with uppercase
- No spaces anywhere

**Correct Camel Case:**
- `goToEnd()`
- `pickUpBall()`
- `turnAroundTwice()`

**Incorrect Formatting:**
- `StopAtWall()` (first word should be lowercase)
- `buildtower()` (missing capital for second word)
- `pick up ball()` (has spaces)

### Function Name Rules

**Must Start With a Letter**
- ✅ `pickUpBalls()`
- ❌ `34BallPickUp()` (starts with number)

**Only Letters and Numbers**
- ✅ `pickUp34Balls()`
- ❌ `pickUpBalls!()` (contains special character)
- ❌ `pick up balls()` (contains spaces)

**Action-Oriented Names**
Functions should be named like actions or commands:
- `move()`, `turn()`, `build()`, `climb()`, `collect()`

## Rules for Defining a Function

Every function definition has three essential parts that must be present and correctly formatted:

![Anatomy of a function showing three parts: keyword, name, and body](./images/function-anatomy.jpg)

### 1. The Function Keyword

Every function definition starts with the word `function`:

```
function
```

### 2. Function Name and Parentheses

The function name followed by parentheses:

```
function pickUpThreeBalls()
```

### 3. Function Body with Curly Braces

The commands that make up the function, enclosed in curly braces:

```
function pickUpThreeBalls() {
    // commands go here
}
```

### Complete Function Example

```
function pickUpThreeBalls() {
    takeBall();
    takeBall();
    takeBall();
}
```

Notice how the commands inside the function are indented. This makes the code easier to read and shows clearly what belongs inside the function.

## Defining vs. Calling a Function

Understanding the difference between defining and calling a function is crucial for programming success.

### Function Definition

**Definition** means writing the instructions that teach Karel what the function does. This is like writing a recipe - you're explaining the steps, but you're not actually cooking yet.

```
function turnAround() {
    turnLeft();
    turnLeft();
}
```

This code teaches Karel what `turnAround()` means, but Karel doesn't actually turn around when you write this definition.

![Function definition showing the template/recipe concept](./images/function-definition-recipe.jpg)

### Function Call

**Calling** means actually using the function to make Karel perform the actions. This is like following the recipe - now you're actually cooking.

```
move();
turnAround();  // This makes Karel actually turn around
move();
```

When Karel encounters `turnAround();` in your program, Karel executes the commands from the function definition.

![Function call showing the action being performed](./images/function-call-action.jpg)

### Key Differences

**Definition Syntax:**
- Starts with `function` keyword
- Includes the function body with `{}`
- Teaches Karel what the function means

**Call Syntax:**
- Just the function name with `()`
- Ends with semicolon
- Makes Karel actually perform the action

## Example: The turnAround() Function

Let's create a complete example by building a `turnAround()` function that makes Karel face the opposite direction.

### Step 1: Name the Function

We want Karel to turn around, so `turnAround()` is perfect:
- Uses Camel Case
- Descriptive action name
- Starts with a letter
- Contains only letters

### Step 2: Declare the Function

```
function turnAround() {

}
```

This creates an empty function that Karel recognizes but doesn't know what to do with yet.

### Step 3: Define the Function Body

To turn around (face the opposite direction), Karel needs to turn 180 degrees:

```
function turnAround() {
    turnLeft();
    turnLeft();
}
```

Two left turns equal a 180-degree turn, making Karel face the opposite direction.

![turnAround function showing two left turns equals opposite direction](./images/turnaround-function-demo.jpg)

### Step 4: Use the Function

Now we can use `turnAround()` in our programs:

```
move();
move();
move();
turnAround();
move();
move();
move();
```

This program makes Karel move forward three spaces, turn around, then move back three spaces.

## Practice: Identifying Reusable Patterns

Looking at the program above, can you spot another place where a function would be useful?

The pattern `move(); move(); move();` appears twice! We could create a function:

```
function moveThreeSpaces() {
    move();
    move();
    move();
}
```

Then our program becomes:

```
moveThreeSpaces();
turnAround();
moveThreeSpaces();
```

Much cleaner and more readable!

## Function Benefits in Action

Let's see how functions improve a more complex program:

### Without Functions (Hard to Read)
```
move();
move();
putBall();
move();
turnLeft();
turnLeft();
move();
move();
putBall();
move();
turnLeft();
turnLeft();
move();
move();
putBall();
```

### With Functions (Clear and Organized)
```
function placeBallAndReturn() {
    move();
    move();
    putBall();
    move();
    turnAround();
}

placeBallAndReturn();
placeBallAndReturn();
placeBallAndReturn();
```

The second version is easier to understand, maintain, and modify.

## Common Function Mistakes

### 1. Forgetting the Function Keyword
```
// Wrong
turnAround() {
    turnLeft();
    turnLeft();
}

// Correct
function turnAround() {
    turnLeft();
    turnLeft();
}
```

### 2. Missing Parentheses
```
// Wrong
function turnAround {
    turnLeft();
    turnLeft();
}

// Correct
function turnAround() {
    turnLeft();
    turnLeft();
}
```

### 3. Confusing Definition and Call
```
// This is a definition (teaches Karel)
function turnAround() {
    turnLeft();
    turnLeft();
}

// This is a call (makes Karel act)
turnAround();
```

### 4. Poor Function Names
```
// Bad names
function doStuff() { ... }
function function1() { ... }

// Good names
function turnAround() { ... }
function buildTower() { ... }
```

## Key Takeaways

1. **Functions are building blocks** that make complex programs from simple commands
2. **Good naming is essential** - use descriptive, action-oriented Camel Case names
3. **Functions improve code quality** by making it cleaner, more reusable, and easier to understand
4. **Problem decomposition** helps solve complex challenges by breaking them into smaller functions
5. **Definition vs. calling** - definition teaches Karel what to do, calling makes Karel do it
6. **Function syntax has specific rules** that must be followed exactly
7. **Functions are the foundation** for all advanced programming concepts

Functions represent a major step forward in your programming journey. You're now thinking like a programmer by creating reusable, well-organized code that solves problems efficiently. These same principles apply to every programming language you'll ever learn.

Next, you'll learn about special functions and more advanced ways to organize your Karel programs!