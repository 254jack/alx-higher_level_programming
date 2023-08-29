#!/usr/bin/python3
""" a module that define the area of square """


class Square():
    """ a class that calculate area of the square
    """

    def __init__(self, size=0):
        """Instantiation ot the square

        Args:
            size (int): the size of the square passed. Set to 0.

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        self.__size = size
        if type(self.__size) != int:
            raise TypeError('size must be an integer')
        elif self.__size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """ calculates the area of the square

        Returns:
            int: the area of the square
        """
        return self.__size**2
