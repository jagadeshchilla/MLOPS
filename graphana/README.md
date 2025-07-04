# Banking Data Generator with Grafana Integration

This project generates synthetic banking transaction data and stores it in a PostgreSQL database for visualization with Grafana.

## What is Grafana?

**Grafana** is an open-source analytics and interactive visualization web application. It provides charts, graphs, and alerts for the web when connected to supported data sources.

### Key Features of Grafana:
- **Data Visualization**: Create beautiful dashboards with various chart types (line graphs, bar charts, pie charts, heatmaps, etc.)
- **Multi-Data Source Support**: Connect to multiple databases (PostgreSQL, MySQL, MongoDB, InfluxDB, Prometheus, etc.)
- **Real-time Monitoring**: Display live data updates and streaming metrics
- **Alerting System**: Set up alerts based on data thresholds and conditions
- **Dashboard Sharing**: Share dashboards with teams and stakeholders
- **Customizable Panels**: Create custom visualizations tailored to your needs

### Uses of Grafana:
- **Business Intelligence**: Track KPIs, sales metrics, and business performance
- **Infrastructure Monitoring**: Monitor server performance, network traffic, and system health
- **Application Performance**: Track application metrics, response times, and error rates
- **Financial Analytics**: Visualize transaction data, fraud detection, and financial trends
- **IoT Data Visualization**: Display sensor data and IoT device metrics
- **Log Analysis**: Analyze and visualize log data from various sources

### Why Use Grafana for Banking Data?
In this project, Grafana helps visualize:
- **Transaction Patterns**: Identify trends in transaction volumes and amounts
- **Fraud Detection**: Monitor suspicious activities and rule triggers
- **Risk Assessment**: Track approval/rejection rates and risk indicators
- **Performance Metrics**: Analyze system performance and data processing rates
- **Compliance Reporting**: Generate reports for regulatory requirements

## Security Setup

### 🔒 Environment Variables Configuration

**IMPORTANT**: This project uses environment variables to protect sensitive database credentials. Never commit actual credentials to version control.

#### Setup Steps:

1. **Copy the environment template:**
   ```bash
   cp .env.example .env
   ```

2. **Edit the `.env` file with your actual database credentials:**
   ```bash
   # Database Configuration
   DB_HOST=your_actual_database_host
   DB_PORT=5432
   DB_NAME=your_database_name
   DB_USER=your_database_username
   DB_PASSWORD=your_secure_password
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   - Open `app.ipynb` in Jupyter Notebook
   - Execute the cells to start generating data

## Files Description

- `app.ipynb` - Main application notebook with secure database connections
- `queries.txt` - SQL queries for Grafana visualizations
- `requirements.txt` - Python dependencies
- `.env.example` - Template for environment variables
- `.gitignore` - Protects sensitive files from version control

## Security Features

✅ **Database credentials protected with environment variables**  
✅ **`.env` file excluded from version control**  
✅ **Connection error handling**  
✅ **Input validation for required variables**  

## Database Schema

The application creates a `banking_data` table with the following structure:
- Transaction metadata (timestamp, unique ID, type)
- Amount and currency information
- Account holder details
- Card information
- Merchant category
- Risk assessment (rules triggered, decision)

## Grafana Queries

Use the queries in `queries.txt` to create visualizations in Grafana:
- Transaction approval/rejection statistics
- Transaction type distribution
- Rules triggered analysis
- Blacklisted account monitoring

## ⚠️ Security Warning

- Never commit `.env` files to version control
- Use strong passwords for database connections
- Regularly rotate database credentials
- Monitor access logs for suspicious activity 