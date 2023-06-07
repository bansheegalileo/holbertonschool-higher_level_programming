#!/usr/bin/python3
"""
the square class model
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a Square, a special type of Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.
            x (int): The x-coordinate of the square's position.
            y (int): The y-coordinate of the square's position.
            id (int): The unique identifier of the square.

        Raises:
            TypeError: If the size, x, or y parameters are not integers.
            ValueError: If the size, x, or y parameters are invalid.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: The string representation of the square.
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )
