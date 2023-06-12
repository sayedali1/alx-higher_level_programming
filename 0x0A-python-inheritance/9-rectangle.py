#!/usr/bin/python3
"""
Module-9:rectangle
inherince from base_geometry

"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ contain the init method """
    def __init__(self, width, height):
        """ init the width and height """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ calc the area """
        return self.__width * self.__height

    def __str__(self):
        """ disply a string """
        return"[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                        self.__width, self.__height)
