#!/usr/bin/python3
"""Defines a class FileStorage that serializes and deserializes objects
"""
import json
from pathlib import Path


class Filestorage:
    """Class that serializes instances to a JSON file and deserializes
    JSON file to instances.
    """
    __file_path: str = 'file.json'
    __objects: dict = {}

    def __init__(self) -> None:
        """Creates new instances of class.
        """
        pass

    def all(self):
        """Returns the dictionary objects.

        Returns:
            dict: objects.
        """
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id.

        Args:
            obj (dict): dict object.
        """
        self.__objects = {f'{obj.__class__.__name__}.{obj.id}': obj}

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path).
        """
        # print(self.all())
        # Read the existing data
        file_path = Path(self.__file_path)

        if file_path.exists() and file_path.stat().st_size != 0:
            with open(file_path, 'r',  encoding="utf-8") as f:
                existing_data = json.load(f)
        else:
            existing_data = {}

        # Update the existing data with the new objects
        data = {key: value.to_dict() for key, value in self.__objects.items()}
        existing_data.update(data)

        with open(file_path, 'w',  encoding="utf-8") as f:
            json.dump(existing_data, f)

    def reload(self):
        """Deserializes the JSON file to __objects only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)
        """
        # Create the file if it doesn't exist
        file_path = Path(self.__file_path)
        file_path.touch(exist_ok=True)

        # Check if the file is empty
        if file_path.stat().st_size == 0:
            self.__objects = {}
            return

        with open(f'{self.__file_path}', 'r',  encoding="utf-8") as f:
            self.__objects = json.load(f)
