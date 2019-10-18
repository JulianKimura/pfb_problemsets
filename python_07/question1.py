#!/usr/bin/env python3

import re

with open('Python_07_nobody.txt', 'r') as poem:
	contents = poem.read()		
	for found in re.finditer(r"(Nobody)", contents):
		start = found.start(1) + 1
		print(start)


