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
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
