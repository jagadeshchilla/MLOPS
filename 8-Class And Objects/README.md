# Module 8: Classes and Objects (OOP)

## Overview

This module introduces Object-Oriented Programming (OOP) in Python. Learn to design and build applications using classes, objects, and the four pillars of OOP: Encapsulation, Inheritance, Polymorphism, and Abstraction.

## Learning Objectives

By the end of this module, you will:
- Create classes and instantiate objects
- Understand inheritance and method overriding
- Implement polymorphism in your designs
- Apply encapsulation for data protection
- Use abstraction for clean interfaces
- Master magic methods and operator overloading
- Handle custom exceptions in OOP context

## Module Contents

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

## Core Concepts

### OOP Fundamentals

#### Basic Class Definition
Classes are blueprints for creating objects. An object is an instance of a class, encapsulating data (attributes) and behavior (methods). Defining a class involves specifying its attributes and methods, including the `__init__` method for object initialization.

### Inheritance

#### Single Inheritance
Single inheritance allows a class (subclass/child) to inherit attributes and methods from another class (superclass/parent). This promotes code reusability and establishes an "is-a" relationship between classes.

#### Multiple Inheritance
Multiple inheritance allows a class to inherit from multiple parent classes, combining their functionalities. Python supports multiple inheritance, but it can introduce complexities like the Method Resolution Order (MRO).

### Polymorphism

#### Method Overriding and Duck Typing
Polymorphism means "many forms." In OOP, it allows objects of different classes to be treated as objects of a common type. Method overriding, where a subclass provides a specific implementation for a method already defined in its superclass, is a key aspect. Duck typing, a concept in Python, emphasizes that an object's suitability is determined by its methods and properties, rather than its type.

### Encapsulation

#### Private and Protected Attributes
Encapsulation is the bundling of data and methods that operate on the data within a single unit (class), and restricting direct access to some of an object's components. In Python, this is achieved through naming conventions (e.g., `_` for protected, `__` for private) and properties.

### Abstraction

#### Abstract Base Classes
Abstraction involves hiding complex implementation details and showing only the essential features of an object. Abstract Base Classes (ABCs) in Python, defined using the `abc` module, allow you to define interfaces (abstract methods) that concrete subclasses must implement.

### Magic Methods

#### Common Magic Methods
Magic methods (also known as dunder methods, e.g., `__init__`, `__str__`) are special methods in Python classes that have double underscores before and after their names. They allow you to define how objects of your class behave with built-in functions and operators.

## Key OOP Principles

### The Four Pillars of OOP

1.  **Encapsulation**: Bundling data and methods that operate on the data within a single unit, and restricting direct access to some of an object's components.
2.  **Inheritance**: A mechanism where a new class (subclass) derives properties and behavior from an existing class (superclass).
3.  **Polymorphism**: The ability of different classes to be treated as instances of a common type, allowing a single interface to represent different underlying forms.
4.  **Abstraction**: The process of hiding the complex implementation details and showing only the essential features of the object.

### Design Patterns in OOP
Design patterns are reusable solutions to common problems in software design. Examples include Singleton (ensuring only one instance of a class), Factory (creating objects without specifying the exact class), Observer (defining a one-to-many dependency), and Strategy (defining a family of algorithms and making them interchangeable).