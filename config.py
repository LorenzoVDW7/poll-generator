import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Centralized configuration"""

    DB_USER = os.getenv("DATABASE_USERNAME", "root")
    DB_PASSWORD = os.getenv("DATABASE_PASSWORD", "")
    DB_HOST = os.getenv("DATABASE_HOST", "127.0.0.1")
    DB_PORT = os.getenv("DATABASE_PORT")
    DB_NAME = os.getenv("DATABASE_DB", "polling")