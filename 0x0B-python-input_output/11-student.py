#!/usr/bin/python3

"""
Module 10-student
Contains class Student
"""


class Student():
    """
    Public Attributes:
        first_name
        last_name
        age
    """
    def __init__(self, first_name, last_name, age):
        """Initializes student with full name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns dictionary description with simple data structure
        """
        if attrs is None:
            return self.__dict__
        else:
            dictt = {}
            for attrs in attrs:
                if attrs in self.__dict__.keys():
                    dictt[attrs] = self.__dict__[attrs]
            return dictt

    def reload_from_json(self, json):
        """
            Transfer all attributes of json to self
        """
        for k, v in json.items():
            setattr(self, k, v)
