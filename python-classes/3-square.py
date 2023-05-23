#!/usr/bin/python3
""" Module Sqaure """


class Square:
    """ Sq class def.d by geom.ic shape

        Attributes:
            size (int): sq size
    """
    def __init__(self, size=0):
        """
        inits sq
        Args:
            size (int): sq side size
        Raises:
            TypeError: size not int
            ValueError: size less than 0
        Returns:
            None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
                raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
            set squarea

            Return:
                the current squarea (int)
        """
        return self.__size ** 2
