#!/usr/bin/python3
"""Square module"""
from models.rectangle import Rectangle
from models.base import Base


class Square(Rectangle):
    """A class that creates square objects with 2 dimensions and offset coordinates.
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns string with numeric representation of square
        """
        return ('[Square] ({:d}) {:d}/'.format(self.id, self.x) +
                '{:d} - {:d}'.format(self.y, self.width))

    @property
    def size(self):
        """`size` getter
        """
        return self.width

    @size.setter
    def size(self, value):
        """`size` setter
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates superclass attributes in a given order based on variable
        amount of non-keyword args.
        """
        if len(args) == 0:
            if len(kwargs) == 0 or len(kwargs) > 4:
                raise TypeError('Square.update() takes 1 to 4 keyword,' +
                                ' or 1 to 4 non-keyword arguments')
            else:
                for key, value in kwargs.items():
                    if key == 'id':
                        if self.id != value:
                            tmp = self.id
                            self.id = value
                            Base._Base__assigned_ids.remove(tmp)
                            Base._Base__assigned_ids.add(value)
                    elif key == 'size':
                        self.size = value
                    elif key == 'x':
                        self.x = value
                    elif key == 'y':
                        self.y = value
                    else:
                        raise KeyError('invalid attribute name: ' +
                                       '{}'.format(key))
        elif len(args) > 4:
            raise TypeError('Square.update() takes 1 to 4 keyword,' +
                            ' or 1 to 4 non-keyword arguments')
        else:
            for i, arg in enumerate(args):
                if i == 0:
                    if self.id != arg:
                        tmp = self.id
                        self.id = arg
                        Base._Base__assigned_ids.remove(tmp)
                        Base._Base__assigned_ids.add(arg)
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg

    def to_dictionary(self):
        """Creates dictionary representation of self without revealing private
        attribute names.
        """
        self_dict = dict()
        self_dict['id'] = self.id
        self_dict['size'] = self.size
        self_dict['x'] = self.x
        self_dict['y'] = self.y
        return self_dict
