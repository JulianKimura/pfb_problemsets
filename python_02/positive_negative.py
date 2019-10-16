#!/usr/bin/env python3

import sys

#when you use sys.argv, it will automatically read in the number as a string and not a numeric
#this step will convert the variable back into a numeric
number = sys.argv[1]
number = float(number)

#this step will spit out whether the number is positive, 0, or negative
if number > 0:
	message = "is positive"
	print(number, message)
elif number == 0:
	message = "is zero"
	print(number, message)
else:
	message = "is negative"
	print(number, message)


