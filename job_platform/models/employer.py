from job_platform.models.base_model import User
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Employer(User):
    """ Creates the Employer class"""
    __tablename__ = 'employers'

    id = Column(ForeignKey("users.id"), primary_key=True)
    company_name = Column(String(128), nullable=False)
    website = Column(String(256), nullable=True)

    jobs = relationship('Job', back_populates='employer',
                        cascade='all, delete')

    __mapper_args__ = {
        'polymorphic_identity': 'employer',
    }
