# 🚀 Apache Airflow with Astro CLI - Complete Setup Guide

## 📚 Table of Contents

- [Introduction to Apache Airflow](#-introduction-to-apache-airflow)
- [Key Components of Apache Airflow](#-key-components-of-apache-airflow)
- [Why Airflow for MLOps](#-why-airflow-for-mlops)
- [Setting Up Airflow with Astro](#-setting-up-airflow-with-astro)
- [Project Overview](#-project-overview)
- [What We've Accomplished](#-what-weve-accomplished)
- [Getting Started](#-getting-started)
- [DAGs in This Project](#-dags-in-this-project)
- [Troubleshooting](#-troubleshooting)

---

## 🌟 Introduction to Apache Airflow

Apache Airflow is an **open-source platform** designed to programmatically author, schedule, and monitor workflows. It allows you to define workflows as **Directed Acyclic Graphs (DAGs)** of tasks, making complex data pipelines manageable and observable.

### Key Features:
- **Dynamic**: Pipelines are configuration as code (Python), allowing for dynamic pipeline generation
- **Extensible**: Easily define your own operators, executors and extend the library
- **Elegant**: Airflow pipelines are lean and explicit with parameterization built into the core
- **Scalable**: Airflow has a modular architecture and uses a message queue to orchestrate workers

---

## 🔧 Key Components of Apache Airflow

### 1. **Web Server** 🌐
- Provides the user interface for monitoring and managing workflows
- Accessible at `http://localhost:8080` (in our setup)
- Offers DAG visualization, task monitoring, and log inspection

### 2. **Scheduler** ⏰
- Heart of Airflow that triggers scheduled workflows
- Monitors all tasks and DAGs, triggering task instances when dependencies are met
- Handles task scheduling based on defined intervals

### 3. **Executor** ⚡
- Defines how and where tasks are executed
- Can run tasks locally, on multiple machines, or in containers
- Our setup uses the default LocalExecutor

### 4. **Metadata Database** 🗄️
- Stores all metadata about DAGs, tasks, variables, and connections
- PostgreSQL database running on port `5433` in our configuration
- Critical for maintaining state and history

### 5. **Workers** 👷
- Execute the actual tasks defined in your DAGs
- Can be scaled horizontally for increased throughput

---

## 🤖 Why Airflow for MLOps

Machine Learning Operations (MLOps) requires robust orchestration of complex workflows. Airflow excels in this domain because:

### **Data Pipeline Management** 📊
- **ETL/ELT Processes**: Extract, transform, and load data from various sources
- **Data Validation**: Ensure data quality before model training
- **Feature Engineering**: Automate feature creation and selection

### **Model Lifecycle Orchestration** 🔄
- **Training Pipelines**: Automate model training with different parameters
- **Model Validation**: Automated testing and validation of model performance
- **Deployment Automation**: Seamless model deployment to production environments

### **Monitoring & Observability** 👁️
- **Pipeline Monitoring**: Track data pipeline health and performance
- **Model Drift Detection**: Monitor model performance over time
- **Alerting**: Automated notifications for pipeline failures or model degradation

### **Scalability & Reliability** 🏗️
- **Retry Logic**: Automatic retry of failed tasks with configurable policies
- **Dependency Management**: Complex task dependencies handled elegantly
- **Resource Management**: Efficient resource allocation and scaling

---

## 🛠️ Setting Up Airflow with Astro

**Astro CLI** is the fastest way to get started with Apache Airflow. It provides:

- **Pre-configured Environment**: Ready-to-use Airflow setup with Docker
- **Local Development**: Test DAGs locally before deployment
- **Production Ready**: Easy deployment to Astronomer's managed service
- **Best Practices**: Built-in best practices and optimizations

### Why Choose Astro CLI?
- ✅ **Zero Configuration**: No manual setup of databases, web servers, or schedulers
- ✅ **Docker-based**: Consistent environment across development and production
- ✅ **Hot Reloading**: Changes to DAGs are reflected immediately
- ✅ **Integrated Tooling**: Built-in testing, linting, and deployment tools

---

## 📋 Project Overview

This project demonstrates a complete Apache Airflow setup using Astro CLI, featuring multiple DAGs that showcase different aspects of workflow orchestration.

### **Project Structure**
```
airflow_ASTRO/
├── dags/                          # DAG definitions
│   ├── mlpipeline.py             # Machine Learning pipeline
│   ├── maths_operation.py        # Mathematical operations chain
│   └── exampledag.py             # Example DAG from template
├── plugins/                       # Custom plugins
├── include/                       # Additional files
├── tests/                         # DAG tests
├── requirements.txt               # Python dependencies
├── Dockerfile                     # Container configuration
├── .env                          # Environment variables
└── README.md                     # This file
```

---

## ✅ What We've Accomplished

### **1. Environment Setup** 🏗️
- ✅ **Installed Astro CLI** (v1.34.1) using Windows Package Manager
- ✅ **Resolved Port Conflicts** by configuring custom ports:
  - PostgreSQL: `5433` (avoiding conflict with existing service on `5432`)
  - Airflow Web Server: `8080`
- ✅ **Successfully Started** all Airflow components in Docker containers

### **2. DAG Development** 📝
- ✅ **Created ML Pipeline DAG** (`mlpipeline.py`):
  - Data preprocessing task
  - Model training task  
  - Model evaluation task
  - Sequential task dependencies
  
- ✅ **Built Mathematical Operations DAG** (`maths_operation.py`):
  - Chain of mathematical operations using XCom
  - Demonstrates data passing between tasks
  - Shows complex workflow orchestration

### **3. Compatibility Fixes** 🔧
- ✅ **Fixed Import Issues**: Updated deprecated `python_operator` imports
- ✅ **Resolved Schedule Parameter**: Changed `schedule_interval` to `schedule`
- ✅ **Removed Deprecated Parameters**: Eliminated `provide_context=True` usage
- ✅ **Ensured Modern Airflow Compatibility**: All DAGs work with Airflow 2.8+

### **4. Configuration Optimization** ⚙️
- ✅ **Custom Port Configuration**: Avoided system conflicts
- ✅ **Environment Variables**: Proper `.env` file setup
- ✅ **Docker Integration**: Seamless container orchestration

---

## 🚀 Getting Started

### **Prerequisites**
- Windows 10/11 with WSL2 enabled
- Windows Package Manager (`winget`)
- Docker or Podman installed

### **Quick Start**
1. **Clone this repository**
   ```bash
   git clone <repository-url>
   cd airflow_ASTRO
   ```

2. **Start the Airflow environment**
   ```bash
   astro dev start
   ```

3. **Access the Airflow UI**
   - Open your browser to `http://localhost:8080`
   - Login with credentials: `admin` / `admin`

4. **Explore the DAGs**
   - Navigate to the main DAGs view
   - Enable and trigger the example DAGs

---

## 📊 DAGs in This Project

### **1. ML Pipeline (`mlpipeline.py`)** 🤖
```python
# Workflow: Data → Model → Evaluation
preprocess_data → train_model → evaluate_model
```
- **Purpose**: Demonstrates a typical ML workflow
- **Schedule**: Weekly (`@weekly`)
- **Tasks**: 3 sequential tasks representing ML pipeline stages

### **2. Mathematical Operations (`maths_operation.py`)** 🔢
```python
# Workflow: 10 → +5 → ×2 → -3 → ^2 = 529
start(10) → add_5(15) → multiply_by_2(30) → subtract_3(27) → square(729)
```
- **Purpose**: Shows XCom data passing between tasks
- **Schedule**: Run once (`@once`)
- **Tasks**: 5 chained mathematical operations

### **3. Example DAG (`exampledag.py`)** 📝
- **Purpose**: Template-generated example DAG
- **Features**: Demonstrates various Airflow concepts

---

## 🔍 Troubleshooting

### **Common Issues & Solutions**

#### **Port Conflicts**
```bash
# Error: Port 5432 already in use
# Solution: We've configured custom ports
POSTGRES_PORT=5433
AIRFLOW_WEBSERVER_PORT=8080
```

#### **Import Errors**
```python
# Old (deprecated):
from airflow.operators.python_operator import PythonOperator

# New (correct):
from airflow.operators.python import PythonOperator
```

#### **Schedule Parameter Issues**
```python
# Old (deprecated):
schedule_interval='@weekly'

# New (correct):
schedule='@weekly'
```

#### **Context Issues**
```python
# Old (deprecated):
PythonOperator(
    task_id='my_task',
    python_callable=my_function,
    provide_context=True  # Remove this line
)

# New (automatic):
PythonOperator(
    task_id='my_task',
    python_callable=my_function  # Context provided automatically
)
```
