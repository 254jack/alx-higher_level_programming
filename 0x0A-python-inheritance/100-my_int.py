#!/usr/bin/python3
""" MyInt module"""


class MyInt(int):
    """ a class MyInt that inherits from int
    """

    def __eq__(self, other):
        """inverts behavior of == operator.

        """
        return int(self) != int(other)

    def __ne__(self, other):
        """inverts behavior of != operator.

        """
        return int(self) == int(other)
