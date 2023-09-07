import jwt
import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
JWT_EXPIRATION = os.getenv("JWT_EXPIRATION_TIME")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")

def create_access_token(role):
    payload = { 
        "role": role 
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=JWT_ALGORITHM)
    return token