#!/usr/bin/python3
"""Defination of class Square"""


class Square:
    """Represention of a Square
    Attributes:
        __size (int): size of a side of a square
    """
    def __init__(self, size):
        """Initializes a square
        Args:
            size (int): size of a size of the square
        Returns: None
        """
        self.__size = size
