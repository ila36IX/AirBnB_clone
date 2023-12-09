#!/usr/bin/python3

"""Contain tests for the state module"""
import unittest
from models.base_model import BaseModel
from models.state import State

class TestState(unittest.TestCase):
    """Test the State class"""

    def test_State_inheritence(self):
        """Testing the state class that contains the attribute 'name'"""
        new_state = State()
        self.assertIsInstance(new_state, BaseModel)

    def test_State_attributes(self):
        """Test the class State which contains the attributes 'name'"""
        new_state = State()
        self.assertTrue("name" in new_state.__dir__())

    def test_State_attributes_type(self):
        """ Test the State class in which attribute name is the class type str"""
        new_state = State()
        name = getattr(new_state, "name")
        self.assertIsInstance(name, str)   