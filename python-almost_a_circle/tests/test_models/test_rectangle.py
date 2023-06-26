"""unittest for rectangle module"""
import unittest
from models.rectangle import Rectangle

class testRectangle(unittest.TestCase):
    """test subclass Rectanlge"""
    def test_init(self):
        r1 = Rectangle(2, 3)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(2, 3, 4, 5, 12)
        self.assertEqual(r2.id, 12)

    def test_args(self):
        r3 = Rectangle(6, 8, 1, 2, 23)
        self.assertEqual(r3.width, 6)
        self.assertEqual(r3.height, 8)
        self.assertEqual(r3.x, 1)
        self.assertEqual(r3.y, 2)
        self.assertEqual(r3.id, 23)
