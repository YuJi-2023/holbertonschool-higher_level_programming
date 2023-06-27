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
