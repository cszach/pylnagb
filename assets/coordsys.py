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
    def __init__(self, dimension):
        """
        :param dimension: Dimension of the coordinate system
        """
        self.ORIGIN = undefinedterms.Point("O", 0, 0)
        self.dimension = dimension


CARTES = CoordSys(2)
CARTES_3 = CoordSys(3)
POLAR = CoordSys(2)
SPHERICAL = CoordSys(3)
