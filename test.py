#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User

new_user = User()
print(new_user.__class__.__name__)
print(new_user.to_dict())
print(new_user)
new_user .save()
