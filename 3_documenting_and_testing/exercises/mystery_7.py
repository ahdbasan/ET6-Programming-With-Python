#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on XX XX XX

@author: Ahd AbdelRahim
"""

# --- before documenting and testing ---

#def mystery_7(a, b):
#    c = []
#    for d in a:
#        if b in d:
#            c.append(d)
#    return c



# --- after documenting and testing ---

def mystery_7(a: list, b) -> list:
    """
    Filters elements in a list `a` that contain the value `b`.

    Parameters:
        a (list): A list of elements to be filtered. Elements can be strings, lists, tuples, etc.
        b (any): A value to search for within each element of `a`.

    Returns:
        list: A list containing elements from `a` that include `b`.

    Examples:
    >>> mystery_7(["apple", "banana", "cherry"], "a")
    ['apple', 'banana']

    >>> mystery_7([(1, 2), (3, 4), (5, 2)], 2)
    [(1, 2), (5, 2)]

    >>> mystery_7(["cat", "dog", "fish"], "z")
    []
    """
    c = []
    for d in a:
        if b in str(d):
            c.append(d)
    return c
