import unittest
import math
from app import (
    is_valid_email,
    is_palindrome,
    calculate_circle_area,
    convert_date,
    filter_even_numbers
)

# Testy funkcji is_palindrome
class TestIsPalindrome(unittest.TestCase):

    def setUp(self):
        self.valid = ["kajak", "A to idiota", "Kobyła ma mały bok"]
        self.invalid = ["Python", "Test test"]

    def test_valid_palindromes(self):
        for text in self.valid:
            with self.subTest(text=text):
                self.assertTrue(is_palindrome(text))

    def test_invalid_palindromes(self):
        for text in self.invalid:
            with self.subTest(text=text):
                self.assertFalse(is_palindrome(text))
                self.assertNotEqual(is_palindrome(text), True)

    def test_empty_and_single_char(self):
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("a"))

# Testy funkcji is_valid_email
class TestIsValidEmail(unittest.TestCase):

    def setUp(self):
        self.valid = ["test@example.com", "john.doe@domain.pl", "a@b.co"]
        self.invalid = ["testexample.com", "user@.com", "@example.com"]

    def test_valid_emails(self):
        for email in self.valid:
            with self.subTest(email=email):
                self.assertTrue(is_valid_email(email))

    def test_invalid_emails(self):
        for email in self.invalid:
            with self.subTest(email=email):
                self.assertFalse(is_valid_email(email))

    def test_empty_email(self):
        self.assertFalse(is_valid_email(""))

# Testy funkcji calculate_circle_area
class TestCalculateCircleArea(unittest.TestCase):

    def test_typical_radius(self):
        self.assertAlmostEqual(calculate_circle_area(1), math.pi)
        self.assertAlmostEqual(calculate_circle_area(2), math.pi * 4)

    def test_zero_radius(self):
        self.assertEqual(calculate_circle_area(0), 0)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            calculate_circle_area(-1)

# Testy funkcji convert_date
class TestConvertDate(unittest.TestCase):

    def test_valid_dates(self):
        self.assertEqual(convert_date("2024-05-02"), "02/05/2024")
        self.assertEqual(convert_date("1999-12-31"), "31/12/1999")

    def test_invalid_format(self):
        with self.assertRaises(ValueError):
            convert_date("02-05-2024")

    def test_empty_date_string(self):
        with self.assertRaises(ValueError):
            convert_date("")

# Testy funkcji filter_even_numbers
class TestFilterEvenNumbers(unittest.TestCase):

    def test_typical_even_filtering(self):
        self.assertEqual(filter_even_numbers([1, 2, 3, 4, 5, 6]), [2, 4, 6])

    def test_no_even_numbers(self):
        self.assertEqual(filter_even_numbers([1, 3, 5]), [])

    def test_empty_list(self):
        self.assertEqual(filter_even_numbers([]), [])

    def test_all_even_numbers(self):
        self.assertEqual(filter_even_numbers([2, 4, 6, 8]), [2, 4, 6, 8])


