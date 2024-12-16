
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on XX XX XX

@author: Ahd AbdelRahim
"""

# --- before documenting and testing ---

#def mystery_4(a):
#    b = []
#
#    c = 0
#    while len(b) < a:
#        b.append(c)
#        c = c + 1
#
#   return b


# --- after documenting and testing ---

def mystery_4(a: int) -> list:
    """
    Generates a list of integers from 0 to a-1.

    Parameters:
        a (int): The number of integers to include in the list.

    Returns:
        list: A list containing integers from 0 to a-1.

    Examples:
    >>> mystery_4(5)
    [0, 1, 2, 3, 4]

    >>> mystery_4(0)
    []

    >>> mystery_4(1)
    [0]
    """
    # Ensure the input is a non-negative integer
    assert isinstance(a, int) and a >= 0, "Input must be a non-negative integer."

    b = []
    c = 0

    # Generate integers until the list reaches the desired length
    while len(b) < a:
        b.append(c)
        c += 1

    return b
