import os

SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key_here")


class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost/healthy_and_diagnosis"

    SQLALCHEMY_TRACK_MODIFICATIONS = False