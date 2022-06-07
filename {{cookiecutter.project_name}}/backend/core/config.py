import os
from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv


env_path = Path(".") / ".env"
load_dotenv(env_path)

class Settings:
    PROJECT_NAME: str = "{{cookiecutter.project_name}}"
    PROJECT_VERSION: str = "1.0.0"

    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    API_USERNAME = os.getenv("API_USER")
    API_PASSWORD = os.getenv("API_PASSWORD")


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()