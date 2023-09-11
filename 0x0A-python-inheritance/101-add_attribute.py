#!/usr/bin/python3
""" add_attribute module """


def add_attribute(obj, attribute, value):
    """a method that adds a new attribute to an object if it’s possible

    Args:
        obj (any): object to have attribute set
        attribute (str): name of new attribute
        value (any): attribute value

    Raises:
        TypeError: If adding/updating attribute not possible.

    """
    if hasattr(obj, "__dict__"):
        setattr(obj, attribute, value)
    elif hasattr(obj, "__slots__") and attribute in obj.__slots__:
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
