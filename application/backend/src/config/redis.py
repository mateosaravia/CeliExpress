import redis
import os

REDIS_HOST = os.environ.get("REDIS_HOST")
REDIS_PORT = os.environ.get("REDIS_PORT")

_connection = None

def create_connection():
    global _connection
    _connection = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)

def get_connection():
    global _connection
    if _connection is None:
        create_connection()

    return _connection