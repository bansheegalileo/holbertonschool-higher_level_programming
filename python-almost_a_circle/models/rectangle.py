#!/usr/bin/python3
"""
the rectangle class model
"""

from models.base import Base


class Rectangle(Base):
    """
    Represents a rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's position.
                Defaults to 0.
            y (int, optional): The y-coordinate of the rectangle's position.
                Defaults to 0.
            id (int, optional): The ID of the rectangle. Defaults to None.
        """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter for the width attribute.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute.

        Args:
            value (int): The new value for the width of the rectangle.
        """
        self.check_integer_parameter(value, "width")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height attribute.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute.

        Args:
            value (int): The new value for the height of the rectangle.
        """
        self.check_integer_parameter(value, "height")
        self.__height = value

    @property
    def x(self):
        """
        Getter for the x-coordinate attribute.

        Returns:
            int: The x-coordinate of the rectangle's position.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for the x-coordinate attribute.

        Args:
            value (int): new x coord pos val
        """
        self.check_integer_parameter(value, "x")
        self.__x = value

    @property
    def y(self):
        """
        Getter for the y-coordinate attribute.

        Returns:
            int: The y-coordinate of the rectangle's position.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for the y-coordinate attribute.

        Args:
            value (int): new val for y val pos
        """
        self.check_integer_parameter(value, "y")
        self.__y = value

    def check_integer_parameter(self, value, param):
        """
        Check if the value is an integer and meets specific constraints.

        Args:
            value (int): The value to check.
            param (str): The parameter name being checked.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value doesn't meet the specified constraints.
        """
        if not isinstance(value, int):
            raise TypeError(f"{param} must be an integer")

        if value <= 0 and param in ("width", "height"):
            raise ValueError(f"{param} must be > 0")

        if value < 0 and param in ("x", "y"):
            raise ValueError(f"{param} must be >= 0")

    def area(self):
        """
        Computes the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        Displays the rectangle using the '#' character.
        """
        if self.__y > 0:
            print("\n" * self.__y, end="")

        for _ in range(self.__height):
            if self.__x > 0:
                print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle.
        """
        return (
        f"[Rectangle] ({self.id}) "
        f"{self.__x}/{self.__y} - "
        f"{self.__width}/{self.__height}"
        )


    def update(self, *args, **kwargs):
        """
        Updates the attributes of the rectangle.

        Args:
            *args: Variable length argument list of values in the order:
                id, width, height, x, y.
            **kwargs: Arbitrary keyword arguments for attribute updates.
        """
        attrs = ["id", "width", "height", "x", "y"]
        num_args = len(args)

        if num_args > len(attrs):
            num_args = len(attrs)

        if num_args > 0:
            for i in range(num_args):
                setattr(self, attrs[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Converts the rectangle object to a dictionary representation.

        Returns:
            dict: The dictionary representation of the rectangle.
        """
        return {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y,
        }
