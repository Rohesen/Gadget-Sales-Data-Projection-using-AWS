# 📊 Gadget Sales Data Projection using DynamoDB CDC Events

![AWS](https://img.shields.io/badge/AWS-DynamoDB-orange?logo=amazon-aws)
![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## 🚀 Project Overview

This project demonstrates a **real-time Change Data Capture (CDC) pipeline** for analyzing gadget sales data.
It captures data changes from **DynamoDB**, streams them through **EventBridge Pipe → Kinesis Firehose → Lambda**, stores transformed data in **S3**, and makes it queryable via **AWS Glue + Athena**.

---

## ⚙️ Architecture

```mermaid
flowchart LR
    A[Mock Data Generator (Python)] --> B[DynamoDB OrdersRawTable]
    B --> C[EventBridge Pipe]
    C --> D[Kinesis Firehose]
    D --> E[Lambda Transformation Layer]
    E --> F[S3 Bucket]
    F --> G[Glue Crawler + Data Catalog]
    G --> H[Athena Queries]
```

---

## 📂 Project Structure

```
📦 gadget-sales-cdc-pipeline
 ┣ 📜 mock_data_generator_for_dynamodb.py   # Python script to generate mock data
 ┣ 📜 transformation_layer_with_lambda.py   # Lambda transformation function
 ┣ 📂 screenshots/                          # Athena + S3 screenshots
 ┣ 📜 README.md                             # Documentation
```

---

## 📝 Setup Instructions

### 1️⃣ Prerequisites

* AWS Account with DynamoDB, EventBridge, Kinesis, Lambda, S3, Glue, Athena access.
* Python 3.9+ installed with `boto3`.

### 2️⃣ Clone Repository

```bash
git clone https://github.com/Rohesen/gadget-sales-cdc-pipeline.git
cd gadget-sales-cdc-pipeline
```

### 3️⃣ Configure AWS CLI

```bash
aws configure
```

### 4️⃣ Run Mock Data Generator

This script continuously inserts random order data into DynamoDB.

```bash
python mock_data_generator_for_dynamodb.py
```

### 5️⃣ Lambda Transformation

Deploy `transformation_layer_with_lambda.py` as a Lambda function.
Attach it to **Kinesis Firehose** as a transformation step.

### 6️⃣ S3 + Glue

* Firehose delivers transformed data to S3 bucket: `kinesis-firehose-destination-rohes`.
* Glue Crawler scans S3 and creates a table in `glue_sales_db`.

### 7️⃣ Query with Athena

```sql
SELECT * 
FROM kinesis_firehose_destination_rohes
LIMIT 10;
```

---

## 📸 Screenshots

* Athena Query Results
* S3 Bucket JSON Files

(See `/screenshots/` folder)

---

## 🧑‍💻 Tech Stack

* **AWS DynamoDB** – CDC Source
* **AWS EventBridge Pipe** – CDC Event Trigger
* **AWS Kinesis Firehose** – Stream Delivery
* **AWS Lambda** – Data Transformation
* **AWS S3** – Storage Layer
* **AWS Glue** – Data Catalog & Schema
* **AWS Athena** – Serverless Query Engine
* **Python** – Data Generation & Lambda

---

## 🎯 Key Learnings

* Streaming real-time CDC events from DynamoDB.
* Using Lambda to transform streaming data.
* Querying S3-based datasets with Athena.
* Automating schema creation with Glue Crawler.

---

## 📌 Future Improvements

* Add dashboards in **Amazon QuickSight** or **Grafana**.
* Support CDC for `UPDATE` and `DELETE` events.
* Implement **partitioned storage** for faster Athena queries.

---

## 👤 Author

**Rohesen**
📅 October 2025
🔗 [GitHub Profile](https://github.com/Rohesen)
