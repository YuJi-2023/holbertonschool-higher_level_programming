#!/usr/bin/python3
"""define sublass Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """subclass inherits class Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialise data"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return a customised string representation"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """retrieve size"""
        return self.width

    @size.setter
    def size(self, value):
        """set the value for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assign value to attributes"""
        att_list = ['id', 'size', 'x', 'y']
        if args is not None and len(args) > 0:
            for index in range(0, min(len(args), len(att_list))):
                setattr(self, att_list[index], args[index])
        elif kwargs is not None:
            for key in kwargs.keys():
                if key in att_list:
                    setattr(self, key, kwargs.get(key))
