import os

class DevelopmentConfig:
    DEBUG = True
    ENV = "development"
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///dev.db")
