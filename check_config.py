import os

print("Environment DB_NAME:", os.environ.get("DB_NAME"))

from app.core.config import settings

print("Settings DB_NAME:", settings.DB_NAME)
print("DATABASE_URL:", settings.DATABASE_URL)