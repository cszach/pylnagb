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


def pol(vector):
    """
    Given a vector expressed in Cartesian coordinates, return the equivalence in
    Polar coordinates.

    :param vector: Vector with Cartesian coordinates
    :return: Equivalence of input vector in Polar coordinates
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
            return [r, azimuth, degrees(acos(vector[2] / r))]
        else:
            return []
    except ValueError:
        return []
