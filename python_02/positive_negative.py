#!/usr/bin/env python3

import sys

#when you use sys.argv, it will automatically read in the number as a string and not a numeric
#this step will convert the variable back into a numeric
number = sys.argv[1]
number = float(number)

#this step will test if the number is greater than zero. if so, will print it is positive
if number > 0:
	message = "is positive"
	print(number, message)
#if positive, will check if number is less than 50
	if number < 50: 
		message2 = "is less than 50"
		print(number, message2)
#if less than 50, will check if it is even
		if number%2 == 0:
			message3 = "is an even number that is smaller than 50"
			print(number, message3)
		else:
			message4 = "is an odd number that is smaller than 50"
			print(number, message4)
#if positive but not less than 50, will see if it is divisible by 3
	elif number%3 == 0: 
		message5 = "is larger than 50 and divisible by 3"
		print(number, message5)
#if not positive, will see if number is negative
elif number < 0:
	message = "is negative"
	print(number, message)
#if not positive or negative, will say it is zero
else:
	message = "is zero"
	print(number, message)



