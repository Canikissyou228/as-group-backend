from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# Import routes
from app.routes import services, contact, scan

app = FastAPI(title="AS Group Backend")

# -------------------
# CORS configuration
# -------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust to your frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------
# Include API routes
# -------------------
app.include_router(services.router, prefix="/services", tags=["Services"])
app.include_router(contact.router, prefix="/contact", tags=["Contact"])
app.include_router(scan.router, prefix="/scan", tags=["Scan"])

# -------------------
# Root endpoint
# -------------------
@app.get("/")
async def root():
    return {"message": "AS Group Backend is running!"}
