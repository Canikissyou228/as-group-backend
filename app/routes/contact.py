from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def submit_contact(name: str, email: str, message: str):
    return {"status": "success", "name": name, "email": email, "message": message}
