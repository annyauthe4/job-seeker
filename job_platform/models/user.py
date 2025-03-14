#!/usr/bin/python3
from sqlalchemy import Column, String, Integer, Enum
from job_platform.models.base_model import BaseModel


class User(BaseModel):
    """Defines a common User model for job seekers and employers"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(128), nullable=False)
    email = Column(String(128), unique=True, nullable=False)
    password = Column(String(128), nullable=False)
    role = Column(Enum("job_seeker", "employer"), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'polymorphic_on': role
    }
