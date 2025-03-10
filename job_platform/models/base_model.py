#!/usr/bin/python3
"""This is the basemodel class where every other classes inherit from"""

from datetime import datetime
import uuid

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """The class from which other classes will be derived."""
    def __init__(self, *args, **kwargs):
        """Initializes the instance of the basemodel class."""
        if kwargs:
            for key, value in kwargs.items():
                if key != __class__:
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at


    def __str__(self):
        """String representation of the BaseModel class."""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)


    def to_dict(self):
        """Returns a dictionarty representatin of the class."""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] = self.__class__name
        return new_dict
