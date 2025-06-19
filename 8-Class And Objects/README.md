# 🏗️ Module 8: Classes and Objects (OOP)

![Python](https://img.shields.io/badge/Python-Object%20Oriented%20Programming-darkblue?style=for-the-badge&logo=python&logoColor=white)
![Difficulty](https://img.shields.io/badge/Difficulty-Intermediate%20to%20Advanced-red?style=for-the-badge)

## 📖 Overview

This module introduces Object-Oriented Programming (OOP) in Python. Learn to design and build applications using classes, objects, and the four pillars of OOP: Encapsulation, Inheritance, Polymorphism, and Abstraction.

## 🎯 Learning Objectives

By the end of this module, you will:
- ✅ Create classes and instantiate objects
- ✅ Understand inheritance and method overriding
- ✅ Implement polymorphism in your designs
- ✅ Apply encapsulation for data protection
- ✅ Use abstraction for clean interfaces
- ✅ Master magic methods and operator overloading
- ✅ Handle custom exceptions in OOP context

## 📂 Module Contents

| File | Description | Key Concepts |
|------|-------------|--------------|
| `8.1-oops.ipynb` | OOP fundamentals | Classes, objects, methods, attributes |
| `8.2-inheritance.ipynb` | Inheritance concepts | Single, multiple, method resolution |
| `8.3-Polymorphism.ipynb` | Polymorphism examples | Method overriding, duck typing |
| `8.4-Encapsulation.ipynb` | Data encapsulation | Private/protected attributes, properties |
| `8.5-Abstraction.ipynb` | Abstract classes | ABC module, abstract methods |
| `8.6-magicmethods.ipynb` | Magic methods | `__init__`, `__str__`, `__len__`, etc. |
| `8.7-OperatorOverloading.ipynb` | Operator overloading | Custom operators for classes |
| `8.8-customexception.ipynb` | Custom exceptions in OOP | Exception hierarchies |
| `oopsquestion.ipynb` | Basic OOP exercises | Class design challenges |
| `oopssolution.ipynb` | Basic OOP solutions | Reference implementations |
| `inhertiancequestions.ipynb` | Inheritance exercises | Inheritance design problems |
| `inheritancesolutions.ipynb` | Inheritance solutions | Reference implementations |
| `classesobjectquestions.ipynb` | Advanced OOP exercises | Complex class interactions |
| `classesobjectssolution.ipynb` | Advanced OOP solutions | Reference implementations |

## 🚀 Quick Start

### Prerequisites
- Completion of Module 7 (Exception Handling)
- Strong understanding of functions and modules

### Running the Notebooks

```bash
# Navigate to this directory
cd "8-Class And Objects"

# Start Jupyter Lab
jupyter lab

# Or start Jupyter Notebook
jupyter notebook
```

## 📚 Detailed Content Guide

### 🏗️ OOP Fundamentals (`8.1-oops.ipynb`)

#### 🔹 Basic Class Definition
```python
class Student:
    """A class representing a student."""
    
    # Class variable (shared by all instances)
    school_name = "Python Academy"
    
    def __init__(self, name, age, student_id):
        """Initialize a new student."""
        self.name = name          # Instance variable
        self.age = age           # Instance variable
        self.student_id = student_id
        self.grades = []
    
    def add_grade(self, grade):
        """Add a grade to the student."""
        if 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            raise ValueError("Grade must be between 0 and 100")
    
    def get_average(self):
        """Calculate average grade."""
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def __str__(self):
        """String representation of student."""
        return f"Student({self.name}, {self.age}, ID: {self.student_id})"

# Usage
student1 = Student("Alice", 20, "S001")
student1.add_grade(85)
student1.add_grade(92)
print(f"Average: {student1.get_average()}")
```

### 🧬 Inheritance (`8.2-inheritance.ipynb`)

#### 🔹 Single Inheritance
```python
class Person:
    """Base class for all persons."""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

class Student(Person):
    """Student class inheriting from Person."""
    
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Call parent constructor
        self.student_id = student_id
        self.courses = []
    
    def enroll(self, course):
        self.courses.append(course)
    
    def introduce(self):  # Method overriding
        return f"{super().introduce()} I'm a student with ID {self.student_id}."

class Teacher(Person):
    """Teacher class inheriting from Person."""
    
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
        self.students = []
    
    def teach(self, student):
        self.students.append(student)
        return f"{self.name} is now teaching {student.name}"
```

#### 🔹 Multiple Inheritance
```python
class Flyable:
    """Mixin for flying capability."""
    
    def fly(self):
        return f"{self.__class__.__name__} is flying!"

class Swimmable:
    """Mixin for swimming capability."""
    
    def swim(self):
        return f"{self.__class__.__name__} is swimming!"

class Animal:
    """Base animal class."""
    
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        pass

class Duck(Animal, Flyable, Swimmable):
    """Duck can fly and swim."""
    
    def make_sound(self):
        return "Quack!"

# Usage
duck = Duck("Donald")
print(duck.make_sound())
print(duck.fly())
print(duck.swim())
```

### 🎭 Polymorphism (`8.3-Polymorphism.ipynb`)

#### 🔹 Method Overriding and Duck Typing
```python
class Shape:
    """Base shape class."""
    
    def area(self):
        raise NotImplementedError("Subclass must implement area method")
    
    def perimeter(self):
        raise NotImplementedError("Subclass must implement perimeter method")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

# Polymorphic function
def print_shape_info(shape):
    """Print information about any shape."""
    print(f"Area: {shape.area():.2f}")
    print(f"Perimeter: {shape.perimeter():.2f}")

# Usage
shapes = [Rectangle(5, 3), Circle(4)]
for shape in shapes:
    print_shape_info(shape)
```

### 🔒 Encapsulation (`8.4-Encapsulation.ipynb`)

#### 🔹 Private and Protected Attributes
```python
class BankAccount:
    """Bank account with encapsulated balance."""
    
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.__balance = initial_balance  # Private attribute
        self._transaction_history = []    # Protected attribute
    
    @property
    def balance(self):
        """Get current balance (read-only)."""
        return self.__balance
    
    def deposit(self, amount):
        """Deposit money to account."""
        if amount > 0:
            self.__balance += amount
            self._record_transaction(f"Deposit: +${amount}")
            return True
        return False
    
    def withdraw(self, amount):
        """Withdraw money from account."""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self._record_transaction(f"Withdrawal: -${amount}")
            return True
        return False
    
    def _record_transaction(self, transaction):
        """Protected method for recording transactions."""
        import datetime
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._transaction_history.append(f"{timestamp}: {transaction}")
    
    def get_statement(self):
        """Get account statement."""
        return self._transaction_history.copy()

# Usage
account = BankAccount("ACC001", 1000)
account.deposit(500)
account.withdraw(200)
print(f"Balance: ${account.balance}")
# print(account.__balance)  # This would raise AttributeError
```

### 🎯 Abstraction (`8.5-Abstraction.ipynb`)

#### 🔹 Abstract Base Classes
```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    """Abstract vehicle class."""
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    @abstractmethod
    def start_engine(self):
        """Start the vehicle engine."""
        pass
    
    @abstractmethod
    def stop_engine(self):
        """Stop the vehicle engine."""
        pass
    
    def get_info(self):
        """Get vehicle information."""
        return f"{self.brand} {self.model}"

class Car(Vehicle):
    """Concrete car implementation."""
    
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type
        self.engine_running = False
    
    def start_engine(self):
        if not self.engine_running:
            self.engine_running = True
            return f"{self.get_info()} engine started."
        return f"{self.get_info()} engine already running."
    
    def stop_engine(self):
        if self.engine_running:
            self.engine_running = False
            return f"{self.get_info()} engine stopped."
        return f"{self.get_info()} engine already stopped."

class ElectricCar(Vehicle):
    """Electric car implementation."""
    
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity
        self.system_on = False
    
    def start_engine(self):
        if not self.system_on:
            self.system_on = True
            return f"{self.get_info()} electric system activated."
        return f"{self.get_info()} system already on."
    
    def stop_engine(self):
        if self.system_on:
            self.system_on = False
            return f"{self.get_info()} electric system deactivated."
        return f"{self.get_info()} system already off."
```

### ✨ Magic Methods (`8.6-magicmethods.ipynb`)

#### 🔹 Common Magic Methods
```python
class Vector:
    """2D vector with magic methods."""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        """String representation."""
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        """Developer representation."""
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, other):
        """Vector addition."""
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented
    
    def __sub__(self, other):
        """Vector subtraction."""
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented
    
    def __mul__(self, scalar):
        """Scalar multiplication."""
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        return NotImplemented
    
    def __eq__(self, other):
        """Equality comparison."""
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False
    
    def __len__(self):
        """Vector magnitude."""
        return int((self.x ** 2 + self.y ** 2) ** 0.5)
    
    def __getitem__(self, index):
        """Index access."""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Vector index out of range")

# Usage
v1 = Vector(3, 4)
v2 = Vector(1, 2)
v3 = v1 + v2
print(f"v1 + v2 = {v3}")
print(f"Length of v1: {len(v1)}")
print(f"v1[0] = {v1[0]}")
```

## 💻 Practice Exercises

### Exercise 1: Library Management System
```python
from datetime import datetime, timedelta

class Book:
    def __init__(self, isbn, title, author, copies=1):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.total_copies = copies
        self.available_copies = copies
    
    def __str__(self):
        return f"{self.title} by {self.author}"

class Member:
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = []
    
    def can_borrow(self):
        return len(self.borrowed_books) < 3  # Max 3 books

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}
        self.borrowed_records = []
    
    def add_book(self, book):
        self.books[book.isbn] = book
    
    def register_member(self, member):
        self.members[member.member_id] = member
    
    def borrow_book(self, member_id, isbn):
        if member_id not in self.members:
            return "Member not found"
        if isbn not in self.books:
            return "Book not found"
        
        member = self.members[member_id]
        book = self.books[isbn]
        
        if not member.can_borrow():
            return "Member has reached borrowing limit"
        if book.available_copies <= 0:
            return "Book not available"
        
        book.available_copies -= 1
        member.borrowed_books.append(isbn)
        due_date = datetime.now() + timedelta(days=14)
        
        self.borrowed_records.append({
            'member_id': member_id,
            'isbn': isbn,
            'borrow_date': datetime.now(),
            'due_date': due_date,
            'returned': False
        })
        
        return f"Book borrowed successfully. Due date: {due_date.date()}"
```

## 🧪 Hands-On Activities

1. **Design a game character system**: Use inheritance for different character types
2. **Create a banking system**: Implement accounts with encapsulation
3. **Build a shapes drawing program**: Use polymorphism for different shapes
4. **Design an employee management system**: Abstract base class with concrete implementations

## 🔍 Key OOP Principles

### The Four Pillars of OOP

1. **Encapsulation**: Bundle data and methods, control access
2. **Inheritance**: Create new classes based on existing ones
3. **Polymorphism**: Same interface, different implementations
4. **Abstraction**: Hide complex implementation details

### Design Patterns in OOP
- **Singleton**: Ensure only one instance exists
- **Factory**: Create objects without specifying exact class
- **Observer**: Define one-to-many dependency between objects
- **Strategy**: Define family of algorithms, make them interchangeable

## 🌟 Best Practices

1. **Follow SOLID principles**: Single responsibility, Open/closed, etc.
2. **Use composition over inheritance**: Prefer "has-a" over "is-a" relationships
3. **Keep interfaces simple**: Follow the principle of least surprise
4. **Document your classes**: Use docstrings and type hints
5. **Test your classes**: Write unit tests for methods
6. **Use properties**: Control attribute access with getters/setters

## 📝 Assignment Checklist

- [ ] Create classes with proper constructors
- [ ] Implement inheritance hierarchies
- [ ] Use method overriding for polymorphism
- [ ] Apply encapsulation with private attributes
- [ ] Create abstract base classes
- [ ] Implement magic methods
- [ ] Design custom exceptions
- [ ] Complete all assignment exercises

## 🆘 Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| Circular imports | Restructure code, use forward references |
| Method resolution order confusion | Understand MRO with `Class.__mro__` |
| Excessive inheritance depth | Prefer composition, keep hierarchies shallow |
| Tight coupling between classes | Use dependency injection, interfaces |
| God objects (classes doing too much) | Apply single responsibility principle |

## 🏆 Challenge Projects

1. **E-commerce System**: Products, customers, orders with full OOP design
2. **Game Engine**: Characters, weapons, levels using inheritance
3. **Social Media Platform**: Users, posts, comments with polymorphism
4. **File System Simulator**: Files, directories using composite pattern
5. **Drawing Application**: Shapes, tools using strategy pattern

---

**Objects Bring Code to Life! 🌟**

*Master OOP to build scalable, maintainable, and elegant software systems!* 