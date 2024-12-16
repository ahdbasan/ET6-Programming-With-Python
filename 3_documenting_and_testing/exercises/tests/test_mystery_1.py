
import unittest

from ..mystery_1 import mystery_1


class TestMystery1(unittest.TestCase):
    """Test the mystery_1 function"""
    
    def test_0(self):
        """It should evaluate 0 and 0 to 0"""
        actual = mystery_1(0, 0)  # call function with test arguments
        expected = 0  # hand-write the expected return value
        self.assertEqual(actual, expected)

    def test_1(self):
        """It should evaluate 2 and 3 to 5"""
        actual = mystery_1(2, 3)
        expected = 5
        self.assertEqual(actual, expected)

    def test_2(self):
        """It should evaluate -1 and 4 to 3"""
        actual = mystery_1(-1, 4)
        expected = 3
        self.assertEqual(actual, expected)

# Run the tests
if __name__ == "__main__":
    unittest.main()
