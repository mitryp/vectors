# encoding: utf-8
# module vectors2d
# from
"""Small module that adds class Vector2D and operations with vectors.

All functions take Vector2D. Also they take tuples or lists with len == 2 of int/float.
Vectors can be added, multiplied by other vector or by int/float and you can get angle between two vectors.

Vector2D + Vector2D -> sum_vectors() -> Vector2D
Vector2D * Vector2D -> scalar_mult_vectors() -> float
Vector2D * int/float -> mult_vector() -> Vector2D
get_angle(Vector2D, Vector2D) -> angle in radians

"""
from math import sqrt, acos


class Vector2D:
    def __init__(self, args=None):
        """Create vector

        Takes tuple or list of int/float with length == 2
        :param args: list or tuple with len == 2 of int/float default = [0,0]

        """
        if args is None:
            args = [0, 0]

        elif type(args) == type(self):
            self.x, self.y = args.x, args.y

        elif len(args) != 2:
            raise ValueError

        else:
            self.x, self.y = args[0], args[1]

    # TODO: Do +=, -=, *= etc

    def __getitem__(self, key: int):
        if key == 0:
            return self.x

        elif key == 1:
            return self.y

        else:
            raise IndexError

    def __setitem__(self, key: int, value: (int, float)):
    	if key == 0:
    		self.x = value
    	
    	elif key == 1:
    		self.y = value

    	else: 
    		raise IndexError

    def __abs__(self):
        """Absolute value of vector

        Returns absolute value of vector

        :return: float

        """

        return absolute_vector(self)

    def __eq__(self, other):
        if type(other) in (type(self), tuple, list):
            return self.vector() == Vector2D(other).vector()

        elif type(other) in (bool, int, float):
            return self.__abs__() == other

        else:
            return self == other

    def __add__(self, other):
        if type(other) in (type(self), tuple, list):
            return sum_vectors(self, other)
        else:
            raise TypeError

    def __sub__(self, other):
        if type(other) in (type(self), tuple, list):
            return sub_vectors(self, other)
        else:
            raise TypeError

    def __mul__(self, other):
        """
        Returns scalar multiplication of vectors or multiplies the vector by given number

        :param other: If Vector2D: returns scalar multiplication(int); if number: returns * (Vector)

        """

        if type(other) in (int, float):
            return mult_vector(self, other)

        elif type(other) in (type(self), list, tuple):
            return scalar_mult_vectors(self, other)

        else:
            raise TypeError

    def __call__(self):
        """
        :return: tuple(x, y)
        """
        return self.vector()

    def coords(self):
        """
        Returns two values vector coordinates: x and y

        :return: x, y
        """
        return self.x, self.y

    def vector(self):
        """
        Returns tuple of vector's coordinates.

        :return: tuple(x,y)
        """
        return tuple((self.x, self.y))


def absolute_vector(vector: (Vector2D, list, tuple)):
    """
    Calculates absolute value of given vector.

    :param vectors: Vector2D or list or tuple
    :return: float
    """
    if type(vector) is not Vector2D:
        vector = Vector2D(vector)

    return sqrt(vector[0] ** 2 + vector[1] ** 2)


def sum_vectors(*vectors: (Vector2D, list, tuple)):
    """
    Adds given vectors.

    :param vectors: Vector2D or list or tuple
    :return: Vector2D
    """
    result = [0, 0]
    for vector in vectors:
        if type(vector) is not Vector2D:
            vector = Vector2D(vector)

        result[0] += vector[0]
        result[1] += vector[1]

    return Vector2D(result)


def sub_vectors(*vectors: (Vector2D, list, tuple)):
    """
    Subtracts given vectors.

    :param vectors: Vector2D or list or tuple
    :return: Vector2D

    """
    result = None
    for vector in vectors:
        if type(vector) is not Vector2D:
            vector = Vector2D(vector)

        if not result:
            result = list(vector)

        else:
            result[0] -= vector[0]
            result[1] -= vector[1]

    return Vector2D(result)


def mult_vector(vector: (Vector2D, tuple, list), modifier: (int, float)):
    """
    Multiplies given vector by given number.

    :param vector: Vector2D or tuple or list
    :param modifier: must be number
    :return: Vector2D
    """
    if type(vector) is not Vector2D:
        vector = Vector2D(vector)

    return Vector2D((vector[0] * modifier, vector[1] * modifier))


def scalar_mult_vectors(*vectors: (Vector2D, list, tuple)):
    """
    Calculates scalar multiplication of given vectors.

    :param vectors: Vector2D or list or tuple
    :return: float
    """
    temp = [1, 1]
    for vector in vectors:
        if type(vector) is not Vector2D:
            vector = Vector2D(vector)

        temp[0] *= vector[0]
        temp[1] *= vector[1]

    result = 0.0
    for coordinate in temp:
        result += coordinate

    return result


def get_angle(vector1: (Vector2D, list, tuple), vector2: (Vector2D, list, tuple)):
    """
    Returns angle between two given vectors in radians.

    :param vector1: Vector2D or list or tuple
    :param vector2: Vector2D or list or tuple
    :return: float
    """
    if type(vector1) is not Vector2D:
        vector1 = Vector2D(vector1)

    if type(vector2) is not Vector2D:
        vector2 = Vector2D(vector2)

    result = scalar_mult_vectors(vector1(), vector2()) / (abs(vector1) * abs(vector2))  # cos of angle

    return acos(result)


def vector_from_dots(dot1: (tuple, list), dot2: (tuple, list)):
    """
    Creates vector from two given dots

    :param dot1: tuple or list
    :param dot2: tuple or list
    :return: Vector2D
    """
    if len(dot1) != 2 or len(dot2) != 2:
        raise TypeError

    else:
        vector = [0, 0]
        vector[0] = dot2[0] - dot1[0]
        vector[1] = dot2[1] - dot1[1]
        return Vector2D(vector)
