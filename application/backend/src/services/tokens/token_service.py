import jwt
import os
from dotenv import load_dotenv

from ...config import redis
from ...utils.exceptions.tokens.token_exceptions import TokenException

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

def verify_token(token):
    black_listed_token = check_black_list_token(token)
    if black_listed_token:
        raise TokenException.InvalidToken()

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=JWT_ALGORITHM)
    except ExpiredSignatureError:
        raise TokenException.TokenExpired()
    except JWTError:
        raise TokenException.InvalidToken()

    return {"user_email": payload["user_email"]}

def black_list_token(token):
    redis_connection = redis.get_connection()
    expires = 12 * 60 * 60
    redis_connection.set(token, "loggedOutToken", {EX: expires})

def check_black_list_token(token):
    redis_connection = redis.get_connection()
    token_value = redis_connection.get(token)

    if token_value == "loggedOutToken":
        return False
    
    return True