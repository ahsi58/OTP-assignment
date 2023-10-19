import unittest

# Import the generate_6_digit_number function from your number generation module
from mobile_generate import generate_10_digit_number

class TestNumberGeneration(unittest.TestCase):
    def test_generated_number_length(self):
        generated_number = generate_10_digit_number()
        self.assertEqual(len(str(generated_number)), 10)

    def test_generated_number_range(self):
        generated_number = generate_10_digit_number()
        self.assertTrue(1000000000 <= generated_number <= 9999999999)

if __name__ == "__main__":
    unittest.main()
