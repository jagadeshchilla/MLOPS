# 🗄️ Module 11: Working With Databases

![SQLite](https://img.shields.io/badge/SQLite-Database-blue?style=for-the-badge&logo=sqlite&logoColor=white)
![Python](https://img.shields.io/badge/Python-Database%20Integration-green?style=for-the-badge&logo=python&logoColor=white)
![Difficulty](https://img.shields.io/badge/Difficulty-Intermediate-orange?style=for-the-badge)

## 📖 Overview

This module teaches you how to work with databases in Python using SQLite3. Learn to create, read, update, and delete data, manage database connections, and integrate databases into your applications.

## 🎯 Learning Objectives

By the end of this module, you will:
- ✅ Connect to SQLite databases using Python
- ✅ Perform CRUD operations (Create, Read, Update, Delete)
- ✅ Design and create database schemas
- ✅ Handle database transactions and error handling
- ✅ Implement data validation and constraints
- ✅ Build database-driven applications

## 📂 Module Contents

| File | Description | Key Concepts |
|------|-------------|--------------|
| `11.1-sqlite.ipynb` | SQLite fundamentals | Connection, tables, basic operations |
| `Module_SQLite3_Assignments_Questions.ipynb` | Practice exercises | Database design challenges |
| `Module_SQLite3_Assignments_Solution.ipynb` | Exercise solutions | Reference implementations |

## 🚀 Quick Start

### Prerequisites
- Completion of Module 10 (Data Analysis)
- Understanding of Python basics and data structures
- Basic knowledge of SQL concepts

### Running the Notebooks

```bash
# Navigate to this directory
cd "11-Working With Databases"

# Start Jupyter Lab
jupyter lab

# Or start Jupyter Notebook
jupyter notebook
```

## 📚 Detailed Content Guide

### 🔧 SQLite Basics (`11.1-sqlite.ipynb`)

#### 🔹 Database Connection and Setup
```python
import sqlite3
from datetime import datetime

# Connect to database (creates if doesn't exist)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Enable foreign key constraints
cursor.execute("PRAGMA foreign_keys = ON")

# Create tables
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT,
        user_id INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
''')

conn.commit()
```

#### 🔹 CRUD Operations
```python
# CREATE - Insert data
def create_user(username, email):
    """Create a new user."""
    try:
        cursor.execute(
            "INSERT INTO users (username, email) VALUES (?, ?)",
            (username, email)
        )
        conn.commit()
        return cursor.lastrowid
    except sqlite3.IntegrityError as e:
        print(f"Error creating user: {e}")
        return None

# READ - Query data
def get_user(user_id):
    """Get user by ID."""
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()

def get_all_users():
    """Get all users."""
    cursor.execute("SELECT * FROM users ORDER BY created_at DESC")
    return cursor.fetchall()

# UPDATE - Modify data
def update_user_email(user_id, new_email):
    """Update user email."""
    cursor.execute(
        "UPDATE users SET email = ? WHERE id = ?",
        (new_email, user_id)
    )
    conn.commit()
    return cursor.rowcount > 0

# DELETE - Remove data
def delete_user(user_id):
    """Delete user and their posts."""
    try:
        # Delete user's posts first (foreign key constraint)
        cursor.execute("DELETE FROM posts WHERE user_id = ?", (user_id,))
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Error deleting user: {e}")
        conn.rollback()
        return False
```

#### 🔹 Advanced Queries
```python
# JOIN operations
def get_users_with_post_count():
    """Get users with their post count."""
    cursor.execute('''
        SELECT u.id, u.username, u.email, COUNT(p.id) as post_count
        FROM users u
        LEFT JOIN posts p ON u.id = p.user_id
        GROUP BY u.id, u.username, u.email
        ORDER BY post_count DESC
    ''')
    return cursor.fetchall()

# Complex filtering
def search_posts(keyword, user_id=None):
    """Search posts by keyword."""
    query = """
        SELECT p.id, p.title, p.content, u.username
        FROM posts p
        JOIN users u ON p.user_id = u.id
        WHERE (p.title LIKE ? OR p.content LIKE ?)
    """
    params = [f'%{keyword}%', f'%{keyword}%']
    
    if user_id:
        query += " AND p.user_id = ?"
        params.append(user_id)
    
    query += " ORDER BY p.created_at DESC"
    cursor.execute(query, params)
    return cursor.fetchall()

# Pagination
def get_posts_paginated(page=1, per_page=10):
    """Get posts with pagination."""
    offset = (page - 1) * per_page
    cursor.execute('''
        SELECT p.id, p.title, p.content, u.username, p.created_at
        FROM posts p
        JOIN users u ON p.user_id = u.id
        ORDER BY p.created_at DESC
        LIMIT ? OFFSET ?
    ''', (per_page, offset))
    return cursor.fetchall()
```

### 🛡️ Database Best Practices

#### 🔹 Context Managers and Connection Handling
```python
import sqlite3
from contextlib import contextmanager

class DatabaseManager:
    """Database manager with proper connection handling."""
    
    def __init__(self, db_path):
        self.db_path = db_path
    
    @contextmanager
    def get_connection(self):
        """Context manager for database connections."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row  # Enable column access by name
        try:
            yield conn
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()
    
    def execute_query(self, query, params=None):
        """Execute a SELECT query."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return cursor.fetchall()
    
    def execute_update(self, query, params=None):
        """Execute INSERT, UPDATE, or DELETE query."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            conn.commit()
            return cursor.rowcount

# Usage
db = DatabaseManager('app.db')
users = db.execute_query("SELECT * FROM users WHERE age > ?", (18,))
```

#### 🔹 Data Validation and Models
```python
from dataclasses import dataclass
from typing import Optional
import re

@dataclass
class User:
    """User data model with validation."""
    username: str
    email: str
    id: Optional[int] = None
    created_at: Optional[str] = None
    
    def __post_init__(self):
        self.validate()
    
    def validate(self):
        """Validate user data."""
        if not self.username or len(self.username) < 3:
            raise ValueError("Username must be at least 3 characters")
        
        if not self.is_valid_email(self.email):
            raise ValueError("Invalid email format")
    
    @staticmethod
    def is_valid_email(email):
        """Validate email format."""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def save(self, db_manager):
        """Save user to database."""
        if self.id is None:
            # Create new user
            query = "INSERT INTO users (username, email) VALUES (?, ?)"
            self.id = db_manager.execute_update(query, (self.username, self.email))
        else:
            # Update existing user
            query = "UPDATE users SET username = ?, email = ? WHERE id = ?"
            db_manager.execute_update(query, (self.username, self.email, self.id))
    
    @classmethod
    def from_db_row(cls, row):
        """Create User from database row."""
        return cls(
            id=row['id'],
            username=row['username'],
            email=row['email'],
            created_at=row['created_at']
        )

class UserRepository:
    """Repository pattern for user operations."""
    
    def __init__(self, db_manager):
        self.db = db_manager
    
    def create(self, user: User) -> int:
        """Create a new user."""
        query = "INSERT INTO users (username, email) VALUES (?, ?)"
        user_id = self.db.execute_update(query, (user.username, user.email))
        user.id = user_id
        return user_id
    
    def get_by_id(self, user_id: int) -> Optional[User]:
        """Get user by ID."""
        query = "SELECT * FROM users WHERE id = ?"
        rows = self.db.execute_query(query, (user_id,))
        if rows:
            return User.from_db_row(rows[0])
        return None
    
    def get_by_email(self, email: str) -> Optional[User]:
        """Get user by email."""
        query = "SELECT * FROM users WHERE email = ?"
        rows = self.db.execute_query(query, (email,))
        if rows:
            return User.from_db_row(rows[0])
        return None
    
    def update(self, user: User) -> bool:
        """Update user."""
        query = "UPDATE users SET username = ?, email = ? WHERE id = ?"
        affected = self.db.execute_update(query, (user.username, user.email, user.id))
        return affected > 0
    
    def delete(self, user_id: int) -> bool:
        """Delete user."""
        query = "DELETE FROM users WHERE id = ?"
        affected = self.db.execute_update(query, (user_id,))
        return affected > 0
    
    def list_all(self) -> list[User]:
        """List all users."""
        query = "SELECT * FROM users ORDER BY created_at DESC"
        rows = self.db.execute_query(query)
        return [User.from_db_row(row) for row in rows]
```

## 💻 Practice Exercises

### Exercise 1: Inventory Management System
```python
class InventoryDB:
    """Inventory management database."""
    
    def __init__(self, db_path):
        self.db = DatabaseManager(db_path)
        self.setup_tables()
    
    def setup_tables(self):
        """Create inventory tables."""
        tables = [
            '''CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                description TEXT
            )''',
            '''CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                sku TEXT UNIQUE NOT NULL,
                category_id INTEGER,
                price DECIMAL(10,2),
                quantity INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (category_id) REFERENCES categories (id)
            )''',
            '''CREATE TABLE IF NOT EXISTS stock_movements (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id INTEGER,
                movement_type TEXT CHECK(movement_type IN ('IN', 'OUT')),
                quantity INTEGER,
                reason TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (product_id) REFERENCES products (id)
            )'''
        ]
        
        for table_sql in tables:
            self.db.execute_update(table_sql)
    
    def add_product(self, name, sku, category_id, price, initial_quantity=0):
        """Add new product to inventory."""
        try:
            # Add product
            product_query = '''
                INSERT INTO products (name, sku, category_id, price, quantity)
                VALUES (?, ?, ?, ?, ?)
            '''
            product_id = self.db.execute_update(
                product_query, (name, sku, category_id, price, initial_quantity)
            )
            
            # Record initial stock if any
            if initial_quantity > 0:
                self.record_stock_movement(product_id, 'IN', initial_quantity, 'Initial stock')
            
            return product_id
        except sqlite3.IntegrityError:
            raise ValueError(f"Product with SKU {sku} already exists")
    
    def update_stock(self, product_id, quantity_change, reason):
        """Update product stock."""
        # Get current quantity
        current = self.db.execute_query(
            "SELECT quantity FROM products WHERE id = ?", (product_id,)
        )
        
        if not current:
            raise ValueError("Product not found")
        
        current_qty = current[0]['quantity']
        new_qty = current_qty + quantity_change
        
        if new_qty < 0:
            raise ValueError("Insufficient stock")
        
        # Update product quantity
        self.db.execute_update(
            "UPDATE products SET quantity = ? WHERE id = ?",
            (new_qty, product_id)
        )
        
        # Record movement
        movement_type = 'IN' if quantity_change > 0 else 'OUT'
        self.record_stock_movement(product_id, movement_type, abs(quantity_change), reason)
    
    def record_stock_movement(self, product_id, movement_type, quantity, reason):
        """Record stock movement."""
        query = '''
            INSERT INTO stock_movements (product_id, movement_type, quantity, reason)
            VALUES (?, ?, ?, ?)
        '''
        self.db.execute_update(query, (product_id, movement_type, quantity, reason))
    
    def get_low_stock_products(self, threshold=10):
        """Get products with low stock."""
        query = '''
            SELECT p.*, c.name as category_name
            FROM products p
            LEFT JOIN categories c ON p.category_id = c.id
            WHERE p.quantity <= ?
            ORDER BY p.quantity ASC
        '''
        return self.db.execute_query(query, (threshold,))
```

### Exercise 2: Library Management System
```python
class LibraryDB:
    """Library management system database."""
    
    def __init__(self, db_path):
        self.db = DatabaseManager(db_path)
        self.setup_tables()
    
    def setup_tables(self):
        """Create library tables."""
        tables = [
            '''CREATE TABLE IF NOT EXISTS authors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                birth_year INTEGER,
                nationality TEXT
            )''',
            '''CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                isbn TEXT UNIQUE,
                author_id INTEGER,
                publication_year INTEGER,
                genre TEXT,
                total_copies INTEGER DEFAULT 1,
                available_copies INTEGER DEFAULT 1,
                FOREIGN KEY (author_id) REFERENCES authors (id)
            )''',
            '''CREATE TABLE IF NOT EXISTS members (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE,
                phone TEXT,
                membership_date DATE DEFAULT (date('now'))
            )''',
            '''CREATE TABLE IF NOT EXISTS loans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                book_id INTEGER,
                member_id INTEGER,
                loan_date DATE DEFAULT (date('now')),
                due_date DATE,
                return_date DATE,
                FOREIGN KEY (book_id) REFERENCES books (id),
                FOREIGN KEY (member_id) REFERENCES members (id)
            )'''
        ]
        
        for table_sql in tables:
            self.db.execute_update(table_sql)
    
    def loan_book(self, book_id, member_id, loan_days=14):
        """Loan a book to a member."""
        from datetime import datetime, timedelta
        
        # Check if book is available
        book_query = "SELECT available_copies FROM books WHERE id = ?"
        book_result = self.db.execute_query(book_query, (book_id,))
        
        if not book_result or book_result[0]['available_copies'] <= 0:
            raise ValueError("Book not available for loan")
        
        # Create loan record
        due_date = (datetime.now() + timedelta(days=loan_days)).date()
        loan_query = '''
            INSERT INTO loans (book_id, member_id, due_date)
            VALUES (?, ?, ?)
        '''
        loan_id = self.db.execute_update(loan_query, (book_id, member_id, due_date))
        
        # Update available copies
        update_query = '''
            UPDATE books 
            SET available_copies = available_copies - 1 
            WHERE id = ?
        '''
        self.db.execute_update(update_query, (book_id,))
        
        return loan_id
    
    def return_book(self, loan_id):
        """Return a book."""
        from datetime import datetime
        
        # Update loan record
        return_query = '''
            UPDATE loans 
            SET return_date = date('now') 
            WHERE id = ? AND return_date IS NULL
        '''
        affected = self.db.execute_update(return_query, (loan_id,))
        
        if affected == 0:
            raise ValueError("Loan not found or already returned")
        
        # Get book_id for the loan
        book_query = "SELECT book_id FROM loans WHERE id = ?"
        book_result = self.db.execute_query(book_query, (loan_id,))
        book_id = book_result[0]['book_id']
        
        # Update available copies
        update_query = '''
            UPDATE books 
            SET available_copies = available_copies + 1 
            WHERE id = ?
        '''
        self.db.execute_update(update_query, (book_id,))
        
        return True
    
    def get_overdue_books(self):
        """Get list of overdue books."""
        query = '''
            SELECT l.id, b.title, m.name as member_name, l.due_date,
                   julianday('now') - julianday(l.due_date) as days_overdue
            FROM loans l
            JOIN books b ON l.book_id = b.id
            JOIN members m ON l.member_id = m.id
            WHERE l.return_date IS NULL AND l.due_date < date('now')
            ORDER BY days_overdue DESC
        '''
        return self.db.execute_query(query)
```

## 🧪 Hands-On Activities

1. **E-commerce database**: Products, orders, customers with full relationships
2. **Student management**: Students, courses, enrollments, grades
3. **Hospital system**: Patients, doctors, appointments, medical records
4. **Social media**: Users, posts, comments, likes, follows

## 🔍 Key Concepts to Remember

### SQL Fundamentals
- **CRUD Operations**: Create, Read, Update, Delete
- **Relationships**: Foreign keys, joins, normalization
- **Constraints**: Primary keys, unique constraints, check constraints
- **Indexing**: Improve query performance

### Python Integration
- **Connection Management**: Proper opening and closing
- **Parameter Binding**: Prevent SQL injection
- **Transaction Handling**: Commit, rollback operations
- **Error Handling**: Database-specific exceptions

## 🌟 Best Practices

1. **Use parameterized queries**: Prevent SQL injection attacks
2. **Handle connections properly**: Use context managers
3. **Implement transactions**: Ensure data consistency
4. **Validate input data**: Check data before database operations
5. **Design normalized schemas**: Reduce data redundancy
6. **Add appropriate indexes**: Optimize query performance

## 📝 Assignment Checklist

- [ ] Connect to SQLite database
- [ ] Create tables with proper schemas
- [ ] Implement CRUD operations
- [ ] Use parameterized queries
- [ ] Handle database errors gracefully
- [ ] Design relational database schemas
- [ ] Implement data validation
- [ ] Complete all assignment exercises

## 🆘 Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| SQL injection vulnerability | Always use parameterized queries |
| Database locked errors | Ensure proper connection closing |
| Foreign key constraint failures | Check relationships and data integrity |
| Performance issues | Add indexes, optimize queries |
| Data type mismatches | Validate data types before insertion |

## 🏆 Challenge Projects

1. **Full E-commerce System**: Complete online store database
2. **School Management System**: Students, teachers, courses, grades
3. **Hospital Management**: Comprehensive medical records system
4. **Social Media Backend**: Users, posts, relationships, messaging
5. **Inventory Tracking**: Multi-location inventory with transfers

---

**Data is Your Foundation! 🏗️**

*Master database operations to build robust, data-driven applications!* 