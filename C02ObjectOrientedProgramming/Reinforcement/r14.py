# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import collections


class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self, d):
        if isinstance(d, int):
            self._coords = [0] * d
        else:
            try:                                     # we test if param is iterable
                self._coords = [val for val in d]
            except TypeError:
                raise TypeError('invalid parameter type')

    def __len__(self):
        """Return the dimension of the vector."""
        return len(self._coords)

    def __getitem__(self, j):
        """Return jth coordinate of vector."""
        return self._coords[j]

    def __setitem__(self, j, val):
        """Set jth coordinate of vector to given value."""
        self._coords[j] = val

    def __add__(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other):          # relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))           # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __radd__(self, other):
        """Return sum of two vectors."""
        return self + other

    def __sub__(self, other):
        """Return difference of two vectors."""
        if len(self) != len(other):          # relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))           # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __mul__(self, other):
        """Return the multiplication of a vector and a scalar."""
        assert isinstance(other, (float, int, Vector)), f"can't multiply Vector and {type(other)}"
        if isinstance(other, Vector):
            return Vector(a * b for a, b in zip(self, other))
        else:
            return Vector(e * other for e in self)

    def __rmul__(self, other):
        """Return the multiplication of a scalar and a vector."""
        return self * other

    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""
        return self._coords == other._coords

    def __ne__(self, other):
        """Return True if vector differs from other."""
        return not self == other             # rely on existing __eq__ definition

    def __str__(self):
        """Produce string representation of vector."""
        return '<' + str(self._coords)[1:-1] + '>'  # adapt list representation

    def __neg__(self):
        """Return copy of vector with all coordinates negated."""
        return Vector(-e for e in self)

    def __lt__(self, other):
        """Compare vectors based on lexicographical order."""
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        return self._coords < other._coords

    def __le__(self, other):
        """Compare vectors based on lexicographical order."""
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        return self._coords <= other._coords


if __name__ == '__main__':
    # the following demonstrates usage of a few methods
    v = Vector(5)              # construct five-dimensional <0, 0, 0, 0, 0>
    v[1] = 23                  # <0, 23, 0, 0, 0> (based on use of __setitem__)
    v[-1] = 45                 # <0, 23, 0, 0, 45> (also via __setitem__)
    print(v[4])                # print 45 (via __getitem__)
    u = v + v                  # <0, 46, 0, 0, 90> (via __add__)
    print(u)                   # print <0, 46, 0, 0, 90>

    # Substraction test
    print("--- Substration ---")
    u[3] = 69
    print(u, v)
    print(u - v)

    # Negation test
    print("--- Negation ---")
    print(u)
    print(-u)

    # Right addition test
    print("--- Right addition ---")
    print(u, [1, 2, 3, 4, 5])
    print(u + [1, 2, 3, 4, 5])
    print([1, 2, 3, 4, 5] + u)

    # Scalar multiplication test
    print("--- Scalar multiplication ---")
    print(u, 3, u * 3)
    print(3.5, u, 3.5 * u)
    try:
        print("wesh", u, "wesh" * u)
    except Exception as e:
        print(e)

    # Vector multiplication test
    print("--- Vector multiplication ---")
    print(u, v, u * v)
    print(v, u, v * u)
