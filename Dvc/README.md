# 📊 DVC: Data Version Control

![DVC](https://img.shields.io/badge/DVC-Data%20Version%20Control-blue?style=for-the-badge&logo=dvc&logoColor=white)
![MLOps](https://img.shields.io/badge/MLOps-Data%20Pipeline-green?style=for-the-badge)
![Difficulty](https://img.shields.io/badge/Difficulty-Advanced-red?style=for-the-badge)

## 📖 Overview

This module introduces Data Version Control (DVC), an essential tool for MLOps workflows. Learn to version datasets, track experiments, build reproducible pipelines, and collaborate effectively on machine learning projects.

## 🎯 Learning Objectives

By the end of this module, you will:
- ✅ Understand the importance of data versioning in ML projects
- ✅ Set up and configure DVC for your projects
- ✅ Track large datasets and model files
- ✅ Create reproducible data pipelines
- ✅ Collaborate on ML projects with version control
- ✅ Integrate DVC with Git and remote storage

## 🔧 What is DVC?

**DVC (Data Version Control)** is an open-source tool that helps you:

- **Version large datasets** and ML models alongside your code
- **Create reproducible ML pipelines** with dependency tracking
- **Share data efficiently** across team members
- **Track experiments** and compare results
- **Integrate with Git** for complete project versioning

## 🚀 Installation and Setup

### Prerequisites
- Git installed and configured
- Python 3.8+ with pip
- Basic understanding of command line

### Installation

```bash
# Install DVC
pip install dvc

# Install with specific remote storage support
pip install 'dvc[s3]'      # For AWS S3
pip install 'dvc[azure]'   # For Azure Blob Storage
pip install 'dvc[gdrive]'  # For Google Drive
pip install 'dvc[gs]'      # For Google Cloud Storage

# Or install all remote storage support
pip install 'dvc[all]'
```

### Initialize DVC in Your Project

```bash
# Initialize Git repository (if not already done)
git init

# Initialize DVC
dvc init

# Check DVC status
dvc status
```

## 📚 Core DVC Concepts

### 🔹 DVC Files and Tracking
```bash
# Add data to DVC tracking
dvc add data/dataset.csv

# This creates:
# - data/dataset.csv.dvc (metadata file tracked by Git)
# - Updates .gitignore to ignore the actual data file

# Commit the .dvc file to Git
git add data/dataset.csv.dvc .gitignore
git commit -m "Add dataset to DVC tracking"
```

### 🔹 Remote Storage Configuration
```bash
# Add remote storage (example with local directory)
dvc remote add -d myremote /path/to/remote/storage

# For cloud storage
dvc remote add -d s3remote s3://my-bucket/dvc-storage
dvc remote add -d gcs_remote gs://my-bucket/dvc-storage

# Push data to remote storage
dvc push

# Pull data from remote storage
dvc pull
```

### 🔹 Data Pipeline Creation
```bash
# Create a pipeline stage
dvc stage add -n prepare \
  -d data/raw_data.csv \
  -o data/prepared_data.csv \
  python scripts/prepare_data.py

# Add training stage
dvc stage add -n train \
  -d data/prepared_data.csv \
  -d scripts/train_model.py \
  -o models/model.pkl \
  -m metrics/train_metrics.json \
  python scripts/train_model.py

# Run the pipeline
dvc repro
```

## 💻 Practical Examples

### Example 1: Basic Data Tracking
```bash
# Project structure
mkdir ml_project
cd ml_project

# Initialize Git and DVC
git init
dvc init

# Create sample data
mkdir data
echo "feature1,feature2,target" > data/dataset.csv
echo "1,2,0" >> data/dataset.csv
echo "3,4,1" >> data/dataset.csv

# Track the dataset
dvc add data/dataset.csv

# Commit to Git
git add data/dataset.csv.dvc .gitignore .dvc/
git commit -m "Initialize project with dataset"

# Check status
dvc status
git status
```

### Example 2: Data Pipeline with Python Scripts

**scripts/prepare_data.py**
```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import yaml
import os

def prepare_data():
    """Prepare data for training."""
    
    # Load parameters
    with open('params.yaml', 'r') as f:
        params = yaml.safe_load(f)
    
    # Load raw data
    df = pd.read_csv('data/raw_data.csv')
    
    # Feature engineering
    df['feature_interaction'] = df['feature1'] * df['feature2']
    df['feature_ratio'] = df['feature1'] / (df['feature2'] + 1e-6)
    
    # Split features and target
    X = df.drop('target', axis=1)
    y = df['target']
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, 
        test_size=params['data']['test_size'], 
        random_state=params['data']['random_state']
    )
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Create output directory
    os.makedirs('data/processed', exist_ok=True)
    
    # Save processed data
    np.save('data/processed/X_train.npy', X_train_scaled)
    np.save('data/processed/X_test.npy', X_test_scaled)
    np.save('data/processed/y_train.npy', y_train)
    np.save('data/processed/y_test.npy', y_test)
    
    # Save scaler
    import joblib
    os.makedirs('models', exist_ok=True)
    joblib.dump(scaler, 'models/scaler.pkl')
    
    print(f"Data prepared: {len(X_train)} train samples, {len(X_test)} test samples")

if __name__ == "__main__":
    prepare_data()
```

**scripts/train_model.py**
```python
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import json
import yaml
import os

def train_model():
    """Train machine learning model."""
    
    # Load parameters
    with open('params.yaml', 'r') as f:
        params = yaml.safe_load(f)
    
    # Load processed data
    X_train = np.load('data/processed/X_train.npy')
    X_test = np.load('data/processed/X_test.npy')
    y_train = np.load('data/processed/y_train.npy')
    y_test = np.load('data/processed/y_test.npy')
    
    # Initialize model
    model = RandomForestClassifier(
        n_estimators=params['model']['n_estimators'],
        max_depth=params['model']['max_depth'],
        random_state=params['model']['random_state']
    )
    
    # Train model
    model.fit(X_train, y_train)
    
    # Make predictions
    train_pred = model.predict(X_train)
    test_pred = model.predict(X_test)
    
    # Calculate metrics
    train_accuracy = accuracy_score(y_train, train_pred)
    test_accuracy = accuracy_score(y_test, test_pred)
    
    # Save metrics
    metrics = {
        'train_accuracy': float(train_accuracy),
        'test_accuracy': float(test_accuracy),
        'model_params': params['model']
    }
    
    os.makedirs('metrics', exist_ok=True)
    with open('metrics/train_metrics.json', 'w') as f:
        json.dump(metrics, f, indent=2)
    
    # Save model
    joblib.dump(model, 'models/model.pkl')
    
    print(f"Model trained - Train Acc: {train_accuracy:.4f}, Test Acc: {test_accuracy:.4f}")

if __name__ == "__main__":
    train_model()
```

**params.yaml**
```yaml
data:
  test_size: 0.2
  random_state: 42

model:
  n_estimators: 100
  max_depth: 10
  random_state: 42

evaluate:
  metrics_file: metrics/eval_metrics.json
```

**dvc.yaml** (Pipeline Definition)
```yaml
stages:
  prepare_data:
    cmd: python scripts/prepare_data.py
    deps:
    - data/raw_data.csv
    - scripts/prepare_data.py
    params:
    - data.test_size
    - data.random_state
    outs:
    - data/processed/X_train.npy
    - data/processed/X_test.npy
    - data/processed/y_train.npy
    - data/processed/y_test.npy
    - models/scaler.pkl

  train_model:
    cmd: python scripts/train_model.py
    deps:
    - data/processed/X_train.npy
    - data/processed/X_test.npy
    - data/processed/y_train.npy
    - data/processed/y_test.npy
    - scripts/train_model.py
    params:
    - model
    outs:
    - models/model.pkl
    metrics:
    - metrics/train_metrics.json
```

### Example 3: Experiment Tracking and Comparison
```bash
# Run initial experiment
dvc repro

# Commit results
git add dvc.yaml dvc.lock metrics/train_metrics.json
git commit -m "Initial model training"
git tag -a "v1.0" -m "First model version"

# Modify parameters for new experiment
# Edit params.yaml to change model parameters

# Run new experiment
dvc repro

# Compare experiments
dvc metrics show
dvc metrics diff v1.0

# Compare multiple experiments
dvc plots show metrics/train_metrics.json
```

## 🛠️ Advanced DVC Features

### 🔹 Data Registry Pattern
```bash
# Create data registry repository
git init data-registry
cd data-registry
dvc init

# Add datasets to registry
dvc add datasets/customer_data_v1.csv
dvc add datasets/product_catalog_v2.json

# Import data in ML project
cd ../ml-project
dvc import ../data-registry datasets/customer_data_v1.csv data/
```

### 🔹 Checkpoints for Iterative Training
```python
# scripts/train_iterative.py
import dvc.api

def train_with_checkpoints():
    """Training with DVC checkpoints."""
    
    for epoch in range(100):
        # Training logic here
        train_model_one_epoch()
        
        # Save checkpoint
        if epoch % 10 == 0:
            save_checkpoint(f'checkpoints/epoch_{epoch}')
            
            # Create DVC checkpoint
            with dvc.api.make_checkpoint():
                pass
```

### 🔹 Multi-Stage Pipeline with Dependencies
```yaml
# Advanced pipeline in dvc.yaml
stages:
  data_validation:
    cmd: python scripts/validate_data.py
    deps:
    - data/raw_data.csv
    - scripts/validate_data.py
    outs:
    - reports/data_validation.html

  feature_engineering:
    cmd: python scripts/feature_engineering.py
    deps:
    - data/raw_data.csv
    - scripts/feature_engineering.py
    - reports/data_validation.html
    params:
    - feature_engineering
    outs:
    - data/features.csv

  model_training:
    cmd: python scripts/train_model.py
    deps:
    - data/features.csv
    - scripts/train_model.py
    params:
    - model
    outs:
    - models/model.pkl
    metrics:
    - metrics/train_metrics.json

  model_evaluation:
    cmd: python scripts/evaluate_model.py
    deps:
    - models/model.pkl
    - data/features.csv
    - scripts/evaluate_model.py
    metrics:
    - metrics/eval_metrics.json
    plots:
    - plots/confusion_matrix.png
    - plots/roc_curve.png
```

## 🔄 Integration with MLOps Tools

### 🔹 DVC + MLflow Integration
```python
import mlflow
import dvc.api
import yaml

def train_with_mlflow_dvc():
    """Integrate DVC with MLflow for complete tracking."""
    
    # Load parameters from DVC
    params = dvc.api.params_show()
    
    with mlflow.start_run():
        # Log parameters
        mlflow.log_params(params['model'])
        
        # Train model (your training code here)
        model = train_model(params)
        
        # Log metrics
        metrics = evaluate_model(model)
        mlflow.log_metrics(metrics)
        
        # Log model
        mlflow.sklearn.log_model(model, "model")
        
        # Save DVC metrics
        with open('metrics/mlflow_metrics.json', 'w') as f:
            json.dump(metrics, f)
```

### 🔹 CI/CD Pipeline with DVC
```yaml
# .github/workflows/ml-pipeline.yml
name: ML Pipeline

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  ml-pipeline:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.8
    
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
    
    - name: Configure DVC
      run: |
        dvc remote modify origin --local auth basic
        dvc remote modify origin --local user ${{ secrets.DVC_USER }}
        dvc remote modify origin --local password ${{ secrets.DVC_PASS }}
    
    - name: Pull data
      run: dvc pull
    
    - name: Run pipeline
      run: dvc repro
    
    - name: Check metrics
      run: |
        dvc metrics show
        dvc plots show
```

## 🧪 Hands-On Activities

1. **Version a dataset**: Practice with different data versions
2. **Build ML pipeline**: Create complete training pipeline
3. **Experiment tracking**: Compare multiple model versions
4. **Team collaboration**: Share data across team members

## 🔍 Key Commands Reference

```bash
# Basic Operations
dvc init                    # Initialize DVC
dvc add <file>             # Track file with DVC
dvc push                   # Push data to remote
dvc pull                   # Pull data from remote
dvc status                 # Check DVC status

# Pipeline Operations
dvc stage add              # Add pipeline stage
dvc repro                  # Reproduce pipeline
dvc dag                    # Show pipeline DAG
dvc pipeline show          # Show pipeline details

# Data Management
dvc import <url> <path>    # Import data from another DVC repo
dvc update <file.dvc>      # Update imported data
dvc checkout               # Checkout DVC files
dvc fetch                  # Fetch data from remote

# Experiment Tracking
dvc metrics show           # Show metrics
dvc metrics diff           # Compare metrics
dvc plots show             # Show plots
dvc plots diff             # Compare plots

# Remote Management
dvc remote add             # Add remote storage
dvc remote list            # List remotes
dvc remote modify          # Modify remote settings
```

## 🌟 Best Practices

1. **Structure your project**: Organize data, scripts, and outputs clearly
2. **Use parameters**: Keep hyperparameters in separate YAML files
3. **Version everything**: Track data, code, and model versions together
4. **Small commits**: Make frequent, small commits for better tracking
5. **Document pipelines**: Add clear descriptions to pipeline stages
6. **Remote storage**: Always use remote storage for team collaboration

## 📝 Assignment Checklist

- [ ] Set up DVC in a new project
- [ ] Track datasets with DVC
- [ ] Configure remote storage
- [ ] Create a data processing pipeline
- [ ] Track model training experiments
- [ ] Compare different model versions
- [ ] Integrate with Git workflow
- [ ] Collaborate on a team project

## 🆘 Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| `dvc pull` fails | Check remote configuration and credentials |
| Pipeline not reproducing | Verify dependencies and parameters are correct |
| Large files in Git | Ensure `.gitignore` is properly configured |
| Remote access denied | Check permissions and authentication |
| Pipeline stages skipped | Check if outputs already exist and are up-to-date |

## 🏆 Challenge Projects

1. **Complete MLOps Pipeline**: End-to-end ML project with DVC
2. **Multi-Team Data Sharing**: Data registry for multiple teams
3. **A/B Testing Framework**: Compare model versions systematically
4. **Automated Retraining**: Pipeline that triggers on data changes
5. **Model Deployment Pipeline**: Production deployment with version control

---

**DVC: Your Data Needs Version Control Too! 📊**

*Master DVC to build reproducible, collaborative, and scalable ML workflows!* 