#!/usr/bin/python3
"""
Modul square that inhert from rectangle
contain 4 methods and setter and getter
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ main class """
    def __init__(self, size, x=0, y=0, id=None):
        """ initilize """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ str format """
        return "[{:s}] ({:d}) {:d}/{:d} {:d}".format(
                self.__class__.__name__,
                self.id,
                self.x,
                self.y,
                self.size)

    @property
    def size(self):
        """ getter size """
        return self.width

    @size.setter
    def size(self, value):
        """ setter size """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update the attribure """
        if args:

            for idx, arg in enumerate(args):
                if idx == 0:
                    self.id = arg
                if idx == 1:
                    self.size = arg
                if idx == 2:
                    self.x = arg
                if idx == 3:
                    self.y = arg
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """ put the attribute in form in dic """
        dic = {}
        dic["id"] = self.id
        dic["x"] = self.x
        dic["size"] = self.size
        dic["y"] = self.y

        return dic
