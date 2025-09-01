# app/database.py
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

DATABASE_URL = "sqlite:///asgroup.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

# Services table
class Service(Base):
    __tablename__ = "services"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

# Scans table (updated to include all tool results)
class Scan(Base):
    __tablename__ = "scans"
    id = Column(Integer, primary_key=True, index=True)
    target = Column(String, index=True)
    nmap_result = Column(Text)
    sqlmap_result = Column(Text)
    dir_result = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)

# Initialize database
def init_db():
    Base.metadata.create_all(bind=engine)
