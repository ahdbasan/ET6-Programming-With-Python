#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on XX XX XX

@author: Ahd AbdelRahim
"""

# --- before documenting and testing ---

#def mystery_3(a, b):
#    if a < b:
#        return a
#    elif a > b:
#        return b
#    else:
#        return a + b
    
# --- after documenting and testing ---


from typing import Union

def mystery_3(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Compares two numbers and returns a result based on their relationship.

    Parameters:
        a (int or float): The first number to compare.
        b (int or float): The second number to compare.

    Returns:
        int or float: 
            - The smaller of the two numbers if they are not equal.
            - The sum of the two numbers if they are equal.

    Examples:
    >>> mystery_3(2, 5)
    2

    >>> mystery_3(10, 3)
    3

    >>> mystery_3(4, 4)
    8

    >>> mystery_3(2.5, 2.5)
    5.0
    """
    if a < b:
        return a
    elif a > b:
        return b
    else:
        return a + b
