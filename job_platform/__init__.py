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
    """Create Flask Object as app."""
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    from job_platform.api.auth import auth_api
    from job_platform.api.job import job_api

    app.register_blueprint(auth_api, url_prefix="/api/auth")
    app.register_blueprint(job_api, url_prefix="/api/job")

    return app
