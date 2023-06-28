#!/usr/bin/python3
""" Module of  classSquare
"""


class Square:
    """ Definition of Square
    """

    def __init__(self, size=0):
        """ InstantiatesSquare
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Compute the area of Square
        """
        return self.__size ** 2
