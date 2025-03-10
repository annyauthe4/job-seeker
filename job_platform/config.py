import os


class Config:
    """Configuratio of SQLAlchemy and other keys."""
    DB_URI = os.getenv(
                       "DATABASE_URL", "mysql+mysqlconnector://username:\
                       password@localhost/job_platform_db"
             )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your_secret_key")
    UPLOAD_FOLDER = "uploads"
