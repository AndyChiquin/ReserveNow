from motor.motor_asyncio import AsyncIOMotorClient
import logging
import os
from dotenv import load_dotenv

# Cargar variables desde .env
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://admin:adminpassword@localhost:27017")
DB_NAME = os.getenv("MONGO_DB", "feedbacks_db")

# Configurar logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    client = AsyncIOMotorClient(MONGO_URI, serverSelectionTimeoutMS=3000)
    database = client[DB_NAME]
    feedbacks_collection = database.get_collection("feedbacks")
    
    client.admin.command("ping")
    logger.info(f" Successfully connected to MongoDB: {MONGO_URI}")

except Exception as e:
    logger.error(f" Failed to connect to MongoDB: {str(e)}")
    client = None
