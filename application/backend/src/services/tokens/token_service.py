import jwt
import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_EXPIRATION = os.getenv("JWT_EXPIRATION_TIME")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")

def create_access_token(user_email, role):
    payload = { 
        "user_email": user_email,
        "role": role 
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=JWT_ALGORITHM)
    return token