"""Doctest for vector

    Test init from iterables
        >>> v1 = Vector([0, 1, 2])
        >>> v2 = Vector((0, 1, 2))
        >>> v3 = Vector(range(3))

    Test repr
        >>> v1
        Vector([0.0, 1.0, 2.0])
        >>> v3
        Vector([0.0, 1.0, 2.0])

    Test str
        >>> print(v2)
        (0.0, 1.0, 2.0)

    unpack
       >>> x, y, z = v1
       >>> x, y, z
       (0.0, 1.0, 2.0)

    eq tst
       >>> v1_clone = eval(repr(v1))
       >>> v1 == v1_clone
       True

    bytes tst
       >>> octets = bytes(v1)
       >>> octets
       b'd\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\xf0?\\x00\\x00\\x00\\x00\\x00\\x00\\x00@'

    abs tst
       >>> abs(v1)
       2.23606797749979

    bool tst
       >>> bool(v1), bool(Vector([0, 0, 0, 0]))
       (True, False)


    cls meth tst
        >>> v1_clone = Vector.frombytes(bytes(v1))
        >>> v1_clone
        Vector([0.0, 1.0, 2.0])
        >>> v1 == v1_clone
        True

    implement sequence proto
       >>> len(v1)
       3
       >>> v1[0], v1[-1]
       (0.0, 2.0)

    slicing
        >>> v1[1,2]
        Traceback (most recent call last):
          ...
        TypeError: Vector indices must be integers
        >>> v1[1]
        1.0
        >>> v1[1:4]
        Vector([1.0, 2.0])
        >>> v1[-1:]
        Vector([2.0])



"""

from array import array
import reprlib
import math
import numbers


class Vector:
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)])
                + bytes(self._components))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)
