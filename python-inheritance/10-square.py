#!/usr/bin/python3
"""
    Square Module
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        Square Class
    """
    def __init__(self, size):
        """
            init sq base on rect
        """
        self.__size = size
        self.integer_validator('size', self.__size)

    def area(self):
        """
            define squarea
        """
        return self.__size ** 2

    def __str__(self):
        """
            __str__
        """
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))
