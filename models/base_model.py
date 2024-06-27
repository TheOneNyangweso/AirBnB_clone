#!/usr/bin/python3
"""Defines a base class to be used by all models
"""
from datetime import datetime
import uuid
from models import storage


class BaseModel:
    """Class that defines properties of base
    """
    __time_format = '%Y-%m-%dT%H:%M:%S.%f'

    def __init__(self, *args, **kwargs):
        """Creates new instances of Base
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ['created_at', 'updated_at']:
                    value = datetime.strptime(value, self.__time_format)

                setattr(self, key, value)

        self.id: str = str(uuid.uuid4())
        self.created_at: datetime = datetime.now()
        self.updated_at: datetime = self.created_at
        storage.new(self)

    def save(self):
        """Update public instance attribute updated_at with current datetime.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all key/values of __dict__ of
        the instance, with class name on top

        Returns:
            dict: key/value pairs.
        """
        model_dict = self.__dict__
        model_dict['__class__'] = self.__class__.__name__
        model_dict['created_at'] = self.created_at.strftime(
            self.__time_format)
        model_dict['updated_at'] = self.updated_at.strftime(
            self.__time_format)
        return model_dict

    def __str__(self) -> str:
        """Returns a string represation of class details.

        Returns:
            str: class details
        """
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'
