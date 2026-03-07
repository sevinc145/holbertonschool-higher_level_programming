#!/usr/bin/python3
"""Function that checks if object is instance of a class"""


def is_kind_of_class(obj, a_class):
    """Return True if object is instance of or inherited from a_class"""
    return isinstance(obj, a_class)
