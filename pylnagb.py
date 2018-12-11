# pylnagb - Python 3 module for Linear Algebra operations
#
# This is free and unencumbered software released into the public domain.
# For more information, please refer to <http://unlicense.org>

from math import *

# Vectors shall be represented by Python arrays of numbers.
# Matrices shall be represented by arrays of arrays of numbers.


def __d_sin(x):
    """
    Return sine of x degrees

    :param x: Angle
    :return: Sine of x in degrees
    """
    return sin(radians(x))


def __d_cos(x):
    """
    Return cosine of x degrees.

    :param x: Angle
    :return: Cosine of x in degrees
    """
    return cos(radians(x))


def rec2(vector):
    """
    Given a vector expressed in 2D Polar coordinates, return the equivalence
    in Cartesian coordinates.

    :param vector: 2D vector with Polar coordinates
    :return: Equivalence of input vector in Cartesian coordinates
    """
    try:
        if len(vector) != 2:
            return []
    except TypeError:
        return []
    return [vector[0] * round(__d_cos(vector[1]), 10),
            vector[0] * round(__d_sin(vector[1]), 10)]


def pol2(vector):
    """
    Given a vector expressed in 2D Cartesian coordinates, return the equivalence
    in Polar coordinates.

    :param vector: 2D vector with Cartesian coordinates
    :return: Equivalence of input vector in Polar coordinates
    """
    try:
        if len(vector) != 2:
            return []
    except TypeError:
        return []
    if vector[0] != 0:
        ang = degrees(atan(vector[1] / vector[0]))
    else:
        ang = 90 if vector[1] > 0 else -90
    return [sqrt(vector[0] ** 2 + vector[1] ** 2), ang]
