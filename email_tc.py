import unittest

# Import the is_valid_email function from your email validation module
from email_validation import is_valid_email

class TestEmailValidation(unittest.TestCase):
    def test_valid_email(self):
        # Test with a valid email address
        valid_email = "user@example.com"  # Change this to a valid email address
        expected = True
        self.assertTrue(is_valid_email(valid_email),expected)

    def test_invalid_email(self):
        # Test with an invalid email address
        invalid_email = "invalid-email"  # Change this to an invalid email address
        self.assertFalse(is_valid_email(invalid_email))

if __name__ == "__main__":
    unittest.main()
