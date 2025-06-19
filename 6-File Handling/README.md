# 📁 Module 6: File Handling

![Python](https://img.shields.io/badge/Python-File%20Handling-cyan?style=for-the-badge&logo=python&logoColor=white)
![Difficulty](https://img.shields.io/badge/Difficulty-Intermediate-orange?style=for-the-badge)

## 📖 Overview

This module teaches you how to work with files and directories in Python. Learn to read, write, and manipulate files, handle different file formats, and manage file paths effectively.

## 🎯 Learning Objectives

By the end of this module, you will:
- ✅ Read and write files using different modes
- ✅ Handle file paths and directories
- ✅ Work with different file formats (text, binary, CSV, JSON)
- ✅ Implement error handling for file operations
- ✅ Use context managers for safe file handling
- ✅ Process large files efficiently

## 📂 Module Contents

| File | Description | Key Concepts |
|------|-------------|--------------|
| `6.1-fileoperation.ipynb` | Basic file operations | Reading, writing, file modes |
| `6.2-filepath.ipynb` | File path manipulation | os.path, pathlib, directory operations |
| `filehandlingquestions.ipynb` | Practice exercises | Hands-on file handling challenges |
| `filehandlingsolution.ipynb` | Exercise solutions | Reference implementations |
| `example.txt` | Sample text file | Reading and writing examples |
| `example.bin` | Binary file example | Binary file operations |
| `destination.txt` | Output file example | File copying and writing |

## 🚀 Quick Start

### Prerequisites
- Completion of Module 5 (Modules)
- Understanding of Python basics and error handling

### Running the Notebooks

```bash
# Navigate to this directory
cd "6-File Handling"

# Start Jupyter Lab
jupyter lab

# Or start Jupyter Notebook
jupyter notebook
```

## 📚 Detailed Content Guide

### 📄 Basic File Operations (`6.1-fileoperation.ipynb`)

#### 🔹 Reading Files
```python
# Basic file reading
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Reading line by line
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())

# Reading all lines into a list
with open('example.txt', 'r') as file:
    lines = file.readlines()
```

#### 🔹 Writing Files
```python
# Writing text to file
with open('output.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("Python File Handling")

# Appending to file
with open('output.txt', 'a') as file:
    file.write("\nAppended line")

# Writing multiple lines
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open('output.txt', 'w') as file:
    file.writelines(lines)
```

#### 🔹 File Modes
```python
# Common file modes
modes = {
    'r': 'Read only (default)',
    'w': 'Write (overwrites existing)',
    'a': 'Append',
    'x': 'Exclusive creation',
    'r+': 'Read and write',
    'rb': 'Read binary',
    'wb': 'Write binary'
}

# Binary file handling
with open('image.jpg', 'rb') as file:
    binary_data = file.read()

with open('copy.jpg', 'wb') as file:
    file.write(binary_data)
```

### 🛤️ File Paths (`6.2-filepath.ipynb`)

#### 🔹 Path Operations with os.path
```python
import os

# Current directory
current_dir = os.getcwd()
print(f"Current directory: {current_dir}")

# Join paths
file_path = os.path.join('folder', 'subfolder', 'file.txt')
print(f"Joined path: {file_path}")

# Split paths
directory, filename = os.path.split(file_path)
name, extension = os.path.splitext(filename)

# Check path properties
exists = os.path.exists('example.txt')
is_file = os.path.isfile('example.txt')
is_directory = os.path.isdir('folder')
```

#### 🔹 Modern Path Handling with pathlib
```python
from pathlib import Path

# Create path objects
file_path = Path('folder') / 'file.txt'
absolute_path = file_path.absolute()

# Path properties
print(f"Name: {file_path.name}")
print(f"Suffix: {file_path.suffix}")
print(f"Parent: {file_path.parent}")

# Check existence
if file_path.exists():
    print("File exists")

# Create directories
new_dir = Path('new_folder')
new_dir.mkdir(exist_ok=True)
```

#### 🔹 Directory Operations
```python
import os
import shutil

# List directory contents
files = os.listdir('.')
print(f"Files in current directory: {files}")

# Create directories
os.makedirs('nested/folders', exist_ok=True)

# Copy files
shutil.copy('source.txt', 'destination.txt')
shutil.copytree('source_folder', 'destination_folder')

# Remove files and directories
os.remove('file.txt')  # Remove file
os.rmdir('empty_folder')  # Remove empty directory
shutil.rmtree('folder_with_content')  # Remove directory and contents
```

## 💻 Practice Exercises

### Exercise 1: File Statistics
```python
import os
from pathlib import Path

def get_file_stats(filepath):
    """Get comprehensive file statistics."""
    path = Path(filepath)
    
    if not path.exists():
        return None
    
    stat = path.stat()
    return {
        'name': path.name,
        'size': stat.st_size,
        'modified': stat.st_mtime,
        'is_file': path.is_file(),
        'is_directory': path.is_dir(),
        'extension': path.suffix
    }

def analyze_directory(directory):
    """Analyze all files in a directory."""
    path = Path(directory)
    results = []
    
    for item in path.iterdir():
        stats = get_file_stats(item)
        if stats:
            results.append(stats)
    
    return results
```

### Exercise 2: Text File Processor
```python
def count_words(filepath):
    """Count words in a text file."""
    try:
        with open(filepath, 'r') as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        return 0

def find_and_replace(filepath, old_text, new_text):
    """Find and replace text in a file."""
    try:
        # Read file
        with open(filepath, 'r') as file:
            content = file.read()
        
        # Replace text
        modified_content = content.replace(old_text, new_text)
        
        # Write back
        with open(filepath, 'w') as file:
            file.write(modified_content)
        
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def merge_files(file_list, output_file):
    """Merge multiple files into one."""
    with open(output_file, 'w') as outfile:
        for filepath in file_list:
            try:
                with open(filepath, 'r') as infile:
                    outfile.write(infile.read())
                    outfile.write('\n---\n')  # Separator
            except FileNotFoundError:
                print(f"Warning: {filepath} not found")
```

### Exercise 3: CSV and JSON Handling
```python
import csv
import json

def read_csv_data(filepath):
    """Read CSV file and return data as list of dictionaries."""
    data = []
    try:
        with open(filepath, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"File {filepath} not found")
    return data

def write_csv_data(filepath, data, fieldnames):
    """Write data to CSV file."""
    try:
        with open(filepath, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        return True
    except Exception as e:
        print(f"Error writing CSV: {e}")
        return False

def save_json(data, filepath):
    """Save data to JSON file."""
    try:
        with open(filepath, 'w') as jsonfile:
            json.dump(data, jsonfile, indent=2)
        return True
    except Exception as e:
        print(f"Error saving JSON: {e}")
        return False

def load_json(filepath):
    """Load data from JSON file."""
    try:
        with open(filepath, 'r') as jsonfile:
            return json.load(jsonfile)
    except FileNotFoundError:
        print(f"File {filepath} not found")
        return None
    except json.JSONDecodeError:
        print(f"Invalid JSON in {filepath}")
        return None
```

## 🧪 Hands-On Activities

1. **File organizer**: Create a script to organize files by extension
2. **Log analyzer**: Process log files and extract information
3. **Backup utility**: Create automated backup scripts
4. **Data converter**: Convert between different file formats

## 🔍 Key Concepts to Remember

### File Handling Best Practices
- **Always use context managers**: `with open() as file:`
- **Handle exceptions**: Use try-except for file operations
- **Close files properly**: Context managers handle this automatically
- **Use appropriate encoding**: Specify encoding for text files

### Common File Operations
- **Reading**: `read()`, `readline()`, `readlines()`
- **Writing**: `write()`, `writelines()`
- **Position**: `seek()`, `tell()`
- **Modes**: 'r', 'w', 'a', 'x', 'b', '+'

## 🌟 Best Practices

1. **Use pathlib for modern path handling**
2. **Always specify encoding for text files**
3. **Handle large files with streaming**
4. **Validate file existence before operations**
5. **Use appropriate file modes**
6. **Implement proper error handling**

## 📝 Assignment Checklist

- [ ] Read and write text files
- [ ] Handle binary files
- [ ] Use context managers properly
- [ ] Manipulate file paths
- [ ] Work with CSV and JSON files
- [ ] Implement error handling
- [ ] Process directories and file listings
- [ ] Complete all assignment exercises

## 🆘 Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| `FileNotFoundError` | Check file path and existence |
| `PermissionError` | Check file permissions and access rights |
| `UnicodeDecodeError` | Specify correct encoding parameter |
| Files not closing | Use context managers (`with` statement) |
| Path separator issues | Use `os.path.join()` or `pathlib` |

## 🏆 Challenge Projects

1. **File Synchronizer**: Sync files between directories
2. **Log File Analyzer**: Parse and analyze log files
3. **Duplicate File Finder**: Find and remove duplicate files
4. **File Encryption Tool**: Encrypt and decrypt files
5. **Data Pipeline**: Process and transform file data

---

**Files Are Your Data Gateway! 🚪**

*Master file handling to work with data efficiently and safely!* 