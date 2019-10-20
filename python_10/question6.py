#!/usr/bin/env python3

import sys

dna = sys.argv[1]



def reverse_complement(dna):
	for nt in dna:
		if nt == 'A':
			dna = dna.replace('A', 't')
		if nt == 'T':
			dna = dna.replace('T', 'a')
		if nt == 'G':
			dna = dna.replace('G', 'c')
		if nt == 'C':
			dna = dna.replace('C', 'g')
	complement = dna.upper()
	reverse_complement = complement[::-1]
	print(reverse_complement)


######execution of the function:

reverse_complement(dna)
