import unittest
import check_number


class TestCalculator(unittest.TestCase):
    def test_when_output_true(self):
        # Tests for is_even() function with an even number as argument
        self.assertTrue(check_number.is_even(4))
        self.assertTrue(check_number.is_even(0))

    def test_when_output_false(self):
        # Tests for is_even() function with an odd number as argument
        self.assertFalse(check_number.is_even(3))
        self.assertFalse(check_number.is_even(-1))


if __name__ == "__main__":
    unittest.main()
