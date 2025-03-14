from job_platform.models.base_model import BaseModel
from sqlalchemy import Column, String


class JobSeeker(BaseModel):
    """User model for job seeker and providers"""
    __tablename__ = "jobseekers"

    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = Column(String(128), nullable=False)
    cv_link = Column(String(256), nullable=True)
