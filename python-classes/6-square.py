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
        self.size = size

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

    def my_print(self):
        """
        print a square from the size using ##

        Returns:
            None
        """
        if self.__size == 0:
            print()
        else:
            for x in range(self.size):
                    print("#" * self.size)

    @property
    def position(self):
        """
        get posit attr
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
            setter of posit
        Args:
            value (tuple): position of the square in 2D space
        Returns:
            None
        """
        if len(value) != 2 or type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) != int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
