import os


class Config:
    """Configuratio of SQLAlchemy and other keys."""
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", "mysql+mysqldb://job_dev:job_dev_pwd\
                       @localhost:3306/job_dev_db"
             )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = "uploads"
