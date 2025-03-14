#!/usr/bin/python3
"""
Handles the database storage for the Job Seeker project
"""
from models.base_model import Base
from models.employee import Employee
from models.employer import Employer
from models.job import Job
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


# Dictionary mapping model class names to actual classes
classes = {'Employee': Employee, 'Employer': Employer, 'Job': Job}

# Database connection credentials from environment variables
user = getenv('JOB_MYSQL_USER')
password = getenv('JOB_MYSQL_PWD')
host = getenv('JOB_MYSQL_HOST')
db = getenv('JOB_MYSQL_DB')


class DBStorage:
    """Interacts with the MySQL Database"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize the database engine"""
        self.__engine = create_engine(
            f"mysql+mysqldb://{user}:{password}@{host}/{db}",
            pool_pre_ping=True
        )
        if getenv('JOB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects of a given class or all classes"""
        new_dict = {}
        for class_name, model_class in classes.items():
            if cls is None or cls in (model_class, class_name):
                objs = self.__session.query(model_class).all()
                for obj in objs:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """Add a new object to the current session"""
        self.__session.add(obj)

    def save(self):
        """Commit changes to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object from the session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reload database tables and create a new session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """Close the session"""
        self.__session.remove()

    def get(self, cls, id):
        """Retrieve an object by class and ID"""
        if cls is None or id is None:
            return None
        cls = classes.get(cls) if isinstance(cls, str) else cls
        if cls not in classes.values():
            return None
        return self.__session.query(cls).filter_by(id=id).first()
