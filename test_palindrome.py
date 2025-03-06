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

#Test 3
    def test_single_character_returns_true(self):
        self.assertTrue(is_palindrome("a"))

#Test 4
    def test_two_identical_characters_returns_true(self):
        self.assertTrue(is_palindrome("bb"))

#Test 5
    def test_non_palindrome_string_returns_false(self):
        self.assertFalse(is_palindrome("abc"))

#Test 6
    def test_palindrome_word_returns_true(self):
        self.assertTrue(is_palindrome("laval"))

#Test 7
    def test_non_palindrome_word_returns_false(self):
        self.assertFalse(is_palindrome("toronto"))