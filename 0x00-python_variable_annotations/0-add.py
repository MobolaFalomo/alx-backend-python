#!/usr/bin/env python3
''' Description: type-annotated function add that takes a float a and a float b
                 as arguments and returns their sum as a float
    Parameters: a: float
                b: float
'''


def add(a: float, b: float) -> float:
    """Add two floating numbers and return the result."""
    result: float = a + b
    return result
