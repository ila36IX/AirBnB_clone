from uuid import uuid4
from datetime import datetime

class BaseModel:
    def __init__(self):
        """Public instance attributes"""
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def save(self):
        self.updated_at = datetime.today()

    def to_dict(self):
        return self.__dict__

    def __str__(self):
        """Friendly string representaion of object"""
        return "[{}] ({}) {}".format(__class__.__name__, self.id, self.__dict__)
        
    
