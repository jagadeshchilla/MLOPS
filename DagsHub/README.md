# 🎯 DagsHub Demo - MLOps Platform Integration

> **A comprehensive demonstration of DagsHub integration for MLOps workflows, combining data versioning, experiment tracking, and collaborative ML development.**

- **Dags hub Repo**: [DagsHub Link](https://dagshub.com/jagadeshchilla/demodagshub)

## 📋 Table of Contents

- [🎯 What is DagsHub?](#-what-is-dagshub)
- [🚀 Getting Started](#-getting-started)
- [🔧 Setup Instructions](#-setup-instructions)
- [📊 Features Demonstrated](#-features-demonstrated)
- [🔄 Workflow Examples](#-workflow-examples)
- [💻 Commands Reference](#-commands-reference)
- [🤝 Collaboration Features](#-collaboration-features)
- [📈 Best Practices](#-best-practices)

## 🎯 What is DagsHub?

**DagsHub** is a platform built for machine learning teams that combines:

- **🗂️ Data Version Control** - Track datasets and models with DVC
- **🔬 Experiment Tracking** - Monitor ML experiments with MLflow
- **👥 Collaboration** - Git-based workflow for ML teams
- **📊 Visualization** - Built-in data and model visualization
- **🔄 Reproducibility** - Ensure consistent results across environments

### **Key Benefits:**
- **Centralized ML Platform** - One place for code, data, experiments, and models
- **GitHub Integration** - Familiar Git workflow with ML enhancements
- **Free for Open Source** - No cost for public repositories
- **Easy Setup** - Minimal configuration required
- **Team Collaboration** - Share datasets and experiments effortlessly

## 🚀 Getting Started

### **Prerequisites**
- Python 3.8+ installed
- Git configured with your credentials
- DagsHub account (free at [dagshub.com](https://dagshub.com))

### **Quick Setup**
1. **Create DagsHub Repository**
   ```bash
   # Visit https://dagshub.com and create a new repository
   # Or fork an existing ML project
   ```

2. **Clone Repository**
   ```bash
   git clone https://dagshub.com/your-username/your-repo.git
   cd your-repo
   ```

3. **Set up Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install Dependencies**
   ```bash
   pip install dvc mlflow dagshub
   ```

## 🔧 Setup Instructions

### **1. Initialize DVC**
```bash
# Initialize DVC in your project
dvc init

# Add DagsHub as remote storage
dvc remote add origin https://dagshub.com/your-username/your-repo.dvc
dvc remote default origin
```

### **2. Configure MLflow**
```bash
# Set MLflow tracking URI to DagsHub
export MLFLOW_TRACKING_URI=https://dagshub.com/your-username/your-repo.mlflow

# Or set in Python
import mlflow
mlflow.set_tracking_uri("https://dagshub.com/your-username/your-repo.mlflow")
```

### **3. Authentication Setup**
```bash
# Set DagsHub credentials
export DAGSHUB_USER_TOKEN=your-token-here

# Or configure Git credentials
git config --global credential.helper store
```

## 📊 Features Demonstrated

### **🗂️ Data Version Control**
- **Dataset Tracking**: Version large datasets efficiently
- **Data Pipeline**: Reproducible data processing workflows
- **Remote Storage**: Cloud-based data storage and sharing
- **Data Lineage**: Track data dependencies and transformations

### **🔬 Experiment Tracking**
- **Parameter Logging**: Track hyperparameters and configurations
- **Metrics Monitoring**: Log training and validation metrics
- **Artifact Storage**: Store models, plots, and other outputs
- **Experiment Comparison**: Compare multiple runs side-by-side

### **👥 Collaboration Features**
- **Shared Experiments**: Team access to all experiments
- **Data Sharing**: Centralized dataset management
- **Model Registry**: Collaborative model versioning
- **Discussion**: Comment and discuss experiments

## 🔄 Workflow Examples

### **Example 1: Data Versioning Workflow**
```bash
# Add dataset to DVC tracking
dvc add data/train.csv
git add data/train.csv.dvc .gitignore
git commit -m "Add training dataset"

# Push data to DagsHub
dvc push
git push origin main

# Team member pulls data
dvc pull  # Downloads the actual data files
```

### **Example 2: Experiment Tracking Workflow**
```python
import mlflow
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Set tracking URI
mlflow.set_tracking_uri("https://dagshub.com/username/repo.mlflow")

# Start experiment
with mlflow.start_run():
    # Log parameters
    mlflow.log_param("n_estimators", 100)
    mlflow.log_param("max_depth", 10)
    
    # Train model
    model = RandomForestClassifier(n_estimators=100, max_depth=10)
    model.fit(X_train, y_train)
    
    # Log metrics
    accuracy = accuracy_score(y_test, model.predict(X_test))
    mlflow.log_metric("accuracy", accuracy)
    
    # Log model
    mlflow.sklearn.log_model(model, "random_forest_model")
```

### **Example 3: Complete ML Pipeline**
```bash
# 1. Data preparation
dvc run -n prepare_data \
    -d data/raw.csv \
    -o data/processed.csv \
    python prepare_data.py

# 2. Model training
dvc run -n train_model \
    -d data/processed.csv \
    -d train.py \
    -o models/model.pkl \
    -M metrics.json \
    python train.py

# 3. Model evaluation
dvc run -n evaluate \
    -d models/model.pkl \
    -d data/test.csv \
    -M evaluation.json \
    python evaluate.py

# 4. Push pipeline to DagsHub
dvc push
git add dvc.yaml dvc.lock
git commit -m "Add ML pipeline"
git push origin main
```

## 💻 Commands Reference

### **DVC Commands**
```bash
# Basic DVC operations
dvc add data/dataset.csv        # Track file with DVC
dvc push                        # Upload data to remote
dvc pull                        # Download data from remote
dvc status                      # Check data status
dvc diff                        # Show data changes

# Pipeline operations
dvc dag                         # Show pipeline DAG
dvc repro                       # Reproduce pipeline
dvc metrics show                # Show metrics
dvc plots show                  # Show plots
```

### **MLflow Commands**
```bash
# MLflow operations
mlflow ui                       # Start local MLflow UI
mlflow experiments list         # List experiments
mlflow runs list               # List runs
mlflow models serve            # Serve model
```

### **Git + DagsHub Commands**
```bash
# Standard Git workflow
git add .
git commit -m "Update experiment"
git push origin main

# Check remote repositories
git remote -v
git log --oneline
```

## 🤝 Collaboration Features

### **🔄 Data Sharing**
- **Centralized Storage**: All team members access the same datasets
- **Version Control**: Track dataset changes over time
- **Access Control**: Manage permissions for sensitive data
- **Automatic Sync**: DVC handles data synchronization

### **📊 Experiment Sharing**
- **Shared Dashboard**: Team visibility into all experiments
- **Comparison Tools**: Compare experiments across team members
- **Model Registry**: Centralized model management
- **Annotations**: Add notes and comments to experiments

### **👥 Team Workflow**
1. **Data Scientist A** adds new dataset and trains model
2. **Data Scientist B** pulls data and experiments with different algorithms
3. **ML Engineer** compares all experiments and selects best model
4. **Team** collaborates on model improvements through shared experiments

## 🎯 Learning Outcomes

After completing this demo, you will understand:

- **DagsHub Platform**: How to use DagsHub for ML projects
- **Data Versioning**: Track and manage datasets with DVC
- **Experiment Tracking**: Monitor ML experiments with MLflow
- **Team Collaboration**: Work effectively with ML teams
- **MLOps Workflows**: Implement end-to-end ML pipelines
- **Best Practices**: Follow industry standards for ML development


## Support & Resources

- 📚 **DagsHub Documentation**: [docs.dagshub.com](https://docs.dagshub.com)
- 💬 **Community Forum**: [dagshub.com/community](https://dagshub.com/community)
- - **Dags hub Repo**: [DagsHub Link](https://dagshub.com/jagadeshchilla/demodagshub)
---

