# Module 9: Advanced Python Concepts

## Overview

This module covers advanced Python concepts that make your code more efficient, elegant, and Pythonic. Master iterators, generators, and decorators to write professional-level Python code.

## Learning Objectives

By the end of this module, you will:
- Understand and implement iterators and iterables
- Create and use generators for memory-efficient code
- Build decorators for code enhancement and reusability
- Apply advanced Python patterns and techniques
- Write more efficient and maintainable code
- Understand Python's internal mechanisms

## Module Contents

| File | Description | Key Concepts |
|------|-------------|--------------|
| `9.1-Iterators.ipynb` | Iterator protocol | `__iter__`, `__next__`, iteration |
| `9.2-Generators.ipynb` | Generator functions | `yield`, generator expressions |
| `9.3-Decorators.ipynb` | Decorator patterns | Function wrapping, closures |

## Core Concepts

### Iterators

#### Understanding the Iterator Protocol
Iterators are objects that can be iterated upon, meaning you can traverse through all the elements. The iterator protocol consists of two methods: `__iter__()`, which returns the iterator object itself, and `__next__()`, which returns the next item from the iteration. When there are no more items, `__next__()` raises a `StopIteration` exception.

### Generators

#### Generator Functions
Generator functions are a simple way to create iterators. They are defined like normal functions but use the `yield` keyword instead of `return`. When a generator function is called, it returns a generator object, which is an iterator. The `yield` keyword pauses the function's execution and sends a value back to the caller, resuming from where it left off on subsequent calls.

#### Generator Expressions
Generator expressions are similar to list comprehensions but return a generator object instead of a list. They are more memory-efficient than list comprehensions for large datasets because they generate items on the fly, one at a time, rather than creating the entire list in memory.

### Decorators

#### Basic Decorators
Decorators are a powerful and elegant way to modify or enhance functions or methods. They allow you to wrap another function to extend its behavior without explicitly modifying it. A decorator is essentially a function that takes another function as an argument, adds some functionality, and returns a new function.

#### Decorators with Parameters
Decorators can also accept arguments, allowing for more flexible and configurable enhancements. This is achieved by creating a "decorator factory" – a function that takes the decorator's parameters and returns the actual decorator function.

#### Class-based Decorators
While decorators are typically implemented as functions, they can also be implemented as classes. A class-based decorator needs to implement the `__init__` method to receive the function to be decorated and the `__call__` method to act as the wrapper function.