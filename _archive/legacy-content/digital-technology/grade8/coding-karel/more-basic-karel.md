---
layout: page
title: More Basic Karel
parent: Introduction to Coding (JavaScript with Karel)
grand_parent: Grade 8 Digital Technology
nav_order: 2
---

# More Basic Karel
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Exploring Karel's World in Detail

Now that you understand Karel's basic commands, let's explore Karel's world more thoroughly. Understanding the coordinate system and navigation will help you write more complex programs and solve challenging problems.

## The Grid Coordinate System

Karel's world operates like a map with a coordinate system. Every location has a specific address that can be described using two numbers.

![Karel's world showing numbered grid from 1-10 on both axes](./images/karel-grid-coordinates.jpg)

### Streets and Avenues

**Streets (Horizontal Rows)**
- Streets run from left to right (horizontally)
- Street numbers start at 1 at the bottom and increase going up
- The bottom row is Street 1, the next row up is Street 2, and so on

**Avenues (Vertical Columns)**
- Avenues run from bottom to top (vertically) 
- Avenue numbers start at 1 on the left and increase going right
- The leftmost column is Avenue 1, the next column right is Avenue 2, and so on

### Locating Karel

Any position in Karel's world can be described using its street and avenue number. For example:
- **Street 1, Avenue 1**: Bottom-left corner
- **Street 5, Avenue 8**: Fifth row up, eighth column from the left
- **Street 10, Avenue 10**: Top-right corner (in a 10x10 world)

![Karel positioned at specific coordinates with street and avenue labels](./images/karel-position-coordinates.jpg)

## Obstacles in Karel's World

Karel's world isn't always empty. Sometimes there are walls that block Karel's movement.

### Walls

**Wall Function**
Walls act as barriers that Karel cannot move through. If Karel tries to move into a wall, the program will stop with an error.

**Wall Placement**
Walls can be placed:
- Between intersections (blocking movement)
- Around the edges of the world (creating boundaries)
- In complex patterns to create maze-like challenges

![Karel's world showing walls blocking movement paths](./images/karel-world-walls.jpg)

Planning your program requires checking for walls and finding paths around them.

## Cardinal Directions

Karel navigates using the four cardinal directions, just like a compass.

![Compass rose showing North, South, East, West directions](./images/cardinal-directions-compass.jpg)

### The Four Directions

**North**: Up (toward higher street numbers)
**East**: Right (toward higher avenue numbers)  
**South**: Down (toward lower street numbers)
**West**: Left (toward lower avenue numbers)

Karel always faces one of these four directions and can only move forward in the direction Karel is facing.

## Karel's Sense of Direction

While we describe directions using North, South, East, and West, Karel thinks about direction relative to the way Karel is facing.

### Relative Directions

**Front**: The direction Karel is currently facing
**Left**: 90 degrees counterclockwise from front
**Right**: 90 degrees clockwise from front

![Karel showing front, left, and right relative to current facing direction](./images/karel-relative-directions.jpg)

This relative thinking is important because Karel's `turnLeft()` command always turns Karel 90 degrees to Karel's left, regardless of which cardinal direction that represents.

## Understanding the turnLeft() Command

The `turnLeft()` command rotates Karel 90 degrees counterclockwise. Let's see how this works from each starting direction.

### Turning From Each Direction

**Starting East → Turn Left → Now Facing North**
If Karel faces east (right) and turns left, Karel now faces north (up).

![Karel facing east, then turning left to face north](./images/karel-turn-east-north.jpg)

**Starting North → Turn Left → Now Facing West**
If Karel faces north (up) and turns left, Karel now faces west (left).

**Starting West → Turn Left → Now Facing South**
If Karel faces west (left) and turns left, Karel now faces south (down).

**Starting South → Turn Left → Now Facing East**
If Karel faces south (down) and turns left, Karel now faces east (right).

### Important Note About Turning Right

Karel only knows how to turn left. To turn right, you need to turn left three times:
- Turn left once: 90 degrees left
- Turn left twice: 180 degrees (facing opposite direction)
- Turn left three times: 270 degrees left = 90 degrees right

## Building More Complex Programs

Now that you understand navigation better, let's create a more complex program that uses multiple commands in sequence.

### Program Challenge: Reach the Center

**Starting Position**: Karel begins at Street 1, Avenue 1, facing East
**Goal**: Get Karel to Street 2, Avenue 2, place a tennis ball, then face the original direction (East)

![Before and after images showing Karel's journey to center of small world](./images/karel-center-program.jpg)

### Planning the Solution

Think through this step-by-step:
1. Karel needs to move one space east
2. Karel needs to turn to face north
3. Karel needs to move one space north
4. Karel needs to place a tennis ball
5. Karel needs to turn back to face east

### The Program

```
move();
turnLeft();
move();
putBall();
turnLeft();
turnLeft();
turnLeft();
```

### Breaking Down the Program

**Line 1**: `move();` - Karel moves from Avenue 1 to Avenue 2 (still on Street 1, facing East)

**Line 2**: `turnLeft();` - Karel turns to face North

**Line 3**: `move();` - Karel moves from Street 1 to Street 2 (now at Avenue 2, Street 2)

**Line 4**: `putBall();` - Karel places a tennis ball at the center position

**Lines 5-7**: Three `turnLeft();` commands turn Karel back to face East
- First `turnLeft()`: East → North → West
- Second `turnLeft()`: West → South  
- Third `turnLeft()`: South → East

## Programming Concepts Reinforced

This more complex program demonstrates several important programming concepts:

### Sequential Execution

Commands execute in the exact order they're written. Changing the order would create a completely different result.

### Planning and Visualization

Before writing code, successful programmers visualize the problem and plan their solution step-by-step.

### Efficiency Considerations

There might be multiple ways to solve the same problem. Consider whether this solution is the most efficient or if there are shorter alternatives.

### Testing and Verification

After writing a program, trace through each command to verify it produces the expected result.

## Common Challenges and Solutions

### Challenge: Karel Hits a Wall

**Problem**: Your program tries to move Karel into a wall
**Solution**: Plan your path carefully and check the world layout before writing commands

### Challenge: Karel Goes the Wrong Direction

**Problem**: Karel ends up facing the wrong way
**Solution**: Count your `turnLeft()` commands carefully and remember that turning right requires three left turns

### Challenge: Complex Navigation

**Problem**: Getting Karel to a distant location
**Solution**: Break the journey into smaller steps - move to intermediate positions first

## Building Problem-Solving Skills

Working with Karel develops critical programming skills:

**Spatial Reasoning**: Understanding how Karel moves through 2D space
**Logical Sequencing**: Organizing commands in the correct order
**Debugging**: Finding and fixing errors in your command sequence
**Efficiency**: Finding the shortest or most elegant solution

## Key Takeaways

1. **Karel's world uses a coordinate system** with numbered streets and avenues
2. **Walls can block Karel's movement** and must be considered when planning programs
3. **Karel thinks in relative directions** (front, left, right) rather than absolute directions
4. **Turning left rotates Karel 90 degrees counterclockwise** from the current facing direction
5. **Complex programs combine multiple commands** in carefully planned sequences
6. **Planning before coding** leads to more successful programs
7. **Multiple solutions may exist** for the same problem

Understanding these fundamentals prepares you for more advanced Karel programming concepts, including functions, loops, and conditional statements that will make your programs even more powerful and efficient.