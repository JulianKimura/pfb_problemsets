#!/usr/bin/env python3
#####set up so it solves question 4. this will reformat every sequence in a fasta file to a specified max line length, and return it in a fasta format
import sys
#takes in the first input after the script on command line as the fasta file name
#takes in the second input after the script on the command line as the width of the lines you want displayed in the final output file
fasta_file = sys.argv[1]
width = sys.argv[2]

#first creating the function here by the def command
def seq_to_lines(fasta_file, width):
#imports re which is neccesary for the fasta parser to run
#sets up empty strings and dictionary for the fasta parser to place iteme into
	import re
	fasta_dict = {}
	key = ''
	sequence = ''
#opens up the fasta file from which we want to parse through and creates dictionary where
#the key is the sequence header and the values are the dna sequences
	with open(fasta_file, 'r') as input_file:
		for line in input_file:
			line = line.rstrip()
			if re.search(r"^>", line):
				key = line
				sequence = ''
			else:
				sequence += line
				fasta_dict[key] = sequence
#for loop that looks at each key in the fasta dictionary and executes the following
	for key in fasta_dict:
#pulls out the sequence from a key
		dna = fasta_dict[key]	
#turns the sequence into a single line string with no line breaks	
		dna = re.sub(r'\n', '', dna)
#uses the regex and compile in order to create line breaks at specified nucleotide lengths
		pattern = re.compile('.{1,'+str(width)+'}')
		dna_list = pattern.findall(dna)
		dna_string = '\n'.join(dna_list)
#prints the dna string
		print(key+'\n'+dna_string)



####################
#execution of the function below:
seq_to_lines(fasta_file, width)

	
