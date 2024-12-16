#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on XX XX XX

@author:  Ahd AbdelRahim
"""

# --- before documenting and testing ---

# def mystery_8(a, b):
#     c = []
#    while a:
#        if b in str(a[0]):
#            c.append(a[0])
#        a = a[1:]
#    return c


# --- after documenting and testing ---


def mystery_8(a:list, b:str) -> list:
    """  Filters elements in a list `a` that contain the value `b`
   
    Parameters:
    a(list): A list of elements to be filtered
    b(any): A value to search for within each element of `a`  
    
    Return Values:
    Examples:
    >>> mystery_8(["apple", "banana", "cherry"], "a")
    ['apple', 'banana']

    >>> mystery_8([(1, 2), (3, 4), (5, 2)], 2)
    [(1, 2), (5, 2)]

    >>> mystery_8(["cat", "dog", "fish"], "z")
    []
    """
    
    c = []
    while a:
        if b in str(a[0]):
            c.append(a[0])
        a = a[1:]
    return c

    