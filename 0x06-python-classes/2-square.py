#!/usr/bin/python3
class Square:
    def __init__(self, size = 0):
        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            elif size >= 0:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

