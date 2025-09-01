from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal, Service

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_services(db: Session = Depends(get_db)):
    services = db.query(Service).all()
    return {"services": [service.name for service in services]}
