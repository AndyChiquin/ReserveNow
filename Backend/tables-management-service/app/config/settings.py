import os

class Settings:
    DB_USERNAME = "tables_admin"          
    DB_PASSWORD = "mysql000"       
    DB_HOST = "tables-management-db.cnkmuauq60b0.us-east-1.rds.amazonaws.com"         
    DB_PORT = 3306                      
    DB_NAME = "tables_management"     
    DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

settings = Settings()
