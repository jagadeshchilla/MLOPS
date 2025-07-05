# 📱 Mobile Price Classification with AWS SageMaker
> A complete machine learning pipeline for mobile phone price classification using AWS SageMaker, achieving 88.33% accuracy with Random Forest classifier.

## 🎯 Project Overview

This project demonstrates a complete end-to-end machine learning workflow on AWS SageMaker for classifying mobile phones into price ranges based on their technical specifications. The solution includes data preprocessing, model training, deployment, and inference capabilities.

### 🔍 What We Built

- **📊 Data Pipeline**: Automated data preprocessing and feature engineering
- **🤖 ML Model**: Random Forest classifier with 88.33% accuracy
- **☁️ Cloud Training**: Distributed training on AWS SageMaker
- **🚀 Model Deployment**: Real-time inference endpoints
- **🔒 Security**: Secure credential management and IAM role configuration

### 📈 Key Results

| Metric | Value |
|--------|-------|
| **Accuracy** | 88.33% |
| **Training Time** | ~2 minutes |
| **Model Size** | Optimized for inference |
| **Price Range 0** | 95% precision, 100% recall |
| **Price Range 3** | 91% precision, 95% recall |

##  Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Data Source   │───▶│   S3 Bucket     │───▶│  SageMaker      │
│                 │    │                 │    │  Training       │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                                        │
                                                        ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Inference     │◀───│   Endpoint      │◀───│   Model         │
│   Results       │    │   Deployment    │    │   Artifacts     │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- AWS Account with SageMaker permissions
- Python 3.10+
- AWS CLI configured
- Jupyter Notebook environment

### 1. Clone and Setup

```bash
git clone <your-repo-url>
cd awssagemaker
pip install -r requirements.txt
```

### 2. Configure AWS Credentials

```bash
aws configure
```

### 3. Run the Notebook

```bash
jupyter notebook research.ipynb
```

## 📋 Dataset

The dataset contains **2,000 mobile phone records** with **21 features**:

| Feature | Description | Type |
|---------|-------------|------|
| `battery_power` | Battery capacity (mAh) | Numeric |
| `blue` | Bluetooth support | Binary |
| `clock_speed` | Processor speed (GHz) | Numeric |
| `dual_sim` | Dual SIM support | Binary |
| `fc` | Front camera megapixels | Numeric |
| `four_g` | 4G support | Binary |
| `int_memory` | Internal memory (GB) | Numeric |
| `ram` | RAM (MB) | Numeric |
| `price_range` | **Target**: 0-3 (Low to High) | Categorical |

### 📊 Data Distribution

- **Balanced Dataset**: 500 samples per price range
- **No Missing Values**: Complete dataset
- **Feature Range**: Mixed numeric and binary features

## 🔧 Implementation Details

### Model Architecture

```python
RandomForestClassifier(
    n_estimators=100,
    random_state=0,
    verbose=2
)
```

### Training Configuration

- **Instance Type**: `ml.m5.large`
- **Framework**: scikit-learn 0.23-1
- **Spot Instances**: Enabled for cost optimization
- **Training Time**: ~100 seconds

### Security Features

- ✅ **No Hardcoded Credentials**: Uses AWS profile configuration
- ✅ **IAM Role Management**: Automatic role detection
- ✅ **Default S3 Bucket**: Managed bucket creation
- ✅ **Environment Detection**: Adapts to different execution contexts

## 🎯 Performance Metrics

### Classification Report

```
              precision    recall  f1-score   support
           0       0.95      1.00      0.97        69
           1       0.85      0.80      0.83        66
           2       0.80      0.77      0.79        74
           3       0.91      0.95      0.93        91

    accuracy                           0.88       300
   macro avg       0.88      0.88      0.88       300
weighted avg       0.88      0.88      0.88       300
```

### Feature Importance

The model identifies key factors affecting mobile phone pricing:
- RAM capacity
- Battery power
- Internal memory
- Camera specifications

## 🛠️ AWS SageMaker Setup Guide

### Step 1: Create SageMaker Execution Role

1. **Navigate to IAM Console**
   ```
   AWS Console → IAM → Roles → Create Role
   ```

2. **Select SageMaker Service**
   - Choose "SageMaker" as the service
   - Select "SageMaker - Execution"

3. **Attach Policies**
   ```
   - AmazonSageMakerFullAccess
   - AmazonS3FullAccess (or specific bucket permissions)
   ```

4. **Name Your Role**
   ```
   Role Name: SageMakerExecutionRole
   ```

### Step 2: Configure SageMaker Domain (Optional)

```bash
# Create SageMaker domain for Studio
aws sagemaker create-domain \
    --domain-name "mobile-price-classification" \
    --auth-mode "IAM" \
    --default-user-settings ExecutionRole=arn:aws:iam::YOUR_ACCOUNT:role/SageMakerExecutionRole
```

### Step 3: Launch SageMaker Studio

1. **Open SageMaker Console**
2. **Launch Studio**
3. **Upload Notebook**
4. **Run the Pipeline**

### Step 4: Monitor Training Jobs

```python
# View training jobs
import boto3
sm = boto3.client('sagemaker')
sm.list_training_jobs()
```

## 📁 Project Structure

```
awssagemaker/
├── 📓 research.ipynb              # Main notebook
├── 📄 script.py                   # Training script
├── 📊 mob_price_classification_train.csv  # Dataset
├── 📋 requirements.txt            # Dependencies
├── 📝 README.md                   # This file
├── 🗂️ train-V-1.csv              # Generated training data
├── 🗂️ test-V-1.csv               # Generated test data
└── 📁 venv/                       # Virtual environment
```

## 🔍 Key Features

### 🎯 **End-to-End Pipeline**
- Data preprocessing and feature engineering
- Automated model training and evaluation
- Model deployment and inference

### ☁️ **Cloud-Native Architecture**
- AWS SageMaker training jobs
- S3 data storage and management
- Scalable inference endpoints

### 🔒 **Security Best Practices**
- IAM role-based access control
- No hardcoded credentials
- Secure data transmission

### 💰 **Cost Optimization**
- Spot instance utilization
- Automatic resource cleanup
- Efficient data storage

## 🚀 Deployment Options

### 1. Real-time Inference
```python
# Deploy model endpoint
predictor = model.deploy(
    initial_instance_count=1,
    instance_type="ml.m4.xlarge"
)
```

### 2. Batch Transform
```python
# Batch predictions
transformer = model.transformer(
    instance_count=1,
    instance_type="ml.m4.xlarge"
)
```

### 3. Serverless Inference
```python
# Serverless endpoint
predictor = model.deploy(
    serverless_inference_config=ServerlessInferenceConfig()
)
```

## 📊 Monitoring and Logging

### CloudWatch Integration
- Training job metrics
- Endpoint performance monitoring
- Cost tracking and alerts

### Model Monitoring
- Data drift detection
- Model performance tracking
- Automated retraining triggers

## 🎓 Learning Outcomes

After completing this project, you'll understand:

- **AWS SageMaker**: Complete ML workflow on cloud
- **MLOps**: Production-ready model deployment
- **Security**: AWS credential and permission management
- **Scalability**: Cloud-native ML architecture
- ✅**Cost Management**: Optimizing AWS resources

### Common Issues

1. **Permission Errors**
   ```bash
   # Check IAM role permissions
   aws iam get-role --role-name SageMakerExecutionRole
   ```

2. **Training Job Failures**
   ```python
   # Check training job logs
   sm.describe_training_job(TrainingJobName='job-name')
   ```

3. **Endpoint Deployment Issues**
   ```python
   # Monitor endpoint status
   sm.describe_endpoint(EndpointName='endpoint-name')
   ```

## 📚 Additional Resources

- [AWS SageMaker Documentation](https://docs.aws.amazon.com/sagemaker/)
- [SageMaker Python SDK](https://sagemaker.readthedocs.io/)
- [AWS ML Blog](https://aws.amazon.com/blogs/machine-learning/)
- [SageMaker Examples](https://github.com/aws/amazon-sagemaker-examples)

---

