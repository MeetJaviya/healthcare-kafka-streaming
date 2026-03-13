import json
from kafka import KafkaConsumer
from sqlalchemy import create_engine, text
from analytics.risk_prediction import calculate_risk

# PostgreSQL connection
engine = create_engine(
    "postgresql+psycopg2://postgres:postgres@localhost:5432/hospital_db"
)

consumer = KafkaConsumer(
    'hospital-patient-data',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Kafka Consumer Started...")

for message in consumer:

    data = message.value

    risk = calculate_risk(
        data["age"],
        data["heart_rate"],
        data["blood_pressure"],
        data["glucose_level"]
    )

    query = text("""
        INSERT INTO patients (
            patient_id,
            age,
            heart_rate,
            blood_pressure,
            glucose_level,
            risk_level,
            timestamp
        ) VALUES (
            :patient_id,
            :age,
            :heart_rate,
            :blood_pressure,
            :glucose_level,
            :risk_level,
            :timestamp
        )
    """)

    try:
        with engine.connect() as conn:
            conn.execute(query, {
                "patient_id": data["patient_id"],
                "age": data["age"],
                "heart_rate": data["heart_rate"],
                "blood_pressure": data["blood_pressure"],
                "glucose_level": data["glucose_level"],
                "risk_level": risk,
                "timestamp": data["timestamp"]
            })
            conn.commit()
        print("Inserted Patient:", data["patient_id"], "Risk:", risk)
    except Exception as e:
        print("ERROR inserting:", e)