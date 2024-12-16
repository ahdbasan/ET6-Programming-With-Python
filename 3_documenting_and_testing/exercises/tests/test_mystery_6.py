import unittest

from ..mystery_6 import mystery_6

class TestMystery6(unittest.TestCase):
    """ """

    def test_minimal_input(self):
        """"""
        self.assertEqual(mystery_6(0, 0), [])

    def test_small_input(self):
        """"""
        actual = mystery_6(0, 1 )  # call function with test arguments
        expected = []  # hand-write the expected return value
        self.assertEqual(actual, expected)
    
    def test_big_input(self):
        """"""
        actual = mystery_6(5, 8)  # call function with test arguments
        expected = [8, 9, 10, 11, 12]  # hand-write the expected return value
        self.assertEqual(actual, expected)
    
    def test_negative_start(self):
        """"""
        actual = mystery_6(-3, 4)  # call function with test arguments
        expected = []  # hand-write the expected return value
        self.assertEqual(actual, expected)
    
    def test_postive_start(self):
        """"""
        actual = mystery_6(3,-2)  # call function with test arguments
        expected = [-2,-1,0]  # hand-write the expected return value
        self.assertEqual(actual, expected)
    
    
    def test_both_negative_input(self):
        """"""
        actual = mystery_6(-3,-1 )  # call function with test arguments
        expected = []  # hand-write the expected return value
        self.assertEqual(actual, expected)
    
    
    
if __name__ == "__main__":
    unittest.main()    
