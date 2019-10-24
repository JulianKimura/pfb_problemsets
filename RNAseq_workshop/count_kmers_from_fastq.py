#!/usr/bin/env python

import os, sys

#these lines will then import the results from the previous scripts that have been run
#each of the scripts from the previous quesitons are used as a library
#the if __name__ == '__main__'
		 	#main()
#syntax is how the magic happens
#if you place __name__ is set to the value '__main__'
#if you find this variable in the module code, it will be set to the name of the module. 
from sequence_to_kmer_list import *
from fastq_file_to_sequence_list import *


## method: count_kmers(kmer_list)
##
##  Counts the frequency of each kmer in the given list of kmers
##
##  input parameters:
##
##  kmer_list : list of kmers (type: list)
##               ie.  ["GATC", "TCGA", "GATC", ...]
##                
##
##  returns kmer_counts_dict : dict containing ( kmer : count )
##                    ie.  {  "GATC" : 2,
##                            "TCGA" : 1,
##                             ...       }
    
def count_kmers(kmer_list):
#takes a kmers list and creates a dictionary where the key is the kmer, and the value is the number of times you see that kmer. this is a lot like what inchworm does. finds kmer, if it hasnt seen it yet, adds to a dictionary. otherwise it will add to the counter

	kmer_count_dict = dict()
	for kmer in kmer_list:
		if kmer in kmer_count_dict:
			kmer_count_dict[kmer] +=1
		else:
			kmer_count_dict[kmer] = 1
	return kmer_count_dict



def main():

	progname = sys.argv[0]
    
	usage = "\n\n\tusage: {} filename.fastq kmer_length num_top_kmers_show\n\n\n".format(progname)
    
	if len(sys.argv) < 4:
		sys.stderr.write(usage)
		sys.exit(1)

    # capture command-line arguments
	fastq_filename = sys.argv[1]
	kmer_length = int(sys.argv[2])
	num_top_kmers_show = int(sys.argv[3])

#the method from the first script that takes out a list of sequences from a fastqfile
	seq_list = seq_list_from_fastq_file(fastq_filename)
	all_kmers = [] 
#for each one of the sequences we need to pull out the kmers
#the code below will produce a list of kmers from each of the sequences in the list of sequences derived from the fastqfile	
	for seq in seq_list:
		kmers = sequence_to_kmer_list(seq, kmer_length)
#all_kmers list will now take kmers, which is actually a list of kmers, all_kmers will simply be a list of kmers rather than a list of lists.
#remember that extend will add all members of a list into the end of a list to extend it!
		all_kmers.extend(kmers)
#count_kmers is a function made which counts the list of all_kmers
	kmer_count_dict = count_kmers(all_kmers)
	unique_kmers = list(kmer_count_dict.keys())

    #########################
    ## Step 3: sort unique_kmers by abundance descendingly
    ## (Note, you can run and test without first implementing Step 3)
    ## begin your code       hint: see the built-in 'sorted' method documentation
#sort the values in the unique kmers not by the kmers themselves by the values in the actual dictionary based on x. It will sort on lowest to high initially. to make it high to low do reverse = true
	unique_kmers = sorted(unique_kmers, key = lambda x: kmer_count_dict[x], reverse = True)
    

    ## end your code

    ## printing the num top kmers to show
	top_kmers_show = unique_kmers[0:num_top_kmers_show]
    
	for kmer in top_kmers_show:
		print("{}: {}".format(kmer, kmer_count_dict[kmer]))
    
        

	sys.exit(0)  # always good practice to indicate worked ok!



if __name__ == '__main__':
	main()
