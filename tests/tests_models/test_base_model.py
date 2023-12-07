from models.base_model import BaseModel
import unittest
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.obj1 = BaseModel()
        self.obj2 = BaseModel()
        self.obj3 = BaseModel()
        self.obj4 = BaseModel()
        self.obj = BaseModel()

    def test_init(self):
        self.assertIsInstance(self.obj.id, str)
        self.assertIsInstance(self.obj.created_at, datetime)
        self.assertIsInstance(self.obj.updated_at, datetime)
        self.assertNotEqual(self.obj1.id, self.obj2.id)
        self.assertNotEqual(self.obj3.id, self.obj4.id)
    def test_to_dict(self):
        self.assertEqual(self.obj.to_dict()["__class__"], "BaseModel")
        self.assertIsInstance(self.obj.to_dict()["created_at"], str)
        self.assertIsInstance(self.obj.to_dict()["updated_at"], str)
        self.assertEqual(len (self.obj.to_dict()), 4)
        self.assertIsInstance(self.obj.to_dict(), dict)
    def test_save(self):
       before_save = self.obj.updated_at
       before_save_create = self.obj.created_at
       self.obj.save()
       after_save_create = self.obj.created_at
       after_save = self.obj.updated_at
       self.assertNotEqual(before_save, after_save)
       self.assertEqual(before_save_create, after_save_create)
    def test_str(self):
        str_rep = "[BaseModel] ({}) {}".format( self.obj.id, self.obj.__dict__)
        self.assertEqual(str_rep, str(self.obj))
        str_rep = "[BaseModel] ({}) {}".format( self.obj1.id, self.obj1.__dict__)
        self.assertEqual(str_rep, str(self.obj1))
        