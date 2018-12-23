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
from collections import Iterable


def validate_vector(obj, throwerr=False):
    """
    Given an object obj, check if it is iterable or otherwise will work with
    the operations implemented in this Python code file.

    :param obj: Test subject
    :param throwerr: Raise an error if the check returns false.
    :return: True if obj is a valid raw representation of mathematical vectors,
    False otherwise
    """
    if isinstance(obj, Iterable) and type(obj) is not str and 1 < len(obj) < 4:
        return True
    else:
        if throwerr:
            raise TypeError("A given object is not an accepted representation"
                            " of a vector")
        return False


def rec(vector, physics=False):
    """
    Given a vector expressed in Polar/Spherical coordinates, return the
    equivalence in Cartesian coordinates. If the vector is given in the
    spherical coordinates often used in physics, set parameter physics to True.

    :param vector: Vector with Polar or Spherical coordinates
    :param physics: True if the given vector is given in physics's Spherical
    coordinates, False (default) otherwise.
    :return: Equivalence of input vector in Cartesian coordinates. Empty Python
    list if the given object as parameter vector is not an acceptable vector
    representation.
    """
    if not validate_vector(vector, True):
        return []

    if len(vector) == 2:
        return [vector[0] * cos(radians(vector[1])),
                vector[0] * sin(radians(vector[1]))]
    else:
        inclin = vector[1] if physics else vector[2]
        azimuth = vector[2] if physics else vector[1]

        return [vector[0] * sin(radians(inclin)) * cos(radians(azimuth)),
                vector[0] * sin(radians(inclin)) * sin(radians(azimuth)),
                vector[0] * cos(radians(inclin))]


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
    :return: Equivalence of input vector in Polar/Spherical coordinates. Empty
    Python list if the value for parameter vector is not a valid vector
    representation.
    """
    if not validate_vector(vector, True):
        return []

    if len(vector) == 2:
        if vector[0] == 0:
            ang = 90 if vector[1] > 0 else -90
        else:
            ang = degrees(atan(vector[1] / vector[0]))
        return [sqrt(vector[0] ** 2 + vector[1] ** 2), ang]
    else:
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


