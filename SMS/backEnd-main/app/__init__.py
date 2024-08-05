from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from .config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}}, methods=["GET", "POST", "DELETE", "PUT", "OPTIONS"])

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes import routes
    app.register_blueprint(routes)

    return app

