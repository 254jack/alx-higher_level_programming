#!/usr/bin/python3
"""base module"""
import json
import csv


class Base:
    """a base class with attribute _nb_objects

    """
    __nb_objects = 0
    real_nb_objects = 0
    __assigned_ids = set()

    def __init__(self, id=None):
        """ initilizing our base class"""
        if id is not None:
            self.id = id
            Base.real_nb_objects += 1
            self.serial = Base.real_nb_objects
            Base.__assigned_ids.add(self.id)
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
            Base.real_nb_objects += 1
            self.serial = Base.real_nb_objects
            Base.__assigned_ids.add(self.id)

    @property
    def id(self):
        """Getter for `id`
        """
        return self.__id

    @id.setter
    def id(self, value):
        """id setter
        """
        if value < 1:
            raise ValueError('id must be positive')
        self.__id = value

    @property
    def serial(self):
        """Getter for `serial`
        """
        return self.__serial

    @serial.setter
    def serial(self, value):
        """seria setter
        """
        self.__serial = value

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts list of dictionaries into JSON string.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves to f a JSON formatted string of a list of dictionary
        representations of objects of `Base` derived classes.
        """
        if list_objs is None:
            list_objs = []

        list_dicts = []
        for item in list_objs:
            list_dicts.append(item.to_dictionary())
        json_dict = cls.to_json_string(list_dicts)

        filename = cls.__name__ + '.json'
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(json_dict)

    @staticmethod
    def from_json_string(json_string):
        """Returns list of objects represented by JSON format string,
        or [] if `json_string` is None or empty
        """
        if json_string is None or json_string == '':
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates a new dummy instance of class and `update()`s it using
        `dictionary` as keyword args
        """
        if cls.__name__ is 'Rectangle':
            tmp = cls(1, 1)
        elif cls.__name__ is 'Square':
            tmp = cls(1)
        tmp.update(**dictionary)
        return tmp

    @classmethod
    def load_from_file(cls):
        """Returns list of instances from f <class name>.json, or empty list
        if no f. `cls` determines class of instances.
        """
        import os.path

        filename = cls.__name__ + '.json'
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                json_str = f.read()
        else:
            return []
        obj_list = cls.from_json_string(json_str)
        instance_list = []
        for item in obj_list:
            instance_list.append(cls.create(**item))
        return instance_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves to f a CSV formatted string of a list of dictionary
        representations of objects of `Base` derived classes.
        """
        if list_objs is None:
            list_objs = []

        if cls.__name__ == 'Rectangle':
            keys = ('id', 'width', 'height', 'x', 'y')
        elif cls.__name__ == 'Square':
            keys = ('id', 'size', 'x', 'y')

        list_dicts = []
        for item in list_objs:
            list_dicts.append(item.to_dictionary())

        filename = cls.__name__ + '.csv'
        with open(filename, 'w', encoding='utf-8') as f:
            csv_writer = csv.DictWriter(f, keys)
            csv_writer.writeheader()
            for dict in list_dicts:
                csv_writer.writerow(dict)

    @classmethod
    def load_from_file_csv(cls):
        """Returns list of instances from f <class name>.csv, or empty list
        if no f. `cls` determines class of instances.
        """
        import os.path

        if cls.__name__ == 'Rectangle':
            keys = ('id', 'width', 'height', 'x', 'y')
        elif cls.__name__ == 'Square':
            keys = ('id', 'size', 'x', 'y')

        filename = cls.__name__ + '.csv'
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                csv_reader = csv.DictReader(f)
                instance_list = []
                for row in csv_reader:
                    for key in keys:
                        row[key] = int(row[key])
                    instance_list.append(cls.create(**row))
                return instance_list
        else:
            return []
