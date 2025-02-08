import os
import mysql.connector
import logging
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Load environment variables
env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../.env'))
if os.path.exists(env_path):
    load_dotenv(env_path)
    logging.info("✅ .env file loaded successfully.")
else:
    raise FileNotFoundError("❌ ERROR: .env file not found.")

# Verify that environment variables are loaded correctly
logging.info("🔍 Checking environment variables...")
for var in ["DB_HOST", "DB_USER", "DB_PASSWORD", "DB_NAME", "DB_PORT"]:
    value = os.getenv(var)
    logging.info(f"{var}: {'NOT SET' if value is None else value}")

# Function to establish a MySQL connection
def get_connection():
    try:
        logging.info("🔄 Attempting to connect to MySQL on AWS...")
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            port=int(os.getenv("DB_PORT", 3306)),
            use_pure=True
        )
        logging.info("✅ Successfully connected to MySQL on AWS.")
        return conn
    except mysql.connector.Error as err:
        logging.error(f"❌ MySQL connection error: {err}")
        raise err
