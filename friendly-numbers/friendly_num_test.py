import unittest
from friendly_num import fun


class FriendlyNumTestCase(unittest.TestCase):
    def test_friendly_1(self):
        lower = 200
        upper = 300
        result = fun(lower, upper)
        expected = (220, 284)
        self.assertEqual(result, expected)

    def test_friendly_2(self):
        lower = 1183
        upper = 1220
        result = fun(lower, upper)
        expected = (1184, 1210)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
