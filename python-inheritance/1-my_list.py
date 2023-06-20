#!/usr/bin/python3
"""create a subclass MyList inherits from class list"""


class MyList(list):
    """create the subclass MyList"""

    def print_sorted(self):
        """a public instance method that prints list in assceding order"""
        print(sorted(self))
