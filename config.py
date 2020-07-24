import os

class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin123@localhost/flask_contacts'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Development(Config):
    Debug = True

class Testing(Config):
    pass


config = {
    'development': Development,
    'testing': Testing
}