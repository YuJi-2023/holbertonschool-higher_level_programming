"""unittest for base module"""
import unittest
from models.base import Base

class testBase(unittest.TestCase):
    """test class Base"""
    def test_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(15)
        self.assertEqual(b3.id, 15)
