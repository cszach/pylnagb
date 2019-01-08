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
        if coordsys not in (Cartesian, Cartesian_3, Polar, PhySpherical, MathSpherical):
            raise TypeError("Invalid coordinate system")
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.__dim = dim
        if dim == 2:
            self.c3 = None
            if coordsys == Cartesian_3:
                self.__coordsys = Cartesian
            elif coordsys in (MathSpherical, PhySpherical):
                self.__coordsys = Polar
        if dim == 3:
            if self.c3 is None: self.c3 = 0
            if coordsys == Cartesian:
                self.__coordsys = Cartesian_3
            elif coordsys == Polar:
                self.__coordsys = MathSpherical

    def __repr__(self):
        """
        Text representation of vector _self_. Vector's elements are put between
        a pair of square brackets and are separated by a colon.

        :return: String representation of self
        """
        return "%s in %s" % \
               (self.lrepr().__repr__(), self.__coordsys.__repr__())

    def lrepr(self):
        """
        Array representation for the vector _self_.

        :return: The array representation of self.
        """
        return [self.coord1, self.coord2] if self.__dim == 2 else \
               [self.coord1, self.coord2, self.coord3]

    def update_coord(self, newvector, coordsys, conv_new_vct=True):
        """
        Update the coordinates of self to match those of newvector.

        :param newvector: New vector (in raw representation) whose coordinates
        self should correspond to
        :param coordsts: Coordinates system used by newvector
        :param conv_new_vct: If True, use self's coordinate system for the
        updated vector, otherwise use newvector's (coordsys)
        :return: void
        """
        vct.validate_vector(newvector, True)
        if coordsys not in (Cartesian, Cartesian_3, Polar, PhySpherical, MathSpherical):
            raise TypeError("Invalid coordinate system")
        if not isinstance(conv_new_vct, bool):
            raise TypeError

        if conv_new_vct and coordsys != self.__coordsys:
            if self.__coordsys in (Cartesian, Cartesian_3):
                newvector = vct.rec(newvector, coordsys == PhySpherical)
            if self.__coordsys in (PhySpherical, MathSpherical):
                newvector = vct.pol(newvector, self.__coordsys == PhySpherical)

        self.c1 = newvector[0]
        self.c2 = newvector[1]
        self.c3 = None if len(newvector) == 2 else newvector[2]

        if not conv_new_vct:
            self.__coordsys = coordsys

    def copy(self, newvector):
        """
        Make self the same as newvector. This function is basically the same
        as Vector.update_coord(), but accepts a Vector class object instead of
        a Python list.

        :param newvector: A Vector object
        :return: void
        """
        if isinstance(newvector, Vector):
            self.update_coord(newvector.lrepr(), newvector.__coordsys, False)
        else:
            raise TypeError("Input must be an instance of Vector")

    def to_cartes(self):
        """
        Convert self to Cartesian coordinates if the current coordinates are
        Polar/Spherical.

        :return: void
        """
        if self.__coordsys in (Polar, PhySpherical, MathSpherical):
            self.__coordsys = Cartesian if self.__coordsys == Polar else Cartesian_3
            self.update_coord(vct.rec(self.list_repr()))

    def to_polar(self, physics=False):
        """
        Convert self to Polar/Spherical coordinates if the current coordinates
        are Cartesian.

        :param physics: If True: Convert to Physic's Spherical coordinates,
        otherwise convert to Mathematics's Spherical coordinates
        :return: void
        """
        if self.__coordsys in (Cartesian, Cartesian_3):
            self.__coordsys = Polar if self.__coordsys == Cartesian \
                else PhySpherical if physics else MathSpherical
            self.update_coord(vct.pol(self.list_repr()))
