# Module 6: File Handling

## Overview

This module teaches you how to work with files and directories in Python. Learn to read, write, and manipulate files, handle different file formats, and manage file paths effectively.

## Learning Objectives

By the end of this module, you will:
- Read and write files using different modes
- Handle file paths and directories
- Work with different file formats (text, binary, CSV, JSON)
- Implement error handling for file operations
- Use context managers for safe file handling
- Process large files efficiently

## Module Contents

| File | Description | Key Concepts |
|------|-------------|--------------|
| `6.1-fileoperation.ipynb` | Basic file operations | Reading, writing, file modes |
| `6.2-filepath.ipynb` | File path manipulation | os.path, pathlib, directory operations |
| `example.txt` | Sample text file | Reading and writing examples |
| `example.bin` | Binary file example | Binary file operations |
| `destination.txt` | Output file example | File copying and writing |

## Core Concepts

### Basic File Operations

#### Reading Files
Reading involves opening a file in read mode ('r') and extracting its content. You can read the entire content, read line by line, or read all lines into a list. Using `with open(...)` is crucial for ensuring files are properly closed.

#### Writing Files
Writing involves opening a file in write mode ('w') to create a new file or overwrite an existing one, or append mode ('a') to add content to the end of an existing file. You can write strings or lists of strings to a file.

#### File Modes
Different modes dictate how a file is opened:
- `'r'`: Read (default)
- `'w'`: Write (creates new or truncates existing)
- `'a'`: Append (creates new or appends to existing)
- `'x'`: Exclusive creation (fails if file exists)
- `'+'`: Update (read and write)
- `'b'`: Binary mode (e.g., 'rb', 'wb')
- `'t'`: Text mode (default, e.g., 'rt', 'wt')

### File Paths and Directory Management

#### Path Manipulation
Python provides modules like `os.path` and `pathlib` for handling file paths. These allow you to:
- Join path components
- Split paths into directory and filename
- Extract file extensions
- Check if a path exists, is a file, or is a directory
- Get absolute paths

#### Directory Operations
Managing directories includes:
- Listing contents of a directory
- Creating single or nested directories
- Copying files and entire directory trees
- Removing files and directories (empty or with content)

### Handling Different File Formats

#### Text Files
Text files are the most common, handled with standard read/write operations. Proper encoding (e.g., UTF-8) is important for text files.

#### Binary Files
Binary files (like images, executables) are read and written in binary mode ('b'). Content is handled as bytes rather than strings.

#### CSV Files
CSV (Comma Separated Values) files are structured text files often used for tabular data. Python's `csv` module provides tools for reading and writing CSV data, handling delimiters and quoting.

#### JSON Files
JSON (JavaScript Object Notation) is a lightweight data-interchange format. Python's `json` module allows you to serialize Python objects to JSON format and deserialize JSON data into Python objects.

### Error Handling for File Operations

File operations can encounter various errors (e.g., file not found, permission denied). Using `try-except` blocks is essential to gracefully handle these exceptions, such as `FileNotFoundError`, `PermissionError`, and `IOError`.

### Context Managers for Safe File Handling

The `with` statement, combined with `open()`, acts as a context manager. It ensures that files are automatically closed after their block is exited, even if errors occur, preventing resource leaks.

### Processing Large Files

For very large files, it's often inefficient to load the entire content into memory. Techniques like reading line by line or in chunks (streaming) are used to process data incrementally, reducing memory consumption.