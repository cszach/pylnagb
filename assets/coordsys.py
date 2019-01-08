"""
coordsys.py - Coordinate systems as Python objects

This is free and unencumbered software released into the public domain.
For more information, please refer to <http://unlicense.org>
"""

import undefinedterms


class CoordSys:
    """
    Coordinate system prototype.
    """
    def __init__(self):
        self.ORIGIN = undefinedterms.Point("O", 0, 0)


class Cartesian(CoordSys):
    def __repr__():
        return "2-dimensional Cartesian coordinates system"


class Cartesian_3(CoordSys):
    def __repr__():
        return "3-dimensional Cartesian coordinates system"


class Polar(CoordSys):
    def __repr__():
        return "Polar coordinates system"


class PhySpherical(CoordSys):
    def __repr__():
        return "Spherical coordinates system (in Physics)"


class MathSpherical(CoordSys):
    def __repr__():
        return "Spherical coordinates system (in Mathematics)"
