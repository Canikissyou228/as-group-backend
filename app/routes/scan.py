# app/routes/scan.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import subprocess
from app.database import SessionLocal, Scan
from datetime import datetime

router = APIRouter()

class ScanRequest(BaseModel):
    target: str

# ✅ Set the correct paths for your downloaded tools
NMAP_PATH = r"C:\Program Files (x86)\Nmap\nmap.exe"
SQLMAP_PATH = r"C:\Users\Aman Shaikh\Downloads\sqlmap-master\sqlmap.py"
DIRSEARCH_PATH = r"C:\Users\Aman Shaikh\Downloads\dirsearch\dirsearch.py"

@router.post("/scan")
async def perform_scan(request: ScanRequest):
    target = request.target
    db = SessionLocal()

    # Nmap Scan
    try:
        nmap_result = subprocess.check_output(
            [NMAP_PATH, "-sV", target],
            universal_newlines=True,
            stderr=subprocess.STDOUT
        )
    except Exception as e:
        nmap_result = f"Nmap scan failed: {e}"

    # SQLmap Scan
    try:
        sqlmap_result = subprocess.check_output(
            ["python", SQLMAP_PATH, "-u", f"http://{target}", "--batch", "--level=1"],
            universal_newlines=True,
            stderr=subprocess.STDOUT
        )
    except Exception as e:
        sqlmap_result = f"SQLmap scan failed: {e}"

    # Directory Scan (Dirsearch)
    try:
        dir_result = subprocess.check_output(
            ["python", DIRSEARCH_PATH, "-u", f"http://{target}", "-e", "php,html,js"],
            universal_newlines=True,
            stderr=subprocess.STDOUT
        )
    except Exception as e:
        dir_result = f"Dirsearch scan failed: {e}"

    # Save scan results to database
    scan_entry = Scan(
        target=target,
        nmap_result=nmap_result,
        sqlmap_result=sqlmap_result,
        dir_result=dir_result,
        timestamp=datetime.utcnow()
    )
    db.add(scan_entry)
    db.commit()
    db.refresh(scan_entry)
    db.close()

    return {
        "id": scan_entry.id,
        "target": target,
        "nmap_result": nmap_result,
        "sqlmap_result": sqlmap_result,
        "dir_result": dir_result,
        "timestamp": scan_entry.timestamp
    }
