#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on XX XX XX

@author: Ahd AbdelRahim
"""

# --- before documenting and testing ---

#def mystery_6(a, b):
#   if a == 0:
#        return []  # If `a` is 0, return an empty list.
#
#    c = []  # Initialize an empty list `c`.
#    while len(c) < a:  # Continue until `c` has `a` elements.
#        c.append(b)  # Append the value of `b` to `c`.
#        b = b + 1  # Increment `b`.
#
#    return c  # Return the resulting list `c`.



# --- after documenting and testing ---

def mystery_6(a: int, b: int) -> list:
    """
    Generates a list of `a` consecutive integers starting from `b`.

    Parameters:
        a (int): The number of integers to include in the list.
        b (int): The starting integer for the sequence.

    Returns:
        list: A list containing `a` consecutive integers starting from `b`.

    Examples:
    >>> mystery_6(5, 10)
    [10, 11, 12, 13, 14]

    >>> mystery_6(0, 5)
    []

    >>> mystery_6(1, 5)
    [5]
    """
    if a == 0:
        return []  # Return an empty list if `a` is 0.

    c = []  # Initialize an empty list `c`.
    while len(c) < a:  # Continue until `c` has `a` elements.
        c.append(b)  # Append the current value of `b` to `c`.
        b += 1  # Increment `b`.

    return c
