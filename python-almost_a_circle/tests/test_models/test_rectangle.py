"""unittest for rectangle module"""
import unittest
from models.rectangle import Rectangle

class testRectangle(unittest.TestCase):
    """test subclass Rectanlge"""
    def test_init(self):
        r0 = Rectangle(1, 2)
        r1 = Rectangle(2, 3)
        self.assertEqual(r0.id + 1, r1.id)
        r2 = Rectangle(2, 3, 4, 5, 12)
        self.assertEqual(r2.id, 12)

    def test_args(self):
        r3 = Rectangle(6, 8, 1, 2, 23)
        self.assertEqual(r3.width, 6)
        self.assertEqual(r3.height, 8)
        self.assertEqual(r3.x, 1)
        self.assertEqual(r3.y, 2)
        self.assertEqual(r3.id, 23)

    def test_rectangle(self):
        re1 = Rectangle(1, 2)
        re2 = Rectangle(1, 2, 3)
        re3 = Rectangle(1, 2, 3, 4)
        self.assertIsInstance(re1, Rectangle)
        self.assertIsInstance(re2, Rectangle)
        self.assertIsInstance(re3, Rectangle)

    def test_raiseErrors(self):
        r4 = Rectangle(5, 2)
        with self.assertRaises(TypeError):
            r4.width = "hello"
        r5 = Rectangle(5, 2)
        with self.assertRaises(TypeError):
            r5.height = "world"

        r6 = Rectangle(5, 2)
        with self.assertRaises(ValueError):
            r6.width = -1
        r7 = Rectangle(5, 2)
        with self.assertRaises(ValueError):
            r7.height = -1

    def test_area(self):
        r8 = Rectangle(3, 6)
        self.assertEqual(r8.area(), 18)