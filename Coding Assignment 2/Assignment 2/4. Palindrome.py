"""
Given a string s, return whether it is a palindrome. A palindrome is when the word is the same forwards and backwards.

For example, "tacocat" is a palindrome.

Example 1
Input

s = "racecar"
Output

Truee
"""
import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def palindrome(s):
    if(s == s[::-1]):
        return True
    else:
        return False



# DO NOT TOUCH THE BELOW CODE
# pylint: disable=unused-variable
class TestPalindrome(unittest.TestCase):

    def test_01(self):
        self.assertEqual(palindrome("racecar"), True)

    def test_02(self):
        self.assertEqual(palindrome("madam"), True)

    def test_03(self):
        self.assertEqual(palindrome("gitam"), False)

    def test_04(self):
        self.assertEqual(palindrome("global"), False)


if __name__ == '__main__':
    unittest.main(verbosity=2)
