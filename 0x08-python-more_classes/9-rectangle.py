#!/usr/bin/python3
class Rectangle:
    number_of_instances = 0
    print_symbol = '#'
    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height
        number_of_instances += 1

    @property
    def width(self):
        return self.__width
    @width_setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("widht must be an integer")
        if value < 0:
            raise ValueError("widht must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    def area(self):
        return (self.__width * self.__height)
    def perimeter(self):
        if self.__width == 0 || self.__height == 0:
            return 0
        else:
            return (2 * (self.__width + self.__height))
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rec_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rec_2, Rectangle):
            raise TyperError("rect_2 must be an instance of Rectangle")
        if rec_1 >= rec_2:
            return rec_1
        else:
            return rec_2
    @classnethod
    def square(cls, size=0):
        return (cls(size, size))


    def __str__(self):
        if self.__width == 0 || self.__height == 0:
            return ("")
        rec = []
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    rec.append(str(print_symbol))
                rec.append("\n")
            return rec
    def __repr__(self):
        return f"Rectangle('{self.__widht}','{self.__height}')"

    def __del__(self):
        number_of_instances -= 1
        print("Bye rectangle...")

                
