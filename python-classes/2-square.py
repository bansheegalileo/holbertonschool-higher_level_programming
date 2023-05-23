#!/usr/bin/python3
""" Module Sqaure """


class Square:
    """ Sq class def.d by geom.ic shape

        Attributes:
            size (int): sq size
    """
    def __init__(self, size=0):
        """
        Init method

        Args:
            size (int): int to assn to sq size
        Raises:
            TypeError: size not int
            ValueError: size less than 0
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
