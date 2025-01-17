# app/config.py
import os


class Config:
    PROVIDER_URL = os.getenv("PROVIDER_URL")
    DB_HOST = os.getenv("DB_HOST", "localhost").split(',')
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
