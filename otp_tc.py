import unittest

# Import the generate_6_digit_number function from your number generation module
from otp_generate import generate_6_digit_number

class TestNumberGeneration(unittest.TestCase):
    def test_generated_number_length(self):
        generated_number = generate_6_digit_number()
        self.assertEqual(len(str(generated_number)), 6)

    def test_generated_number_range(self):
        generated_number = generate_6_digit_number()
        self.assertTrue(100000 <= generated_number <= 999999)

if __name__ == "__main__":
    unittest.main()
