#!/usr/bin/python3
""" This module contains the base class
    for all classes
"""
from datetime import datetime
from sqlalchemy.orm import declarative_base
import uuid
from sqlalchemy import Column, String, DateTime

time = "%Y-%m-%dT%H:%M:%S.%f"

Base = declarative_base()  # Base for all SQL tables


class BaseModel(Base):
    """Base model for all database tables."""
    # Prevents SQLAlchemy from creating a table for BaseModel
    __abstract__ = True

    id = Column(String(36), primary_key=True,
                default=lambda: str(uuid.uuid4()))
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        nullable=False, onupdate=datetime.utcnow)

    def to_dict(self):
        """Converts model instance to dictionary."""
        new_dict = self.__dict__.copy()
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]  # SQLAlchemy internal attribute
        new_dict["created_at"] = self.created_at.strftime(time)
        new_dict["updated_at"] = self.updated_at.strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        return new_dict

    def __repr__(self):
        """Returns string representation of the object."""
        return "[{}] ({}) {}".format(
                                     self.__class__.__name__,
                                     self.id, self.to_dict())
