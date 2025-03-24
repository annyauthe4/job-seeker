#!/usr/bin/python3
""" Sets up table for job seekers information in the database"""
from job_platform.models.user import User
from job_platform.models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey


class JobSeeker(User):
    """User model for job seeker"""
    __tablename__ = "jobseekers"

    id = Column(String(36), ForeignKey("users.id"), primary_key=True)
    cv_link = Column(String(256), nullable=True)

    __mapper_args__ = {
        'polymorphic_identity': 'job_seeker',
    }
