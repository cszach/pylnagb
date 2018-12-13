"""
undefinedterms.py - Geometry's undefined terms as Python objects

In geometry, undefined terms are the most basic shapes; Other shapes are created
using these undefined terms. Undefined terms are point, line, and plane.
This module implements point and line as classes and ignores planes.
"""

from numbers import Number
import equ


class Point:
    """
    Undefined mathematical term Point as a Python object.
    """

    def __init__(self, pname, a, b, c=None):
        if pname.__class__.__name__ != "str":
            raise ValueError("Point's name (pname) not of type str")
        elif len(pname) != 1 or not pname.isalpha():
            raise ValueError("Point's name must be a single alphabet letter")
        if not isinstance(a, Number) or not isinstance(b, Number):
            raise ValueError("Point's coordinates must be numbers")
        if c is not None and not isinstance(c, Number):
            raise ValueError("Point's coordinates must be numbers")
        self.name = pname
        self.a = a
        self.b = b
        self.c = None if c is None else c

    def __repr__(self):
        return "%s(%s, %s%s)" % (self.name, self.a, self.b,
                                 "" if self.c is None else ", %s" % self.c)


class Line:
    def __init__(self, equation):
        if equation.__class__.__name__ == "LinearEquation":
            self.equ = equation

    def __repr__(self):
        return "<line of equation %s>" % self.equ.__repr__()
