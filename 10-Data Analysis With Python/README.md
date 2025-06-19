# 📊 Module 10: Data Analysis With Python

![Python](https://img.shields.io/badge/Python-Data%20Analysis-brightgreen?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge)
![Difficulty](https://img.shields.io/badge/Difficulty-Intermediate-orange?style=for-the-badge)

## 📖 Overview

This module introduces you to the powerful world of data analysis using Python's most popular libraries: NumPy, Pandas, Matplotlib, and Seaborn. You'll learn to manipulate, analyze, and visualize data effectively.

## 🎯 Learning Objectives

By the end of this module, you will:
- ✅ Master NumPy for numerical computations and arrays
- ✅ Use Pandas for data manipulation and analysis
- ✅ Create visualizations with Matplotlib and Seaborn
- ✅ Read and write data from various file formats
- ✅ Perform exploratory data analysis (EDA)
- ✅ Clean and transform real-world datasets

## 📂 Module Contents

| File | Description | Library Focus |
|------|-------------|---------------|
| `10.1-numpy.ipynb` | NumPy fundamentals | Arrays, mathematical operations |
| `10.2-pandas.ipynb` | Pandas basics | DataFrames, Series |
| `10.3-datamanipulation.ipynb` | Data transformation | Filtering, grouping, merging |
| `10.4-readdata.ipynb` | File I/O operations | CSV, Excel, JSON reading |
| `10.5-matplotlib.ipynb` | Data visualization | Plots, charts, customization |
| `10.6-seaborn.ipynb` | Statistical visualization | Advanced plotting |
| `numpyassignments.ipynb` | NumPy practice | Hands-on exercises |
| `numpysolutions.ipynb` | NumPy solutions | Reference answers |
| `pandasasssignments.ipynb` | Pandas practice | Data manipulation exercises |
| `pandassolution.ipynb` | Pandas solutions | Reference answers |

### 📁 Data Files
| File | Description | Format |
|------|-------------|--------|
| `data.csv` | Sample dataset | CSV |
| `sales_data.csv` | Sales records | CSV |
| `sales1_data.csv` | Additional sales data | CSV |
| `wine.csv` | Wine quality dataset | CSV |
| `data.xlsx` | Excel sample | Excel |
| `sample_data.xlsx` | Excel dataset | Excel |

## 🚀 Quick Start

### Prerequisites
- Completion of Python fundamentals (Modules 1-9)
- Basic understanding of mathematics and statistics

### Installation
```bash
pip install numpy pandas matplotlib seaborn openpyxl
```

### Running the Notebooks
```bash
# Navigate to this directory
cd "10-Data Analysis With Python"

# Start Jupyter Lab
jupyter lab

# Or start Jupyter Notebook
jupyter notebook
```

## 📚 Detailed Content Guide

### 🔢 NumPy (`10.1-numpy.ipynb`)

**NumPy** is the foundation of scientific computing in Python.

```python
import numpy as np

# Creating arrays
arr1d = np.array([1, 2, 3, 4, 5])
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
zeros = np.zeros((3, 4))
ones = np.ones((2, 3))
random_array = np.random.rand(3, 3)

# Array operations
result = arr1d * 2              # Element-wise multiplication
math_ops = np.sqrt(arr1d)       # Mathematical functions
aggregations = np.sum(arr2d, axis=0)  # Sum along axis

# Indexing and slicing
subset = arr1d[1:4]             # Slicing
filtered = arr1d[arr1d > 3]     # Boolean indexing
```

**Key NumPy Features:**
- **N-dimensional arrays**: Efficient storage and computation
- **Broadcasting**: Operations on arrays of different shapes
- **Mathematical functions**: Trigonometry, statistics, linear algebra
- **Performance**: Vectorized operations are much faster than loops

### 🐼 Pandas (`10.2-pandas.ipynb`)

**Pandas** provides high-level data structures and analysis tools.

```python
import pandas as pd

# Creating DataFrames
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Tokyo']
})

# Reading data
df_csv = pd.read_csv('data.csv')
df_excel = pd.read_excel('data.xlsx')

# Basic operations
print(df.head())                # First 5 rows
print(df.info())                # Data types and info
print(df.describe())            # Statistical summary

# Data selection
names = df['Name']              # Select column
subset = df[df['Age'] > 25]     # Filter rows
specific = df.loc[0, 'Name']    # Select specific cell
```

### 🔄 Data Manipulation (`10.3-datamanipulation.ipynb`)

```python
# Data cleaning
df.dropna()                     # Remove missing values
df.fillna(0)                    # Fill missing values
df.drop_duplicates()            # Remove duplicates

# Data transformation
df['Age_Group'] = df['Age'].apply(lambda x: 'Young' if x < 30 else 'Old')
df_grouped = df.groupby('City').mean()  # Group by and aggregate

# Merging DataFrames
merged = pd.merge(df1, df2, on='common_column')
concatenated = pd.concat([df1, df2])
```

### 📁 Reading Data (`10.4-readdata.ipynb`)

```python
# CSV files
df_csv = pd.read_csv('sales_data.csv')
df_csv.to_csv('output.csv', index=False)

# Excel files
df_excel = pd.read_excel('sample_data.xlsx', sheet_name='Sheet1')
df_excel.to_excel('output.xlsx', index=False)

# JSON files
df_json = pd.read_json('data.json')
df_json.to_json('output.json')

# Database connections
import sqlite3
conn = sqlite3.connect('database.db')
df_db = pd.read_sql_query("SELECT * FROM table", conn)
```

### 📈 Matplotlib (`10.5-matplotlib.ipynb`)

**Matplotlib** is the fundamental plotting library.

```python
import matplotlib.pyplot as plt

# Basic plots
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Line Plot')
plt.scatter(x, y, label='Scatter Plot')
plt.bar(categories, values, label='Bar Plot')
plt.hist(data, bins=20, label='Histogram')

# Customization
plt.title('My Plot')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.legend()
plt.grid(True)
plt.show()

# Subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes[0, 0].plot(x, y)
axes[0, 1].scatter(x, y)
axes[1, 0].bar(categories, values)
axes[1, 1].hist(data)
```

### 🎨 Seaborn (`10.6-seaborn.ipynb`)

**Seaborn** provides beautiful statistical visualizations.

```python
import seaborn as sns

# Set style
sns.set_style("whitegrid")
sns.set_palette("husl")

# Statistical plots
sns.histplot(df, x='column', hue='category')
sns.boxplot(data=df, x='category', y='value')
sns.scatterplot(data=df, x='x_col', y='y_col', hue='category')
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')

# Relationship plots
sns.pairplot(df, hue='category')
sns.regplot(data=df, x='x_col', y='y_col')

# Distribution plots
sns.violinplot(data=df, x='category', y='value')
sns.distplot(df['column'])
```

## 💻 Practice Exercises

### Exercise 1: Sales Analysis
```python
# Load and analyze sales data
sales_df = pd.read_csv('sales_data.csv')

# Basic statistics
print("Total sales:", sales_df['amount'].sum())
print("Average sale:", sales_df['amount'].mean())
print("Top products:", sales_df['product'].value_counts().head())

# Time series analysis
sales_df['date'] = pd.to_datetime(sales_df['date'])
monthly_sales = sales_df.groupby(sales_df['date'].dt.month)['amount'].sum()

# Visualization
plt.figure(figsize=(10, 6))
monthly_sales.plot(kind='bar')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales Amount')
plt.show()
```

### Exercise 2: Wine Quality Analysis
```python
# Load wine dataset
wine_df = pd.read_csv('wine.csv')

# Exploratory data analysis
print(wine_df.info())
print(wine_df.describe())

# Correlation analysis
correlation = wine_df.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(correlation, annot=True, cmap='coolwarm', center=0)
plt.title('Wine Features Correlation')
plt.show()

# Quality distribution
plt.figure(figsize=(8, 6))
sns.countplot(data=wine_df, x='quality')
plt.title('Wine Quality Distribution')
plt.show()
```

## 🧪 Hands-On Activities

1. **Complete NumPy assignments**: Master array operations
2. **Work through Pandas exercises**: Practice data manipulation
3. **Create visualizations**: Use both Matplotlib and Seaborn
4. **Analyze real datasets**: Apply all learned techniques
5. **Build a data analysis pipeline**: From raw data to insights

## 🔍 Key Concepts to Remember

### NumPy Best Practices
- **Vectorization**: Use NumPy operations instead of loops
- **Memory efficiency**: NumPy arrays use less memory than lists
- **Broadcasting**: Understand how operations work on different shapes
- **Data types**: Choose appropriate dtypes for memory optimization

### Pandas Best Practices
- **Method chaining**: Chain operations for cleaner code
- **Categorical data**: Use categorical dtype for memory efficiency
- **Index usage**: Leverage indexing for faster operations
- **Memory optimization**: Use appropriate data types

### Visualization Best Practices
- **Clear titles and labels**: Make plots self-explanatory
- **Appropriate chart types**: Choose the right visualization for your data
- **Color usage**: Use colors meaningfully
- **Simplicity**: Don't overcomplicate visualizations

## 🌟 Essential Libraries Comparison

| Library | Primary Use | Strengths |
|---------|-------------|-----------|
| **NumPy** | Numerical computing | Speed, memory efficiency, mathematical functions |
| **Pandas** | Data manipulation | Intuitive API, data structures, file I/O |
| **Matplotlib** | Basic plotting | Flexibility, customization, publication-quality |
| **Seaborn** | Statistical plots | Beautiful defaults, statistical functions |

## 🎯 Common Data Analysis Workflow

1. **Data Collection**: Import data from various sources
2. **Data Cleaning**: Handle missing values, duplicates, outliers
3. **Exploratory Data Analysis**: Understand data distribution and patterns
4. **Data Transformation**: Create new features, normalize data
5. **Analysis**: Apply statistical methods and algorithms
6. **Visualization**: Create meaningful charts and graphs
7. **Insights**: Draw conclusions and make recommendations

## 🔗 What's Next?

After mastering data analysis, you're ready to move to:
- **Module 11**: Working with Databases (Data storage and retrieval)
- **Module 12**: Logging (Production-ready code practices)
- **MLflow**: Experiment tracking and model management

## 📝 Assignment Checklist

- [ ] Master NumPy array operations
- [ ] Understand Pandas DataFrames and Series
- [ ] Create various types of visualizations
- [ ] Read data from different file formats
- [ ] Perform data cleaning and transformation
- [ ] Complete all practice assignments
- [ ] Analyze at least one real dataset

## 🆘 Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| `MemoryError` with large datasets | Use chunking or more efficient data types |
| Plots not showing | Add `plt.show()` or use `%matplotlib inline` |
| Pandas `KeyError` | Check column names and spelling |
| NumPy shape mismatch | Understand broadcasting rules |
| Excel reading errors | Install `openpyxl`: `pip install openpyxl` |

## 🏆 Real-World Projects

1. **Sales Dashboard**: Comprehensive sales analysis with visualizations
2. **Stock Market Analysis**: Time series analysis and prediction
3. **Customer Segmentation**: Clustering analysis using data science techniques
4. **A/B Testing Analysis**: Statistical testing and comparison
5. **Social Media Analytics**: Text and engagement data analysis

---

**Data is the New Oil! ⛽**

*Master these data analysis tools, and you'll be able to extract valuable insights from any dataset!* 