import random
import uuid
from datetime import datetime

def generate_patient_data():
    return {
        "patient_id": str(uuid.uuid4()),
        "age": random.randint(20, 80),
        "heart_rate": random.randint(60, 140),
        "blood_pressure": random.randint(90, 180),
        "glucose_level": random.randint(70, 200),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }