import os

class ProductionConfig:
    DEBUG = False
    ENV = "production"
    SECRET_KEY = os.getenv("SECRET_KEY")
    DATABASE_URL = os.getenv("DATABASE_URL")