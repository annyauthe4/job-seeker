from job_platform.models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Employer(BaseModel):
    """ Creates the Employer class"""
    __tablename__ = 'employers'

    fullname = Column(String(128), nullable=False)
    email = Column(String(128), unique=True, nullable=False)
    password = Column(String(128), nullable=False)

    jobs = relationship('Job', back_populates='employer',
                        cascade='all, delete')
