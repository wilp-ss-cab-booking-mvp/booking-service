# Loads env variables
import os
from dotenv import load_dotenv

load_dotenv()

# These values are read from .env file or fallback to defaults
DB_URI = os.getenv("DB_URI")
JWT_SECRET = os.getenv("JWT_SECRET", "default-secret")