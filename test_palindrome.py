"""
Tests the palindrome module
"""
import unittest
from palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):

    def test_raises_value_error_for_non_string(self):
        with self.assertRaises(ValueError):
            is_palindrome(123)
