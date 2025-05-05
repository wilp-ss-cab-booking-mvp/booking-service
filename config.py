# Loads env variables
import os
from dotenv import load_dotenv

load_dotenv()

# These values are read from .env file or fallback to defaults
DB_URI = os.getenv("DB_URI")
JWT_SECRET = os.getenv("JWT_SECRET", "default-secret")
USER_SERVICE_URL = os.getenv("USER_SERVICE_URL")
DRIVER_SERVICE_URL = os.getenv("DRIVER_SERVICE_URL")
RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "rabbitmq")
RABBITMQ_QUEUE = os.getenv("RABBITMQ_QUEUE", "booking_queue")
RABBITMQ_USER = os.getenv("RABBITMQ_USER", "guest")
RABBITMQ_PASS = os.getenv("RABBITMQ_PASS", "guest")