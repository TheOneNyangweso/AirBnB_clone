#!/usr/bin/python3
"""Defines a base class to be used by all models
"""
from datetime import datetime
import uuid


class BaseModel:
    """Class that defines properties of base
    """

    def __init__(self):
        """Creates new instances of Base
        """
        self.id: str = str(uuid.uuid4())
        self.created_at: datetime = datetime.now()
        self.updated_at: datetime = datetime.now()

    def save(self):
        """Update public instance attribute updated_at with current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all key/values of __dict__ of
        the instance.

        Returns:
            dict: key/value pairs.
        """
        model_dict = self.__dict__
        model_dict['__class__'] = self.__class__.__name__
        model_dict['created_at'] = self.created_at.strftime(
            '%Y-%m-%dT%H:%M:%S.%f')
        model_dict['updates_at'] = self.updated_at.strftime(
            '%Y-%m-%dT%H:%M:%S.%f')
        return model_dict

    def __str__(self) -> str:
        """Returns a string represation of class details.

        Returns:
            str: class details
        """
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'
