"""
vectorutils.py - Vector operations implemented for raw representation of vectors
which are Python lists or tuples or any iterable that works with len() and
numeric indexing. The operations work with 2D and 3D vectors only. Vectors in
other dimensional spaces are not supported.

The same operations but are implemented to work with objects of class Vector
are defined in the Vector class (see /assets/vector.py).

This is free and unencumbered software released into the public domain.
For more information, please refer to <http://unlicense.org>
"""
from math import sqrt, degrees, cos, sin, acos, atan, radians


def rec(vector):
    """
    Given a vector expressed in Polar coordinates, return the equivalence
    in Cartesian coordinates. Works for 2D or 3D vectors.

    :param vector: Vector with Polar coordinates
    :return: Equivalence of input vector in Cartesian coordinates
    """
    try:
        sin_lat = sin(radians(vector[1]))
        cos_lat = round(cos(radians(vector[1])))
        if len(vector) == 2:
            return [vector[0] * cos_lat,
                    vector[0] * round(sin_lat, 10)]
        elif len(vector) == 3:
            return [vector[0] * round(sin_lat * cos(radians(vector[2])), 10),
                    vector[0] * round(sin_lat * sin(radians(vector[2])), 10),
                    vector[0] * cos_lat]
        else: return []
    except ValueError:
        return []


def pol(vector, physics=False):
    """
    Given a vector expressed in Cartesian coordinates, return the equivalence in
    Polar coordinates. For 3D vectors, return them in spherical coordinates,
    using the one often used in mathematics (not physics): azimuthal angle
    'theta' and polar angle 'phi'. If using the one often used in physics is
    interested, that can be done by setting the parameter 'physics' to True.

    :param vector: Vector with Cartesian coordinates
    :param physics: True if the output needs to be in physics's spherical
    coordinates (default: False); only used in conversions of 3D vectors
    :return: Equivalence of input vector in Polar/Spherical coordinates
    """
    try:
        if len(vector) == 2:
            if vector[0] == 0:
                ang = 90 if vector[1] > 0 else -90
            else:
                ang = degrees(atan(vector[1] / vector[0]))
            return [sqrt(vector[0] ** 2 + vector[1] ** 2), ang]
        elif len(vector) == 3:
            r = sqrt(vector[0] ** 2 + vector[1] ** 2 + vector[2] ** 2)
            if vector[0] != 0:
                azimuth = degrees(atan(vector[1] / vector[0]))
            else:
                azimuth = 90 if vector[1] > 0 else -90
            inclination = degrees(acos(vector[2] / r))
            if physics:
                # Return the result in spherical coordinates often used in
                # Physics
                return [r, inclination, azimuth]
            else:
                # Return the result in spherical coordinates often used in
                # Mathematics: The azimuth and inclination are swapped
                return [r, azimuth, inclination]
        else:
            return []
    except ValueError:
        return []


def add(*args):
    """
    Add vectors. The process involves converting both vectors to Cartesian
    coordinates (if necessary), add them, and then convert both vectors back
    to their original coordinate system.

    :param args: Vectors to add
    :return: Result of adding
    """


