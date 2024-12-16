import unittest

from ..mystery_2 import mystery_2

class TestMystery2(unittest.TestCase):
    """Test the mystery_2 function."""

    def test_empty_list(self):
        """It should return None for an empty list."""
        self.assertIsNone(mystery_2([]))

    def test_single_element_list(self):
        """It should return 1 for a list with one element."""
        self.assertEqual(mystery_2([5]), 1)

    def test_multiple_elements_list(self):
        """It should return the length of a list with multiple elements."""
        self.assertEqual(mystery_2([1, 2, 3]), 3)

    def test_string_elements(self):
        """It should return the length of a list with string elements."""
        self.assertEqual(mystery_2(['a', 'b', 'c']), 3)

    def test_mixed_elements(self):
        """It should return the length of a list with mixed data types."""
        self.assertEqual(mystery_2([1, 'two', 3.0]), 3)

    def test_none_type_in_list(self):
        """It should return 1 for a list containing None as an element."""
        self.assertEqual(mystery_2([None]), 1)


if __name__ == '__main__':
    unittest.main()
