"""unittest for square module"""
import io
import sys
import os
import unittest
from models.square import Square

class testSquare(unittest.TestCase):
    """test subclass Square"""
    def test_01_init(self):
        s0 = Square(1)
        s1 = Square(2, 3)
        self.assertEqual(s0.id + 1, s1.id)
        s2 = Square(2, 4, 5, 12)
        self.assertEqual(s2.id, 12)

    def test_02_args(self):
        s3 = Square(6, 1, 2, 23)
        self.assertEqual(s3.size, 6)
        self.assertEqual(s3.x, 1)
        self.assertEqual(s3.y, 2)
        self.assertEqual(s3.id, 23)

    def test_03_square(self):
        sq1 = Square(2)
        sq2 = Square(2, 3)
        sq3 = Square(2, 3, 4)
        self.assertIsInstance(sq1, Square)
        self.assertIsInstance(sq2, Square)
        self.assertIsInstance(sq3, Square)
        with self.assertRaises(TypeError):
            Square("1")
        with self.assertRaises(TypeError):
            Square(1, "2")
        with self.assertRaises(TypeError):
            Square(1, 2, "3")
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(ValueError):
            Square(1, -2)
        with self.assertRaises(ValueError):
            Square(1, 2, -3)
        with self.assertRaises(ValueError):
            Square(0)

    def test_04_raiseErrors(self):
        s3 = Square(5)
        with self.assertRaises(TypeError):
            s3.size = "hello"

        s4 = Square(5)
        with self.assertRaises(ValueError):
            s4.size = -1

    def test_05_area(self):
        s5 = Square(3)
        self.assertEqual(s5.area(), 9)

    def test_06_str(self):
        sq_str = Square(5, 1, 1, 10)
        self.assertEqual(str(sq_str), "[Square] (10) 1/1 - 5")

    def test_07_update(self):
        s_u = Square(2, 3, 4, 5)
        s_u.update(89)
        self.assertTrue(s_u.id == 89)

        s_u.update(89, 1)
        self.assertTrue(s_u.id == 89 and s_u.size == 1)

        s_u.update(89, 2, 3)
        self.assertTrue(s_u.x == 3)

        s_u.update(89, 2, 3, 4)
        self.assertTrue(s_u.y == 4)


    def test_08_save_to_file(self):
        Square.save_to_file(None)
        self.assertTrue(os.path.exists("Square.json"))
        os.remove("Square.json")

        Square.save_to_file([])
        with open("Square.json", "r") as t_file:
            self.assertEqual(t_file.read(), "[]")
            os.remove("Square.json")

        sq_s = Square(2, 3, 4, 5)
        Square.save_to_file([sq_s])
        with open("Square.json", "r") as t_file:
            self.assertEqual(t_file.read(), '[{"id": 5, "size": 2, "x": 3, "y": 4}]')
            os.remove("Square.json")

    def test_09_load_from_file(self):
        obj_list = Square.load_from_file()
        self.assertEqual(obj_list, [])

        s_l1 = Square(4)
        s_l2 = Square(9)
        list_of_obj = [s_l1, s_l2]
        Square.save_to_file(list_of_obj)

        rslt_list = Square.load_from_file()
        self.assertTrue(len(rslt_list) == 2)
        self.assertIsInstance(rslt_list[0], Square)
        os.remove("Square.json")
