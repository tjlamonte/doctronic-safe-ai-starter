from fastapi import FastAPI
from app.routes import bulletin

app = FastAPI(title="Doctronic API (starter)")

app.include_router(bulletin.router)


@app.get("/")
def read_root():
    return {"message": "Doctronic API is running"}
