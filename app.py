from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import yaml
from flasgger import Swagger
from app.my_project.auth.controller.controller import controller

app = Flask(__name__)

app.register_blueprint(controller)
swagger = Swagger(app)  


if __name__ == "__main__":
    app.run(debug=True)

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Завантаження конфігурації
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)
    
    dev_config = config["development"]  # або "production"
    mysql_config = config["ADDITIONAL_CONFIG"]
    
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"mysql+pymysql://{mysql_config['MYSQL_USER']}:"
        f"{mysql_config['MYSQL_PASSWORD']}@"
        f"{mysql_config['MYSQL_HOST']}/"
        f"{mysql_config['MYSQL_DB']}"
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = dev_config['SQLALCHEMY_TRACK_MODIFICATIONS']
    app.config['DEBUG'] = dev_config['DEBUG']
    
    db.init_app(app)
    
    from app.my_project.auth.route.route import register_routes
    register_routes(app)
    
    return app
