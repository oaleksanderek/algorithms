import unittest
from dates_sort import fun


class DatesSTestCase(unittest.TestCase):
    def test_sort_1(self):
        dates = [{"day": 1, "month": 1, "year": 2005},
                 {"day": 20, "month": 12, "year": 2001},
                 {"day": 16, "month": 2, "year": 2003}]

        expected = [{"day": 20, "month": 12, "year": 2001},
                 {"day": 16, "month": 2, "year": 2003},
                 {"day": 1, "month": 1, "year": 2005}]

        result = fun(dates)
        self.assertEqual(result, expected)

    def test_sort_2(self):
        dates = [{"day": 6, "month": 2, "year": 2022},
                 {"day": 16, "month": 12, "year": 2000},
                 {"day": 16, "month": 2, "year": 2003},
                 {"day": 6, "month": 9, "year": 2003},
                 {"day": 27, "month": 5, "year": 1998}]

        expected = [{"day": 27, "month": 5, "year": 1998},
                 {"day": 16, "month": 12, "year": 2000},
                 {"day": 16, "month": 2, "year": 2003},
                 {"day": 6, "month": 9, "year": 2003},
                 {"day": 6, "month": 2, "year": 2022}]

        result = fun(dates)
        self.assertEqual(result, expected)

    def test_sort_3(self):
        dates = [{"day": 27, "month": 5, "year": 1998},
                 {"day": 11, "month": 9, "year": 2001},
                 {"day": 6, "month": 9, "year": 2003},
                 {"day": 16, "month": 2, "year": 2003},
                 {"day": 13, "month": 3, "year": 2023},
                 {"day": 1, "month": 4, "year": 966}]

        expected = [{"day": 1, "month": 4, "year": 966},
                 {"day": 27, "month": 5, "year": 1998},
                 {"day": 11, "month": 9, "year": 2001},
                 {"day": 16, "month": 2, "year": 2003},
                 {"day": 6, "month": 9, "year": 2003},
                 {"day": 13, "month": 3, "year": 2023}]

        result = fun(dates)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
