#!/usr/bin/env python3

#have to create the initia seqs dictionary
seqs = {}

#open file
with open('Python_08.fasta.txt', 'r') as fasta_file:
	for line in fasta_file:
		line = line.rstrip()
#if there is a carrot in the line, then define it as a header
		if '>' in line:
			header = line
#adding the header into the dictionary
			seqs[header]={}
#creating numerical entries for the second dictionary
			seqs[header]['A']=0
			seqs[header]['T']=0
			seqs[header]['G']=0
			seqs[header]['C']=0		
#if you dont find a header, then we do the line.count method and sequentially adding the counts of each line/ 
		else:
			seqs[header]['A'] += line.count('A')
			seqs[header]['T'] += line.count('T')
			seqs[header]['G'] += line.count('G')
			seqs[header]['C'] += line.count('C')
print(seqs)

#an alternative would be to simply use the fasta parser. at this point you should have the sequences already available as strings, and you can simply do the string.count() method
