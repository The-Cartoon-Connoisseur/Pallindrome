"""
Validates strings as palindromes.
"""

from collections import deque

def is_palindrome(value: str) -> bool:
    if not  isinstance(value, str):
        raise ValueError("Input must be a string")

    if value == "":
        return False

    normalized = "".join(c.lower() for c in value if c.isalnum())

    char_deque = deque(normalized)

    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False

        return True