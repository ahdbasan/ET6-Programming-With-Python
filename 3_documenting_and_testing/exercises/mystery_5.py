#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on XX XX XX

@author: Ahd AbdelRahim
"""

#def mystery_5(a, b=None):
#    if b is None:
#        b = []
#    while a:
#        c = min(a)
#        a.remove(c)
#        b.append(c)
#    return b

def mystery_5 (a,b=None):
    """ Sorts the elements of the list `a` in ascending order and appends them to list `b`.

    Parameters:
        a (list): A list of comparable elements to be sorted.
        b (list, optional): A list to which the sorted elements are appended. Defaults to an empty list.

    Returns:
        list: A list containing the sorted elements of `a` appended to `b`.

    Examples:
    >>> mystery_5([3, 1, 2])
    [1, 2, 3]

    >>> mystery_5([5, 4], [1])
    [1, 4, 5]
    """
    if b is None:
        b = []  # Initialize b as an empty list if it is not provided.

    while a:  # Continue until `a` is empty.
        c = min(a)  # Find the smallest element in `a`.
        a.remove(c)  # Remove the smallest element from `a`.
        b.append(c)  # Append the smallest element to `b`.

    return b
