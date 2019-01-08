from numbers import Number


class Equation:
    """
    A mathematic equation represented by a Python class.
    Equation are defined by coefficients. How many dependant variables and how
    those variables will pair with the coefficients depend on the type of
    equation.
    """

    def __init__(self, coefs):
        self._coefs = []
        if coefs.__class__.__name__ == "list":
            for coef in coefs:
                if isinstance(coef, Number):
                    self._coefs.append(coef)
                else:
                    break


class LinearEquation(Equation):
    """
    A linear equation of any number of variables.
    """

    def __repr__(self):
        if len(self._coefs) < 3:
            return "<Invalid Linear Equation>"
        if len(self._coefs) == 3:
            # Equation of a 2-dimensional graph
            return "%sx + %sy = %s" %\
                   (self._coefs[0], self._coefs[1], self._coefs[2])
        if len(self._coefs) == 4:
            # Equation of a 3-dimensional graph
            return "%sx + %sy + %sz = %s" % \
                   (self._coefs[0], self._coefs[1], self._coefs[2], self._coefs[3])

        # Equation of n variables where n = len(self._coefs) - 1
        equrep = ""
        for i in range(len(self._coefs) - 1):
            equrep += "%sx%d + " % (self._coefs[i], i + 1)
        return equrep[:-2] + ("= %s" % self._coefs[i + 1])


class SysLinEquation:
    """
    A system of linear equation. This is pretty much like a list of objects of
    type LinearEquation defined above in the same code file.
    """

    def __init__(self, linequs):
        self.equs = []
        if linequs.__class__.__name__ == "list":
            for i in linequs:
                if i.__class__.__name__ == "LinearEquation":
                    self.equs.append(i)
                else:
                    break

    def __repr__(self):
        result = ""
        for i in self.equs:
            result += "%s\n" % i.__repr__()
        return result[:-1]
