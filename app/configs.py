import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("SECRET_KEY")


class Settings(BaseSettings):
    app_name: str = "Capital.com SMS Service API"
    admin_email: str = "admin@admin.com"
    items_per_user: int = 50


settings = Settings()
