import os


class Config:
    """Configuratio of SQLAlchemy and other keys."""
    DB_URI = os.getenv(
                       "mysql+mysqldb://job_dev:job_dev_pwd\
                       @localhost:3306/job_dev_db"
             )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = "uploads"
