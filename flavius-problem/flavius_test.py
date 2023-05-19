import unittest
from flavius import fun

class FlaviusTestCase(unittest.TestCase):
    def test_flav_1(self):
        n = 7
        result = fun(n)
        expected = 7
        self.assertEqual(result, expected)

    def test_flav_2(self):
        n = 2
        result = fun(n)
        expected = 1
        self.assertEqual(result, expected)

    def test_flav_3(self):
        n = 13
        result = fun(n)
        expected = 11
        self.assertEqual(result, expected)

    def test_flav_4(self):
        n = 10
        result = fun(n)
        expected = 5
        self.assertEqual(result, expected)

    def test_flav_5(self):
        n = 40
        result = fun(n)
        expected = 17
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
