#!/usr/bin/python3
""" a module that defines a size of square """


prev_square = __import__("0-square").Square


class Square(prev_square):
    """ a class inherited from our previously defined square class
    Args:
        prev_square(class): a class that defines a square
    """

    def __init__(self, size):
        """initialization function
        Args:
                size(integer): size attribute
            """
        self.__size = size
