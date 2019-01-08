"""
vector.py - Vector class

This is free and unencumbered software released into the public domain.
For more information, please refer to <http://unlicense.org>
"""
from raw import vectorutils as vct
from sys import path as syspath
from coordsys import *
syspath.insert(0, "../sys")
from linagb_error import *
from numbers import Number


class Vector:
    def __init__(self, c1, c2, c3=None, dim=2, coordsys=Cartesian):
        """
        Initiate a Vector object

        :param c1: First coordinate (Cartesian: x ; Polar: r)
        :param c2: Second coordinate (Cartesian: y ; Polar: azimuthal/polar angle)
        :param c3: Third coordinate (Cartesian: z ; Polar: polar/azimuthal angle)
        :param dim: Number of dimensions (either 2 or 3)
        :param coordsys: Coordinate system of the coordinates
        """
        if not isinstance(c1, Number) or not isinstance(c2, Number) \
                or (not isinstance(c3, Number) and c3 is not None):
            raise TypeError("Input coordinate(s) is/are invalid")
        if not isinstance(dim, int) or isinstance(dim, bool):
            raise TypeError("Input dimension is invalid")
        if dim < 2 or dim > 3:
            raise TypeError("Module only supports 2-dimensional and 3-dimensional vectors")
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.__dim = dim
        if dim == 2: self.c3 = None
        if dim == 3 and self.c3 is None: self.c3 = 0
        self.__coordsys = coordsys

    def __repr__(self):
        """
        Text representation of vector _self_. Vector's elements are put between
        a pair of square brackets and are separated by a colon.

        :return: String representation of self
        """
        return "%s in %s" % \
               (self.list_repr().__repr__(), self.__coordsys.__repr__())

    def list_repr(self):
        """
        Array representation for the vector _self_.

        :return: The array representation of self.
        """
        return [self.coord1, self.coord2] if self.__dim == 2 else \
               [self.coord1, self.coord2, self.coord3]

    def update_coord(self, newvector, cartesian=None, updnew=True):
        """
        Update the coordinates of self vector to match those of newvector.

        :param newvector: New vector whose coordinates self should correspond to
        :param cartesian: Is newvector in Cartesian coordinates?
        :param updnew: If newvector is in a different coordinate system, and
        updnew is True, convert newvector to self's coordinate system,
        otherwise convert self to newvector's coordinate system
        :return: void
        """
        if cartesian is not None and cartesian != self.__is_cartesian and updnew:
            newvector = vct.rec(newvector) if self.__is_cartesian \
                else vct.pol(newvector)
        self.coord1 = newvector[0]
        self.coord2 = newvector[1]
        self.coord3 = None if len(newvector) == 2 else newvector[2]
        self.__dim = 2 if len(newvector) == 2 else 3
        if cartesian is not None and cartesian != self.__is_cartesian and not updnew:
            self.__is_cartesian = cartesian

    def copy(self, newvector):
        """
        Make self the same as newvector. This function is basically the same
        as Vector.update_coord(), but accepts a Vector class object instead of
        an array.

        :param newvector: A Vector object
        :return: void
        """
        if newvector.__class__.__name__ == "Vector":
            self.update_coord(newvector.list_repr(), newvector.__is_cartesian, updnew=False)

    def to_cartes(self):
        """
        Convert self to Cartesian coordinates if the current coordinates are
        Polar.

        :return: void
        """
        if self.__is_cartesian is False:
            self.__is_cartesian = True
            self.update_coord(vct.rec(self.list_repr()))

    def to_polar(self):
        """
        Convert self to Polar coordinates if the current coordinates are
        Cartesian.

        :return: void
        """
        if self.__is_cartesian is True:
            self.__is_cartesian = False
            self.update_coord(vct.pol(self.list_repr()))
