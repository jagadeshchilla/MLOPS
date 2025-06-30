# Control Flow in Python

## Overview

This module covers the fundamental concepts of controlling program execution flow in Python. You'll learn how to make decisions in your programs and execute code repeatedly based on conditions.

## What We Learned

### Conditional Statements

#### Basic if Statement
- Execute code only when a specific condition is true
- Understanding boolean expressions and how they evaluate
- Proper indentation for code blocks

#### if-else Statement
- Create binary decision structures
- Execute different code paths based on conditions
- Handle both true and false scenarios

#### if-elif-else Statement
- Handle multiple conditions in sequence
- Python checks conditions from top to bottom
- First true condition executes, others are skipped
- Useful for creating multiple categories or ranges

#### Nested Conditional Statements
- Place conditional statements inside other conditionals
- Create complex decision trees
- Handle multi-level decision making
- Proper indentation becomes critical with nesting

### Loops

#### Understanding range() Function
- Generate sequences of numbers for iteration
- Three forms: range(stop), range(start, stop), range(start, stop, step)
- Memory efficient - generates numbers on demand
- Essential for controlling loop iterations

#### for Loops
- Iterate over sequences and ranges
- Automatic variable management
- Perfect when you know the number of iterations
- Can iterate over strings character by character
- Support for step values including negative steps for reverse iteration

#### while Loops
- Continue execution while a condition remains true
- Require manual variable management to avoid infinite loops
- More flexible than for loops
- Ideal when the number of iterations is unknown
- Condition checked before each iteration

#### Loop Control Statements

**break Statement**
- Immediately exit the loop
- Transfer control to the statement after the loop
- Useful for early termination based on conditions

**continue Statement**
- Skip the current iteration
- Move directly to the next iteration
- Useful for filtering or conditional processing

**pass Statement**
- Null operation that does nothing
- Acts as a placeholder where code is syntactically required
- Useful for future implementation or empty exception handlers

#### Nested Loops
- Loops inside other loops
- Outer loop controls major iterations
- Inner loop completes all iterations for each outer loop iteration
- Total iterations = outer iterations × inner iterations
- Common in matrix operations and pattern generation

### Practical Applications

#### Mathematical Calculations
- Sum of natural numbers using both while and for loops
- Comparison of different approaches to the same problem
- Understanding algorithm efficiency

#### Prime Number Detection
- Complex nested loop structures
- Using break statements for early termination
- Loop-else construct for clean prime detection logic
- Demonstrates practical use of multiple loop concepts together

## Key Concepts Mastered

### Decision Making
- Boolean logic and condition evaluation
- Sequential condition checking
- Complex nested decision structures
- Real-world problem solving with conditionals

### Iteration Control
- Different types of loops for different scenarios
- Loop variable management
- Controlling loop execution flow
- Optimizing loop performance

### Program Flow
- Understanding how Python executes conditional and loop structures
- Combining conditionals and loops for complex logic
- Creating efficient and readable code structures

## Module Files

- **Conditionalstatements.ipynb**: Complete guide to if, elif, else statements with practical examples
- **Loops.ipynb**: Comprehensive coverage of for loops, while loops, and loop control statements

