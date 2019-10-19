#!/usr/bin/env python3

import re
fasta_dict = {}
header = ''
sequence = ''
with open('Python_07.fasta.txt', 'r') as fasta_file:
	for line in fasta_file:
		line = line.rstrip()
		#if  re.search(r">\S+\s.+", line)
		if  re.search(r"^>", line):
			header = line
			sequence = ''
		else:
			sequence += line
			fasta_dict[header] = sequence
    
			
print(fasta_dict)
