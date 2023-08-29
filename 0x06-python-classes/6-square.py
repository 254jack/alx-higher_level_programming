#!/usr/bin/python3
""" a module of the coordinates of a square"""


class Square():
    """ a class that defines a square by: (based on 5-square.py)
    """

    def __init__(self, size=0, position=(0, 0)):
        """Instantiation square

        Args:
            size (int): the size of the square passed. Set to 0.

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        self.__size = size
        self.__position = position
        error = 'position must be a tuple of 2 positive integers'

        try:
            if position[1]:
                pass
        except IndexError:
            raise TypeError(error)

        for pos in self.__position:
            if type(pos) != int:
                raise TypeError(error)
            elif pos < 0:
                raise TypeError(error)

        if type(self.__size) != int:
            raise TypeError('size must be an integer')
        elif self.__size < 0:
            raise ValueError('size must be >= 0')

    @property
    def size(self):
        """size getter

        Returns:
            integer: sends the value of private size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """size setter

        Args:
            value (int): a new size value

        Raises:
            TypeError: if not integer
            ValueError: if < 0
        """

        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    def area(self):
        """ calculating the area of the square

        Returns:
            int: the area of the square
        """
        return self.__size**2

    def printt(self):
        """printing the square"""
        if self.__size == 0:
            print()
            return
        print('\n'*self.__position[1], end="")
        for i in range(self.__size):
            for x in range(self.__position[0]):
                print(' ', end="")
            for w in range(self.__size):
                print('#', end="")
            print()

    @property
    def position(self):
        return self.__position
