"""unittest for base module"""
import unittest
from models.base import Base
from models.rectangle import Rectangle

class testBase(unittest.TestCase):
    """test class Base"""
    def test_id(self):
        b1 = Base()
        b2 = Base()
        self.assertNotEqual(b1.id, b2.id)
        self.assertEqual(b1.id + 1, b2.id)
        b3 = Base(15)
        self.assertEqual(b3.id, 15)

    def test_to_json_string(self):
        b4 = Rectangle(2, 3, 4, 5, 6)
        dictionary = b4.to_dictionary()
        json_dict = Base.to_json_string([dictionary])
        self.assertIsInstance(json_dict, str)
        b5 = Rectangle(3, 5)
        dictionary = b5.to_dictionary()
        json_dict = Base.to_json_string([dictionary])
        self.assertEqual(json_dict, '[{"id": 3, "width": 3, "height": 5, "x": 0, "y": 0}]')
        self.assertEqual(Base.to_json_string([]),"[]")
        self.assertEqual(Base.to_json_string(None), "[]")
