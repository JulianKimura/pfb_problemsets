#!/usr/bin/env python

import os, sys

## method: seq_list_from_fastq_file(fastq_filename)
##
##  Extracts the sequence lines from a fastq file and returns a list
##  of the sequence lines
##
##  input parameters:
##
##  fastq_filename :  name of the fastq file (type: string)
##
##  returns seq_list : list of read sequences.
##                    ie.  ["GATCGCATAG", "CGATGCAG", ...]


def seq_list_from_fastq_file(fastq_filename):

	seq_list = list()

	with open('reads.fq','r') as fastq_file:
		line_count = 0
		for line in fastq_file:
			line = line.rstrip()
			line_count += 1
			#we know that we have a periodcity of 4. we want the 2nd one of 4 lines. if we do a %4 on the line coounter on each line, we will get 1, 2, 3, 0, 1, 2, 3, 0 for each line!! this means that for every 2nd line in the 4 line block %4 will be 2				
			if (line_count %4 ==2):
				seq_list.append(line)
    
#this function will return the seq_list back into the script
	return seq_list


def main():
#this defines the prgname asthe name of the script
	progname = sys.argv[0]
	usage = "\n\n\tusage: {} filename.fastq num_seqs_show\n\n\n".format(progname)
#if the user doesnt input the proper number of lines in the command line then it will print out the usage string above and will exit the script with an error
	if len(sys.argv) < 3:
		sys.stderr.write(usage)
		sys.exit(1)
#we are captureing the command line arguments. 
    # capture command-line arguments
	fastq_filename = sys.argv[1]
	num_seqs_show = int(sys.argv[2])
#needs to use the function used above and define the seq_list as list once again. 
	seq_list = seq_list_from_fastq_file(fastq_filename)
#print out the sequences from the list from 0-9. the first 10 instamces
	print(seq_list[0:num_seqs_show])
#will exit successfully
	sys.exit(0)  # always good practice to indicate worked ok!



if __name__ == '__main__':
    main()
