from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # створюємо інстанс глобально

def create_app():
    app = Flask(__name__)

    # конфігурація бази даних
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://azureuser:my_password@74.234.24.16/weather_db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)  # прив'язуємо db до цього додатка

    from app.my_project.auth.route.route import register_routes
    register_routes(app)

    return app
