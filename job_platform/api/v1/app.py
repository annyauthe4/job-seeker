from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from job_seeker.config import Config  # Change path to models.config or something necessary

db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    from job_seeker.routes.auth_routes import auth_routes   # Change to correct path
    from job_seeker.routes.job_routes import job_routes  # Change to correct path

    app.register_blueprint(auth_routes, url_prefix="/api/auth")
    app.register_blueprint(job_routes, url_prefix="/api/job")

    return app
