#!/usr/bin/python3

"""Module that defines a square"""


class Square:
    """The class that represents a square"""
    def __init__(self, size=0):
        """Initializing the square class
        Args:
            size: represents the size of the square
        Raises:
            TypeError: if the size is not an integer
            ValueError: if the size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """
        Calculates the area of the square
        Returns: The square of the size
        """

        return (self.__size ** 2)
