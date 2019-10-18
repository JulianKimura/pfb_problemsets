#!/usr/bin/env python3

import re
#this opens an existing file and creates a new file 
with open('Python_07_nobody.txt', 'r') as poem, open('Patrick.txt', 'w') as patrick :
	#this converts the contents of the original poem into a string by using .read() and then storing it into a vairable
	contents = poem.read()		
	#this then substitutes all instances of Nobody with Patrick
	new_poem = re.sub(r"(Nobody)", 'Patrick',  contents)
	#we are writing a new poem into Patrick.txt
	patrick.write(new_poem)


