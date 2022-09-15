"""
Author: Indhu Cimbali Suresh
CWID:10478874
Date: 14 September 2022
Objective: In this assignment is to test triangle classification
"""

import unittest
import math

class TestTriangles(unittest.TestCase):

    def test_classify_triangle_success(self): # test valid inputs
        self.assertEqual(classify_triangle(3, 5, 4),'Scalene Right','(3, 4, 5) is a Scalene Right Triangle')
        self.assertEqual(classify_triangle(4, 4, 5), 'Isosceles', '(4, 4, 5) is an Isosceles Triangle')
        self.assertEqual(classify_triangle(1.2, 3.4, 4.5), 'Scalene', '(1.2, 3.4, 4.5) is a Scalene Triangle')
        self.assertEqual(classify_triangle(5, 5, 5), 'Equilateral', '(5, 5, 5) is an Equilateral Triangle')

    def test_classify_triangle_failure(self): # test invalid inputs
        self.assertEqual(classify_triangle(0, 0, 0), 'Not a triangle')
        self.assertEqual(classify_triangle(-3, -4, -5), 'Not a triangle')
        self.assertEqual(classify_triangle(0, 1, 2), 'Not a triangle', '(0, 1, 2) is not a valid triangle')
        self.assertEqual(classify_triangle(1, 5, 1), 'Not a triangle', '(1, 5, 1) is not a valid triangle')
        self.assertEqual(classify_triangle(-1, 0.5, 0.8), 'Not a triangle', '(-1, 0.5, 0.8) is not a valid triangle')
        self.assertEqual(classify_triangle(1, 0.5, 0), 'Not a triangle')
        self.assertEqual(classify_triangle('a', 'b', 'c'), 'Not a triangle')
        self.assertEqual(classify_triangle([3, 4, 5], (3, 4, 5), 3), 'Not a triangle')

    def test_classify_triangle_intentionalBug(self): # This test fails because python thinks (5*sqrt(2))^2 != 50, example of buggy code
        self.assertEqual(classify_triangle(5, 5, 5 * math.sqrt(2)), 'Isosceles Right', "(5*sqrt(2))^2 doesn't exactly equal 5^2 + 5^2")

def classify_triangle(a, b, c):
    '''Returns what kind of triangle lengths a, b, and c produce'''
    def correct_type(var):
        '''Helper function to check input validity'''
        return type(var) == int or type(var) == float

    if not(correct_type(a)) or not(correct_type(b)) or not(correct_type(c)) or a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
        return "Not a triangle"

    triangleType = ''
    if a == b == c:
        triangleType += "Equilateral"
    elif a == b != c or a != b == c:
        triangleType += "Isosceles"
    else:
        triangleType += "Scalene"

    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        triangleType += " Right"

    return triangleType

def main():
    inputs = [(3,4,5), (2,2,3), (4,4,4), (5,4,5), (-0.5, 2, 3)]
    for input in inputs:
        print(f'{input} is {classify_triangle(input[0], input[1], input[2])}.')
    
    unittest.main(exit=True)
    

if __name__ == "__main__":
    main()