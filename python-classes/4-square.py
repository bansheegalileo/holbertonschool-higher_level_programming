#!/usr/bin/python3
""" Module Sqaure """


class Square:
    """ Sq class def.d by geom.ic shape

        Attributes:
            size (int): sq size
    """
    def __init__(self, size=0):
        """
        inits square
        Args:
            size (int): sq side size

        Returns:
            None
        """
        self.__size = size

    def area(self):
        """
        set squarea

        Return:
            the current squarea (int)
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        getter of size

        Return:
            sq size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter of size

        Args:
            size (int): sq side size
        Raises
            TypeError: size not int
            ValueError: size less than 0
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
                raise ValueError("size must be >= 0")
        else:
            self.__size = value
