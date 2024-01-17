#!/usr/bin/env python3
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """it returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """it Sets in __objects the obj with key <obj class name>.id"""
        k = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[k] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, "w", encoding="utf-8") as f:
            s_objects = {k: val.to_dict() for k, val in self.__objects.items()}
            json.dump(s_objects, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                serialized_objects = json.load(f)
                for serial_val in serialized_objects.values():
                    self.new(eval(serial_val["__class__"])(**serial_val))
        except FileNotFoundError:
            pass
