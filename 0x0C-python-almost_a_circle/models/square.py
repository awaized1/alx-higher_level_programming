#!/usr/bin/python3
'''Code is a module for Square class.'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Square class.'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Function Constructor.'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Returns string information about square.'''
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        '''The size of square.'''
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        '''The internal method that updates attributes using */**args.'''
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''Code updates the attributes using no-keyword & keyword args.'''
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        '''Function returns dictionary rep of the class.'''
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
