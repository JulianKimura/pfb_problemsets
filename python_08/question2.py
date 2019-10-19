#!/usr/bin/env python3

#####NOT FINISHED

import re
fasta_dict = {}
codons = ''
x = 0
y = 3

#fasta parser takes in the fasta file into a dictionary
with open('test.fasta', 'r') as fasta_file:
	for line in fasta_file:
		line = line.rstrip()
		if re.search(r"^>", line):
			header = line
			sequence = ''
		else:
			sequence += line
			fasta_dict[header] = sequence
print(fasta_dict)

for key in fasta_dict:
	sequence = fasta_dict[key]
	codons = codons+'\t'+sequence[0:3]
print(codons)



#			codons = codons+line+'-frame-1-codons\n'
#		else:
#			for nt in line:
#				codons = codons+line[0:3]
#				#x = x+3
#				#y = y+3
#				#z = z+3
#				#a = a+3
#print(codons)
#print(codons)

			
