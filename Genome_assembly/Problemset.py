#!/usr/bin/env python3

import re
#creates sequence_list which will be a list containing all sequences of the genome
#contig_counts will be a counter used to count the number of contigs
#sequence will be a string that stores the sequence lines until a new contig is reached
sequence_list = []
contig_counts = 0
sequence = ''
with open('ecoli_0.25.contigs.fasta.txt', 'r') as input_file:
	for line in input_file:
		line = line.rstrip()
		if re.search(r"^>", line):
			contig_counts += 1
			if sequence:
				sequence_list.append(sequence)
				sequence = ''
		else:
			sequence += line
sequence_list.append(sequence)

#the number of contigs in the file are printed 
print('There are {} contigs in this file'.format(contig_counts))

#now that we have a list of all of the sequences, we need to sort based on the length of the string with the following. 
sequence_list = sorted(sequence_list, key = len)
shortest_contig = len(sequence_list[0])
longest_contig = len(sequence_list[66])
print("The shortest contig is {} bases long, the longest contig is {} bases long".format(shortest_contig,longest_contig))

#smallest number of contigs to get to 50% of the genome is the N50
#we have the list currently in ascending order of the length of strings. we are reversing this, then creating onemega string containing all of the sequences in order
sequence_list.reverse()
all_sequence_string = ''.join(sequence_list)

#here we are creating a counter which will represents the position in the genome based on the number of bases we have gone through the string
sequence_numbers = 0
for sequence in sequence_list:
	sequence_numbers += int(len(sequence))
#if the sequence position reaches a point that is greater than or equal to the midpoint of the genome, it will stop. and pull out the index number from the list of sequences and add 1. this will represent the contig number. 
	if sequence_numbers >= float(len(all_sequence_string))/2:
		n50 = int(sequence_list.index(sequence))+1
		break

print("The N50 of the genome is {}".format(n50))

#the length of the contig that crosses the 50% threshp;d is the L50

l50 = len(sequence_list[n50])
print("The L50 of the genome is {}".format(l50))
