# Порожній файл __init__.py
# app/my_project/auth/controller/__init__.py, app/my_project/auth/dao/__init__.py і т.д.
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config  # або твій спосіб завантаження конфігу

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Прив'язуємо SQLAlchemy до додатку
    db.init_app(app)

    # Імпортуємо маршрути всередині create_app, щоб не було циклічних імпортів
    from app.my_project.auth.route.route import register_routes
    register_routes(app)

    return app
