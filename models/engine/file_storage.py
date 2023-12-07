from models.base_model import BaseModel
import json
class FileStorage:
    __file_path = "/home/heicho/AirBnB_clone/UgotMe.json"
    __objects = {}
    def all(self):
        return FileStorage.__objects
    def new(self, obj):
        objs = FileStorage.__objects
        key = "{}.{}".format(__class__.__name__, obj.id)
        objs[key] = obj
    def save(self):
        objs = FileStorage.__objects
        objs_clone = {k:v.to_dict() for (k,v) in objs.items()}
        with open(FileStorage.__file_path, "r") as f:
            json.dump.dump(objs_clone, f)
    def reload(self):
        with open(FileStorage.__file_path, "r") as f:
            obj_clone = json.load.load(f)
            objs = {k:BaseModel(v) for (k,v) in objs_clone.items()}
