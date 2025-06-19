# 📝 Module 12: Logging in Python

![Python](https://img.shields.io/badge/Python-Logging-yellow?style=for-the-badge&logo=python&logoColor=white)
![Monitoring](https://img.shields.io/badge/Monitoring-Production%20Ready-green?style=for-the-badge)
![Difficulty](https://img.shields.io/badge/Difficulty-Intermediate-orange?style=for-the-badge)

## 📖 Overview

This module teaches you professional logging practices in Python. Learn to implement comprehensive logging systems for debugging, monitoring, and maintaining production applications.

## 🎯 Learning Objectives

By the end of this module, you will:
- ✅ Implement Python's built-in logging module
- ✅ Configure multiple loggers for different components
- ✅ Use different log levels and formatters
- ✅ Set up file and console logging handlers
- ✅ Integrate logging with real applications
- ✅ Follow logging best practices for production

## 📂 Module Contents

| File | Description | Key Concepts |
|------|-------------|--------------|
| `12.1-logging.ipynb` | Logging fundamentals | Basic logging, levels, formatters |
| `12.2-multiplelogger.ipynb` | Advanced logging | Multiple loggers, handlers, filters |
| `app.py` | Flask app with logging | Real-world logging implementation |
| `Module_Logging_Assignments_Questions.ipynb` | Practice exercises | Logging challenges |
| `Module_Logging_Assignments_Solutions.ipynb` | Exercise solutions | Reference implementations |

### 📁 Directory Structure
```
logs/                   # Log files directory
ML Flow/               # MLflow logging examples
```

## 🚀 Quick Start

### Prerequisites
- Completion of Module 11 (Databases)
- Understanding of Python modules and classes

### Running the Notebooks

```bash
# Navigate to this directory
cd "12-Logging In Python"

# Start Jupyter Lab
jupyter lab

# Or start Jupyter Notebook
jupyter notebook
```

## 📚 Detailed Content Guide

### 📊 Logging Basics (`12.1-logging.ipynb`)

#### 🔹 Basic Logging Setup
```python
import logging

# Basic configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Create logger
logger = logging.getLogger(__name__)

# Log messages at different levels
logger.debug("Debug message - detailed information")
logger.info("Info message - general information")
logger.warning("Warning message - something unexpected")
logger.error("Error message - serious problem")
logger.critical("Critical message - program may stop")
```

#### 🔹 Log Levels and When to Use Them
```python
import logging

# Log levels (in order of severity)
log_levels = {
    'DEBUG': logging.DEBUG,      # 10 - Detailed diagnostic info
    'INFO': logging.INFO,        # 20 - General information
    'WARNING': logging.WARNING,  # 30 - Something unexpected
    'ERROR': logging.ERROR,      # 40 - Serious problem
    'CRITICAL': logging.CRITICAL # 50 - Program may stop
}

def demonstrate_log_levels():
    """Demonstrate different log levels."""
    
    # DEBUG: Detailed information for diagnosing problems
    logging.debug("Starting function execution")
    logging.debug(f"Processing item: {item}")
    
    # INFO: General workflow information
    logging.info("User logged in successfully")
    logging.info("Processing 100 records")
    
    # WARNING: Something unexpected but not an error
    logging.warning("Disk space is running low")
    logging.warning("Deprecated function called")
    
    # ERROR: Serious problem occurred
    logging.error("Failed to connect to database")
    logging.error("Invalid user input received")
    
    # CRITICAL: Very serious error, program may stop
    logging.critical("Out of memory")
    logging.critical("Security breach detected")
```

#### 🔹 Formatters and Handlers
```python
import logging
import os

# Create formatter
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s'
)

# Create console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

# Create file handler
os.makedirs('logs', exist_ok=True)
file_handler = logging.FileHandler('logs/app.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# Create logger and add handlers
logger = logging.getLogger('MyApp')
logger.setLevel(logging.DEBUG)
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Test logging
logger.debug("Debug message")
logger.info("Info message")
logger.error("Error message")
```

### 🔧 Advanced Logging (`12.2-multiplelogger.ipynb`)

#### 🔹 Multiple Loggers and Hierarchies
```python
import logging
from datetime import datetime

class LoggerSetup:
    """Setup multiple loggers for different components."""
    
    @staticmethod
    def setup_loggers():
        """Configure multiple loggers with different settings."""
        
        # Root logger configuration
        root_logger = logging.getLogger()
        root_logger.setLevel(logging.WARNING)
        
        # Application logger
        app_logger = logging.getLogger('app')
        app_logger.setLevel(logging.INFO)
        
        # Database logger
        db_logger = logging.getLogger('app.database')
        db_logger.setLevel(logging.DEBUG)
        
        # Security logger
        security_logger = logging.getLogger('app.security')
        security_logger.setLevel(logging.WARNING)
        
        # Performance logger
        perf_logger = logging.getLogger('app.performance')
        perf_logger.setLevel(logging.INFO)
        
        return {
            'app': app_logger,
            'database': db_logger,
            'security': security_logger,
            'performance': perf_logger
        }
    
    @staticmethod
    def setup_handlers():
        """Setup different handlers for different purposes."""
        
        # Console handler for development
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        console_handler.setFormatter(console_formatter)
        
        # General application file handler
        app_handler = logging.FileHandler('logs/application.log')
        app_handler.setLevel(logging.DEBUG)
        app_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s'
        )
        app_handler.setFormatter(app_formatter)
        
        # Error file handler
        error_handler = logging.FileHandler('logs/errors.log')
        error_handler.setLevel(logging.ERROR)
        error_handler.setFormatter(app_formatter)
        
        # Security events handler
        security_handler = logging.FileHandler('logs/security.log')
        security_handler.setLevel(logging.WARNING)
        security_formatter = logging.Formatter(
            '%(asctime)s - SECURITY - %(levelname)s - %(message)s'
        )
        security_handler.setFormatter(security_formatter)
        
        return {
            'console': console_handler,
            'app': app_handler,
            'error': error_handler,
            'security': security_handler
        }

# Usage example
def setup_application_logging():
    """Complete logging setup for an application."""
    
    # Create logs directory
    os.makedirs('logs', exist_ok=True)
    
    # Setup loggers and handlers
    loggers = LoggerSetup.setup_loggers()
    handlers = LoggerSetup.setup_handlers()
    
    # Configure app logger
    loggers['app'].addHandler(handlers['console'])
    loggers['app'].addHandler(handlers['app'])
    loggers['app'].addHandler(handlers['error'])
    
    # Configure database logger
    loggers['database'].addHandler(handlers['app'])
    
    # Configure security logger
    loggers['security'].addHandler(handlers['security'])
    loggers['security'].addHandler(handlers['error'])
    
    # Configure performance logger
    loggers['performance'].addHandler(handlers['app'])
    
    return loggers
```

#### 🔹 Custom Filters and Formatters
```python
import logging
import json
from datetime import datetime

class JSONFormatter(logging.Formatter):
    """Custom formatter that outputs JSON."""
    
    def format(self, record):
        log_entry = {
            'timestamp': datetime.fromtimestamp(record.created).isoformat(),
            'level': record.levelname,
            'logger': record.name,
            'module': record.module,
            'function': record.funcName,
            'line': record.lineno,
            'message': record.getMessage()
        }
        
        # Add exception info if present
        if record.exc_info:
            log_entry['exception'] = self.formatException(record.exc_info)
        
        # Add extra fields
        for key, value in record.__dict__.items():
            if key not in ['name', 'msg', 'args', 'levelname', 'levelno', 
                          'pathname', 'filename', 'module', 'exc_info', 
                          'exc_text', 'stack_info', 'lineno', 'funcName', 
                          'created', 'msecs', 'relativeCreated', 'thread', 
                          'threadName', 'processName', 'process', 'getMessage']:
                log_entry[key] = value
        
        return json.dumps(log_entry)

class SecurityFilter(logging.Filter):
    """Filter for security-related log messages."""
    
    def filter(self, record):
        # Only allow security-related messages
        security_keywords = ['login', 'logout', 'authentication', 'authorization', 
                           'access denied', 'security', 'breach', 'attack']
        message = record.getMessage().lower()
        return any(keyword in message for keyword in security_keywords)

class PerformanceFilter(logging.Filter):
    """Filter for performance-related log messages."""
    
    def filter(self, record):
        return hasattr(record, 'execution_time') or 'performance' in record.getMessage().lower()

# Usage example
def setup_advanced_logging():
    """Setup advanced logging with custom formatters and filters."""
    
    # JSON formatter for structured logging
    json_formatter = JSONFormatter()
    
    # JSON file handler
    json_handler = logging.FileHandler('logs/application.json')
    json_handler.setFormatter(json_formatter)
    json_handler.setLevel(logging.INFO)
    
    # Security handler with filter
    security_handler = logging.FileHandler('logs/security.log')
    security_handler.addFilter(SecurityFilter())
    security_handler.setLevel(logging.WARNING)
    
    # Performance handler with filter
    perf_handler = logging.FileHandler('logs/performance.log')
    perf_handler.addFilter(PerformanceFilter())
    perf_handler.setLevel(logging.INFO)
    
    # Setup logger
    logger = logging.getLogger('advanced_app')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(json_handler)
    logger.addHandler(security_handler)
    logger.addHandler(perf_handler)
    
    return logger
```

### 🌐 Real-World Application (`app.py`)

```python
import logging
import logging.config
from flask import Flask, request, jsonify
import time
import functools

# Logging configuration
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
        'detailed': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'logs/flask_app.log',
            'formatter': 'detailed'
        },
        'error_file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'logs/errors.log',
            'formatter': 'detailed'
        }
    },
    'loggers': {
        'flask_app': {
            'handlers': ['console', 'file', 'error_file'],
            'level': 'DEBUG',
            'propagate': False
        },
        'werkzeug': {
            'handlers': ['file'],
            'level': 'WARNING',
            'propagate': False
        }
    }
}

def setup_logging():
    """Setup logging configuration."""
    import os
    os.makedirs('logs', exist_ok=True)
    logging.config.dictConfig(LOGGING_CONFIG)
    return logging.getLogger('flask_app')

def log_performance(func):
    """Decorator to log function performance."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger = logging.getLogger('flask_app')
        start_time = time.time()
        
        try:
            result = func(*args, **kwargs)
            execution_time = time.time() - start_time
            logger.info(f"{func.__name__} executed in {execution_time:.4f} seconds")
            return result
        except Exception as e:
            execution_time = time.time() - start_time
            logger.error(f"{func.__name__} failed after {execution_time:.4f} seconds: {str(e)}")
            raise
    
    return wrapper

# Flask application with logging
app = Flask(__name__)
logger = setup_logging()

@app.before_request
def log_request_info():
    """Log incoming request information."""
    logger.info(f"Request: {request.method} {request.url} from {request.remote_addr}")
    logger.debug(f"Headers: {dict(request.headers)}")

@app.after_request
def log_response_info(response):
    """Log response information."""
    logger.info(f"Response: {response.status_code} for {request.method} {request.url}")
    return response

@app.route('/api/users', methods=['GET'])
@log_performance
def get_users():
    """Get all users."""
    logger.info("Fetching all users")
    # Simulate database operation
    time.sleep(0.1)
    users = [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}]
    logger.debug(f"Retrieved {len(users)} users")
    return jsonify(users)

@app.route('/api/users', methods=['POST'])
@log_performance
def create_user():
    """Create a new user."""
    try:
        data = request.get_json()
        logger.info(f"Creating user: {data.get('name', 'Unknown')}")
        
        # Validate input
        if not data or 'name' not in data:
            logger.warning("Invalid user data provided")
            return jsonify({'error': 'Name is required'}), 400
        
        # Simulate user creation
        user_id = 123
        logger.info(f"User created successfully with ID: {user_id}")
        return jsonify({'id': user_id, 'name': data['name']}), 201
        
    except Exception as e:
        logger.error(f"Failed to create user: {str(e)}", exc_info=True)
        return jsonify({'error': 'Internal server error'}), 500

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    logger.warning(f"404 error: {request.url} not found")
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    logger.error(f"500 error: {str(error)}", exc_info=True)
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    logger.info("Starting Flask application")
    app.run(debug=True, host='0.0.0.0', port=5000)
```

## 💻 Practice Exercises

### Exercise 1: Logging Decorator
```python
import logging
import functools
import time

def create_logger_decorator(logger_name=None, level=logging.INFO):
    """Create a configurable logging decorator."""
    
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            logger = logging.getLogger(logger_name or func.__module__)
            
            # Log function entry
            logger.log(level, f"Entering {func.__name__} with args={args}, kwargs={kwargs}")
            
            start_time = time.time()
            try:
                result = func(*args, **kwargs)
                execution_time = time.time() - start_time
                logger.log(level, f"Exiting {func.__name__} successfully in {execution_time:.4f}s")
                return result
            except Exception as e:
                execution_time = time.time() - start_time
                logger.error(f"Exception in {func.__name__} after {execution_time:.4f}s: {str(e)}")
                raise
        
        return wrapper
    return decorator

# Usage examples
@create_logger_decorator('math_operations', logging.DEBUG)
def divide(a, b):
    return a / b

@create_logger_decorator('business_logic')
def process_order(order_id, items):
    # Simulate order processing
    time.sleep(0.1)
    return f"Order {order_id} processed with {len(items)} items"
```

## 🧪 Hands-On Activities

1. **Web scraper with logging**: Log all scraping activities and errors
2. **Data processing pipeline**: Log each stage of data transformation
3. **API client with retry logic**: Log all API calls and retry attempts
4. **Database operations**: Log all database interactions and performance

## 🔍 Key Concepts to Remember

### Logging Levels
- **DEBUG**: Detailed diagnostic information
- **INFO**: General operational messages
- **WARNING**: Something unexpected happened
- **ERROR**: Serious problem occurred
- **CRITICAL**: Program may stop working

### Best Practices
- **Use appropriate levels**: Don't log everything as ERROR
- **Structured logging**: Use consistent formats
- **Avoid sensitive data**: Don't log passwords or personal info
- **Performance considerations**: Logging can impact performance
- **Log rotation**: Prevent log files from growing too large

## 🌟 Production Logging Best Practices

1. **Use structured formats**: JSON for easier parsing
2. **Include context**: User ID, request ID, session info
3. **Log aggregation**: Use tools like ELK stack or Splunk
4. **Monitor log levels**: Adjust based on environment
5. **Security considerations**: Sanitize sensitive information
6. **Performance impact**: Use async logging for high-volume apps

## 📝 Assignment Checklist

- [ ] Configure basic logging with different levels
- [ ] Set up multiple loggers for different components
- [ ] Create custom formatters and filters
- [ ] Implement file and console handlers
- [ ] Add logging to a real application
- [ ] Create performance monitoring with logging
- [ ] Handle exceptions with proper logging
- [ ] Complete all assignment exercises

## 🆘 Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| Logs not appearing | Check logger level and handler configuration |
| Duplicate log messages | Check logger propagation settings |
| Log files not created | Ensure directory exists and permissions are correct |
| Performance degradation | Use appropriate log levels, consider async logging |
| Sensitive data in logs | Implement log sanitization |

## 🏆 Challenge Projects

1. **Comprehensive Web App Logging**: Full request/response logging system
2. **Microservices Logging**: Distributed logging with correlation IDs
3. **Log Analysis Dashboard**: Parse and visualize log data
4. **Alerting System**: Monitor logs and send alerts on errors
5. **Audit Trail System**: Complete user action logging

---

**Logging is Your Application's Voice! 📢**

*Master logging to monitor, debug, and maintain production applications effectively!* 