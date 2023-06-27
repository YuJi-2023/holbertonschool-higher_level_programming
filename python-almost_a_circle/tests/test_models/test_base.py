"""unittest for base module"""
import unittest
from models.base import Base

class testBase(unittest.TestCase):
    """test class Base"""
    def test_id(self):
        b1 = Base()
        b2 = Base()
        self.assertNotEqual(b1.id, b2.id)
        self.assertEqual(b1.id + 1, b2.id)
        b3 = Base(15)
        self.assertEqual(b3.id, 15)
