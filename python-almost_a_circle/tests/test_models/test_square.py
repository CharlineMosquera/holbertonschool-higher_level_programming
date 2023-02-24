#!/usr/bin/python3
"""
    Module of unit tests for the Square class.
"""
import unittest
import os.path
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """These tests ensure that the Square class behaves
    correctly and has the expected functionality."""

    def test_square_exists(self):
        s = Square(1)
        self.assertIsInstance(s, Square)

    def test_square_with_two_arguments_exists(self):
        s = Square(1, 2)
        self.assertIsInstance(s, Square)

    def test_square_with_three_arguments_exists(self):
        s = Square(1, 2, 3)
        self.assertIsInstance(s, Square)

    def test_square_with_one_argument_string_exists(self):
        s = Square("1")
        self.assertIsInstance(s, Square)

    def test_square_with_two_arguments_one_string_exists(self):
        s = Square(1, "2")
        self.assertIsInstance(s, Square)

    def test_square_with_three_arguments_one_string_exists(self):
        s = Square(1, 2, "3")
        self.assertIsInstance(s, Square)

    def test_square_with_four_arguments_exists(self):
        s = Square(1, 2, 3, 4)
        self.assertIsInstance(s, Square)

    def test_square_with_negative_size_exists(self):
        s = Square(-1)
        self.assertIsInstance(s, Square)

    def test_square_with_negative_x_exists(self):
        s = Square(1, -2)
        self.assertIsInstance(s, Square)

    def test_square_with_negative_y_exists(self):
        s = Square(1, 2, -3)
        self.assertIsInstance(s, Square)

    def test_square_with_zero_size_exists(self):
        s = Square(0)
        self.assertIsInstance(s, Square)

    def test_square_str_exists(self):
        s = Square(1)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 1")

    def test_square_to_dictionary_exists(self):
        s = Square(1)
        d = s.to_dictionary()
        expected_dict = {'id': 1, 'size': 1, 'x': 0, 'y': 0}
        self.assertDictEqual(d, expected_dict)

    def test_square_update_exists(self):
        s = Square(1)
        s.update(2)
        self.assertEqual(str(s), "[Square] (2) 0/0 - 1")

    def test_square_update_with_one_argument_exists(self):
        s = Square(1)
        s.update(89)
        self.assertEqual(str(s), "[Square] (89) 0/0 - 1")

    def test_square_update_with_two_arguments_exists(self):
        s = Square(1)
        s.update(89, 1)
        self.assertEqual(str(s), "[Square] (89) 0/0 - 1")

    def test_square_update_with_three_arguments_exists(self):
        s = Square(1)
        s.update(89, 1, 2)
        self.assertEqual(str(s), "[Square] (89) 2/0 - 1")

    def test_square_update_with_four_arguments_exists(self):
        s = Square(1)
        s.update(89, 1, 2, 3)
        self.assertEqual(str(s), "[Square] (89) 2/3 - 1")

    def test_square_update_with_dictionary_exists(self):
        s = Square(1)
        s.update(**{'id': 89})
        self.assertEqual(str(s), "[Square] (89) 0/0 - 1")

if __name__ == '__main__':
    unittest.main()
