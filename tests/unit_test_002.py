import unittest

class TestUnit2(unittest.TestCase):
    def test_addition_2(self):
        self.assertEqual(2 + 2, 4)

    def test_multiplication_2(self):
        self.assertEqual(2 * 2, 4)

    def test_division_2(self):
        self.assertEqual(4 / 2, 2)