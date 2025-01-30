import pymysql
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

def get_connection():
    try:
        connection = pymysql.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            port=int(os.getenv("DB_PORT")),
            cursorclass=pymysql.cursors.DictCursor
        )
        print("Successful connection to MariaDB on AWS")
        return connection
    except pymysql.err.OperationalError as e:
        print(f"Connection error: {e}")
        return None
    except pymysql.err.InternalError as e:
        print(f"Internal error in MariaDB: {e}")
        return None
    except Exception as e:
        print(f"Unknown error: {e}")
        return None