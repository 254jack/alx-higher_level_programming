#!/usr/bin/python3
"""square module"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a square function that inherits from Rectangle
    Args:
        size (int): length of side of square

    Attributes:
        __size (int): length of side of square

    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """a function that returns square area as size * size.

        Attributes:
            __size (int): length of side of square

        Returns:
            __size ** 2

        """
        return self.__size ** 2
