import os

class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://azureuser:my_password@74.234.24.16/weather_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
