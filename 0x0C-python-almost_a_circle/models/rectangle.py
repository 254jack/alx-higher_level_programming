#!/usr/bin/python3
"""rectangle module"""
from models.base import Base


class Rectangle(Base):
    """Creates rectangle objects with 2 dimensions
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __integer_validator(self, attr, value):
        """Validates incoming argument values for use with internal attributes.
        """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(attr))
        if attr is 'width' or attr is 'height':
            if value <= 0:
                raise ValueError('{} must be > 0'.format(attr))
        elif attr is 'x' or attr is 'y':
            if value < 0:
                raise ValueError('{} must be >= 0'.format(attr))

    @property
    def width(self):
        """`__width` getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """__width setter
        """
        self.__integer_validator('width', value)
        self.__width = value

    @property
    def height(self):
        """`__height` getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height setter
        """
        self.__integer_validator('height', value)
        self.__height = value

    @property
    def x(self):
        """`__x` getter
        """
        return self.__x

    @x.setter
    def x(self, value):
        """x setter
        """
        self.__integer_validator('x', value)
        self.__x = value

    @property
    def y(self):
        """`__y` getter
        """
        return self.__y

    @y.setter
    def y(self, value):
        """y setter
        """
        self.__integer_validator('y', value)
        self.__y = value

    def area(self):
        """Returns area of rectangle as product of `width` and `height`.
        """
        return self.width * self.height

    def display(self):
        """Prints representation of rectangle to stdout using '#'.
        """
        display = ''
        for row in range(self.y):
            display += '\n'
        for row in range(self.height):
            for column in range(self.x):
                display += ' '
            for column in range(self.width):
                display += '#'
            if row < self.height - 1:
                display += '\n'
        self.__display = display
        print(display)

    def __str__(self):
        """Returns string with numeric representation of rectangle
        """
        return ('[Rectangle] ({:d}) {:d}/'.format(self.id, self.x) +
                '{:d} - {:d}/{:d}'.format(self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """Updates attributes in a given order based on variable amount of
        non-keyword args, or in any order with keyword args.
        """
        if len(args) == 0:
            if len(kwargs) == 0 or len(kwargs) > 5:
                raise TypeError('Rectangle.update() takes 1 to 5 keyword,' +
                                ' or 1 to 5 non-keyword arguments')
            else:
                for key, value in kwargs.items():
                    if key == 'id':
                        self.id = value
                        Base._Base__assigned_ids.add(value)
                    elif key == 'width':
                        self.width = value
                    elif key == 'height':
                        self.height = value
                    elif key == 'x':
                        self.x = value
                    elif key == 'y':
                        self.y = value
                    else:
                        raise KeyError('invalid attribute name: ' +
                                       '{}'.format(key))
        elif len(args) > 5:
            raise TypeError('Rectangle.update() takes 1 to 5 keyword,' +
                            ' or 1 to 5 non-keyword arguments')
        else:
            for i, arg in enumerate(args):
                if i == 0:
                    if self.id != arg:
                        self.id = arg
                        Base._Base__assigned_ids.add(arg)
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg

    def to_dictionary(self):
        """Creates dictionary representation of self without revealing private
        attribute names.
        """
        self_dict = dict()
        self_dict['id'] = self.id
        self_dict['width'] = self.width
        self_dict['height'] = self.height
        self_dict['x'] = self.x
        self_dict['y'] = self.y
        return self_dict
