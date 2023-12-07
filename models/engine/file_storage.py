#!/usr/bin/python3

"""

Serializes instances to a JSON file and
deserializes JSON file to instances

"""

from models.base_model import BaseModel
import json
from models.user import User
from models.state import State
from models.state import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review 

class FileStorage:
    """Serializes instances to a JSON file and
    deserializes JSON file to instances
    """

    __file_path = "/home/vagrant/AirBnB_clone/datebase.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with a key"""
        objs = FileStorage.__objects
        class_name = obj.__class__.__name__
        key = "{}.{}".format(class_name, obj.id)
        objs[key] = obj

    def save(self):
        """save the objects into _object attribute"""
        objs = FileStorage.__objects
        objs_clone = {k: v.to_dict() for (k, v) in objs.items()}
        objs = objs_clone
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objs_clone, f, indent=4)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                objs_clone = json.load(f)
                objs = {k: BaseModel(**v) for (k, v) in objs_clone.items()}
                FileStorage.__objects = objs
        except Exception:
            return
