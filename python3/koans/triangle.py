#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    try:
        if a <= 0:
            raise TriangleError('sides must be greater than 0')
        elif b <= 0:
            raise TriangleError('sides must be greater than 0')
        elif c <= 0:
            raise TriangleError('sides must be greater than 0')
        elif a + b <= c:
            raise TriangleError('sides must be greater than 0')
        elif a + c <= b:
            raise TriangleError('sides must be greater than 0')
        elif b + c <= a:
            raise TriangleError('sides must be greater than 0')
    except TriangleError as err:
        raise err

    if a == b == c:
        return 'equilateral'
    elif a == b:
        return 'isosceles'
    elif b == c:
        return 'isosceles'
    elif a == c:
        return 'isosceles'
    else:
        return 'scalene'
# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass