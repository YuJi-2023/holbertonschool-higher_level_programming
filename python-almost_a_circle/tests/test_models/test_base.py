"""unittest for base module"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class testBase(unittest.TestCase):
    """test class Base"""
    def test_01_id(self):
        b1 = Base()
        b2 = Base()
        self.assertNotEqual(b1.id, b2.id)
        self.assertEqual(b1.id + 1, b2.id)
        b3 = Base(15)
        self.assertEqual(b3.id, 15)

    def test_02_to_json_string(self):
        b4 = Rectangle(2, 3, 4, 5, 6)
        dictionary = b4.to_dictionary()
        json_dict = Base.to_json_string([dictionary])
        self.assertIsInstance(json_dict, str)
        self.assertEqual(json_dict, '[{"id": 6, "width": 2, "height": 3, "x": 4, "y": 5}]')
        b5 = Rectangle(3, 5)
        dictionary = b5.to_dictionary()
        json_dict = Base.to_json_string([dictionary])
        self.assertEqual(json_dict, '[{"id": 3, "width": 3, "height": 5, "x": 0, "y": 0}]')
        self.assertEqual(Base.to_json_string([]),"[]")
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_03_from_json_string(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(''), [])
        j_string = '[{"id":3, "width": 3, "height": 5, "x": 0, "y": 0}]'
        self.assertEqual(type(Base.from_json_string(j_string)), list)
        self.assertEqual(Base.from_json_string(j_string), [{'id': 3, 'width': 3, 'height': 5, 'x': 0, 'y': 0}])

    def test_04_create(self):
        r_c = Rectangle(3, 4, 5)
        r_c_dict = r_c.to_dictionary()
        r_c_new = Rectangle.create(**r_c_dict)
        self.assertIsNot(r_c_new, r_c)
