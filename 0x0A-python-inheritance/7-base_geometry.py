#!/usr/bin/python3
"""
Module-7:7-basegeometry
contain two public method
"""


class BaseGeometry:
    """ contain one method """
    def area(self):
        """ impemented aread method """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ check the validate of integer """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
