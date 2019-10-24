#!/usr/bin/env python

import os, sys



## method: sequence_to_kmer_list(sequence, kmer_length)
##
##  Extracts all kmers of a specified length from a sequence
##
##  ie.  sequence: GATCGATCGATCGA
##   and given kmer_length = 4
##   would yield
##                 GATC
##                  ATCG
##                   TCGA
##                    .... and so forth
##                       
##  input parameters:
##
##  seuqence : nucleotide sequence (type: string)
##
##  returns kmer_list : list of kmer sequences.
##                    ie.  ["GATC", "ATCG", ...]
    
def sequence_to_kmer_list(sequence, kmer_length):

	kmers_list = list()
	sequence = sys.argv[1]
	kmer_length = sys.argv[2]
    ## begin your code
#this will set up the counter equal to the actual index in the string
	nt_index = -1
	for nt in sequence:
#the counter will start its count from 0
		nt_index += 1
#if the length of the sequence that we are pulling out to append into our list at the bottom is equal to the length specified, append. if not, dont. this prevents us from adding any kmers that are smaller at the end of the sequence
		if len(sequence[nt_index : nt_index + int(kmer_length)]) == int(kmer_length):
#the command below will append a string that is in the interval specified in the second field of input
			kmers_list.append(sequence[nt_index:nt_index+int(kmer_length)])
	return kmers_list

'''
Brian Haas solution:
	for kmer_start_pos in range(0,len(sequence)-kmer_length):
		kmer_end_pos = kmer_start_pos + kmer_length
		kmer_seq = sequence[kmer_start_pos:
'''



def main():

	progname = sys.argv[0]
    
	usage = "\n\n\tusage: {} sequence kmer_length\n\n\n".format(progname)
    
	if len(sys.argv) < 3:
		sys.stderr.write(usage)
		sys.exit(1)

    # capture command-line arguments
	sequence = sys.argv[1]
	kmer_length = int(sys.argv[2])

	kmers  = sequence_to_kmer_list(sequence, kmer_length)

	print(kmers)

	sys.exit(0)  # always good practice to indicate worked ok!



if __name__ == '__main__':
	main()
