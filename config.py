import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:passpost@localhost:5432/rmorty'
    SQLALCHEMY_TRACK_MODIFICATIONS = False