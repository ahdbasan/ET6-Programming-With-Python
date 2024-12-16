import unittest

from ..mystery_4 import mystery_4

class TestMystery4(unittest.TestCase):
    """ Test the function of mystery_4"""

    def test_zero_case(self):
        """"""
        self.assertEqual(mystery_4(0), [])

    def test_integer_number(self):
        """It should evaluate 0 to 1"""
        actual = mystery_4(1)
        expected = [0]
        self.assertEqual(actual, expected)
        
    def test_negative_input(self):
        with self.assertRaises(AssertionError):
            mystery_4(-1)  

    def test_normal_case(self):
        """It should evaluate 0 to 1"""
        actual = mystery_4(5)
        expected = [0,1,2,3,4] 
        self.assertEqual(actual, expected) 

    def test_non_integer_input(self):
        with self.assertRaises(AssertionError):
            mystery_4(3.5)
