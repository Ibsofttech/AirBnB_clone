#!/usr/bin/env python3
"""Starts the BaseModel class defination"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """A class that defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at':
                        self.created_at = datetime.fromisoformat(value)
                    elif key == 'updated_at':
                        self.updated_at = datetime.fromisoformat(value)
                    else:
                        self.__dict__[key] = value
        else:
            self.__dict__['id'] = str(uuid.uuid4())
            self.__dict__['created_at'] = datetime.now()
            self.__dict__['updated_at'] = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """returns [<class name>] (<self.id>) <self.__dict__>"""

        class_name = self.__class__.__name__
        instance_id = self.id
        isinstance_dict = self.__dict__
        return f"[{class_name}], ({instance_id}), {isinstance_dict}"

    def save(self):
        """updates the public instance attribute"""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance"""

        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return instance_dict
