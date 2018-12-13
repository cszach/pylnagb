"""
vector.py - Vector class

This is free and unencumbered software released into the public domain.
For more information, please refer to <http://unlicense.org>
"""
from raw import vectorutils as vct
from sys.lnagb_errors import DimensionError


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
            self.update_coord(newvector.vrepr(), newvector.__is_cartesian, updnew=False)

    def to_cartes(self):
        """
        Convert self to Cartesian coordinates if the current coordinates are
        Polar.

        :return: void
        """
        if self.__is_cartesian is False:
            self.__is_cartesian = True
            self.update_coord(vct.rec(self.vrepr()))

    def to_polar(self):
        """
        Convert self to Polar coordinates if the current coordinates are
        Cartesian.

        :return: void
        """
        if self.__is_cartesian is True:
            self.__is_cartesian = False
            self.update_coord(vct.pol(self.vrepr()))

    def add(self, vector):
        """

        :param vector:
        :return:
         """
        if vector.__dim != self.__dim:
            raise DimensionError("Cannot perform operations on vectors of different dimensional spaces")
        else:
            vector = vector.to_cartes()
            self.coord1 += vector.coord1
            self.coord2 += vector.coord2
            if self.coord3 is not None:
                self.coord3 += vector.coord3
