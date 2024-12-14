#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Variables: Cat Detector

Asks the use for the input "cat", throws an assertion error if the input is wrong

"""

maybe_cat = input('Enter "cat": ')

is_cat = maybe_cat == "cat"

assert is_cat, 'you should have entered "cat"'

print("thank you for the cat")




#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Variables: Cat Detector

Asks the user for the input "cat", provides feedback for incorrect input,
and keeps asking until the input is correct.
"""

while True:
    maybe_cat = input('Enter "cat": ').strip()
    
    # Check for "cat" (case-insensitive)
    if maybe_cat.lower() == "cat":
        print("Thank you for the cat!")
        break  # Exit the loop on correct input
    else:
        print('That is not "cat". Please try again.')
