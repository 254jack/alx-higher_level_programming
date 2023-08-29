#!/usr/bin/python3
""" a module that define size of a square """


prev_square = __import__("1-square").Square


class Square(prev_square):
    """ a class that defines a square
    Args:
        prev_square (class): a class that defines the size of the square
    """

    def __init__(self, size=0):
        """instantiation the square

        Args:
            size (int): the size of the square passed. Set to 0.

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        prev_square.__size = size
        self.__size = prev_square.__size

        if type(prev_square.__size) != int:
            raise TypeError('size must be an integer')
        elif prev_square.__size < 0:
            raise ValueError('size must be >= 0')
