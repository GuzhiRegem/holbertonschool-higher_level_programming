#!/usr/bin/python3


class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size
    @property
    def position(self):
        return self.__position

    @size.setter:
    def size(self, size):
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    @position.setter
    def position(self, position):
        if isinstance(position, tuple) and len(position) == 2:
            try:
                if position[0] > 0 and position[1] > 0:
                    self.__position = position
            except:
                raise TypeError('position must be a tuple of 2 positive integers')
        else:
            raise TypeError('position must be a tuple of 2 positive integers')
    def my_print(self):
        for y in range(self.__position[1]):
            print()
        for y in range(self.__size):
            for x in range(self.__position[0]):
                print(" ", end="")
            for x in range(self.__size):
                print("#", end="")
            print()
        if not self.__size:
                print()
