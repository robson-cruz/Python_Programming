from string_to_lower import string_to_lower
import unittest


class TestStringToLower(unittest.TestCase):
    def test_string_to_lower(self):
        # Test for an exception one way
        self.assertRaises(ValueError, string_to_lower, 123)

        # testing for an exception another way
        with self.assertRaises(ValueError):
            string_to_lower(123)


if __name__ == "__main__":
    unittest.main()
