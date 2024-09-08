from unittest import TestCase

from apps.cars.service import calc


class CalcTestCase(TestCase):
    def test_plus(self):
        result = calc(2, 3, "+")
        self.assertEqual(result, 5)

    def test_minus(self):
        result = calc(1, 2, "-")
        self.assertEqual(result, -1)

    def test_multi(self):
        result = calc(1, 2, "*")
        self.assertEqual(result, 2)
