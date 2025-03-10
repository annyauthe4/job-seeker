from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from job_platform.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()


def create_app():
    """Create flask application."""
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    from job_platform.routes.auth_routes import auth_routes
    from job_platform.routes.job_routes import job_routes


    app.register_blueprint(auth_routes, url_prefix="/api/auth")
    app.register_blueprint(job_routes, url_prefix="/api/job")

    return app
