import redis
import os
from dotenv import load_dotenv

# Cargar variables desde el archivo .env
load_dotenv()

def get_redis_connection():
    """Get a Redis connection using environment variables."""
    redis_host = os.getenv("REDIS_HOST", "redis-container")
    redis_port = int(os.getenv("REDIS_PORT", 6379))

    return redis.Redis(host=redis_host, port=redis_port, decode_responses=True)
