---
layout: page
title: If/Else Statements
parent: Introduction to Coding (JavaScript with Karel)
grand_parent: Grade 8 Digital Technology
nav_order: 10
---

# If/Else Statements
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Building on If Statements

In the previous lesson, you learned how if statements let Karel make decisions based on conditions. If statements execute code when conditions are true, but what happens when conditions are false?

Consider this if statement:
```
if(frontIsClear()) {
    move();
}
```

This works great when Karel's front is clear - Karel moves forward. But what should Karel do when the front is blocked? Currently, Karel just does nothing and continues to the next line of code.

Sometimes doing nothing is fine, but often we want Karel to take a specific action when a condition is false. This is where **if/else statements** become powerful.

## The Need for "Otherwise" Logic

One of the driving forces behind writing conditionals is the need to vary the program's behavior based on different conditions. When writing comprehensive programs, you'll often want your program to do something specific when an if statement evaluates as false.

Think about decision-making in real life:
- **If it's raining**, take an umbrella. **Otherwise**, leave it at home.
- **If you're hungry**, eat something. **Otherwise**, keep working.
- **If it's the weekend**, sleep until 10 AM. **Otherwise**, wake up at 7 AM.

The "otherwise" part is crucial because it ensures you handle both possible scenarios.

## Introducing If/Else Statements

Think of the **else statement** as the "otherwise" conditional. It provides an alternative action when the if condition is false.

### Real-World Example: Alarm Clock

Consider this pseudocode for an alarm clock:
- **If it is the weekend**, go off at 10 AM.
- **Otherwise**, go off at 7 AM.

The "otherwise" clause allows us to account for all possible scenarios with just two simple rules.

Compare this to using only if statements:
- **If it is the weekend**, go off at 10 AM.
- **If it is a weekday**, go off at 7 AM.

While both approaches work, the if/else version is clearer because it explicitly handles "everything else."

### A More Complex Example

Suppose we want the alarm to go off at 7 AM on Tuesday and Thursday, and 8 AM on all other days.

**Using if/else (concise):**
- **If it is Tuesday or Thursday**, go off at 7 AM.
- **Otherwise**, go off at 8 AM.

**Using only if statements (verbose):**
- **If it is Tuesday or Thursday**, go off at 7 AM.
- **If it is Sunday, Monday, Wednesday, Friday, or Saturday**, go off at 8 AM.

The if/else version is clearly more concise and practical.

## If/Else Syntax

The basic format of an if/else statement is:

```
if(condition) {
    /* code to run if condition is true */
} else {
    /* code to run if condition is false */
}
```

![If/else statement flowchart showing two paths based on condition](./images/if-else-flow.jpg)

### Key Syntax Rules

1. **Every else statement must be preceded by an if statement**
2. **Not every if statement must have an else statement**
3. **Else statements have no conditions** - no parentheses after "else"
4. **Only one of the two code blocks will execute** - never both

## Karel If/Else Examples

### Example 1: Movement Decision

Suppose we want Karel to move if possible, and turn left otherwise:

```
if(frontIsClear()) {
    move();
} else {
    turnLeft();
}
```

This handles both situations:
- If Karel's front is clear → Karel moves forward
- If Karel's front is blocked → Karel turns left

### Example 2: Ball Collection Strategy

```
if(ballsPresent()) {
    takeBall();
} else {
    putBall();
}
```

This creates a consistent behavior:
- If there are balls → Karel takes one
- If there are no balls → Karel puts one down

### Example 3: Direction-Based Actions

```
if(facingEast()) {
    turnLeft();   // Turn to face north
} else {
    turnRight();  // Turn toward east from any other direction
}
```

This provides different actions based on Karel's current direction.

## Style and Formatting

There are two acceptable ways to format if/else statements:

### Style 1: Else on Same Line (Recommended)
```
if(frontIsClear()) {
    move();
} else {
    turnLeft();
}
```

### Style 2: Else on New Line
```
if(frontIsClear()) {
    move();
}
else {
    turnLeft();
}
```

Both are correct - choose one style and be consistent throughout your program.

## Practical If/Else Applications

### Safe Navigation with Alternatives

```
function navigateOrTurn() {
    if(frontIsClear()) {
        move();
    } else {
        turnLeft();
    }
}
```

This function ensures Karel always takes some action - either moving forward or changing direction.

### Adaptive Ball Handling

```
function handleBalls() {
    if(ballsPresent()) {
        takeBall();
        // Process the ball somehow
    } else {
        putBall();
        // Create a ball for future use
    }
}
```

### Smart Building Behavior

```
function buildTowerOrMove() {
    if(noBallsPresent()) {
        putBall();  // Build tower here
    } else {
        move();     // Space already occupied, move on
    }
}
```

## Complex Decision Trees

You can chain multiple if/else statements for more complex decision-making:

```
function smartNavigation() {
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

Note: This uses `else if`, which we'll explore more in advanced programming.

## Combining If/Else with Other Concepts

### If/Else with For Loops

```
function buildAlternatingPattern() {
    for(var i = 0; i < 10; i++) {
        if(ballsPresent()) {
            takeBall();     // Remove existing balls
        } else {
            putBall();      // Add balls where missing
        }
        
        if(frontIsClear()) {
            move();
        }
    }
}
```

### If/Else with Functions

```
function start() {
    for(var i = 0; i < 5; i++) {
        smartMove();
        handleCurrentPosition();
    }
}

function smartMove() {
    if(frontIsClear()) {
        move();
    } else {
        findAlternatePath();
    }
}

function handleCurrentPosition() {
    if(ballsPresent()) {
        collectBalls();
    } else {
        markPosition();
    }
}
```

## When to Use If/Else vs. Just If

### Use If/Else When:
- You want to ensure one of two actions always happens
- The actions are mutually exclusive alternatives
- You want to handle "everything else" cases efficiently

```
// Good use of if/else - exactly one action will happen
if(frontIsClear()) {
    move();
} else {
    turnLeft();
}
```

### Use Separate If Statements When:
- Multiple conditions can be true simultaneously
- Each condition represents an independent check
- Actions aren't mutually exclusive

```
// Good use of separate if statements - multiple actions might happen
if(ballsPresent()) {
    takeBall();
}

if(facingNorth()) {
    putBall();
}

if(frontIsClear()) {
    move();
}
```

## Common If/Else Mistakes

### Mistake 1: Adding Conditions to Else

```
// Wrong - else cannot have conditions
if(frontIsClear()) {
    move();
} else(frontIsBlocked()) {  // Error!
    turnLeft();
}

// Correct - else has no conditions
if(frontIsClear()) {
    move();
} else {
    turnLeft();
}
```

### Mistake 2: Forgetting Curly Braces

```
// Risky - only first command is part of else
if(frontIsClear()) {
    move();
} else
    turnLeft();
    putBall();  // This always happens!

// Correct - curly braces group all commands
if(frontIsClear()) {
    move();
} else {
    turnLeft();
    putBall();
}
```

### Mistake 3: Using Else Without If

```
// Wrong - else must follow an if
else {
    turnLeft();
}

// Correct - else follows an if
if(frontIsClear()) {
    move();
} else {
    turnLeft();
}
```

### Mistake 4: Redundant Conditions

```
// Unnecessary - if first condition is false, second must be true
if(frontIsClear()) {
    move();
}
if(frontIsBlocked()) {  // Redundant check
    turnLeft();
}

// Better - use else for the opposite condition
if(frontIsClear()) {
    move();
} else {  // This automatically means front is blocked
    turnLeft();
}
```

## The Power of If/Else: From Specific to General

If/else statements represent a major evolution in your programming thinking. You've gone from solving very specific problems to creating programs that can handle different types of worlds and situations.

### Before If/Else: Specific Solutions
```
// This only works in one specific world layout
function start() {
    move();
    move();
    turnLeft();
    move();
    putBall();
}
```

### After If/Else: General Solutions
```
// This works in many different world layouts
function start() {
    navigateToDestination();
    markArrival();
}

function navigateToDestination() {
    for(var i = 0; i < 10; i++) {
        if(frontIsClear()) {
            move();
        } else {
            turnLeft();
        }
    }
}

function markArrival() {
    if(noBallsPresent()) {
        putBall();
    } else {
        takeBall();
    }
}
```

The second version can adapt to different wall configurations and ball placements.

## Real-World Applications

If/else logic appears everywhere in programming:

**Web Development**: Show different content to logged-in vs. guest users

**Game Development**: Different actions when player presses different keys

**Mobile Apps**: Different behaviors for different device orientations

**Data Processing**: Different calculations for different data types

**Robotics**: Different responses to different sensor inputs

## Key Takeaways

1. **If/else statements handle both true and false conditions** with specific actions for each
2. **Else clauses have no conditions** - they represent "everything else"
3. **Only one code block executes** - either the if block or the else block, never both
4. **If/else makes programs more robust** by ensuring appropriate actions for all scenarios
5. **Use if/else for mutually exclusive alternatives** and separate if statements for independent checks
6. **If/else enables general solutions** that work in multiple different situations
7. **This is fundamental logic that appears in all programming languages**

If/else statements complete your understanding of basic conditional logic. Combined with functions, for loops, and if statements, you now have the essential building blocks for creating sophisticated, adaptive programs that can handle real-world complexity and variability.

You've progressed from writing programs that work in one specific situation to writing programs that can adapt to many different situations - this is the mark of mature programming thinking!