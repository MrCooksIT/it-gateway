---
layout: page
title: If Statements
parent: Introduction to Coding (JavaScript with Karel)
grand_parent: Grade 8 Digital Technology
nav_order: 9
---

# If Statements and Conditionals
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## The Problem: Karel Can Crash

So far, our Karel programs have worked in predictable worlds where we knew exactly what to expect. But what happens when Karel's world changes? What if there's a wall where we didn't expect one, or no tennis ball where we thought there would be?

When we have a mistake in our program that causes it to fail, it's called a **bug**. For example, if Karel tries to move but runs into a wall, that's a bug that will crash the program.

Consider this simple program:
```
function start() {
    move();
    move();
    move();
    putBall();
}
```

This works fine if Karel has a clear path, but what if there's a wall after the second move? Karel would crash into the wall, and the program would stop with an error.

We need a way for Karel to check the world conditions before taking actions.

## Asking Questions About Karel's World

Karel's world tends to change a lot. Sometimes it's large, other times small. It often has walls, but not always. Though there are usually tennis balls scattered throughout the world, they're rarely in the same place for each exercise.

Given these changing conditions, there are many useful questions Karel might ask:

- **Is there a ball where Karel is standing?**
- **Is Karel's front clear, or is there a wall?**
- **Is Karel facing north?**
- **Can Karel move left without hitting a wall?**

Being able to ask and answer these questions allows Karel to adapt to different situations and avoid crashes.

## Introducing Conditions

These types of questions can be asked using **conditions**. Conditions are special functions that look at the state of Karel's world and return a **true or false answer**.

Think of conditions as Karel's way of sensing and understanding the current situation before deciding what to do.

### Karel's Built-in Conditions

Karel knows how to check many different conditions:

**Movement Conditions:**
- `frontIsClear()` - Returns true if Karel can move forward
- `frontIsBlocked()` - Returns true if there's a wall in front of Karel
- `leftIsClear()` - Returns true if Karel can move to the left
- `leftIsBlocked()` - Returns true if there's a wall to Karel's left
- `rightIsClear()` - Returns true if Karel can move to the right  
- `rightIsBlocked()` - Returns true if there's a wall to Karel's right

**Tennis Ball Conditions:**
- `ballsPresent()` - Returns true if there are tennis balls at Karel's location
- `noBallsPresent()` - Returns true if there are NO tennis balls at Karel's location

**Direction Conditions:**
- `facingNorth()` - Returns true if Karel is facing north (up)
- `facingSouth()` - Returns true if Karel is facing south (down)
- `facingEast()` - Returns true if Karel is facing east (right)
- `facingWest()` - Returns true if Karel is facing west (left)

**Important**: Like Karel's other commands, conditions must include parentheses `()` at the end.

### Understanding True and False

Conditions always return one of two answers:
- **True**: The condition is correct/satisfied
- **False**: The condition is incorrect/not satisfied

For example, if Karel is standing on a tennis ball:
- `ballsPresent()` returns **true**
- `noBallsPresent()` returns **false**

If Karel is facing east:
- `facingEast()` returns **true**
- `facingNorth()` returns **false**
- `facingSouth()` returns **false**
- `facingWest()` returns **false**

## Introducing If Statements

Checking conditions allows us to write programs that can respond to changes in Karel's world. We use **if statements** to check a condition before executing code.

If statements let us control the flow of the program based on the current situation. The basic format is:

```
if(condition) {
    // code to run only if condition is true
}
```

An if statement will **only execute the code inside the curly braces if the condition is true**.

![If statement flowchart showing condition check leading to code execution or skipping](./images/if-statement-flow.jpg)

## Real-World If Statement Examples

If statements work just like decision-making in everyday life:

**Example 1:**
```
if(it is raining) {
    use an umbrella
}
```

**Example 2:**
```
if(room is dirty) {
    clean room
}
```

**Example 3:**
```
if(I am hungry) {
    eat food
}
```

**Example 4:**
```
if(there is music) {
    dance
}
```

Notice the structure: The first part checks the condition of the world, and the second part contains the action that happens if the check is true.

## Karel If Statement Examples

Karel uses if statements and conditions in the same way:

### Example 1: Safe Movement

```
if(frontIsClear()) {
    move();
}
```

This checks if Karel's front is clear before moving, helping Karel avoid crashing into walls.

### Example 2: Conditional Ball Pickup

```
if(ballsPresent()) {
    takeBall();
}
```

This only picks up a tennis ball if there's actually one at Karel's current location.

### Example 3: Direction-Based Actions

```
if(facingNorth()) {
    putBall();
}
```

This only puts down a tennis ball if Karel is facing north.

### Example 4: Multiple Conditions

```
if(frontIsClear()) {
    move();
}

if(ballsPresent()) {
    takeBall();
}

if(facingEast()) {
    turnLeft();
}
```

Each if statement is checked independently, so multiple actions might happen in the same program step.

## Practical If Statement Applications

### Safe Navigation

```
function moveIfPossible() {
    if(frontIsClear()) {
        move();
    }
}
```

This function prevents Karel from crashing into walls by checking before moving.

### Selective Ball Collection

```
function collectBallsInRow() {
    for(var i = 0; i < 10; i++) {
        if(ballsPresent()) {
            takeBall();
        }
        
        if(frontIsClear()) {
            move();
        }
    }
}
```

This combines for loops and if statements to safely collect tennis balls while moving across a row.

### Direction-Specific Actions

```
function turnToFaceEast() {
    if(facingNorth()) {
        turnRight();
    }
    
    if(facingSouth()) {
        turnLeft();
    }
    
    if(facingWest()) {
        turnAround();
    }
    
    // If already facing east, do nothing
}
```

This function uses multiple if statements to turn Karel to face east regardless of the starting direction.

## Combining If Statements with Other Concepts

### If Statements with Functions

```
function start() {
    safelyMoveToWall();
    collectAllBalls();
    returnToStart();
}

function safelyMoveToWall() {
    while(frontIsClear()) {  // We'll learn while loops next!
        move();
    }
}

function collectAllBalls() {
    if(ballsPresent()) {
        takeBall();
    }
}
```

### If Statements with For Loops

```
function buildSelectiveTower() {
    for(var i = 0; i < 5; i++) {
        if(noBallsPresent()) {  // Only put ball if there isn't one already
            putBall();
        }
        
        if(frontIsClear()) {
            move();
            turnLeft();
        }
    }
}
```

## Common If Statement Patterns

### Pattern 1: Safety Checks

Always check before potentially dangerous actions:
```
// Check before moving
if(frontIsClear()) {
    move();
}

// Check before taking balls
if(ballsPresent()) {
    takeBall();
}
```

### Pattern 2: Conditional Actions

Do something only when conditions are right:
```
// Only work when facing the right direction
if(facingEast()) {
    buildWall();
}

// Only clean up if there are balls
if(ballsPresent()) {
    takeBall();
}
```

### Pattern 3: Multiple Checks

Check multiple conditions for complex decision-making:
```
function smartMove() {
    if(frontIsClear()) {
        move();
    } else if(leftIsClear()) {
        turnLeft();
        move();
    } else if(rightIsClear()) {
        turnRight();
        move();
    } else {
        turnAround();  // No clear path, turn around
    }
}
```

Note: We'll learn about `else if` in the next lesson!

## Debugging with If Statements

If statements help prevent bugs and make programs more robust:

### Before If Statements (Fragile)

```
function fragileProgram() {
    move();      // Might crash into wall
    takeBall();  // Might try to take non-existent ball
    move();      // Might crash again
}
```

### After If Statements (Robust)

```
function robustProgram() {
    if(frontIsClear()) {
        move();
    }
    
    if(ballsPresent()) {
        takeBall();
    }
    
    if(frontIsClear()) {
        move();
    }
}
```

The second version can handle different world configurations without crashing.

## Common If Statement Mistakes

### Mistake 1: Forgetting Parentheses

```
// Wrong - missing parentheses
if frontIsClear {
    move();
}

// Correct - parentheses required
if(frontIsClear()) {
    move();
}
```

### Mistake 2: Forgetting Curly Braces

```
// Risky - only first command is part of if statement
if(frontIsClear())
    move();
    putBall();  // This always happens!

// Correct - curly braces group all commands
if(frontIsClear()) {
    move();
    putBall();  // Both commands only happen if condition is true
}
```

### Mistake 3: Using Assignment Instead of Conditions

```
// Wrong - trying to assign instead of check
if(facingEast() = true) {  // = is assignment
    move();
}

// Correct - condition functions return true/false automatically
if(facingEast()) {
    move();
}
```

### Mistake 4: Redundant Checks

```
// Unnecessary - condition functions already return true/false
if(frontIsClear() == true) {
    move();
}

// Better - cleaner syntax
if(frontIsClear()) {
    move();
}
```

## When to Use If Statements

Use if statements when:

### You Need Safety Checks
Prevent crashes by checking conditions before taking actions.

### Behavior Depends on World State
Different actions for different situations (balls present vs. absent, walls vs. clear paths).

### You Want Adaptive Programs
Programs that work in multiple different world configurations.

### You're Building Robust Solutions
Programs that handle unexpected situations gracefully.

## Key Takeaways

1. **Conditions are functions that return true or false** based on Karel's world state
2. **If statements execute code only when conditions are true** - they control program flow
3. **Always use parentheses and curly braces** with proper syntax
4. **If statements prevent crashes** by checking before taking potentially dangerous actions
5. **Combine if statements with functions and loops** for powerful, adaptive programs
6. **Use if statements to make programs robust** and able to handle different situations
7. **If statements are fundamental to all programming** - they enable decision-making in code

If statements represent another major leap in your programming abilities. You can now write programs that adapt to different situations, make decisions based on current conditions, and avoid crashes. Combined with functions and for loops, if statements give you the tools to create sophisticated, intelligent programs.

Next, you'll learn about if/else statements, which provide even more powerful decision-making capabilities by specifying what to do when conditions are false!