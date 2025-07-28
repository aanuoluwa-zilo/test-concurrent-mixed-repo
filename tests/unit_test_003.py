import unittest

class TestUnit3(unittest.TestCase):
    def test_addition_3(self):
        self.assertEqual(3 + 3, 6)

    def test_multiplication_3(self):
        self.assertEqual(3 * 3, 9)

    def test_division_3(self):
        self.assertEqual(6 / 2, 3)