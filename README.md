# Procurement Pipeline using Kafka, PySpark, FastAPI, PostgreSQL and Redis

## Project Overview

This project implements an end-to-end procurement invoice processing pipeline using:

- Python Producer
- Apache Kafka
- PySpark Consumer
- PostgreSQL Database
- FastAPI REST APIs
- Redis Caching
- Docker & Docker Compose

The system allows invoices to be produced as Kafka messages, consumed by PySpark, stored in PostgreSQL, and accessed through FastAPI APIs with Redis caching.

---

# Architecture

```text
Python Producer
       ↓
     Kafka
       ↓
PySpark Consumer
       ↓
   PostgreSQL
       ↓
     FastAPI
       ↓
      Redis
```

---

# Technologies Used

- Python 3
- Apache Kafka
- PySpark
- PostgreSQL 16
- FastAPI
- SQLAlchemy
- Redis
- Docker
- Docker Compose

---

# Project Structure

```text
task1/
│
├── fastapi_project/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── redis_client.py
│   ├── test_db.py
│   └── test_redis.py
│
├── kafka_consumer.py
├── producer.py
├── docker-compose.yml
├── Dockerfile
├── Dockerfile.consumer
├── requirements.txt
│
├── setup.sh
├── start.sh
├── stop.sh
├── health.sh
├── run_producer.sh
├── run_consumer.sh
└── README.md
```

---

# Clone Repository

```bash
git clone https://github.com/Kaustubh-Waje/Fractal-Analytics-Group-C.git
cd Fractal-Analytics-Group-C
```

---

# First Time Setup

Give execute permissions:

```bash
chmod +x *.sh
```

Run setup:

```bash
./setup.sh
```

The setup script:

- Creates Python virtual environment
- Installs dependencies
- Prepares the project for execution
- Sets up the development environment

---

# Start the Project

Start all Docker services:

```bash
./start.sh
```

or

```bash
docker compose up -d
```

---

# Check Service Health

```bash
./health.sh
```

or

```bash
docker ps
```

Expected containers:

- postgres
- redis
- kafka
- fastapi

---

# Run Producer

```bash
./run_producer.sh
```

or

```bash
python producer.py
```

Sample invoice:

```json
{
  "vendor": "Kaustubh",
  "amount": 15000,
  "status": "Pending"
}
```

The producer sends invoice data to the Kafka topic:

```text
invoice-topic
```

---

# Run Consumer

```bash
./run_consumer.sh
```

or

```bash
python kafka_consumer.py
```

The consumer:

1. Reads messages from Kafka.
2. Parses JSON data.
3. Writes invoice data into PostgreSQL.

---

# Verify Database

Open PostgreSQL:

```bash
docker exec -it postgres psql -U kaustubh -d procurement
```

Check tables:

```sql
\dt
```

View invoices:

```sql
SELECT * FROM kafka_invoices;
```

---

# FastAPI Documentation

Swagger UI:

```text
http://localhost:8000/docs
```

---

# API Endpoints

## Home

```http
GET /
```

Response:

```json
{
  "message": "FastAPI is working!"
}
```

---

## Get All Invoices

```http
GET /invoices
```

---

## Create Invoice

```http
POST /invoices
```

Request Body:

```json
{
  "vendor": "Google",
  "amount": 25000,
  "status": "Approved"
}
```

---

## Update Invoice

```http
PUT /invoices/{invoice_id}
```

Request Body:

```json
{
  "vendor": "Amazon",
  "amount": 30000,
  "status": "Approved"
}
```

---

## Delete Invoice

```http
DELETE /invoices/{invoice_id}
```

---

# Redis Caching

The endpoint:

```http
GET /invoices
```

uses Redis caching.

Cache key:

```text
all_invoices
```

The cache is automatically cleared whenever:

- POST /invoices
- PUT /invoices/{id}
- DELETE /invoices/{id}

are called.

---

# End-to-End Workflow

### 1. Setup Project

```bash
./setup.sh
```

### 2. Start Services

```bash
./start.sh
```

### 3. Check Health

```bash
./health.sh
```

### 4. Send Invoice

```bash
./run_producer.sh
```

### 5. Consume and Store Data

```bash
./run_consumer.sh
```

### 6. Verify Database

```sql
SELECT * FROM kafka_invoices;
```

### 7. Access APIs

```text
http://localhost:8000/docs
```

### 8. Stop Services

```bash
./stop.sh
```

---

# Docker Services

| Service | Port |
|---------|------|
| FastAPI | 8000 |
| PostgreSQL | 5433 |
| Redis | 6380 |
| Kafka | 9092 |

---

# Features

✅ Dockerized Infrastructure  
✅ Kafka-based Messaging  
✅ PySpark Data Processing  
✅ PostgreSQL Storage  
✅ FastAPI CRUD APIs  
✅ Redis Caching  
✅ Health Check Scripts  
✅ End-to-End Invoice Processing Pipeline

---

# Screenshots (Optional)

- Docker Containers Running
- Kafka Producer Output
- Kafka Consumer Output
- PostgreSQL Table
- FastAPI Swagger UI
- GET /invoices Response
- GitHub Repository

---

# Author

**Kaustubh Waje**

Second Year Computer Engineering Student  
Fr. Conceicao Rodrigues Institute of Technology (FCRIT), Vashi

---

# License

This project is developed for learning and internship purposes.
