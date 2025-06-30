# Data Structures

## Overview

This module covers Python's four fundamental built-in data structures: Lists, Tuples, Sets, and Dictionaries. These are essential tools for organizing and storing data in Python programs.

## What We Learned

### 📋 Lists
**File:** `3.1-Lists.ipynb`, `3.1.1-ListExamples.ipynb`

Lists are ordered, mutable collections that can store multiple items of any data type. They allow duplicates and support indexing, slicing, and various methods for adding, removing, and modifying elements.

**Key Features:**
- Ordered and indexed
- Mutable (can be changed)
- Allow duplicate values
- Support various methods like append(), remove(), pop()
- List comprehensions for efficient creation

**Real-world Examples:**
- To-do lists and task management
- Student grade tracking and calculations
- Inventory management systems
- User feedback collection and analysis

### 🔒 Tuples
**File:** `3.2-Tuples.ipynb`

Tuples are ordered, immutable collections that store multiple items. Once created, their contents cannot be changed, making them ideal for data that should remain constant.

**Key Features:**
- Ordered and indexed
- Immutable (cannot be changed)
- Allow duplicate values
- Support packing and unpacking
- Can be used as dictionary keys
- Faster than lists for some operations

**Common Use Cases:**
- Storing coordinates (x, y)
- RGB color values
- Database records
- Function return values
- Configuration settings

### 🎯 Sets
**File:** `3.3-Sets.ipynb`

Sets are unordered collections of unique elements. They automatically remove duplicates and support mathematical set operations like union, intersection, and difference.

**Key Features:**
- Unordered collections
- Only unique elements (no duplicates)
- Mutable (can add/remove elements)
- Fast membership testing
- Support mathematical set operations

**Mathematical Operations:**
- Union: Combine elements from multiple sets
- Intersection: Find common elements
- Difference: Find elements in one set but not another
- Symmetric difference: Elements in either set, but not both

**Practical Applications:**
- Removing duplicates from data
- Fast membership testing
- Finding unique elements
- Data validation and comparison

### 🗂️ Dictionaries
**File:** `3.4-Dictionaries.ipynb`

Dictionaries store data in key-value pairs, providing fast lookups and natural data organization. Keys must be unique and immutable, while values can be any data type.

**Key Features:**
- Key-value pair structure
- Unordered (but maintain insertion order in Python 3.7+)
- Mutable (can modify, add, remove items)
- Fast O(1) lookup time
- Keys must be immutable, values can be anything

**Essential Methods:**
- Access: `get()` for safe retrieval
- Views: `keys()`, `values()`, `items()`
- Modification: `update()`, `pop()`, `clear()`
- Dictionary comprehensions for efficient creation

**Real-world Applications:**
- User profiles and settings
- Database-like record storage
- Configuration management
- Frequency counting and data analysis
- Caching and memoization

## When to Use Each Data Structure

- **Lists:** When you need ordered, changeable collections (shopping lists, student rosters)
- **Tuples:** When you need ordered, unchangeable collections (coordinates, database records)
- **Sets:** When you need unique elements and set operations (tags, unique IDs)
- **Dictionaries:** When you need key-value mapping and fast lookups (user data, configurations)

## Module Structure

| File | Topic | Description |
|------|-------|-------------|
| `3.1-Lists.ipynb` | Lists Fundamentals | Basic list operations and methods |
| `3.1.1-ListExamples.ipynb` | Real-world List Examples | Practical applications and use cases |
| `3.2-Tuples.ipynb` | Tuples | Immutable sequences and their uses |
| `3.3-Sets.ipynb` | Sets | Unique collections and set operations |
| `3.4-Dictionaries.ipynb` | Dictionaries | Key-value pairs and mapping operations |

## Key Concepts Mastered

- Understanding mutability vs immutability
- Choosing appropriate data structures for different scenarios
- Performing efficient operations on collections
- Working with nested data structures
- Using comprehensions for data creation and transformation
- Handling real-world data organization problems 