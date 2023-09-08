from fastapi import FastAPI
import uvicorn
import secrets

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}