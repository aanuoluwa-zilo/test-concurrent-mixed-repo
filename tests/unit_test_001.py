import unittest

class TestUnit1(unittest.TestCase):
    def test_addition_1(self):
        self.assertEqual(1 + 1, 2)

    def test_multiplication_1(self):
        self.assertEqual(1 * 1, 1)

    def test_division_1(self):
        self.assertEqual(2 / 2, 1)