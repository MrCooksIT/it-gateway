---
layout: page
title: Commenting Your Code
parent: Introduction to Coding (JavaScript with Karel)
grand_parent: Grade 8 Digital Technology
nav_order: 7
---

# Commenting Your Code
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## It's Not Enough for Your Program to Work

You've learned to create functions, organize programs with the start() function, and break down complex problems using top-down design. But there's another crucial aspect of programming that separates good code from great code: **style**.

Good programming style means:
- Breaking down problems in reasonable ways
- Making your code clear to others (and to yourself later!)
- Writing code that tells a story about what it does

Your code is useless if nobody else can understand what it does. You'd be surprised how quickly it becomes useless even to you because you've forgotten what the goal of your program was!

## Why Comments Matter

Imagine finding this code six months from now:

```
function start() {
    moveAndTurn();
    doTheWork();
    goBack();
}

function moveAndTurn() {
    move();
    move();
    move();
    turnLeft();
    move();
}

function doTheWork() {
    putBall();
    move();
    putBall();
    move();
    putBall();
}
```

Questions you might have:
- What is this program supposed to accomplish?
- Why does `moveAndTurn()` move exactly 3 times?
- What do the tennis balls represent?
- Where is Karel supposed to end up?

Even with descriptive function names, the **purpose** and **context** aren't clear.

## Introducing Comments

Comments are a way to leave notes about what your code is doing in plain English, so other people (including future you) can understand it.

Comments are special lines in your program that:
- Are written in plain English, not code
- Are completely ignored by Karel when running the program
- Help humans understand what the code does and why

Think of comments as notes you're writing to someone else who needs to understand your program.

## Types of Comments

### Single Line Comments

Single line comments start with `//` and extend to the end of that line:

```
// This is a single line comment
move();

move(); // You can also put comments at the end of lines

// Comments can explain what's coming next
turnLeft();
```

### Multi-Line Comments

Multi-line comments start with `/*` and end with `*/`. Everything between these markers is a comment:

```
/*  This is a multi-line comment.
 *  You can write several lines of explanation
 *  to describe complex parts of your program.
 *  All lines between the markers are comments.
 */

function buildTower() {
    putBall();
    putBall();
    putBall();
}
```

## When to Use Comments

### Always Comment Your Functions

Every function should have a comment explaining what it does. This is absolutely essential for good programming style.

```
// Makes Karel turn right by turning left three times
function turnRight() {
    turnLeft();
    turnLeft();
    turnLeft();
}

/* Builds a tower of tennis balls at Karel's current location.
 * Karel will place 3 balls in a vertical stack.
 */
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

### Comment Complicated Code

If you have a complex sequence of commands that might be confusing, add comments to explain the logic:

```
function navigateAroundWall() {
    // Go around the wall by turning left and moving up
    turnLeft();
    move();
    move();
    
    // Now turn right to go around the top of the wall
    turnRight();
    move();
    
    // Turn right again to come back down the other side
    turnRight();
    move();
    move();
    
    // Finally turn left to face the original direction
    turnLeft();
}
```

### Comment the Overall Program Purpose

Always include a comment at the top of your program explaining what it does:

```
/*
 * Hurdle Jump Program
 * Makes Karel navigate down a street jumping over hurdles.
 * Karel starts at the beginning of the street and ends at the wall.
 * Program assumes there are exactly 3 hurdles to jump.
 */

function start() {
    runToHurdle();
    jumpHurdle();
    runToHurdle();
    jumpHurdle();
    runToHurdle();
    jumpHurdle();
    runToFinish();
}
```

## What NOT to Comment

### Don't Comment Obvious Code

Don't comment every single line or explain things that are already clear:

```
// Bad commenting - too obvious
move(); // Karel moves forward
putBall(); // Karel puts down a tennis ball
turnLeft(); // Karel turns to the left

// Good commenting - explains the purpose
// Move to the center of the world and mark it
move();
putBall();
turnLeft();
```

### Don't Comment Bad Code - Fix It Instead

If you need lots of comments to explain confusing code, consider rewriting the code to be clearer:

```
// Bad approach - confusing code with lots of comments
function confusingFunction() {
    // Turn around by turning left twice
    turnLeft();
    turnLeft();
    // Move forward three times to get to the wall
    move();
    move();
    move();
    // Turn around again to face the original direction
    turnLeft();
    turnLeft();
}

// Better approach - clear code with minimal comments
function returnToStart() {
    turnAround();
    moveThreeSpaces();
    turnAround();
}
```

## Preconditions and Postconditions

For function comments, use **preconditions** and **postconditions** to clearly describe what the function expects and what it accomplishes.

### Preconditions

Preconditions describe:
- What assumptions the function makes about Karel's world
- What must be true **before** the function is called
- Karel's expected position, direction, or world state

### Postconditions

Postconditions describe:
- What will be true about Karel's world **after** the function is called
- Karel's final position, direction, or changes to the world
- What the function has accomplished

### Examples of Preconditions and Postconditions

```
/*
 * Precondition: Karel is standing next to a hurdle, facing east
 * Postcondition: Karel has jumped over the hurdle and is facing east
 *                on the other side of the hurdle
 */
function jumpHurdle() {
    turnLeft();      // Face north to go over hurdle
    move();          // Move up and over
    turnRight();     // Face east again
    move();          // Move to other side
    turnRight();     // Face south to come down
    move();          // Come down from hurdle
    turnLeft();      // Face east to continue
}

/*
 * Precondition: Karel is facing east at the beginning of the street
 * Postcondition: Karel is facing east at the end of the street,
 *                having jumped over all hurdles along the way
 */
function navigateStreet() {
    runToHurdle();
    jumpHurdle();
    runToHurdle();
    jumpHurdle();
    runToFinish();
}

/*
 * Precondition: Karel is at any position, facing any direction
 * Postcondition: Karel is at the same position, facing the opposite direction
 */
function turnAround() {
    turnLeft();
    turnLeft();
}
```

## Complete Example: Well-Commented Program

Here's a complete Karel program with good commenting style:

```
/*
 * Tower Builder Program
 * Karel builds three towers of tennis balls, each getting progressively taller.
 * Karel starts at (1,1) facing east and ends at (7,1) facing east.
 * First tower: 1 ball, Second tower: 2 balls, Third tower: 3 balls
 */

function start() {
    buildFirstTower();    // Build 1-ball tower
    moveToNextPosition();
    buildSecondTower();   // Build 2-ball tower  
    moveToNextPosition();
    buildThirdTower();    // Build 3-ball tower
}

/*
 * Precondition: Karel is at ground level, facing east
 * Postcondition: Karel is at ground level, facing east,
 *                with a 1-ball tower at the starting position
 */
function buildFirstTower() {
    putBall();
}

/*
 * Precondition: Karel is at ground level, facing east
 * Postcondition: Karel is at ground level, facing east,
 *                with a 2-ball tower at the starting position
 */
function buildSecondTower() {
    putBall();
    turnLeft();
    move();
    putBall();
    
    // Return to ground level
    turnAround();
    move();
    turnRight();
}

/*
 * Precondition: Karel is at ground level, facing east
 * Postcondition: Karel is at ground level, facing east,
 *                with a 3-ball tower at the starting position
 */
function buildThirdTower() {
    putBall();
    turnLeft();
    move();
    putBall();
    move();
    putBall();
    
    // Return to ground level
    turnAround();
    move();
    move();
    turnRight();
}

/*
 * Precondition: Karel is facing east
 * Postcondition: Karel has moved 2 spaces east and is still facing east
 */
function moveToNextPosition() {
    move();
    move();
}

// Helper function for turning around
function turnAround() {
    turnLeft();
    turnLeft();
}

// Helper function for turning right
function turnRight() {
    turnLeft();
    turnLeft();
    turnLeft();
}
```

## Benefits of Good Commenting

### 1. Code Maintenance

Six months from now, you'll be able to quickly understand what your program does and how it works.

### 2. Collaboration

Other people can easily understand and modify your code.

### 3. Debugging

When something goes wrong, comments help you quickly identify which function is responsible for what task.

### 4. Learning

Writing comments forces you to think clearly about what your code does, which often reveals problems or improvements.

### 5. Professional Standards

All professional programmers write commented code - it's an essential skill for any programming career.

## Common Commenting Mistakes

### 1. No Comments At All

```
// Bad - no explanation of purpose
function mystery() {
    move();
    turnLeft();
    move();
    putBall();
    turnRight();
}
```

### 2. Too Many Obvious Comments

```
// Bad - over-commenting obvious actions
function moveThree() {
    move(); // move forward once
    move(); // move forward again  
    move(); // move forward a third time
}
```

### 3. Outdated Comments

```
// Bad - comment doesn't match the code
// Makes Karel turn left
function turnRight() {  // Actually turns right!
    turnLeft();
    turnLeft();
    turnLeft();
}
```

### 4. Comments Instead of Clear Code

```
// Bad - using comments to explain confusing code
function doStuff() {
    // This complicated sequence makes Karel go to the corner
    move();
    move();
    turnLeft();
    move();
    turnLeft();
    turnLeft();
    turnLeft();
}

// Better - clear function name and structure
function goToCorner() {
    moveToWall();
    turnLeft();
    moveToWall();
    turnAround();
}
```

## Key Takeaways

1. **Comments are essential for readable code** - they explain what code does and why
2. **Every function needs a comment** describing its purpose
3. **Use preconditions and postconditions** to clearly specify function behavior
4. **Comment complex logic** but don't over-comment obvious code
5. **Comments should explain purpose and context**, not just repeat what the code does
6. **Good commenting is a professional skill** that makes you a better programmer
7. **Comments help you debug and maintain code** over time

Learning to write good comments is as important as learning to write good code. Comments make your programs professional, maintainable, and accessible to others. This skill will serve you well in all programming languages and is essential for working on team projects or professional software development.

Next, you'll learn about Super Karel - an enhanced version of Karel with additional capabilities that will expand your programming possibilities!