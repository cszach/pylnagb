# pylnagb - Python 3 module for Linear Algebra operations
#
# This is free and unencumbered software released into the public domain.
# For more information, please refer to <http://unlicense.org>

import vectorutils


class Vector:
    def __init__(self, coord1, coord2, coord3=None, dim=2, cartesian=True):
        """
        Initiate a Vector object

        :param coord1: First coordinate (Cartesian: x ; Polar: r)
        :param coord2: Second coordinate (Cartesian: y ; Polar: azimuthal angle)
        :param coord3: Third coordinate (Cartesian: z ; Polar: polar angle)
        :param dim: Number of dimensions (either 2 or 3)
        :param cartesian: Are the coordinates Cartesian or Polar?
        """
        self.coord1 = coord1
        self.coord2 = coord2
        self.coord3 = coord3
        self.__dim = dim
        if coord3 is not None: self.__dim = 3
        elif dim == 3: self.coord3 = 0
        self.__is_cartesian = cartesian

        # Vector as represented by an array
        self.__vrepr = [coord1, coord2] if self.__dim == 2 else \
                       [coord1, coord2, coord3]

    def __repr__(self):
        return "[%.10f, %.10f%s]" %\
               (self.coord1, self.coord2,
                ", %.10f" % self.coord3 if self.__dim == 3 else "")

    def to_cartes(self):
        """
        Convert self to Cartesian coordinates if the current coordinates are
        Polar.

        :return:
        """
        if self.__is_cartesian is False:
            cvect = vectorutils.rec(self.__vrepr)
            self.coord1 = cvect[0]
            self.coord2 = cvect[1]
            self.coord3 = None if self.__dim == 2 else cvect[2]

    def to_polar(self):
        """
        Convert self to Polar coordinates if the current coordinates are
        Cartesian.

        :return:
        """
        if self.__is_cartesian is True:
            cvect = vectorutils.pol(self.__vrepr)
            self.coord1 = cvect[0]
            self.coord2 = cvect[1]
            self.coord3 = None if self.__dim == 2 else cvect[2]
