import os

class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:P@ssword01@localhost:5432/dinduodb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
