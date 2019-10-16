#!/usr/bin/env python3
import sys

#defining variables based on the position of the command line input
#starts with 1 rather than 0 because 0 would simply be the python script

name = sys.argv[1]
color = sys.argv[2] 
activity = sys.argv[3]
animal = sys.argv[4]

#print function with the strings surrounded by quotes, variables not
#"\n" specifies the line breaks. no commas prevents extra spaces at breaks


print("My name:", name,"\n"
"My favorite color:", color,"\n"
"My favorite activity:", activity,"\n"
"My favorite animal:", animal)






