# 🗃️ Module 3: Data Structures

![Python](https://img.shields.io/badge/Python-Data%20Structures-purple?style=for-the-badge&logo=python&logoColor=white)
![Difficulty](https://img.shields.io/badge/Difficulty-Beginner-green?style=for-the-badge)

## 📖 Overview

This module introduces you to Python's built-in data structures: Lists, Tuples, Sets, and Dictionaries. These are fundamental tools for organizing and manipulating data efficiently in your programs.

## 🎯 Learning Objectives

By the end of this module, you will:
- ✅ Master Python's four main data structures
- ✅ Understand when to use each data structure
- ✅ Perform common operations on data structures
- ✅ Apply data structures to solve real-world problems
- ✅ Understand mutability vs immutability

## 📂 Module Contents

| File | Description | Data Structure |
|------|-------------|----------------|
| `3.1-Lists.ipynb` | Lists fundamentals | Ordered, mutable collections |
| `3.1.1-ListExamples.ipynb` | Advanced list operations | List methods, comprehensions |
| `3.2-Tuples.ipynb` | Tuples overview | Ordered, immutable collections |
| `3.3-Sets.ipynb` | Sets and operations | Unordered, unique elements |
| `3.4-Dictionaries.ipynb` | Dictionaries and keys | Key-value pairs |

## 🚀 Quick Start

### Prerequisites
- Completion of Module 2 (Control Flow)
- Understanding of variables and basic operations

### Running the Notebooks

```bash
# Navigate to this directory
cd "3-Data Structures"

# Start Jupyter Lab
jupyter lab

# Or start Jupyter Notebook
jupyter notebook
```

## 📚 Detailed Content Guide

### 📋 Lists (`3.1-Lists.ipynb`, `3.1.1-ListExamples.ipynb`)

**Characteristics**: Ordered, mutable, allows duplicates

```python
# Creating lists
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 42, True, 3.14]

# Common operations
fruits.append("grape")           # Add element
fruits.insert(1, "mango")       # Insert at index
fruits.remove("banana")         # Remove element
popped = fruits.pop()           # Remove and return last
fruits[0] = "pineapple"         # Modify element

# List comprehensions
squares = [x**2 for x in range(5)]
even_numbers = [x for x in range(10) if x % 2 == 0]
```

### 🔒 Tuples (`3.2-Tuples.ipynb`)

**Characteristics**: Ordered, immutable, allows duplicates

```python
# Creating tuples
coordinates = (10, 20)
colors = ("red", "green", "blue")
single_element = (42,)  # Note the comma

# Common operations
x, y = coordinates              # Unpacking
first_color = colors[0]         # Accessing elements
length = len(colors)            # Get length

# Tuples are immutable
# colors[0] = "yellow"  # This would raise an error
```

### 🎯 Sets (`3.3-Sets.ipynb`)

**Characteristics**: Unordered, mutable, unique elements only

```python
# Creating sets
unique_numbers = {1, 2, 3, 4, 5}
letters = set("hello")          # {'h', 'e', 'l', 'o'}

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union = set1 | set2             # {1, 2, 3, 4, 5}
intersection = set1 & set2      # {3}
difference = set1 - set2        # {1, 2}

# Adding and removing
unique_numbers.add(6)
unique_numbers.remove(1)
unique_numbers.discard(10)      # Won't raise error if not found
```

### 🗂️ Dictionaries (`3.4-Dictionaries.ipynb`)

**Characteristics**: Unordered (Python 3.7+ maintains insertion order), mutable, key-value pairs

```python
# Creating dictionaries
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

# Common operations
student["email"] = "alice@email.com"    # Add new key-value
name = student.get("name", "Unknown")   # Safe access
del student["age"]                      # Remove key-value

# Dictionary methods
keys = student.keys()           # Get all keys
values = student.values()       # Get all values
items = student.items()         # Get key-value pairs

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(5)}
```

## 💻 Practice Exercises

### Exercise 1: Shopping List (Lists)
```python
shopping_list = []

# Add items
shopping_list.extend(["milk", "bread", "eggs"])

# Check if item exists
if "milk" in shopping_list:
    print("Don't forget the milk!")

# Remove item
if "bread" in shopping_list:
    shopping_list.remove("bread")

print(f"Shopping list: {shopping_list}")
```

### Exercise 2: Grade Book (Dictionaries)
```python
grades = {
    "Alice": [85, 90, 92],
    "Bob": [78, 85, 80],
    "Charlie": [92, 88, 95]
}

# Calculate averages
for student, scores in grades.items():
    average = sum(scores) / len(scores)
    print(f"{student}: {average:.1f}")
```

### Exercise 3: Data Cleaning (Sets)
```python
# Remove duplicates from a list
data = [1, 2, 2, 3, 4, 4, 5, 1]
unique_data = list(set(data))
print(f"Original: {data}")
print(f"Unique: {unique_data}")

# Find common elements
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = list(set(list1) & set(list2))
print(f"Common elements: {common}")
```

## 🧪 Hands-On Activities

1. **Complete all assignment notebooks** for each data structure
2. **Create a contact book** using dictionaries
3. **Implement a simple inventory system** using lists and dictionaries
4. **Build a word frequency counter** using dictionaries
5. **Create a set-based tag system** for categorizing items

## 🔍 Key Concepts to Remember

### When to Use Each Data Structure

| Data Structure | Use When | Example Use Case |
|----------------|----------|------------------|
| **List** | Need ordered, changeable collection | Shopping list, student roster |
| **Tuple** | Need ordered, unchangeable collection | Coordinates, RGB colors |
| **Set** | Need unique elements, set operations | Tags, unique IDs |
| **Dictionary** | Need key-value mapping | Student records, configuration |

### Performance Characteristics

| Operation | List | Tuple | Set | Dictionary |
|-----------|------|-------|-----|------------|
| Access by index | O(1) | O(1) | N/A | N/A |
| Access by key | N/A | N/A | N/A | O(1) |
| Search | O(n) | O(n) | O(1) | O(1) |
| Insert | O(n) | N/A | O(1) | O(1) |
| Delete | O(n) | N/A | O(1) | O(1) |

## 🌟 Best Practices

1. **Choose the right data structure** for your use case
2. **Use list comprehensions** for creating lists efficiently
3. **Use get() method** for dictionaries to avoid KeyError
4. **Use sets for membership testing** when you have many elements
5. **Consider tuples for data that shouldn't change**
6. **Use meaningful keys** in dictionaries

## 🎯 Common Patterns

### Pattern 1: Grouping Data
```python
# Group students by grade
students = [
    {"name": "Alice", "grade": "A"},
    {"name": "Bob", "grade": "B"},
    {"name": "Charlie", "grade": "A"}
]

grouped = {}
for student in students:
    grade = student["grade"]
    if grade not in grouped:
        grouped[grade] = []
    grouped[grade].append(student["name"])
```

### Pattern 2: Counting Items
```python
# Count word frequency
text = "hello world hello python world"
word_count = {}

for word in text.split():
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)  # {'hello': 2, 'world': 2, 'python': 1}
```

### Pattern 3: Data Transformation
```python
# Transform list of dictionaries
data = [{"name": "Alice", "score": 85}, {"name": "Bob", "score": 92}]

# Extract names
names = [person["name"] for person in data]

# Create name-score mapping
scores = {person["name"]: person["score"] for person in data}
```

## 🔗 What's Next?

After mastering data structures, you're ready to move to:
- **Module 4**: Functions (Code organization and reusability)
- **Module 5**: Modules and Packages (Code modularity)

## 🆘 Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| `KeyError` in dictionary | Use `.get()` method or check if key exists |
| `IndexError` in list | Check list length before accessing index |
| Modifying list while iterating | Create a copy or iterate in reverse |
| Set elements must be immutable | Use tuples instead of lists as set elements |
| Dictionary keys must be immutable | Use strings, numbers, or tuples as keys |

## 🏆 Challenge Projects

1. **Student Management System**: Use all data structures
2. **Inventory Tracker**: Dictionaries with lists as values
3. **Text Analyzer**: Count words, characters, unique elements
4. **Recipe Book**: Nested dictionaries and lists
5. **Social Network**: Sets for connections, dictionaries for profiles

---

**Data Structures are Powerful! 💪**

*Master these fundamental containers, and you'll be able to organize and manipulate data efficiently in any Python program!* 