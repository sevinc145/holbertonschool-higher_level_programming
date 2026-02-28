#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """A class that defines a square."""

    def __init__(self, size=0):
        self.size = size  # setter çgırıl

    @property
    def size(self):
        """Getter: size-i qaytarır"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter: size-i teyin edir ve  validation edir"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Kvadratın saesini qaytarır"""
        return self.__size * self.__size
