---
layout: page
title: Karel Can't Turn Right
parent: Introduction to Coding (JavaScript with Karel)
grand_parent: Grade 8 Digital Technology
nav_order: 3
---

# Karel Can't Turn Right
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## The Problem with Only Turning Left

So far, Karel has only known four basic commands: `move()`, `turnLeft()`, `putBall()`, and `takeBall()`. While these commands are powerful, they can sometimes lead to awkward and repetitive code, especially when you need Karel to turn right.

## Revisiting the Tower Problem

Let's imagine we've built a tower of tennis balls and Karel is at the top, facing north. Now we want Karel to come back down to the bottom of the tower.

![Karel at the top of a tennis ball tower, facing north](./images/karel-tower-top.jpg)

### The Challenge

To get Karel facing downward (south) to descend the tower, we need Karel to turn right. But Karel doesn't know how to `turnRight()`! 

### The Awkward Solution

With only `turnLeft()` available, we have to tell Karel:

```
turnLeft();
turnLeft();
turnLeft();
```

This works because three left turns equal one right turn:
- First `turnLeft()`: North → West
- Second `turnLeft()`: West → South  
- Third `turnLeft()`: South → East... wait, that's too far!

Actually, let me correct that:
- First `turnLeft()`: North → West
- Second `turnLeft()`: West → South
- Third `turnLeft()`: South → East

That's still not right. Let me think through this properly:

If Karel is facing North and wants to face South (turn right):
- First `turnLeft()`: North → West
- Second `turnLeft()`: West → South

So it's actually just two left turns to go from North to South. But for a 90-degree right turn:
- First `turnLeft()`: North → West  
- Second `turnLeft()`: West → South
- Third `turnLeft()`: South → East

Yes, three left turns equals one right turn.

![Diagram showing three left turns equaling one right turn](./images/karel-three-left-turns.jpg)

### Why This is Problematic

Writing `turnLeft()` three times every time you want to turn right has several problems:

**Poor Readability**: It's not immediately clear what three left turns are supposed to accomplish.

**More Typing**: You have to write three lines instead of one.

**Error-Prone**: You might accidentally write two or four `turnLeft()` commands instead of three.

**Unclear Intent**: Someone reading your code has to figure out that you're trying to turn right.

## Don't You Wish You Could Say turnRight()?

Wouldn't it be much clearer if you could simply write:

```
turnRight();
```

This would make your code:
- Easier to read and understand
- Shorter and cleaner
- More expressive of your actual intent
- Less likely to contain errors

## Introducing Functions

The solution to this problem is **functions** - a way to teach Karel new commands!

### What is a Function?

A function is a way to teach Karel a new word or command. Just like you might teach a dog a new trick by combining basic actions they already know, you can teach Karel new commands by combining the basic commands Karel already understands.

![Concept diagram showing basic commands combining into new function](./images/function-concept-diagram.jpg)

Think of functions as:
- **Custom commands** that you create
- **Recipes** that combine basic ingredients (commands) into something new
- **Shortcuts** that package multiple steps into one easy command
- **Building blocks** for more complex programs

## Writing the turnRight() Function

Let's teach Karel how to turn right by creating a `turnRight()` function.

### Step 1: Declare the Function

First, we need to tell Karel that `turnRight()` is going to be a new command:

```
function turnRight() {

}
```

![Code showing function declaration with empty body](./images/function-declaration.jpg)

This creates an empty function. Karel now knows that `turnRight()` is a command, but doesn't yet know what it should do.

### Step 2: Define What the Function Does

Now we need to fill in the **function body** - the commands that Karel should execute when we call `turnRight()`:

```
function turnRight() {
    turnLeft();
    turnLeft();
    turnLeft();
}
```

![Complete turnRight function with three turnLeft commands in body](./images/turnright-function-complete.jpg)

### Understanding Function Syntax

Let's break down the parts of our function:

**`function`** - This keyword tells Karel we're creating a new function

**`turnRight`** - This is the name of our new function (what we'll call it)

**`()`** - Parentheses are required after the function name (we'll learn why later)

**`{`** - Opening curly brace marks the beginning of the function body

**Function Body** - The commands between the curly braces that execute when the function is called

**`}`** - Closing curly brace marks the end of the function body

### Key Syntax Rules

**Exact Spelling**: Function names must be spelled exactly the same way every time

**Parentheses Required**: Always include `()` after the function name

**Curly Braces**: Everything Karel should do must be INSIDE the curly braces

**Indentation**: Commands inside the function should be indented for readability

## Using Your New Function

Once you've defined the `turnRight()` function, you can use it just like any of Karel's built-in commands:

```
move();
turnRight();  // This now works!
move();
putBall();
```

![Karel using the new turnRight function in a program](./images/karel-using-turnright.jpg)

When Karel encounters `turnRight()` in your program, Karel will automatically execute the three `turnLeft()` commands you defined in the function body.

## Benefits of Functions

Creating the `turnRight()` function demonstrates several important benefits:

### Improved Readability

**Before (confusing):**
```
move();
turnLeft();
turnLeft();
turnLeft();
move();
```

**After (clear):**
```
move();
turnRight();
move();
```

### Reusability

Once you define `turnRight()`, you can use it as many times as needed throughout your program without rewriting the three `turnLeft()` commands.

### Easier Maintenance

If you later discovered a better way to turn right, you'd only need to change the function definition in one place, not everywhere you turn right.

### Building Complexity

Functions let you build more complex behaviors by combining simpler ones, just like building with LEGO blocks.

## Function Concepts in Programming

The `turnRight()` function introduces several fundamental programming concepts:

### Abstraction

Functions let you think at a higher level. Instead of worrying about the details of three left turns, you can simply think "turn right."

### Code Reuse

Write once, use many times. This is a core principle of efficient programming.

### Modularity

Programs become collections of functions that each handle specific tasks.

### Problem Decomposition

Complex problems can be broken down into simpler functions.

## Real-World Function Examples

Functions in Karel are similar to functions in real life:

**Recipe Functions**: A cake recipe is like a function - it combines basic ingredients and steps into something more complex.

**Math Functions**: In mathematics, f(x) = 2x + 1 is a function that transforms an input into an output.

**Machine Functions**: A car's "start" function combines many basic operations (fuel injection, spark ignition, etc.) into one simple action.

## Common Mistakes and Tips

### Function Definition vs. Function Call

**Definition** (teaching Karel what turnRight means):
```
function turnRight() {
    turnLeft();
    turnLeft();
    turnLeft();
}
```

**Call** (telling Karel to turn right):
```
turnRight();
```

### Remember the Syntax

- Don't forget the `function` keyword when defining
- Always include parentheses `()`
- Use curly braces `{}` to contain the function body
- Indent commands inside the function for readability

### Define Before Use

You must define a function before you can use it in your program. Define your functions at the top of your program or before the first place you call them.

## Key Takeaways

1. **Karel's basic commands can be limiting** when you need more complex behaviors
2. **Functions let you teach Karel new commands** by combining existing ones
3. **Function syntax requires specific keywords and symbols** (`function`, `()`, `{}`)
4. **Functions improve code readability** by giving meaningful names to complex operations
5. **Functions enable code reuse** - write once, use many times
6. **Functions are building blocks** for more complex programs
7. **This is your first step into real programming** - functions exist in all programming languages

Creating the `turnRight()` function marks an important milestone in your programming journey. You've moved from simply using pre-existing commands to creating your own custom commands. This is the foundation for building increasingly sophisticated programs and is a skill that transfers directly to all programming languages.

Next, you'll learn about more advanced function concepts and how to create even more useful custom commands for Karel.