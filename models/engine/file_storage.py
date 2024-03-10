#!/usr/bin/env python3
"""Module containing FileStorage class that moderates instances and
json
"""
import json
from pathlib import Path
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage():
    """Serializes instances to JSON file and deserializes JSON file to
    instances
    """

    __file_path = Path('file.json')
    __objects = {}

    def all(self):
        """returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id

        Args:
            obj (BaseModel): BaseModel object
        """
        self.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
        """serializes __objects to the JSON file(path: __file_path)
        """
        serialized_objects = {
            key: obj.to_dict() for key, obj in self.__objects.items()
            }
        with open(self.__file_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(serialized_objects))

    def reload(self):
        """read storage file, parse the JSON string and re-create
        the objects
        """
        if self.__file_path.exists():
            try:
                with open(self.__file_path, encoding="utf-8") as f:
                    serialized_objects = json.loads(f.read())
                    self.__objects = {}
                    for key, value in serialized_objects.items():
                        class_name = value['__class__']
                        obj = eval(f"{class_name}(**{value})")
                        self.__objects[key] = obj
            except json.JSONDecodeError:
                return
