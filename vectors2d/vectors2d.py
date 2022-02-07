# encoding: utf-8
# module vectors2d

"""Small module that adds class Vector2D and operations with vectors.

All functions take Vector2D. Also they take tuples or lists of int/float with len == 2.
Vectors can be added, subbed, multiplied by other vector or by int/float the angle between two vectors can be found.
===

abs(Vector2D) -> absolute_vector() -> float
Vector2D + Vector2D -> sum_vectors() -> Vector2D
Vector2D - Vector2D -> sub_vectors() -> Vector2D
Vector2D * Vector2D -> scalar_mult_vectors() -> float
Vector2D * int/float -> mult_vector() -> Vector2D
get_angle(Vector2D, Vector2D) -> angle in radians
===
Extended version of documentation can be found on GitHub: https://github.com/MitryP/vectors/
"""
from math import sqrt, acos, pi
from typing import Union


class Vector2D:
    def __init__(self, *args: Union[int, float, tuple, list, 'Vector2D']):
        """Create vector

        Takes tuple or list of int/float with length == 2
        :param args: list or tuple with len == 2 of int/float default = [0,0]
        """

        if len(args) == 0:
            args = [0, 0]
            self.vector = list(args)

        elif len(args) == 1:
            if type(args[0]) in [list, tuple]:
                self.vector = args[0]

            elif type(args[0]) is type(self):
                self.vector = args[0]()

            else:
                self.vector = [args[0], 0]

        elif len(args) > 2:
            raise TypeError

        else:
            if type(args[0]) in [int, float] and type(args[1]) in [int, float]:
                self.vector = list(args)

            else:
                raise TypeError

    def __getitem__(self, key: int) -> Union[float, int]:
        if key > len(self.vector) - 1 or key < -1:
            raise IndexError

        else:
            return self.vector[key]

    def __setitem__(self, key: int, value: Union[int, float]) -> None:
        if key > len(self.vector)-1 or key < -1:
            raise IndexError

        else:
            self.vector[key] = value

    def __abs__(self) -> float:
        """Absolute value of vector

        Returns absolute value of vector

        :return: float
        """

        return absolute_vector(self)

    def __eq__(self, other) -> bool:
        if type(other) in (type(self), tuple, list):
            return self.vector == Vector2D(other).vector

        elif type(other) in (bool, int, float):
            return self.__abs__() == other

        else:
            return self == other

    def __add__(self, other: Union[list, tuple, 'Vector2D']) -> 'Vector2D':
        if type(other) in (type(self), tuple, list):
            return sum_vectors(self, other)

        else:
            raise TypeError(f"Unsupported type '{other.__class__.__name__}' for addition operation.")

    def __sub__(self, other: Union[list, tuple, 'Vector2D']) -> 'Vector2D':
        if type(other) in (type(self), tuple, list):
            return sub_vectors(self, other)

        else:
            raise TypeError(f"Unsupported type '{other.__class__.__name__}' for subtraction operation.")

    def __mul__(self, other: Union[int, float, list, tuple, 'Vector2D']) -> Union['Vector2D', float]:
        """
        Returns scalar multiplication of vectors or multiplies the vector by given number

        :param other: If Vector2D: returns scalar multiplication(float); if number: returns * (Vector)
        :returns: If scalar_mult_vectors multiplication, returns float; If vector multiplication, returns Vector2D
        """

        if type(other) in (int, float):
            return mult_vector(self, other)

        elif type(other) in (type(self), list, tuple):
            return scalar_mult_vectors(self, other)

        else:
            raise TypeError(f"Unsupported type '{other.__class__.__name__}' for multiplication operation.")

    def __imul__(self, other: Union[int, float]) -> 'Vector2D':
        return mult_vector(self.vector, other)

    def __call__(self) -> tuple:
        """
        :return: tuple(x, y)
        """

        return tuple(self.vector)

    def __neg__(self) -> 'Vector2D':
        """
        Returns vector with negative coordinates of self.

        :return: Vector2D
        """

        result_vector = self.vector.copy()
        result_vector[0] *= -1
        result_vector[1] *= -1

        return Vector2D(result_vector)

    def is_zero(self) -> bool:
        """
        Check if the vector is zero vector.

        :return: bool
        """

        return self.vector[0] == 0 and self.vector[1] == 0

    def is_perpendicular_to(self, vector: Union[tuple, list, 'Vector2D']) -> bool:
        """
        Check if vector is perpendicular to the given vector.

        :param vector: Vector2D or list or tuple
        :return: bool
        """

        if type(vector) is not type(self):
            vector = Vector2D(vector)

        if self.is_zero() or vector.is_zero():
            return False

        if get_angle(self, vector) == pi/2:
            return True

        else:
            return False

    def is_parallel_to(self, vector: Union[tuple, list, 'Vector2D']) -> bool:
        """
        Check if vector is co-directional to the given vector.

        :param vector: Vector2D or list or tuple
        :return: bool
        """

        if type(vector) is not type(self):
            vector = Vector2D(vector)

        if self.is_zero() or vector.is_zero():
            return False

        elif get_angle(self, vector) in [0, pi]:
            return True

        else:
            return False

    def is_codirectional_to(self, vector: Union[tuple, list, 'Vector2D']) -> bool:
        """
        Check if vector is co-directed to given vector.

        :param vector: Vector2D or list or tuple
        :return: bool
        """

        if type(vector) is not type(self):
            vector = Vector2D(vector)

        if self.is_zero() or vector.is_zero():
            return False

        elif get_angle(self, vector) == 0:
            return True

        else:
            return False

    def __repr__(self) -> str:
        return f"<Vector2D {self.vector}>"


def absolute_vector(vector: Union[Vector2D, list, tuple]) -> float:
    """
    Calculates an absolute value of given vector.

    :param vector: Vector2D or list or tuple
    :return: float
    """

    if type(vector) is not Vector2D:
        vector = Vector2D(vector)

    return sqrt(vector[0] ** 2 + vector[1] ** 2)


def sum_vectors(*vectors: Union[Vector2D, list, tuple]) -> Vector2D:
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


def sub_vectors(*vectors: Union[Vector2D, list, tuple]) -> Vector2D:
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


def mult_vector(vector: Union[Vector2D, tuple, list], modifier: Union[int, float]) -> Vector2D:
    """
    Multiplies the given vector by the given number.

    :param vector: Vector2D or tuple or list
    :param modifier: must be number
    :return: Vector2D
    """

    if type(vector) is not Vector2D:
        vector = Vector2D(vector)

    return Vector2D((vector[0] * modifier, vector[1] * modifier))


def scalar_mult_vectors(*vectors: Union[Vector2D, list, tuple]) -> float:
    """
    Calculates a scalar multiplication of the given vectors.

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


def get_angle(vector1: Union[Vector2D, list, tuple], vector2: Union[Vector2D, list, tuple]) -> float:
    """
    Returns an angle between the two given vectors in radians.

    :param vector1: Vector2D or list or tuple
    :param vector2: Vector2D or list or tuple
    :return: float
    """

    if type(vector1) is not Vector2D:
        vector1 = Vector2D(vector1)

    if type(vector2) is not Vector2D:
        vector2 = Vector2D(vector2)

    if vector1.is_zero() or vector2.is_zero():
        return 0.0

    try:
        result = scalar_mult_vectors(vector1(), vector2()) / (abs(vector1) * abs(vector2))  # cos of angle
    except ZeroDivisionError:
        result = 1

    return round(acos(result), 5)


def vector_from_dots(dot1: Union[tuple, list], dot2: Union[tuple, list]) -> Vector2D:
    """
    Creates a vector from the two given dots

    :param dot1: tuple or list
    :param dot2: tuple or list
    :return: Vector2D
    """

    if len(dot1) != 2 or len(dot2) != 2:
        raise TypeError

    else:
        vector = [dot2[0] - dot1[0], dot2[1] - dot1[1]]

        return Vector2D(vector)
