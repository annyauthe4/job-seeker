#!/usr/bin/python3
""" Job module that sets up job postings for employers
in the Job Seeker project """

from job_platform.models.base_model import BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Job(BaseModel):
    """ Creates the Job class and sets the table in the database """
    __tablename__ = 'jobs'

    job_title = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    location = Column(String(256), nullable=False)
    company = Column(String(128), nullable=False)
    salary = Column(Integer, nullable=True)
    website_link = Column(String(256), nullable=True)
    employer_id = Column(String(36), ForeignKey('employers.id'),
                         nullable=False)

    employer = relationship('Employer', back_populates='jobs')
