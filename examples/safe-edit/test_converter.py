import unittest

from converter import kilometers_to_miles


class ConverterTests(unittest.TestCase):
    def test_preserves_defined_conversion_factor(self):
        self.assertAlmostEqual(kilometers_to_miles(1), 0.621371, places=6)

    def test_zero_remains_zero(self):
        self.assertEqual(kilometers_to_miles(0), 0)


if __name__ == "__main__":
    unittest.main()
