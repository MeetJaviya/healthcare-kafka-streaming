import json
import time
from kafka import KafkaProducer
from data_generator.patient_data_generator import generate_patient_data

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic = "hospital-patient-data"

print("Starting Kafka Producer...")

while True:

    patient_data = generate_patient_data()

    producer.send(topic, value=patient_data)
    producer.flush()
    
    print("Sent:", patient_data)

    time.sleep(2)