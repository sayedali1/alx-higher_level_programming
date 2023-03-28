#!/usr/bin/python3
"""
Moudle: 2-square
Difines class square
"""


class Square:
    """
    class defintion

    Args: size of the square
    """
    def __init__(self, size=0):
        """
        initialize square
        Attributes: __size of the square
        """
        self.__size = size

    @property
    def size(self):
        """
        getter

        Return: size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter

        args:
            value: set size to value
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        calc area of the square

        Return: area
        """
        return ((self.__size)**2)
