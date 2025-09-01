from app.database import SessionLocal, Service

db = SessionLocal()

services_list = ["Cybersecurity", "AI Solutions", "Software Development", "Networking", "Data Analytics"]

for name in services_list:
    if not db.query(Service).filter_by(name=name).first():
        db.add(Service(name=name))

db.commit()
db.close()
print("Services added successfully!")
