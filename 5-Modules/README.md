# 📦 Module 5: Modules and Packages

![Python](https://img.shields.io/badge/Python-Modules%20%26%20Packages-green?style=for-the-badge&logo=python&logoColor=white)
![Difficulty](https://img.shields.io/badge/Difficulty-Intermediate-orange?style=for-the-badge)

## 📖 Overview

This module teaches you how to organize your Python code into reusable modules and packages. Learn to import functionality, use the Python standard library, and create your own packages for better code organization.

## 🎯 Learning Objectives

By the end of this module, you will:
- ✅ Understand Python's import system
- ✅ Use the Python standard library effectively
- ✅ Create and organize custom modules
- ✅ Build packages with proper structure
- ✅ Handle file operations and directory management
- ✅ Follow best practices for code organization

## 📂 Module Contents

| File | Description | Key Concepts |
|------|-------------|--------------|
| `5.1-import.ipynb` | Import systems | import, from, as keywords |
| `5.2-Standardlibrary.ipynb` | Built-in modules | os, sys, datetime, math, random |
| `packagesquestion.ipynb` | Package exercises | Package creation, __init__.py |
| `packagessolution.ipynb` | Package solutions | Reference implementations |
| `test.py` | Custom module example | Module creation and testing |
| `source.txt` | Source file for operations | File handling examples |
| `destination.txt` | Destination file | File copying demonstrations |

### 📁 Package Structure
```
package/
├── __init__.py          # Package initialization
├── maths.py            # Mathematics utilities
└── subpackages/        # Nested package
    ├── __init__.py     # Subpackage initialization
    └── mult.py         # Multiplication utilities
```

### 📁 Test Directory
```
test_dir/               # Directory for file operations
```

## 🚀 Quick Start

### Prerequisites
- Completion of Module 4 (Functions)
- Understanding of Python functions and variables

### Running the Notebooks

```bash
# Navigate to this directory
cd "5-Modules"

# Start Jupyter Lab
jupyter lab

# Or start Jupyter Notebook
jupyter notebook
```

## 📚 Detailed Content Guide

### 📥 Import Systems (`5.1-import.ipynb`)

#### 🔹 Basic Import Statements
```python
# Import entire module
import math
result = math.sqrt(16)  # 4.0

# Import specific functions
from math import sqrt, pi
result = sqrt(25)       # 5.0
area = pi * (5 ** 2)   # 78.54

# Import with alias
import numpy as np
array = np.array([1, 2, 3])

# Import all (use sparingly)
from math import *
```

#### 🔹 Custom Module Imports
```python
# Import custom module
import test
test.my_function()

# Import specific function from custom module
from test import specific_function
specific_function()

# Import from package
from package import maths
from package.maths import add, subtract

# Import from subpackage
from package.subpackages.mult import multiply
```

#### 🔹 Conditional Imports
```python
try:
    import pandas as pd
    PANDAS_AVAILABLE = True
except ImportError:
    PANDAS_AVAILABLE = False
    print("Pandas not available")

# Or use importlib
import importlib
import sys

def optional_import(module_name):
    try:
        return importlib.import_module(module_name)
    except ImportError:
        return None

numpy = optional_import('numpy')
if numpy:
    print("NumPy is available")
```

### 📚 Standard Library (`5.2-Standardlibrary.ipynb`)

#### 🔹 Operating System Interface
```python
import os

# Current directory
current_dir = os.getcwd()
print(f"Current directory: {current_dir}")

# List directory contents
files = os.listdir('.')
print(f"Files: {files}")

# Create directory
os.makedirs('new_directory', exist_ok=True)

# Environment variables
python_path = os.environ.get('PYTHONPATH', 'Not set')

# Path operations
file_path = os.path.join('folder', 'subfolder', 'file.txt')
directory, filename = os.path.split(file_path)
name, extension = os.path.splitext(filename)
```

#### 🔹 System-specific Parameters
```python
import sys

# Python version
print(f"Python version: {sys.version}")

# Module search path
print(f"Module paths: {sys.path}")

# Command line arguments
print(f"Arguments: {sys.argv}")

# Exit program
# sys.exit(0)  # Uncomment to exit
```

#### 🔹 Date and Time
```python
import datetime

# Current date and time
now = datetime.datetime.now()
print(f"Current time: {now}")

# Specific date
birthday = datetime.date(1995, 5, 15)
print(f"Birthday: {birthday}")

# Time operations
tomorrow = now + datetime.timedelta(days=1)
print(f"Tomorrow: {tomorrow}")

# Formatting
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted: {formatted}")
```

#### 🔹 Mathematical Operations
```python
import math
import random

# Math functions
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Ceiling of 4.3: {math.ceil(4.3)}")
print(f"Floor of 4.7: {math.floor(4.7)}")
print(f"Sin of π/2: {math.sin(math.pi/2)}")

# Random numbers
print(f"Random float: {random.random()}")
print(f"Random integer: {random.randint(1, 10)}")
print(f"Random choice: {random.choice(['A', 'B', 'C'])}")

# Shuffle list
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(f"Shuffled: {numbers}")
```

#### 🔹 Regular Expressions
```python
import re

# Pattern matching
text = "Contact us at support@example.com or sales@company.org"
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
emails = re.findall(email_pattern, text)
print(f"Found emails: {emails}")

# Search and replace
cleaned_text = re.sub(r'\s+', ' ', "  Multiple   spaces  ")
print(f"Cleaned: '{cleaned_text}'")
```

### 📦 Package Creation

#### 🔹 Creating a Package Structure
```python
# package/__init__.py
"""
Mathematics package for basic operations.
"""

__version__ = "1.0.0"
__author__ = "Your Name"

# Import main functions to package level
from .maths import add, subtract, multiply, divide

__all__ = ['add', 'subtract', 'multiply', 'divide']
```

```python
# package/maths.py
"""
Basic mathematical operations.
"""

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(base, exponent):
    """Calculate base raised to exponent."""
    return base ** exponent
```

```python
# package/subpackages/__init__.py
"""
Subpackage for advanced operations.
"""

from .mult import advanced_multiply

__all__ = ['advanced_multiply']
```

```python
# package/subpackages/mult.py
"""
Advanced multiplication operations.
"""

def advanced_multiply(*args):
    """Multiply multiple numbers."""
    result = 1
    for num in args:
        result *= num
    return result

def matrix_multiply(matrix1, matrix2):
    """Simple matrix multiplication."""
    # Simplified implementation
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Invalid matrix dimensions")
    
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            sum_val = 0
            for k in range(len(matrix2)):
                sum_val += matrix1[i][k] * matrix2[k][j]
            row.append(sum_val)
        result.append(row)
    return result
```

## 💻 Practice Exercises

### Exercise 1: File Utilities Module
```python
# file_utils.py
import os
import shutil
from datetime import datetime

def copy_file(source, destination):
    """Copy file from source to destination."""
    try:
        shutil.copy2(source, destination)
        return True
    except FileNotFoundError:
        print(f"Source file {source} not found")
        return False

def get_file_info(filepath):
    """Get file information."""
    if not os.path.exists(filepath):
        return None
    
    stat = os.stat(filepath)
    return {
        'size': stat.st_size,
        'modified': datetime.fromtimestamp(stat.st_mtime),
        'is_file': os.path.isfile(filepath),
        'is_directory': os.path.isdir(filepath)
    }

def create_backup(filepath):
    """Create backup of file with timestamp."""
    if not os.path.exists(filepath):
        return False
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"{filepath}.backup_{timestamp}"
    return copy_file(filepath, backup_name)
```

### Exercise 2: Data Processing Package
```python
# data_processor/__init__.py
"""
Data processing package for common operations.
"""

from .cleaner import clean_data, remove_duplicates
from .analyzer import analyze_data, get_statistics
from .exporter import export_csv, export_json

__version__ = "1.0.0"
__all__ = [
    'clean_data', 'remove_duplicates',
    'analyze_data', 'get_statistics',
    'export_csv', 'export_json'
]
```

```python
# data_processor/cleaner.py
def clean_data(data):
    """Clean data by removing None values and empty strings."""
    return [item for item in data if item is not None and item != '']

def remove_duplicates(data):
    """Remove duplicate items while preserving order."""
    seen = set()
    result = []
    for item in data:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def normalize_strings(data):
    """Normalize strings to lowercase and strip whitespace."""
    return [item.lower().strip() if isinstance(item, str) else item for item in data]
```

### Exercise 3: Configuration Module
```python
# config.py
import os
import json

class Config:
    """Configuration management class."""
    
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.settings = self.load_config()
    
    def load_config(self):
        """Load configuration from file."""
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                return json.load(f)
        return self.get_default_config()
    
    def get_default_config(self):
        """Return default configuration."""
        return {
            'database_url': 'sqlite:///app.db',
            'debug': True,
            'log_level': 'INFO',
            'max_connections': 100
        }
    
    def get(self, key, default=None):
        """Get configuration value."""
        return self.settings.get(key, default)
    
    def set(self, key, value):
        """Set configuration value."""
        self.settings[key] = value
    
    def save_config(self):
        """Save configuration to file."""
        with open(self.config_file, 'w') as f:
            json.dump(self.settings, f, indent=2)

# Usage
config = Config()
db_url = config.get('database_url')
config.set('api_key', 'your-api-key')
config.save_config()
```

## 🧪 Hands-On Activities

1. **Build a utility package**: Create a package with common utility functions
2. **Explore standard library**: Try different modules like `collections`, `itertools`
3. **Create a project structure**: Organize a larger project with multiple modules
4. **Version your package**: Add proper versioning and metadata

## 🔍 Key Concepts to Remember

### Module System Concepts
- **Module**: A single Python file containing code
- **Package**: A directory containing multiple modules and an `__init__.py` file
- **Namespace**: The scope where names are stored and accessed
- **Import Path**: How Python finds modules to import

### Best Practices
- **`__init__.py`**: Always include this file in packages (can be empty)
- **`__all__`**: Define what gets imported with `from module import *`
- **Relative vs Absolute Imports**: Use absolute imports for clarity
- **Circular Imports**: Avoid modules importing each other

## 🌟 Advanced Concepts

### Dynamic Imports
```python
import importlib

def load_plugin(plugin_name):
    """Dynamically load a plugin module."""
    try:
        plugin_module = importlib.import_module(f'plugins.{plugin_name}')
        return plugin_module
    except ImportError:
        print(f"Plugin {plugin_name} not found")
        return None

# Reload a module (useful in development)
importlib.reload(module_name)
```

### Module Search Path
```python
import sys

# Add custom path to module search
sys.path.insert(0, '/path/to/custom/modules')

# Check where Python looks for modules
for path in sys.path:
    print(path)
```

### Package Resources
```python
import pkg_resources

# Get package version
version = pkg_resources.get_distribution('numpy').version

# Access package data files
data_file = pkg_resources.resource_filename('mypackage', 'data/config.json')
```

## 🔗 Integration with Other Modules

Modules and packages are essential for:
- **Organizing complex applications**
- **Sharing code between projects**
- **Using third-party libraries**
- **Building distributable packages**

## 📝 Assignment Checklist

- [ ] Import modules using different methods
- [ ] Explore Python standard library modules
- [ ] Create custom modules with functions
- [ ] Build a package with `__init__.py`
- [ ] Use subpackages and nested imports
- [ ] Handle file operations with `os` module
- [ ] Work with dates using `datetime`
- [ ] Create reusable utility modules
- [ ] Complete all assignment exercises

## 🆘 Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError` | Check module name spelling and Python path |
| Circular imports | Restructure code or use late imports |
| `__init__.py` missing | Create empty `__init__.py` file in package directory |
| Import conflicts | Use specific imports or aliases |
| Package not found | Ensure package is in Python path |

## 🏆 Challenge Projects

1. **Personal Utility Library**: Create a package with your most-used functions
2. **Data Processing Pipeline**: Build modular data processing components
3. **Plugin System**: Create an extensible application with plugins
4. **API Client Library**: Build a reusable API client package
5. **Configuration Management**: Create a flexible configuration system

---

**Modules Make Code Organized! 📚**

*Master modules and packages to build scalable, maintainable Python applications!* 