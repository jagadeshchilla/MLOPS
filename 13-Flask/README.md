# 🌐 Module 13: Flask Web Development

![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Web Development](https://img.shields.io/badge/Web%20Development-Frontend%20%26%20Backend-blue?style=for-the-badge)
![Difficulty](https://img.shields.io/badge/Difficulty-Intermediate-orange?style=for-the-badge)

## 📖 Overview

This module introduces Flask, a lightweight Python web framework for building web applications and APIs. Learn to create dynamic web pages, handle HTTP requests, and deploy machine learning models as web services.

## 🎯 Learning Objectives

By the end of this module, you will:
- ✅ Build web applications using Flask framework
- ✅ Create RESTful APIs for ML model deployment
- ✅ Handle HTTP requests (GET, POST, PUT, DELETE)
- ✅ Use Jinja2 templating for dynamic content
- ✅ Serve static files (CSS, JavaScript, images)
- ✅ Deploy Flask applications for production

## 📂 Module Contents

### 📁 flask/ Directory
| File | Description | Focus Area |
|------|-------------|------------|
| `app.py` | Basic Flask application | Flask fundamentals |
| `main.py` | Advanced routing | URL patterns, methods |
| `getpost.py` | HTTP methods demo | GET/POST handling |
| `jinja.py` | Template rendering | Jinja2 templating |
| `api.py` | RESTful API example | JSON APIs, ML serving |

### 📁 templates/ Directory
| File | Description | Purpose |
|------|-------------|---------|
| `index.html` | Home page template | Main landing page |
| `about.html` | About page | Static content page |
| `form.html` | Form page | User input handling |
| `result.html` | Results display | Dynamic content |
| `result1.html` | Alternative results | Multiple templates |
| `getresult.html` | GET method results | Query parameter display |

### 📁 static/ Directory
| File | Description | Type |
|------|-------------|------|
| `css/style.css` | Stylesheet | CSS styling |

## 🚀 Quick Start

### Prerequisites
- Completion of Python fundamentals
- Basic understanding of HTML/CSS
- Knowledge of HTTP protocol basics

### Installation
```bash
# Install Flask
pip install Flask

# Install additional dependencies
pip install Flask-WTF Flask-SQLAlchemy
```

### Running Flask Applications
```bash
# Navigate to flask directory
cd "13-Flask/flask"

# Run basic app
python app.py

# Or run with Flask CLI
export FLASK_APP=app.py  # On Windows: set FLASK_APP=app.py
flask run

# Access at http://localhost:5000
```

## 📚 Detailed Content Guide

### 🚀 Basic Flask App (`app.py`)

**Simple Flask application structure:**

```python
from flask import Flask, render_template, request

# Create Flask application
app = Flask(__name__)

# Basic route
@app.route('/')
def home():
    return "Hello, Flask!"

# Route with template
@app.route('/welcome')
def welcome():
    return render_template('index.html')

# Route with parameter
@app.route('/user/<name>')
def user(name):
    return f"Hello, {name}!"

# Run application
if __name__ == '__main__':
    app.run(debug=True)
```

### 🔀 Advanced Routing (`main.py`)

**URL patterns and HTTP methods:**

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Multiple HTTP methods
@app.route('/data', methods=['GET', 'POST'])
def handle_data():
    if request.method == 'GET':
        return "Getting data"
    elif request.method == 'POST':
        return "Posting data"

# URL parameters
@app.route('/api/users/<int:user_id>')
def get_user(user_id):
    return f"User ID: {user_id}"

# Query parameters
@app.route('/search')
def search():
    query = request.args.get('q', '')
    return f"Searching for: {query}"

# JSON responses
@app.route('/api/status')
def status():
    return jsonify({
        'status': 'success',
        'message': 'API is running'
    })
```

### 📝 Form Handling (`getpost.py`)

**Processing user input:**

```python
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/form', methods=['GET', 'POST'])
def handle_form():
    if request.method == 'GET':
        return render_template('form.html')
    
    elif request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        
        # Process form data
        return render_template('result.html', 
                             username=username, 
                             email=email)

# File upload handling
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file selected'
    
    file = request.files['file']
    if file.filename != '':
        file.save(f'uploads/{file.filename}')
        return 'File uploaded successfully'
    
    return 'No file selected'
```

### 🎨 Jinja2 Templating (`jinja.py`)

**Dynamic content rendering:**

```python
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/template-demo')
def template_demo():
    data = {
        'title': 'Flask Demo',
        'current_time': datetime.now(),
        'users': ['Alice', 'Bob', 'Charlie'],
        'is_authenticated': True
    }
    return render_template('demo.html', **data)
```

**Template file (demo.html):**
```html
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <h1>Welcome to {{ title }}</h1>
    <p>Current time: {{ current_time.strftime('%Y-%m-%d %H:%M:%S') }}</p>
    
    {% if is_authenticated %}
        <h2>User List</h2>
        <ul>
        {% for user in users %}
            <li>{{ user }}</li>
        {% endfor %}
        </ul>
    {% else %}
        <p>Please log in to see users.</p>
    {% endif %}
</body>
</html>
```

### 🔌 RESTful API (`api.py`)

**Building APIs for ML model serving:**

```python
from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load pre-trained model (example)
# model = joblib.load('model.pkl')

@app.route('/api/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data
        data = request.get_json()
        
        # Extract features
        features = np.array(data['features']).reshape(1, -1)
        
        # Make prediction
        # prediction = model.predict(features)
        prediction = [0.85]  # Mock prediction
        
        return jsonify({
            'success': True,
            'prediction': prediction[0],
            'confidence': 0.92
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@app.route('/api/health')
def health_check():
    return jsonify({
        'status': 'healthy',
        'service': 'ML Prediction API',
        'version': '1.0.0'
    })

# CORS support
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response
```

## 💻 Practice Exercises

### Exercise 1: Personal Portfolio Website
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('portfolio_home.html')

@app.route('/projects')
def projects():
    projects = [
        {'name': 'Data Analysis', 'description': 'Python data analysis project'},
        {'name': 'ML Model', 'description': 'Machine learning classifier'}
    ]
    return render_template('projects.html', projects=projects)

@app.route('/contact')
def contact():
    return render_template('contact.html')
```

### Exercise 2: Simple Calculator API
```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    operation = data.get('operation')
    a = float(data.get('a'))
    b = float(data.get('b'))
    
    operations = {
        'add': a + b,
        'subtract': a - b,
        'multiply': a * b,
        'divide': a / b if b != 0 else 'Cannot divide by zero'
    }
    
    result = operations.get(operation, 'Invalid operation')
    
    return jsonify({
        'result': result,
        'operation': operation,
        'inputs': {'a': a, 'b': b}
    })
```

### Exercise 3: ML Model Deployment
```python
from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load your trained model
# with open('model.pkl', 'rb') as f:
#     model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        features = np.array(data['features']).reshape(1, -1)
        
        # Make prediction
        # prediction = model.predict(features)[0]
        # probability = model.predict_proba(features)[0].max()
        
        prediction = 1  # Mock prediction
        probability = 0.85
        
        return jsonify({
            'prediction': int(prediction),
            'probability': float(probability),
            'status': 'success'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400
```

## 🧪 Hands-On Activities

1. **Build a personal website**: Create multiple pages with templates
2. **Create a blog application**: Implement CRUD operations
3. **Develop a REST API**: Build endpoints for data operations
4. **Deploy an ML model**: Serve predictions via Flask API
5. **Add authentication**: Implement user login/logout

## 🔍 Flask Best Practices

### 🏗️ Application Structure
```
flask_app/
├── app.py              # Main application
├── config.py           # Configuration settings
├── requirements.txt    # Dependencies
├── templates/          # HTML templates
│   ├── base.html      # Base template
│   └── index.html     # Page templates
├── static/            # Static files
│   ├── css/          # Stylesheets
│   ├── js/           # JavaScript
│   └── images/       # Images
└── models/           # ML models (if applicable)
```

### 🔒 Security Considerations
```python
from flask import Flask
import os

app = Flask(__name__)

# Use environment variables for secrets
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key')

# Input validation
from flask_wtf import FlaskForm
from wtforms import StringField, validators

class ContactForm(FlaskForm):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    email = StringField('Email', [validators.Email()])
```

### 📊 Error Handling
```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request'}), 400
```

## 🌟 Flask vs Other Frameworks

| Feature | Flask | Django | FastAPI | Express.js |
|---------|-------|--------|---------|------------|
| **Complexity** | Simple | Complex | Medium | Simple |
| **Performance** | Good | Good | Excellent | Excellent |
| **Learning Curve** | Easy | Steep | Medium | Easy |
| **Flexibility** | High | Medium | High | High |
| **Built-in Features** | Minimal | Extensive | Modern | Minimal |

## 🚀 Deployment Options

### Local Development
```bash
# Development server
python app.py

# With Flask CLI
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

### Production Deployment
```bash
# Using Gunicorn
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app

# Using Docker
FROM python:3.9-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"]
```

## 🔗 Integration with MLOps

Flask serves as the deployment layer in MLOps pipelines:

1. **Model Serving**: Deploy ML models as REST APIs
2. **Monitoring**: Add logging and metrics collection
3. **A/B Testing**: Serve different model versions
4. **Batch Predictions**: Handle bulk prediction requests
5. **Model Updates**: Hot-swap models without downtime

## 📝 Assignment Checklist

- [ ] Create basic Flask application
- [ ] Implement routing and templates
- [ ] Handle forms and user input
- [ ] Build RESTful API endpoints
- [ ] Serve static files (CSS, JS)
- [ ] Deploy ML model via Flask API
- [ ] Add error handling and validation
- [ ] Test API endpoints

## 🆘 Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| Template not found | Check template folder path and file names |
| Static files not loading | Verify static folder structure |
| CORS errors | Add appropriate CORS headers |
| JSON parsing errors | Validate JSON format and content type |
| Import errors | Check Python path and package installation |

## 🏆 Real-World Projects

1. **ML Model API**: Deploy trained models for predictions
2. **Data Dashboard**: Visualize data with interactive charts
3. **File Processing Service**: Upload and process files
4. **Authentication System**: User registration and login
5. **Microservice Architecture**: Build service-oriented applications

---

**Flask Makes Web Development Simple! 🌟**

*Master Flask to deploy your ML models and create powerful web applications with minimal code!* 