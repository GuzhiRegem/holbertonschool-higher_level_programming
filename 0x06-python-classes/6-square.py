#!/usr/bin/python3
"""
    6-square
    kill me pls
    return {}
"""


class Square:
    """
        square
    """
    def __init__(self, size=0, position=(0, 0)):
        """ .c """
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
        msg = 'position must be a tuple of 2 positive integers'
        if isinstance(position, tuple) and len(position) == 2:
            try:
                if position[0] >= 0 and position[1] >= 0:
                    self.__position = position
                else:
                    raise TypeError(msg)
            except TypeError:
                raise TypeError(msg)
        else:
            raise TypeError(msg)

    def area(self):
        """ area """
        return self.__size ** 2

    @property
    def size(self):
        """ size """
        return self.__size

    @property
    def position(self):
        """ position """
        return self.__position

    @size.setter
    def size(self, size):
        """ size """
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    @position.setter
    def position(self, position):
        """ position """
        msg = 'position must be a tuple of 2 positive integers'
        if isinstance(position, tuple) and len(position) == 2:
            try:
                if position[0] >= 0 and position[1] >= 0:
                    self.__position = position
                else:
                    raise TypeError(msg)
            except TypeError:
                raise TypeError(msg)
        else:
            raise TypeError(msg)

    def my_print(self):
        """ my print """
        if not self.__size:
            print()
            return
        for y in range(self.__position[1]):
            print()
        for y in range(self.__size):
            for x in range(self.__position[0]):
                print(" ", end="")
            for x in range(self.__size):
                print("#", end="")
            print()
