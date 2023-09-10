import os

class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:P%40ssw0rd01@localhost:5432/dinduodb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
