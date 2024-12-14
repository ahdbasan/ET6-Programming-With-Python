#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Pausing on Errors

By default, the debugger will stop on errors and show what went wrong.
    
You can change this setting in the breakpoints pane down left.
        
"""

a = 1

b = 2     #"2" str! = int  *type_error

# the error message will appear below this line
#   and the values in memory can help you understand what went wrong
c = a + b

print(c) 



#RUNTIME ERROR
#OR SOLVE IT LIKE THAT!!

a=1
b="2"
c = a + int (b)
print(c)
