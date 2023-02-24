#!/usr/bin/python3
"""
    Module of unit tests for the Base class.
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """These tests ensure that the Base class behaves
    correctly and has the expected functionality."""

    def test_contructor(self):
        """Test that a new instance of Base can be created
        and is an instance of the Base class."""
        dummy = Base()
        self.assertIsInstance(dummy, Base)

    def test_id_none(self):
        """Test of Base() for assigning automatically
        an ID + 1 of the previous exists"""
        base1 = Base(None)
        self.assertEqual(base1.id, 2)

    def test_assignment_id(self):
        """Verify that the id passed to the instance is equal to"""
        base1 = Base(25)
        self.assertEqual(base1.id, 25)

    def test_to_json_string(self):
        """Test verifies that the method exists"""
        base2 = Base()
        list = base2.to_json_string(None)
        self.assertEqual(list, [])


if __name__ == '__main__':
    unittest.main()
