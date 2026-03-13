from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/hospital_db")

metadata = MetaData()

patients = Table(
    "patients", metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("patient_id", String),
    Column("age", Integer),
    Column("heart_rate", Integer),
    Column("blood_pressure", Integer),
    Column("glucose_level", Integer),
    Column("risk_level", String),
    Column("timestamp", String),
)

metadata.create_all(engine)

print("Patient table created successfully.")