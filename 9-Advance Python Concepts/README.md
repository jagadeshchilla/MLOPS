# 🚀 Module 9: Advanced Python Concepts

![Python](https://img.shields.io/badge/Python-Advanced%20Concepts-gold?style=for-the-badge&logo=python&logoColor=white)
![Difficulty](https://img.shields.io/badge/Difficulty-Advanced-red?style=for-the-badge)

## 📖 Overview

This module covers advanced Python concepts that make your code more efficient, elegant, and Pythonic. Master iterators, generators, and decorators to write professional-level Python code.

## 🎯 Learning Objectives

By the end of this module, you will:
- ✅ Understand and implement iterators and iterables
- ✅ Create and use generators for memory-efficient code
- ✅ Build decorators for code enhancement and reusability
- ✅ Apply advanced Python patterns and techniques
- ✅ Write more efficient and maintainable code
- ✅ Understand Python's internal mechanisms

## 📂 Module Contents

| File | Description | Key Concepts |
|------|-------------|--------------|
| `9.1-Iterators.ipynb` | Iterator protocol | `__iter__`, `__next__`, iteration |
| `9.2-Generators.ipynb` | Generator functions | `yield`, generator expressions |
| `9.3-Decorators.ipynb` | Decorator patterns | Function wrapping, closures |

## 🚀 Quick Start

### Prerequisites
- Completion of Module 8 (Classes and Objects)
- Strong understanding of functions and OOP concepts

### Running the Notebooks

```bash
# Navigate to this directory
cd "9-Advance Python Concepts"

# Start Jupyter Lab
jupyter lab

# Or start Jupyter Notebook
jupyter notebook
```

## 📚 Detailed Content Guide

### 🔄 Iterators (`9.1-Iterators.ipynb`)

#### 🔹 Understanding the Iterator Protocol
```python
# Built-in iterator example
numbers = [1, 2, 3, 4, 5]
iterator = iter(numbers)

print(next(iterator))  # 1
print(next(iterator))  # 2
# StopIteration raised when exhausted

# Custom iterator
class CountDown:
    def __init__(self, start):
        self.start = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        self.start -= 1
        return self.start + 1

# Usage
countdown = CountDown(3)
for num in countdown:
    print(num)  # 3, 2, 1
```

#### 🔹 Advanced Iterator Examples
```python
class FibonacciIterator:
    """Iterator for Fibonacci sequence."""
    
    def __init__(self, max_count):
        self.max_count = max_count
        self.count = 0
        self.a, self.b = 0, 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count >= self.max_count:
            raise StopIteration
        
        if self.count == 0:
            self.count += 1
            return self.a
        elif self.count == 1:
            self.count += 1
            return self.b
        else:
            self.a, self.b = self.b, self.a + self.b
            self.count += 1
            return self.b

class RangeIterator:
    """Custom range iterator."""
    
    def __init__(self, start, stop, step=1):
        self.current = start
        self.stop = stop
        self.step = step
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if (self.step > 0 and self.current >= self.stop) or \
           (self.step < 0 and self.current <= self.stop):
            raise StopIteration
        
        result = self.current
        self.current += self.step
        return result
```

### 🌟 Generators (`9.2-Generators.ipynb`)

#### 🔹 Generator Functions
```python
def countdown_generator(start):
    """Generator function for countdown."""
    while start > 0:
        yield start
        start -= 1

# Usage
for num in countdown_generator(5):
    print(num)  # 5, 4, 3, 2, 1

def fibonacci_generator(max_count):
    """Generate Fibonacci sequence."""
    a, b = 0, 1
    count = 0
    
    while count < max_count:
        yield a
        a, b = b, a + b
        count += 1

# Memory efficient - generates on demand
fib_gen = fibonacci_generator(10)
fib_list = list(fib_gen)
print(fib_list)
```

#### 🔹 Generator Expressions
```python
# Generator expression (like list comprehension but lazy)
squares_gen = (x**2 for x in range(10))
print(next(squares_gen))  # 0
print(next(squares_gen))  # 1

# Memory efficient file processing
def read_large_file(filepath):
    """Read large file line by line."""
    with open(filepath, 'r') as file:
        for line in file:
            yield line.strip()

# Process without loading entire file
def count_words_in_large_file(filepath):
    """Count words without loading entire file."""
    total_words = 0
    for line in read_large_file(filepath):
        total_words += len(line.split())
    return total_words
```

#### 🔹 Advanced Generator Patterns
```python
def pipeline_example():
    """Demonstrate generator pipeline."""
    
    def numbers():
        """Generate numbers."""
        for i in range(10):
            yield i
    
    def squares(nums):
        """Square the numbers."""
        for num in nums:
            yield num ** 2
    
    def evens(nums):
        """Filter even numbers."""
        for num in nums:
            if num % 2 == 0:
                yield num
    
    # Chain generators together
    result = evens(squares(numbers()))
    return list(result)  # [0, 4, 16, 36, 64]

# Generator with send() method
def accumulator():
    """Generator that accumulates values."""
    total = 0
    while True:
        value = yield total
        if value is not None:
            total += value

# Usage
acc = accumulator()
next(acc)  # Prime the generator
print(acc.send(10))  # 10
print(acc.send(5))   # 15
```

### 🎨 Decorators (`9.3-Decorators.ipynb`)

#### 🔹 Basic Decorators
```python
def timer_decorator(func):
    """Decorator to measure execution time."""
    import time
    import functools
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer_decorator
def slow_function():
    import time
    time.sleep(1)
    return "Done!"

# Usage
result = slow_function()  # Prints timing information
```

#### 🔹 Decorators with Parameters
```python
def retry(max_attempts=3, delay=1):
    """Decorator to retry function on failure."""
    def decorator(func):
        import time
        import functools
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < max_attempts - 1:
                        print(f"Attempt {attempt + 1} failed: {e}")
                        time.sleep(delay)
                    else:
                        print(f"All {max_attempts} attempts failed")
            
            raise last_exception
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.5)
def unreliable_function():
    import random
    if random.random() < 0.7:
        raise Exception("Random failure")
    return "Success!"
```

#### 🔹 Class-based Decorators
```python
class CountCalls:
    """Decorator to count function calls."""
    
    def __init__(self, func):
        self.func = func
        self.count = 0
        functools.update_wrapper(self, func)
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"{self.func.__name__} has been called {self.count} times")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello(name):
    return f"Hello, {name}!"

# Usage
say_hello("Alice")  # say_hello has been called 1 times
say_hello("Bob")    # say_hello has been called 2 times
```

#### 🔹 Advanced Decorator Patterns
```python
def cache(maxsize=128):
    """LRU cache decorator."""
    def decorator(func):
        import functools
        
        @functools.lru_cache(maxsize=maxsize)
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        
        # Add cache info method
        wrapper.cache_info = wrapper.cache_info
        wrapper.cache_clear = wrapper.cache_clear
        return wrapper
    return decorator

@cache(maxsize=64)
def expensive_calculation(n):
    """Simulate expensive calculation."""
    import time
    time.sleep(0.1)  # Simulate work
    return n * n

# Property decorator for classes
def validate_type(expected_type):
    """Decorator for type validation."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, value):
            if not isinstance(value, expected_type):
                raise TypeError(f"Expected {expected_type.__name__}, got {type(value).__name__}")
            return func(self, value)
        return wrapper
    return decorator

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    @validate_type(str)
    def name(self, value):
        self._name = value
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    @validate_type(int)
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value
```

## 💻 Practice Exercises

### Exercise 1: Custom Range with Step
```python
class CustomRange:
    """Enhanced range with additional features."""
    
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            start, stop = 0, start
        
        self.start = start
        self.stop = stop
        self.step = step
    
    def __iter__(self):
        current = self.start
        while (self.step > 0 and current < self.stop) or \
              (self.step < 0 and current > self.stop):
            yield current
            current += self.step
    
    def __len__(self):
        if self.step == 0:
            raise ValueError("step argument must not be zero")
        return max(0, (self.stop - self.start + self.step - 1) // self.step)
    
    def __contains__(self, value):
        if self.step == 0:
            return False
        if self.step > 0:
            return self.start <= value < self.stop and (value - self.start) % self.step == 0
        else:
            return self.start >= value > self.stop and (self.start - value) % (-self.step) == 0
```

### Exercise 2: Data Processing Pipeline
```python
def data_pipeline():
    """Create a data processing pipeline using generators."""
    
    def read_data():
        """Simulate reading data."""
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for item in data:
            yield item
    
    def filter_even(data_stream):
        """Filter even numbers."""
        for item in data_stream:
            if item % 2 == 0:
                yield item
    
    def multiply_by_two(data_stream):
        """Multiply each item by 2."""
        for item in data_stream:
            yield item * 2
    
    def accumulate(data_stream):
        """Accumulate running sum."""
        total = 0
        for item in data_stream:
            total += item
            yield total
    
    # Build pipeline
    pipeline = accumulate(multiply_by_two(filter_even(read_data())))
    return list(pipeline)
```

## 🧪 Hands-On Activities

1. **Build a custom iterator**: Create an iterator for tree traversal
2. **Design a generator pipeline**: Process data streams efficiently
3. **Create utility decorators**: Build debugging and profiling decorators
4. **Implement caching system**: Use decorators for memoization

## 🔍 Key Concepts to Remember

### Memory Efficiency
- **Generators**: Use memory proportional to one item, not the entire sequence
- **Lazy Evaluation**: Compute values only when needed
- **Iterator Protocol**: Standard way to traverse collections

### Decorator Benefits
- **Code Reuse**: Apply same functionality to multiple functions
- **Separation of Concerns**: Keep business logic separate from cross-cutting concerns
- **Clean Code**: Enhance functions without modifying their core logic

## 🌟 Best Practices

1. **Use generators for large datasets**: Avoid loading everything into memory
2. **Keep decorators simple**: Complex decorators are hard to debug
3. **Preserve function metadata**: Use `functools.wraps`
4. **Document decorator behavior**: Explain what the decorator does
5. **Test decorated functions**: Ensure decorators don't break functionality
6. **Use built-in tools**: `itertools`, `functools` modules


## 🆘 Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| Generator exhaustion | Generators can only be used once |
| Decorator argument confusion | Use decorator factories for parameters |
| Memory leaks with generators | Ensure proper cleanup and exception handling |
| Complex decorator debugging | Use `functools.wraps` and proper logging |
| Iterator state management | Be careful with mutable iterator state |

## 🏆 Challenge Projects

1. **Stream Processing Framework**: Build a data processing pipeline
2. **Caching Library**: Advanced memoization with different strategies
3. **Async Task Scheduler**: Use generators for task management
4. **Custom Collection Types**: Implement advanced data structures
5. **Profiling Toolkit**: Comprehensive function profiling decorators

---

**Advanced Python Unlocks True Power! ⚡**

*Master these concepts to write elegant, efficient, and professional Python code!* 