# ⚠️ Module 7: Exception Handling

![Python](https://img.shields.io/badge/Python-Exception%20Handling-red?style=for-the-badge&logo=python&logoColor=white)
![Difficulty](https://img.shields.io/badge/Difficulty-Intermediate-orange?style=for-the-badge)

## 📖 Overview

This module teaches you how to handle errors gracefully in Python programs. Learn to anticipate, catch, and handle exceptions to build robust and reliable applications.

## 🎯 Learning Objectives

By the end of this module, you will:
- ✅ Understand different types of exceptions in Python
- ✅ Use try-except blocks for error handling
- ✅ Create custom exceptions for specific use cases
- ✅ Implement proper exception handling strategies
- ✅ Debug and troubleshoot Python programs
- ✅ Write resilient code that handles edge cases

## 📂 Module Contents

| File | Description | Key Concepts |
|------|-------------|--------------|
| `7.1-exception.ipynb` | Exception fundamentals | try, except, finally, else |
| `7.2-customexception.ipynb` | Custom exceptions | Creating and raising custom errors |
| `exceptionhandlingquestions.ipynb` | Practice exercises | Error handling challenges |
| `exceptionhandlingsolution.ipynb` | Exercise solutions | Reference implementations |
| `example1.txt` | Sample file | File handling with exceptions |

## 🚀 Quick Start

### Prerequisites
- Completion of Module 6 (File Handling)
- Understanding of Python functions and control flow

### Running the Notebooks

```bash
# Navigate to this directory
cd "7-Exception Handling"

# Start Jupyter Lab
jupyter lab

# Or start Jupyter Notebook
jupyter notebook
```

## 📚 Detailed Content Guide

### 🛡️ Exception Basics (`7.1-exception.ipynb`)

#### 🔹 Basic Try-Except Structure
```python
# Basic exception handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
    result = 0

# Multiple exception types
try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

#### 🔹 Complete Exception Handling
```python
try:
    # Code that might raise exceptions
    file_content = open('data.txt', 'r').read()
    number = int(file_content)
    result = 100 / number
except FileNotFoundError:
    print("File not found!")
    result = None
except ValueError:
    print("File content is not a valid number!")
    result = None
except ZeroDivisionError:
    print("Number cannot be zero!")
    result = None
except Exception as e:
    print(f"Unexpected error: {e}")
    result = None
else:
    print("Operation completed successfully!")
finally:
    print("Cleanup operations")
```

#### 🔹 Exception Information
```python
import traceback

try:
    risky_operation()
except Exception as e:
    print(f"Error type: {type(e).__name__}")
    print(f"Error message: {str(e)}")
    print(f"Error arguments: {e.args}")
    
    # Full traceback
    traceback.print_exc()
```

### 🏗️ Custom Exceptions (`7.2-customexception.ipynb`)

#### 🔹 Creating Custom Exception Classes
```python
class CustomError(Exception):
    """Base class for custom exceptions."""
    pass

class ValidationError(CustomError):
    """Raised when validation fails."""
    def __init__(self, message, field_name=None):
        super().__init__(message)
        self.field_name = field_name

class DatabaseError(CustomError):
    """Raised when database operations fail."""
    def __init__(self, message, error_code=None):
        super().__init__(message)
        self.error_code = error_code

# Usage
def validate_age(age):
    if not isinstance(age, int):
        raise ValidationError("Age must be an integer", "age")
    if age < 0 or age > 150:
        raise ValidationError("Age must be between 0 and 150", "age")

try:
    validate_age(-5)
except ValidationError as e:
    print(f"Validation error in field '{e.field_name}': {e}")
```

#### 🔹 Exception Hierarchy
```python
class AppError(Exception):
    """Base application exception."""
    pass

class UserError(AppError):
    """User-related errors."""
    pass

class SystemError(AppError):
    """System-related errors."""
    pass

class InvalidCredentialsError(UserError):
    """Invalid user credentials."""
    pass

class DatabaseConnectionError(SystemError):
    """Database connection failed."""
    pass
```

## 💻 Practice Exercises

### Exercise 1: Safe Calculator
```python
class CalculatorError(Exception):
    """Base calculator exception."""
    pass

class InvalidOperationError(CalculatorError):
    """Invalid mathematical operation."""
    pass

class SafeCalculator:
    """Calculator with comprehensive error handling."""
    
    def add(self, a, b):
        try:
            return float(a) + float(b)
        except (ValueError, TypeError):
            raise InvalidOperationError("Invalid numbers for addition")
    
    def divide(self, a, b):
        try:
            a, b = float(a), float(b)
            if b == 0:
                raise InvalidOperationError("Division by zero")
            return a / b
        except (ValueError, TypeError):
            raise InvalidOperationError("Invalid numbers for division")
    
    def sqrt(self, a):
        try:
            import math
            a = float(a)
            if a < 0:
                raise InvalidOperationError("Cannot calculate square root of negative number")
            return math.sqrt(a)
        except (ValueError, TypeError):
            raise InvalidOperationError("Invalid number for square root")

# Usage
calc = SafeCalculator()
try:
    result = calc.divide(10, 0)
except InvalidOperationError as e:
    print(f"Calculator error: {e}")
```

### Exercise 2: File Processor with Error Handling
```python
import os
import json

class FileProcessorError(Exception):
    """Base file processor exception."""
    pass

class FileProcessor:
    """Process files with comprehensive error handling."""
    
    def read_json_file(self, filepath):
        """Read and parse JSON file."""
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileProcessorError(f"File not found: {filepath}")
        except json.JSONDecodeError as e:
            raise FileProcessorError(f"Invalid JSON in {filepath}: {e}")
        except PermissionError:
            raise FileProcessorError(f"Permission denied: {filepath}")
        except Exception as e:
            raise FileProcessorError(f"Unexpected error reading {filepath}: {e}")
    
    def write_json_file(self, filepath, data):
        """Write data to JSON file."""
        try:
            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            
            with open(filepath, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)
            return True
        except PermissionError:
            raise FileProcessorError(f"Permission denied writing to: {filepath}")
        except Exception as e:
            raise FileProcessorError(f"Error writing to {filepath}: {e}")
    
    def process_multiple_files(self, filepaths):
        """Process multiple files with error collection."""
        results = []
        errors = []
        
        for filepath in filepaths:
            try:
                data = self.read_json_file(filepath)
                results.append({"file": filepath, "data": data, "status": "success"})
            except FileProcessorError as e:
                errors.append({"file": filepath, "error": str(e), "status": "failed"})
        
        return {"results": results, "errors": errors}
```

### Exercise 3: Network Request Handler
```python
import time
import random

class NetworkError(Exception):
    """Base network exception."""
    pass

class TimeoutError(NetworkError):
    """Request timeout error."""
    pass

class ConnectionError(NetworkError):
    """Connection failed error."""
    pass

class RetryableError(NetworkError):
    """Error that can be retried."""
    pass

def make_request(url, timeout=5, retries=3):
    """Make network request with retry logic."""
    
    def simulate_request():
        """Simulate network request."""
        # Simulate various failure scenarios
        failure_chance = random.random()
        
        if failure_chance < 0.2:  # 20% chance of timeout
            raise TimeoutError(f"Request to {url} timed out")
        elif failure_chance < 0.3:  # 10% chance of connection error
            raise ConnectionError(f"Failed to connect to {url}")
        elif failure_chance < 0.4:  # 10% chance of retryable error
            raise RetryableError(f"Temporary error accessing {url}")
        else:
            return {"status": "success", "data": f"Response from {url}"}
    
    last_exception = None
    
    for attempt in range(retries + 1):
        try:
            return simulate_request()
        except (TimeoutError, RetryableError) as e:
            last_exception = e
            if attempt < retries:
                wait_time = 2 ** attempt  # Exponential backoff
                print(f"Attempt {attempt + 1} failed: {e}. Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                print(f"All {retries + 1} attempts failed.")
        except ConnectionError as e:
            # Don't retry connection errors
            raise e
    
    # If we get here, all retries failed
    raise last_exception

# Usage
try:
    response = make_request("https://api.example.com/data")
    print(f"Success: {response}")
except NetworkError as e:
    print(f"Network error: {e}")
```

## 🧪 Hands-On Activities

1. **Input validator**: Create robust input validation with custom exceptions
2. **API client**: Build an API client with comprehensive error handling
3. **Data processor**: Process data files with graceful error recovery
4. **Web scraper**: Handle various web scraping errors

## 🔍 Key Exception Types

### Built-in Exceptions
```python
# Common Python exceptions
exceptions_guide = {
    'ValueError': 'Invalid value for operation',
    'TypeError': 'Invalid type for operation',
    'KeyError': 'Key not found in dictionary',
    'IndexError': 'Index out of range',
    'FileNotFoundError': 'File does not exist',
    'PermissionError': 'Insufficient permissions',
    'ZeroDivisionError': 'Division by zero',
    'AttributeError': 'Attribute does not exist',
    'ImportError': 'Module import failed',
    'NameError': 'Name not defined'
}
```

### Exception Handling Patterns
```python
# Pattern 1: Specific exception handling
try:
    risky_operation()
except SpecificError:
    handle_specific_error()
except AnotherError:
    handle_another_error()

# Pattern 2: Exception chaining
try:
    low_level_operation()
except LowLevelError as e:
    raise HighLevelError("High level operation failed") from e

# Pattern 3: Context managers for cleanup
class ResourceManager:
    def __enter__(self):
        self.resource = acquire_resource()
        return self.resource
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        release_resource(self.resource)
        return False  # Don't suppress exceptions
```

## 🌟 Best Practices

1. **Be specific**: Catch specific exceptions, not generic `Exception`
2. **Fail fast**: Handle errors early and clearly
3. **Log errors**: Use logging for error tracking
4. **Clean up**: Use `finally` or context managers for cleanup
5. **Don't ignore**: Never use bare `except:` clauses
6. **Chain exceptions**: Use `raise ... from` for exception chaining

## 📝 Assignment Checklist

- [ ] Use try-except blocks effectively
- [ ] Handle multiple exception types
- [ ] Create custom exception classes
- [ ] Implement exception hierarchies
- [ ] Use finally for cleanup operations
- [ ] Chain exceptions appropriately
- [ ] Debug using exception information
- [ ] Complete all assignment exercises

## 🆘 Common Mistakes & Solutions

| Mistake | Solution |
|---------|----------|
| Catching all exceptions with `except:` | Be specific about exception types |
| Ignoring exceptions silently | Log errors and handle appropriately |
| Not cleaning up resources | Use `finally` or context managers |
| Poor error messages | Provide clear, actionable error messages |
| Exception chains breaking | Use `raise ... from` for chaining |

## 🏆 Challenge Projects

1. **Robust File Processor**: Handle all possible file operation errors
2. **API Rate Limiter**: Handle rate limiting with exponential backoff
3. **Data Validator**: Comprehensive data validation with custom exceptions
4. **Fault-Tolerant Web Crawler**: Handle various web scraping errors
5. **Database Connection Pool**: Manage database connections with error recovery

---

**Handle Errors Gracefully! 🛡️**

*Master exception handling to build robust, production-ready applications!* 