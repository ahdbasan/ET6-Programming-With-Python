import unittest

from ..mystery_5 import mystery_5

class TestMystery5(unittest.TestCase):
    """ """

    def test_minimal_input(self):
        """"""
        self.assertEqual(mystery_5([], []), [])

    def test_minimal_input_none(self):
        """"""
        self.assertEqual(mystery_5([], None), [])

    def test_minimal_input_default_argument(self):
        """"""
        self.assertEqual(mystery_5([]), [])

    def test__(self):
        """"""
        self.assertEqual(mystery_5(['n','a','m','e'],[]), ['a','e','m','n'])
        
    def test_1(self):    
        """"""
        actual= mystery_5(['Ahd','Aseel', '1', '1a'])
        expected = ['1', '1a', 'Ahd','Aseel']
        self.assertEqual(actual,expected)

    def test_2(self):    
        """"""
        actual= mystery_5([3,1,1,2])
        expected = [1,1,2,3]
        self.assertEqual(actual,expected)
