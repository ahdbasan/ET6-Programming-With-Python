import unittest

from ..mystery_8 import mystery_8

class TestMystery8(unittest.TestCase):
    """ """

    def test_minimal_input(self):
        """"""
        self.assertEqual(mystery_8([], ''), [])
    
    def test_1(self):
        """"""
        actual = mystery_8(['apple','banana','cherry'], 'a')
        expected = ['apple','banana']
        self.assertEqual(actual, expected)

    def test_2(self):
        """"""
        actual = mystery_8([1,2,2,3,4,5],'2')
        expected = [2,2]
        self.assertEqual(actual, expected)

    def test_3(self):
        """"""
        actual = mystery_8(["hello","world","help","hold"],'hel')
        expected = ['hello','help']
        self.assertEqual(actual, expected)

    def test_4(self):
        """"""
        actual = mystery_8([1,3,5,7],'2')
        expected = []
        self.assertEqual(actual, expected)
