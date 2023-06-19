#!/usr/bin/python3
"""
Module contain the base class
contain methods that discribed down
"""


import json


class Base():
    """ the main class """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize id, increment class attribute if no id and set as id"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ encode dic to json """
        if list_dictionaries is None or len (list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save json in file """
        lists = []
        fileName = cls.__name__ + ".json"
        if list_objs is not None:
            for listt in list_objs:
                lists.append(cls.to_dictionary(listt))
        with open(fileName, "w") as f:
            f.write(cls.to_json_string(lists))

    @staticmethod
    def from_json_string(json_string):
        """ load json from file """
        if json_string is None or len(json_string) == 0:
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1, 1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns list of instances"""
        filenamee = cls.__name__ + ".json"
        listt = []
        try:
            with open(filenamee, "r") as f:
                instances = cls.from_json_string(f.read())
            for i, dic in enumerate(instances):
                listt.append(cls.create(**instances[i]))
        except:
            return
        return listt
