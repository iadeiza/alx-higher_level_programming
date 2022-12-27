#!/usr/bin/python3

class Square:
    def __init__(self, size):
        self.__size = size

    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
    def area(self):
        return (self.__size*self__size)
