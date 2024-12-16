import unittest

from ..mystery_7 import mystery_7

class TestMystery7(unittest.TestCase):
    """ """

    def test_minimal_input_list(self):
        """"""
        self.assertEqual(mystery_7([], []), [])

    def test_minimal_input_string(self):
        """"""
        self.assertEqual(mystery_7('', ''), [])
    
    def test_1(self):
        """"""
        actual = mystery_7([10,21,35,42,51,63,74],'2')
        expected = [21,42]
        self.assertEqual(actual, expected)
    
    def test_tuples(self):
        actual = mystery_7([(1, 2), (3, 4), (5, 2)], '2')
        expected =[(1, 2), (5, 2)]
        self.assertEqual(actual,expected)
