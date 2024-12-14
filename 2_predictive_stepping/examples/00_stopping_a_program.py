#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time


""" Stopping a Program

You can stop a program at any time when you are in the debugger.
        - just press the red box!
        
""" 

#while True:
#    print("...")


""" Stopping a Program after 5 seconds """

start_time = time.time()
while time.time() - start_time < 5:  # Run the loop for 5 seconds
    print("...")
print("Program terminated after 5 seconds.")


#WITHOUT USING TIME, BECAUSE PYTHON TUTOR DOESN'T RUN WITH TIME BUT WITH ITERATIONS
""" Stopping a Program after 5 seconds (Simulated with a Count) """

count = 0
while count < 5:  # Simulate 5 iterations instead of real time
    print("...")
    count += 1  # Increment the counter
print("Program terminated after 5 iterations.")
