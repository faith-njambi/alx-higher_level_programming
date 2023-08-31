#!/usr/bin/python3
"""Square class definition"""


class Square():
    """Represents a square of given size"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square
        Args:
            size (int): size of a side of the sq.
            position (tuple): coordinates of a sq.
        """
        self.size = size
        self.position = position

    def area(self):
        """Returns Area of a square"""
        area = self.__size ** 2
        return area

    @property
    def size(self):
        """getter of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter of size"""
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        """Get the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is tuple and len(value) == 2 and type(value[0]) \
            is int and type(value[1]) is int and value[0] >= 0 and \
                value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of \
                    2 positive integers")

    def my_print(self):
        """Prints the square using #"""
        if self.__size > 0:
            for y in range(self.__position[1]):
                print()
            for x in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
        else:
            print()
