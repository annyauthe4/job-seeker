from job_platform.models.user import User
from sqlalchemy import Column, String, ForeignKey


class JobSeeker(User):
    """User model for job seeker"""
    __tablename__ = "jobseekers"

    id = Column(ForeignKey("users.id"), primary_key=True)
    cv_link = Column(String(256), nullable=True)

    __mapper_args__ = {
        'polymorphic_identity': 'job_seeker',
    }
