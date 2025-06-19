# 🔀 Module 2: Control Flow

![Python](https://img.shields.io/badge/Python-Control%20Flow-orange?style=for-the-badge&logo=python&logoColor=white)
![Difficulty](https://img.shields.io/badge/Difficulty-Beginner-green?style=for-the-badge)

## 📖 Overview

This module teaches you how to control the flow of your Python programs using conditional statements and loops. You'll learn to make decisions in your code and execute repetitive tasks efficiently.

## 🎯 Learning Objectives

By the end of this module, you will:
- ✅ Write conditional statements using if, elif, and else
- ✅ Implement various types of loops (for, while)
- ✅ Understand loop control statements (break, continue)
- ✅ Apply nested conditions and loops
- ✅ Handle decision-making logic in programs

## 📂 Module Contents

| File | Description | Key Concepts |
|------|-------------|--------------|
| `Conditionalstatements.ipynb` | If, elif, else statements | Decision making, boolean logic |
| `Loops.ipynb` | For and while loops | Iteration, range, loop control |
| `assignments.ipynb` | Practice exercises | Hands-on coding challenges |
| `assignment_solutions.ipynb` | Solutions to exercises | Reference solutions with explanations |

## 🚀 Quick Start

### Prerequisites
- Completion of Module 1 (Python Basics)
- Understanding of variables and operators

### Running the Notebooks

```bash
# Navigate to this directory
cd "2-Control Flow"

# Start Jupyter Lab
jupyter lab

# Or start Jupyter Notebook
jupyter notebook
```

## 📚 Detailed Content Guide

### Conditional Statements (`Conditionalstatements.ipynb`)

#### 🔹 If Statement
```python
age = 18
if age >= 18:
    print("You are an adult")
```

#### 🔹 If-Else Statement
```python
score = 85
if score >= 60:
    print("Pass")
else:
    print("Fail")
```

#### 🔹 If-Elif-Else Statement
```python
grade = 92
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
else:
    print("F")
```

#### 🔹 Nested Conditions
```python
weather = "sunny"
temperature = 25

if weather == "sunny":
    if temperature > 20:
        print("Perfect day for outdoor activities!")
    else:
        print("Sunny but a bit cold")
```

### Loops (`Loops.ipynb`)

#### 🔄 For Loops
```python
# Iterating through a range
for i in range(5):
    print(f"Number: {i}")

# Iterating through a list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I like {fruit}")
```

#### 🔄 While Loops
```python
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1
```

#### 🔄 Loop Control Statements
```python
# Break statement
for i in range(10):
    if i == 5:
        break
    print(i)

# Continue statement
for i in range(5):
    if i == 2:
        continue
    print(i)
```

## 💻 Practice Exercises

### Exercise 1: Grade Calculator
```python
def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Test the function
student_score = 85
print(f"Grade: {calculate_grade(student_score)}")
```

### Exercise 2: Number Guessing Game
```python
import random

secret_number = random.randint(1, 10)
guess = 0

while guess != secret_number:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Congratulations! You guessed it!")
```

### Exercise 3: Multiplication Table
```python
number = 7
print(f"Multiplication table for {number}:")
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")
```

## 🧪 Hands-On Activities

1. **Complete assignment exercises**: Work through `assignments.ipynb`
2. **Create a simple calculator**: Use conditional statements for operations
3. **Build a countdown timer**: Use while loops with decremental logic
4. **Pattern printing**: Use nested loops to create patterns

## 🔍 Key Concepts to Remember

### Conditional Statements
- **Boolean expressions**: Conditions that evaluate to True or False
- **Comparison operators**: `==`, `!=`, `<`, `>`, `<=`, `>=`
- **Logical operators**: `and`, `or`, `not`
- **Indentation**: Critical for defining code blocks

### Loops
- **For loops**: Best for known number of iterations
- **While loops**: Best for unknown number of iterations
- **Range function**: `range(start, stop, step)`
- **Loop control**: `break` (exit loop), `continue` (skip iteration)

## 🌟 Best Practices

1. **Use descriptive variable names**: `user_age` instead of `age`
2. **Keep conditions simple**: Break complex conditions into smaller parts
3. **Avoid infinite loops**: Always ensure while loops have exit conditions
4. **Use elif instead of multiple if statements** when checking related conditions
5. **Comment complex logic**: Explain the purpose of conditions and loops

## 🎯 Common Patterns

### Pattern 1: Input Validation
```python
while True:
    user_input = input("Enter a positive number: ")
    if user_input.isdigit() and int(user_input) > 0:
        number = int(user_input)
        break
    else:
        print("Invalid input. Please try again.")
```

### Pattern 2: Menu System
```python
while True:
    print("\n--- Menu ---")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        print("You selected Option 1")
    elif choice == "2":
        print("You selected Option 2")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
```

## 🔗 What's Next?

After mastering control flow, you're ready to move to:
- **Module 3**: Data Structures (Lists, tuples, sets, dictionaries)
- **Module 4**: Functions (Code organization and reusability)

## 📝 Assignment Checklist

- [ ] Understand if, elif, else statements
- [ ] Master for and while loops
- [ ] Use break and continue statements
- [ ] Implement nested conditions and loops
- [ ] Create programs with decision-making logic
- [ ] Complete all assignment exercises

## 🆘 Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| `IndentationError` | Check proper indentation for code blocks |
| Infinite loops | Ensure loop conditions can become False |
| `SyntaxError` in conditions | Check for proper use of comparison operators |
| Logic errors in conditions | Test with different input values |
| Nested loop confusion | Use descriptive variable names for loop counters |

## 🏆 Challenge Projects

1. **Rock, Paper, Scissors Game**: Use conditionals for game logic
2. **Prime Number Checker**: Use loops to check divisibility
3. **Password Strength Validator**: Use multiple conditions
4. **Simple ATM System**: Combine loops and conditionals

---

**Keep Practicing! 🚀**

*Control flow is the foundation of programming logic. Master these concepts, and you'll be able to solve complex problems!* 