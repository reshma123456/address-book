"""Application configuration loaded from environment variables."""
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./address.db")
LOG_FILE: str = os.getenv("LOG_FILE", "logs/app.log")
API_VERSION: str = "v1"