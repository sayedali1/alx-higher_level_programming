#!/usr/bin/python3
"""
Moudel rectangle that inhert from base
contain 5 methods and getter and setter
"""


from models.base import Base


class Rectangle(Base):
    """ main class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initiatlize tributes """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ getter width """
        return self.__width

    @property
    def height(self):
        """ getter height """
        return self.__height

    @property
    def x(self):
        """ getter x """
        return self.__x

    @property
    def y(self):
        """ getter y """
        return self.__y

    @width.setter
    def width(self, value):
        """ set the width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ set height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """ set x """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """ set y """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ calc the area """
        return self.__height * self.__width

    def display(self):
        """ display the rectangle """
        print("\n" * self.__y + "\n".join(" " * self.__x +
                                          "#" * self.__width
                                          for i in range(self.__height)))

    def __str__(self):
        """ display string """
        return "[{:s}] ({:d}) {:d}/{:d} -{:d}/{:d}".format(
                self.__class__.__name__,
                self.id, self.__x,
                self.__y,
                self.__width,
                self.__height)

    def update(self, *args, **kwargs):
        """ update the attribute """
        if args:

            for idx, arg in enumerate(args):
                if idx == 0:
                    self.id = arg
                if idx == 1:
                    self.width = arg
                if idx == 2:
                    self.height = arg
                if idx == 3:
                    self.x = arg
                if idx == 4:
                    self.y = arg
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """ put the attribute in form in dic """
        dic = {}
        dic["x"] = self.x
        dic["y"] = self.y
        dic["id"] = self.id
        dic["width"] = self.width
        dic["height"] = self.height
        return dic
