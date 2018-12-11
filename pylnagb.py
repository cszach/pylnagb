# pylnagb - Python 3 module for Linear Algebra operations
#
# This is free and unencumbered software released into the public domain.
# For more information, please refer to <http://unlicense.org>

import vectorutils as vct


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

    def __repr__(self):
        """
        Text representation of vector _self_. Vector's elements are put between
        a pair of square brackets and are separated by a colon.

        :return: String representation of self
        """
        return "[%.10f, %.10f%s]" %\
               (self.coord1, self.coord2,
                ", %.10f" % self.coord3 if self.__dim == 3 else "")

    def vrepr(self):
        """
        Array representation for the vector _self_.

        :return: The array representation of self.
        """
        return [self.coord1, self.coord2] if self.__dim == 2 else \
               [self.coord1, self.coord2, self.coord3]

    def update_coord(self, newvector, cartesian = None):
        """
        Update the coordinates of self vector to match those of newvector. If
        newvector has a different coordinate system, convert it to self's
        coordinate system before matching.

        :param newvector: New vector whose coordinates self should correspond to
        :param cartesian: Is newvector in Cartesian coordinates?
        :return: void
        """
        if cartesian is not None and cartesian != self.__is_cartesian:
            newvector = vct.rec(newvector) if self.__is_cartesian \
                else vct.pol(newvector)
        self.coord1 = newvector[0]
        self.coord2 = newvector[1]
        self.coord3 = None if len(newvector) == 2 else newvector[2]
        self.__dim = 2 if len(newvector) == 2 else 3

    def to_cartes(self):
        """
        Convert self to Cartesian coordinates if the current coordinates are
        Polar.

        :return: void
        """
        if self.__is_cartesian is False:
            cvect = vct.rec(self.vrepr())
            self.coord1 = cvect[0]
            self.coord2 = cvect[1]
            self.coord3 = None if self.__dim == 2 else cvect[2]

    def to_polar(self):
        """
        Convert self to Polar coordinates if the current coordinates are
        Cartesian.

        :return: void
        """
        if self.__is_cartesian is True:
            cvect = vct.pol(self.vrepr())
            self.coord1 = cvect[0]
            self.coord2 = cvect[1]
            self.coord3 = None if self.__dim == 2 else cvect[2]
