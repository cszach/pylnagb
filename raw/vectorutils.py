"""
vectorutils.py - Vector operations implemented for raw representations of
vectors which are Python lists or tuples. The operations work with 2D and 3D
vectors only. Vectors in other dimensional spaces are not supported.

The same operations but are implemented to work with objects of class Vector
are defined in the Vector class (see /assets/vector.py).

This is free and unencumbered software released into the public domain.
For more information, please refer to <http://unlicense.org>
"""
from sys import path as syspath
from math import sqrt, degrees, cos, sin, acos, atan, radians
syspath.insert(0, "../sys")
syspath.insert(0, "../assets")
from linagb_error import *
from coordsys import *


def validate_vector(obj, throwerr=False):
    """
    Given an object obj, check if it is a valid raw representation of a real
    mathematical vector. An accepted object would:
        1. be a Python list or Python tuple
        2. be 2 or 3 items in length

    :param obj: Test subject
    :param throwerr: Raise an error if the check returns false.
    :return: True if obj is a valid raw representation of mathematical vectors,
    False otherwise
    """
    if isinstance(obj, (list, tuple)) and 1 < len(obj) < 4:
        return True
    else:
        if throwerr:
            raise TypeError("A given object is not an accepted representation"
                            " of a vector (must be a Python list or tuple)")
        return False


def two_to_three(vector_2):
    """
    Convert a 2D Cartesian coordinated vector to a 3D Cartesian coordinated
    vector by setting z = 0.

    :param vector_2: Input vector.
    :return: Converted vector.
    """
    if validate_vector(vector_2, True):
        return vector_2 if len(vector_2) == 3 else vector_2 + [0]


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
    if not validate_vector(vector):
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
    if not validate_vector(vector):
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


def add_cartes(*args, fix_dim=False, base_dim=None):
    """
    Add multiple vectors. The coordinates are assumed to be Cartesian. If
    vectors of different dimensions are given, by default the function will
    raise a DimensionError and return an empty Python list. This behavior can
    be disabled by setting parameter fix_dim to True (it is False by default).
    A coordinate is added in the case of converting a 2D vector to a 3D one,
    and is removed in the opposite case. All 3D vectors will be converted to 2D
    vectors if the first vector given in the parameters is 2D and vice versa.

    :param args: Vectors to add
    :param fix_dim: Option to fix mismatching dimensions
    :param base_dim: If there are multiple vectors given, convert all vectors
    to base_dim coordinate system. The result vector will also be in this
    coordinate system. Valid values are either Cartesian or Cartesian_3 (these
    are classes). If base_dim is None, use the first vector given in args's
    coordinate system as base_dim
    :return: Result of adding. If any error occurs (mismatch dimensions, object
    not valid,...), an empty list ( [] ) is returned.
    """
    try:
        if validate_vector(args[0], True) and base_dim is None:
            base_dim = Cartesian if len(args[0]) == 2 else Cartesian_3
        elif base_dim not in (Cartesian, Cartesian_3):
            raise ValueError

        result = [0, 0] if base_dim == Cartesian else [0, 0, 0]

        for v in args:
            if validate_vector(v, True):
                if ((len(v) == 2 and base_dim == Cartesian_3)
                        or (len(v) == 3 and base_dim == Cartesian)) \
                        and not fix_dim:
                    raise DimensionError

                result[0] += v[0]
                result[1] += v[1]
                if base_dim == Cartesian_3 and len(v) == 3:
                    result[2] += v[2]

        return result
    except (TypeError, ValueError, DimensionError) as e:
        return []
