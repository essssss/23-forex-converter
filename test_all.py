from app import app
from calculations import conversion_function, invalidate_cur_code, append_symbol
from unittest import TestCase


class CalculationsTestCase(TestCase):
    def test_conversion(self):
        self.assertEqual(conversion_function('USD', 'USD', 1), 1)
        self.assertEqual(conversion_function('USD', 'USD', 1.006), 1.01)

    def test_symbol(self):
        self.assertEqual(append_symbol('USD', 1), "$1")
        self.assertEqual(append_symbol('JPY', 1), "¥1")
        self.assertEqual(append_symbol('DKK', 1), "1 Kr")

    def test_invalidate(self):
        self.assertEqual(invalidate_cur_code("USD"), False)
        self.assertEqual(invalidate_cur_code("usd"), False)
        self.assertEqual(invalidate_cur_code("XYZ"), True)
