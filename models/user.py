#!/usr/bin/python3

"""

Model for the User class

"""

from models.base_model import BaseModel
class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""
