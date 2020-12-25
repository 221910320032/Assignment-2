"""Manhattan distance
Given integers x0, y0, x1 and y1 return the sum of the absolute
differences of their Cartesian coordinates(x0, y0) and (x1, y1).

Example 1
Input
x0 = 0
y0 = 1
x1 = 3
y1 = 2

Output
4

Explanation
abs(3 - 0) + abs(2 - 1) = 4
"""


import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def manhattan_distance(x0, y0, x1, y1):
    return(abs(x0-x1) + abs(y0-y1))
    


# DO NOT TOUCH THE BELOW CODE
# pylint: disable=unused-variable
class TestManhattanDistance(unittest.TestCase):

    def test_01(self):
        self.assertEqual(manhattan_distance(0, 1, 3, 2), 4)

    def test_02(self):
        self.assertEqual(manhattan_distance(3, 5, 6, 1), 7)

    def test_03(self):
        self.assertEqual(manhattan_distance(5, 5, 5, 5), 0)

    def test_04(self):
        self.assertEqual(manhattan_distance(24, 23, 25, 18), 6)

    def test_05(self):
        self.assertEqual(manhattan_distance(131, 333, 479, 297), 384)

    def test_06(self):
        self.assertEqual(manhattan_distance(145, 311, 261, 145), 282)

    def test_07(self):
        self.assertEqual(manhattan_distance(283, 861, 251, 806), 87)

    def test_08(self):
        self.assertEqual(manhattan_distance(583, 254, 564, 167), 106)


if __name__ == '__main__':
    unittest.main(verbosity=2)
