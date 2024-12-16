
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on XX XX XX

@author: Evan Cole
"""

# --- before documenting and testing ---

# def mystery_1(a,b):
#     return a + b


# --- after documenting and testing ---

def mystery_1(a: int, b: int) -> int:
    """Adds two integers and returns the result.

    Parameters:
        a: The first integer.
        b: The second integer.

    Returns:
        int: The sum of a and b.

    Examples:
    >>> mystery_1(2, 3)
    5

    >>> mystery_1(-1, 4)
    3

    >>> mystery_1(0, 0)
    0
    """
    return a + b


    #the input should both be integers
    assert isinstance(a, int), "The first argument is an integer."
    assert isinstance(b, int), "The second argument is an integer."
    

    # Add the two numbers
    return a + b
