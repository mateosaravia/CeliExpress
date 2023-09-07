from fastapi import FastAPI
import uvicorn
import secrets

app = FastAPI()

@app.get("/")
def read_root():
    secret_key = secrets.token_hex(32)
    return {"Hello": secret_key}