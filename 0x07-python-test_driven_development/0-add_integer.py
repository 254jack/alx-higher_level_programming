#!/usr/bin/python3
def add_integer(a, b=98):
    """
    A function that add two integers.

    Args:
        a(int/float): first integer or float
        b(int/float): second integer or float which have a default value 98
    Returns:
        int: The return value. a + b
    Raises:
        TypeError: If a or b is not an integer or float
    """

    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    elif type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")

    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)

    return a + b
