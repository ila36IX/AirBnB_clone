from uuid import uuid4
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        """Public instance attributes"""
        if kwargs == {}:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()

    def save(self):
        self.updated_at = datetime.today()

    def to_dict(self):
        dict_clone = {**self.__dict__}
        dict_clone['created_at'] = dict_clone["created_at"].isoformat()
        dict_clone['updated_at'] = dict_clone['updated_at'].isoformat()
        dict_clone["__class__"] = __class__.__name__
        return dict_clone

    def __str__(self):
        """Friendly string representaion of object"""
        return "[{}] ({}) {}".format(__class__.__name__, self.id, self.__dict__)
        
if __name__ == "__main__":
    kill = BaseModel()
    print(kill.to_dict())
    print(kill.__dict__)