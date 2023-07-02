"""unittest for rectangle module"""
import io
import sys
import os
import unittest
from models.base import Base
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
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

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

    def test_str(self):
        re_str = Rectangle(5, 5, 1, 2, 77)
        self.assertEqual(str(re_str), "[Rectangle] (77) 1/2 - 5/5")

    def test_display(self):
        r9 = Rectangle(1, 1)
        expected_pattern = '#\n'

        captured_pattern = io.StringIO()
        sys.stdout = captured_pattern

        r9.display()
        printout_pattern = captured_pattern.getvalue()
        sys.stdout = sys.__stdout__
        self.assertEqual(printout_pattern, expected_pattern)

        r10 = Rectangle(1, 1, 1, 1)
        exp_pattern = '\n #\n'
        cap_pattern = io.StringIO()
        sys.stdout = cap_pattern
        r10.display()
        prt_pattern = cap_pattern.getvalue()
        sys.stdout = sys.__stdout__
        self.assertEqual(prt_pattern, exp_pattern)

    def test_08_update(self):
        r_u = Rectangle(1, 2, 3, 4, 5)
        r_u.update(89)
        self.assertTrue(r_u.id == 89)

        r_u.update(89, 2)
        self.assertTrue(r_u.id == 89 and r_u.width == 2)

        r_u.update(89, 2, 3)
        self.assertTrue(r_u.height == 3)

        r_u.update(89, 2, 3, 4)
        self.assertTrue(r_u.x == 4)

        r_u.update(89, 2, 3, 4, 5)
        self.assertTrue(r_u.y == 5)

    def test_save_None(self):
        """testNone"""
        Rectangle.save_to_file(None)
        self.assertTrue(os.path.exists("Rectangle.json"))
        os.remove("Rectangle.json")

    def test_save_Empty(self):
        """testEmpty"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as t_file:
            self.assertEqual(t_file.read(), "[]")
            os.remove("Rectangle.json")

    def test_save_to_file(self):
        """testNormal"""
        r_s = Rectangle(1, 2, 4, 5, 77)
        Rectangle.save_to_file([r_s])
        with open("Rectangle.json", "r") as t_file:
            self.assertEqual(t_file.read(), '[{"id": 77, "width": 1, "height": 2, "x": 4, "y": 5}]')
            os.remove("Rectangle.json")

    def test_load_from_file(self):
        """fileNotExists"""
        obj_list = Rectangle.load_from_file()
        self.assertEqual(obj_list, [])
        """normalCase"""
        r_l1 = Rectangle(4, 5)
        r_l2 = Rectangle(3, 9)
        list_of_obj = [r_l1, r_l2]
        Rectangle.save_to_file(list_of_obj)

        rslt_list = Rectangle.load_from_file()
        self.assertTrue(len(rslt_list) == 2)
        self.assertIsInstance(rslt_list[0], Rectangle)
        os.remove("Rectangle.json")
