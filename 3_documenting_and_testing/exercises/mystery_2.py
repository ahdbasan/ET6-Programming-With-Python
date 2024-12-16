#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on XX XX XX

@author: Evan Cole
"""

# --- before documenting and testing ---

#def mystery_2(a):
#    if len(a) == 0:
#        return None
#
#    return len(a)


# --- after documenting and testing ---


def mystery_2(a: list) -> int:
    """Returns the length of the list, or None if the list is empty.

    Parameters:
        a (list): A list of any type. If the list is empty, the function returns None.

    Returns:
        int or None: The length of the list if it is not empty, otherwise None.

    >>> mystery_2([1, 2, 3])
    3

    >>> mystery_2([])
    None

    >>> mystery_2(['a', 'b'])
    2
    """
    

    if len(a) == 0:
        return None
    return len(a)
