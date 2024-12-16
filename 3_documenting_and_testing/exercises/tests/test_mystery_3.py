import unittest

from ..mystery_3 import mystery_3 

class TestMystery3(unittest.TestCase):
    """ Test mystery_3 function"""

    def test_0(self):
        """Test when a is smaller than b."""
        self.assertEqual(mystery_3(2, 5), 2)

    def test_1(self):
        """Test when a is greater than b."""
        self.assertEqual(mystery_3(10, 3), 3)

    def test_2(self):
        """Test when a is equal to b."""
        self.assertEqual(mystery_3(4, 4), 8)

    def test_3(self):
        """Test when a and b are floats."""
        self.assertEqual(mystery_3(2.5, 5.5), 2.5)
        self.assertEqual(mystery_3(6.7, 6.7), 13.4)

    def test_4(self):
        """Test when a is an int and b is a float, or vice versa."""
        self.assertEqual(mystery_3(3, 3.0), 6.0)
        self.assertEqual(mystery_3(2.5, 2), 2)

if __name__ == "__main__":
    unittest.main()
