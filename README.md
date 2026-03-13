# 🏥 Real-Time Healthcare Kafka Streaming Pipeline

A real-time data engineering project that simulates hospital patient monitoring using Apache Kafka for streaming, Python for processing, PostgreSQL for storage, and Power BI for live visualization.

## 🔧 Tech Stack
- Apache Kafka 4.x (KRaft mode)
- Python 3.x
- PostgreSQL 18
- SQLAlchemy
- kafka-python
- Power BI Desktop

## 🏗️ Architecture
```
Patient Data Generator → Kafka Producer → Apache Kafka → Kafka Consumer → PostgreSQL → Power BI
```

## 📁 Project Structure
```
healthcare-kafka-streaming/
├── data_generator/
│   └── patient_data_generator.py   # Generates random patient vitals
├── producer/
│   └── kafka_producer.py           # Sends data to Kafka every 2 seconds
├── consumer/
│   └── kafka_consumer_to_db.py     # Consumes from Kafka, saves to PostgreSQL
├── analytics/
│   └── risk_prediction.py          # Rule-based risk scoring engine
├── database/
│   └── create_tables.py            # Creates PostgreSQL schema
└── requirements.txt
```

## ⚙️ How It Works
1. Patient vitals (age, heart rate, blood pressure, glucose) are randomly generated every 2 seconds
2. Data is published to a Kafka topic called `hospital-patient-data`
3. Consumer reads from Kafka and calculates risk level (LOW / MEDIUM / HIGH)
4. Records are stored in PostgreSQL with risk classification
5. Power BI connects via DirectQuery for live dashboard updates

## 🚀 How to Run

### Prerequisites
- Java 11+
- Python 3.8+
- Apache Kafka 4.x
- PostgreSQL

### Steps
1. Install dependencies:
```bash
   pip install -r requirements.txt
```
2. Create database:
```bash
   psql -U postgres -c "CREATE DATABASE hospital_db;"
```
3. Format and start Kafka:
```bash
   bin/windows/kafka-storage.bat format -t <UUID> -c config/server.properties --standalone
   bin/windows/kafka-server-start.bat config/server.properties
```
4. Create table:
```bash
   python database/create_tables.py
```
5. Start consumer:
```bash
   python -m consumer.kafka_consumer_to_db
```
6. Start producer:
```bash
   python -m producer.kafka_producer
```

## 📊 Risk Scoring Logic

| Vital | Threshold | Points |
|-------|-----------|--------|
| Age | > 60 years | +2 |
| Heart Rate | > 120 bpm | +2 |
| Blood Pressure | > 160 mmHg | +2 |
| Glucose Level | > 180 mg/dL | +2 |

- Score 0–2 → **LOW** risk
- Score 3–4 → **MEDIUM** risk
- Score 5+ → **HIGH** risk

## 📊 Power BI Dashboard
- Connected via DirectQuery to PostgreSQL
- Auto page refresh enabled for live updates

## 👤 Author
Meet Javiya