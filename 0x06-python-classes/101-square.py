#!/usr/bin/python3
"""Square module """


class Square:
    """Defines the class Square"""

    def __str__(self):
        """let the program print the square"""
        return self.pos_print[:-1]

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square
        Args:
            size: the size of square
            position: location of the square based on coordinates
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """property of the length of a side of square
        Raises:
            TypeError: if size is not an int.
            ValueError: if size is < 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ set the size of square
        Args:
            value: the size
        Raises:
                TypeError: if value is not int
                ValueError: if valie < 0
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """property of the position of square
        Raises:
            TypeError: if value != tuple of 2 ints >= 0.
        Returns: the position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """set the position
        Args:
            value: where
        Raises:
                TypeError: if not tuple, ints, positive
        Returns: the position
        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """ the area of square
        Returns:
            size * size
        """
        return self.__size * self.__size

    def pos_print(self):
        """returns the printed square with position"""
        positioning = ""
        if not self.size:
            return "\n"
        for w in range(self.position[1]):
            positioning += "\n"
        for w in range(self.size):
            for i in range(self.position[0]):
                positioning += " "
            for j in range(self.size):
                positioning += "#"
            positioning += "\n"
        return positioning

    def my_print(self):
        """print square."""
        print(self.pos_print(), end="")
