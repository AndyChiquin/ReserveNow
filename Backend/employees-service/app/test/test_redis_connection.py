import redis

# Connecting to Redis in Docker container
REDIS_HOST = "localhost"  
REDIS_PORT = 6379

try:
    redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
    redis_client.ping()  
    print("Successful connection to Redis in Docker")
except Exception as e:
    print(f" Error connecting to Redis in Docker: {e}")
