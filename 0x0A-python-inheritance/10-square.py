#!/usr/bin/python3
"""
Module-10:square
inherince from Rectangle

"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherits from Rectangle, who inherits from BaseGeometry
    """
    def __init__(self, size):
        """initializes size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
