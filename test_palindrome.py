"""
Tests the palindrome module
"""
import unittest
from palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):

#Test 1
    def test_raises_value_error_for_non_string(self):
        with self.assertRaises(ValueError):
            is_palindrome(123)

#Test 2
    def test_empty_string_returns_false(self):
        self.assertFalse(is_palindrome(""))