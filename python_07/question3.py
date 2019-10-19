#!/usr/bin/env python3

import re

with open('Python_07.fasta.txt', 'r') as fasta_file:
	content = fasta_file.read()
	print(type(content))
#here you dont need the carrot at the beginning because you are converting the whole file into a string. so there is only one begining to the file.
#the \s does not work. instead add in a space charactr here. 	
	header = re.findall(r">\S.+ ", content)
	print(header)
