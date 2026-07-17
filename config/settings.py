import os

from dotenv import load_dotenv

from config.constants import *

MAX_HISTORY = 20

# ===========================
# LOAD ENV
# ===========================

load_dotenv(ROOT_DIR / ".env")

# ===========================
# APP
# ===========================

APP_NAME = os.getenv("APP_NAME", "FRISK")

OWNER = os.getenv("OWNER", "Unknown")

LANGUAGE = os.getenv("LANGUAGE", "es")

DEBUG = os.getenv("DEBUG", "False").lower() == "true"

# ===========================
# AI
# ===========================

AI_PROVIDER = os.getenv("AI_PROVIDER", "groq")

PRIMARY_MODEL = os.getenv(
    "PRIMARY_MODEL",
    "groq/compound"
)

BACKUP_MODEL = os.getenv(
    "BACKUP_MODEL",
    "llama-3.3-70b-versatile"
)

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")