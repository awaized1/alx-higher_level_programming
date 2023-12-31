#!/usr/bin/python3
"""code for Module 4-rectangle"""



class Rectangle:
    """Defines a rectangle class"""

    def __init__(self, width=0, height=0):
        """Code Initializes a Rectangle props in a contructor.
        """
        self.width = width
        self.height = height

    def __str__(self):
        """Returns informal string representation of rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return ''
        rectangle_str = ''
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle_str += '#'
            rectangle_str += '\n'
        return rectangle_str[:-1]

    def __repr__(self):
        """Return an internal string representation of rectangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    @property
    def width(self):
        """function fetrieves the width of a Rectangle instance."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width of a Rectangle instance
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of a Rectangle instance."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of a Rectangle instance
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Code calculates the area of a Rectangle instance
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates perimeter of a Rectangle instance
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
