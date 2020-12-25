"""
Number of bits
Given an integer n greater than or equal to 0,
return the number of 1 bits in n.

Example 1
Input
n = 0

Output
0

Example 2
Input
n = 1

Output
1

Example 3
Input
n = 2

Output
1

Explanation
2 is 10 in binary.

Example 4
Input
n = 3

Output
2

Explanation
3 is 11 in binary.

Example 5
Input
n = 4

Output
1

Explanation
4 is 100 in binary.
"""

import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def number_of_bits(n):
    count=0
    while(n!=0):
        if(n%2==1):
            count=count+1
        n=n//2
    return count    


# DO NOT TOUCH THE BELOW CODE
# pylint: disable=unused-variable
class TestNumberOfBits(unittest.TestCase):

    def test_01(self):
        self.assertEqual(number_of_bits(0), 0)

    def test_02(self):
        self.assertEqual(number_of_bits(1), 1)

    def test_03(self):
        self.assertEqual(number_of_bits(2), 1)

    def test_04(self):
        self.assertEqual(number_of_bits(3), 2)

    def test_05(self):
        self.assertEqual(number_of_bits(4), 1)

    def test_06(self):
        self.assertEqual(number_of_bits(20), 2)

    def test_07(self):
        self.assertEqual(number_of_bits(32), 1)

    def test_08(self):
        self.assertEqual(number_of_bits(127), 7)

    def test_09(self):
        self.assertEqual(number_of_bits(1023), 10)

    def test_10(self):
        self.assertEqual(number_of_bits(8191), 13)


if __name__ == '__main__':
    unittest.main(verbosity=2)
