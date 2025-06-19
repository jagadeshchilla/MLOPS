# ⚙️ Module 4: Functions

![Python](https://img.shields.io/badge/Python-Functions-blue?style=for-the-badge&logo=python&logoColor=white)
![Difficulty](https://img.shields.io/badge/Difficulty-Intermediate-orange?style=for-the-badge)

## 📖 Overview

This module teaches you how to write reusable code using functions in Python. Learn to create modular, maintainable programs by breaking complex problems into smaller, manageable functions.

## 🎯 Learning Objectives

By the end of this module, you will:
- ✅ Define and call functions with parameters and return values
- ✅ Understand scope and variable lifetime
- ✅ Use lambda functions for concise code
- ✅ Apply map(), filter(), and reduce() functions
- ✅ Master advanced function concepts (decorators, generators)
- ✅ Write clean, reusable code

## 📂 Module Contents

| File | Description | Key Concepts |
|------|-------------|--------------|
| `4.1-functions.ipynb` | Function fundamentals | Definition, parameters, return values |
| `4.2-examplesfunctions.ipynb` | Practical examples | Real-world function applications |
| `4.3-Lambda.ipynb` | Lambda functions | Anonymous functions, one-liners |
| `4.4-Mapsfunction.ipynb` | Map function | Applying functions to iterables |
| `4.5-filterfunction.ipynb` | Filter function | Filtering data with conditions |
| `advancefunctions.ipynb` | Advanced concepts | Decorators, closures, generators |
| `advancefunctionsolution.ipynb` | Advanced solutions | Reference implementations |
| `functionsassignment.ipynb` | Practice exercises | Hands-on coding challenges |
| `functionsassignmentsoln.ipynb` | Assignment solutions | Reference solutions |
| `sample.txt` | Sample data file | File for reading exercises |

## 🚀 Quick Start

### Prerequisites
- Completion of Module 3 (Data Structures)
- Understanding of control flow and basic Python syntax

### Running the Notebooks

```bash
# Navigate to this directory
cd "4-Functions"

# Start Jupyter Lab
jupyter lab

# Or start Jupyter Notebook
jupyter notebook
```

## 📚 Detailed Content Guide

### 🔧 Function Basics (`4.1-functions.ipynb`)

#### 🔹 Defining Functions
```python
def greet(name):
    """Greet a person with their name."""
    return f"Hello, {name}!"

def calculate_area(length, width):
    """Calculate rectangle area."""
    return length * width

def print_info(name, age=18):
    """Print person info with default age."""
    print(f"Name: {name}, Age: {age}")
```

#### 🔹 Function Parameters
```python
# Positional arguments
def add(a, b):
    return a + b

result = add(5, 3)  # 8

# Keyword arguments
def create_profile(name, age, city="Unknown"):
    return {"name": name, "age": age, "city": city}

profile = create_profile(name="Alice", age=25, city="New York")

# Variable arguments
def sum_all(*args):
    return sum(args)

total = sum_all(1, 2, 3, 4, 5)  # 15

# Keyword variable arguments
def create_dict(**kwargs):
    return kwargs

data = create_dict(name="Bob", age=30, job="Engineer")
```

#### 🔹 Return Values
```python
def divide_with_remainder(dividend, divisor):
    """Return quotient and remainder."""
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

q, r = divide_with_remainder(17, 5)  # 3, 2

def validate_age(age):
    """Validate age and return boolean."""
    return 0 <= age <= 120
```

### 🔥 Lambda Functions (`4.3-Lambda.ipynb`)

**Lambda functions** are small, anonymous functions for simple operations.

```python
# Basic lambda syntax
square = lambda x: x ** 2
print(square(5))  # 25

# Lambda with multiple arguments
add = lambda x, y: x + y
print(add(3, 4))  # 7

# Lambda in sorting
students = [("Alice", 85), ("Bob", 90), ("Charlie", 78)]
students.sort(key=lambda student: student[1])  # Sort by grade

# Lambda with conditionals
max_value = lambda a, b: a if a > b else b
print(max_value(10, 5))  # 10
```

### 🗺️ Map Function (`4.4-Mapsfunction.ipynb`)

**Map** applies a function to every item in an iterable.

```python
# Basic map usage
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# Map with built-in functions
strings = ["1", "2", "3", "4"]
integers = list(map(int, strings))
print(integers)  # [1, 2, 3, 4]

# Map with custom function
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius_temps = [0, 20, 30, 40]
fahrenheit_temps = list(map(celsius_to_fahrenheit, celsius_temps))
print(fahrenheit_temps)  # [32.0, 68.0, 86.0, 104.0]

# Map with multiple iterables
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
products = list(map(lambda x, y: x * y, numbers1, numbers2))
print(products)  # [4, 10, 18]
```

### 🔍 Filter Function (`4.5-filterfunction.ipynb`)

**Filter** creates an iterator from elements of an iterable for which a function returns true.

```python
# Basic filter usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4, 6, 8, 10]

# Filter with custom function
def is_adult(age):
    return age >= 18

ages = [12, 18, 15, 21, 17, 25]
adult_ages = list(filter(is_adult, ages))
print(adult_ages)  # [18, 21, 25]

# Filter strings
words = ["python", "java", "javascript", "c++", "go"]
long_words = list(filter(lambda word: len(word) > 4, words))
print(long_words)  # ["python", "javascript"]

# Filter with None (removes falsy values)
mixed_data = [1, 0, "hello", "", None, "world", False, True]
truthy_values = list(filter(None, mixed_data))
print(truthy_values)  # [1, "hello", "world", True]
```

### 🚀 Advanced Functions (`advancefunctions.ipynb`)

#### 🔹 Decorators
```python
def timing_decorator(func):
    """Decorator to measure function execution time."""
    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    import time
    time.sleep(1)
    return "Done!"

slow_function()
```

#### 🔹 Closures
```python
def create_multiplier(factor):
    """Create a function that multiplies by factor."""
    def multiplier(number):
        return number * factor
    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15
```

#### 🔹 Generators
```python
def fibonacci_generator(n):
    """Generate Fibonacci sequence up to n terms."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Using the generator
fib_gen = fibonacci_generator(10)
fib_sequence = list(fib_gen)
print(fib_sequence)  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

## 💻 Practice Exercises

### Exercise 1: Calculator Functions
```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

def calculator(operation, a, b):
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }
    return operations.get(operation, lambda x, y: "Invalid operation")(a, b)

# Test the calculator
print(calculator('+', 5, 3))  # 8
print(calculator('/', 10, 2))  # 5.0
```

### Exercise 2: Data Processing Pipeline
```python
def clean_data(data):
    """Remove None values and convert to lowercase."""
    return list(filter(None, map(lambda x: x.lower() if x else None, data)))

def filter_long_words(words, min_length=5):
    """Filter words longer than min_length."""
    return list(filter(lambda word: len(word) >= min_length, words))

def process_text_data(raw_data):
    """Complete data processing pipeline."""
    cleaned = clean_data(raw_data)
    filtered = filter_long_words(cleaned)
    return filtered

# Test the pipeline
raw_text = ["Python", "java", None, "JAVASCRIPT", "", "Go", "Rust"]
processed = process_text_data(raw_text)
print(processed)  # ['python', 'javascript']
```

### Exercise 3: Function Factory
```python
def create_validator(min_val, max_val):
    """Create a validation function for a range."""
    def validator(value):
        return min_val <= value <= max_val
    return validator

def create_formatter(prefix, suffix):
    """Create a formatting function."""
    def formatter(text):
        return f"{prefix}{text}{suffix}"
    return formatter

# Create specific validators and formatters
age_validator = create_validator(0, 120)
score_validator = create_validator(0, 100)
html_formatter = create_formatter("<p>", "</p>")

print(age_validator(25))    # True
print(score_validator(150)) # False
print(html_formatter("Hello World"))  # <p>Hello World</p>
```

## 🧪 Hands-On Activities

1. **Complete function assignments**: Work through `functionsassignment.ipynb`
2. **Build a text analyzer**: Use map/filter to analyze text data
3. **Create a data processing pipeline**: Chain multiple functions together
4. **Implement a simple caching decorator**: Practice advanced concepts

## 🔍 Key Concepts to Remember

### Function Design Principles
- **Single Responsibility**: Each function should do one thing well
- **Pure Functions**: Avoid side effects when possible
- **Descriptive Names**: Function names should clearly indicate their purpose
- **Documentation**: Use docstrings to explain function behavior

### Functional Programming Concepts
- **Higher-Order Functions**: Functions that take other functions as arguments
- **Immutability**: Prefer not modifying input data
- **Composition**: Building complex operations by combining simple functions

## 🌟 Best Practices

1. **Use type hints**: `def add(a: int, b: int) -> int:`
2. **Write docstrings**: Document function purpose, parameters, and return values
3. **Keep functions small**: Aim for functions that fit on one screen
4. **Use meaningful parameter names**: `def calculate_tax(income, rate)` not `def calc(x, y)`
5. **Return early**: Use guard clauses to handle edge cases first
6. **Avoid global variables**: Pass data through parameters instead

## 🎯 Common Patterns

### Pattern 1: Validation and Processing
```python
def process_user_input(user_data):
    """Validate and process user input."""
    if not user_data:
        return None
    
    if not isinstance(user_data, str):
        return None
    
    # Process valid data
    return user_data.strip().lower()
```

### Pattern 2: Configuration Functions
```python
def create_api_client(base_url, api_key, timeout=30):
    """Create configured API client."""
    def make_request(endpoint, method="GET", data=None):
        # Implementation here
        return f"Making {method} request to {base_url}/{endpoint}"
    
    return make_request
```

### Pattern 3: Data Transformation Pipeline
```python
def transform_data(data, *transformations):
    """Apply multiple transformations to data."""
    result = data
    for transform in transformations:
        result = transform(result)
    return result

# Usage
numbers = [1, 2, 3, 4, 5]
result = transform_data(
    numbers,
    lambda x: map(lambda n: n * 2, x),      # Double
    lambda x: filter(lambda n: n > 5, x),   # Filter > 5
    list                                     # Convert to list
)
```

## 🔗 Integration with Other Modules

Functions serve as the building blocks for:
- **Module 5**: Organizing functions into modules and packages
- **Module 8**: Methods in classes and objects
- **Module 10**: Data analysis with pandas and numpy
- **Module 13**: Flask web application routes

## 📝 Assignment Checklist

- [ ] Define functions with parameters and return values
- [ ] Use default parameters and keyword arguments
- [ ] Master lambda functions for simple operations
- [ ] Apply map() and filter() to process data
- [ ] Understand variable scope (local vs global)
- [ ] Implement decorators and closures
- [ ] Create generator functions
- [ ] Write comprehensive function documentation
- [ ] Complete all assignment exercises

## 🆘 Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| `NameError: name 'function' is not defined` | Define function before calling it |
| Functions modifying global variables | Use parameters and return values instead |
| Complex functions that are hard to test | Break into smaller, focused functions |
| Performance issues with large datasets | Consider generators or numpy operations |
| Lambda functions becoming too complex | Use regular functions for better readability |

## 🏆 Challenge Projects

1. **Text Analysis Suite**: Functions for word counting, sentiment analysis
2. **Data Validation Library**: Comprehensive validation functions
3. **Mathematical Operations Module**: Calculator with advanced functions
4. **File Processing Pipeline**: Functions for reading, processing, and writing data
5. **API Response Processor**: Functions for handling JSON data

---

**Functions Make Code Reusable! 🔄**

*Master functions to write clean, maintainable, and efficient Python code!* 