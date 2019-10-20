#!/usr/bin/env python3
#######this script will calculate the GC content of an input sequence on the command line

#import sys and specify tha the first input after the script on the command line is the sequence
import sys
dna = sys.argv[1]

#creating a function
def gc_content(dna):
#counts the Gs and Cs of the sequence provided and the total length of the sequence 
#calculates the GC content then spits out a final string
	c_count = dna.count('C')
	g_count = dna.count('G')
	sequence_length = len(dna)
	gc_content = ((c_count+g_count)/sequence_length)*100
	output_string = "The GC content of the sequence is {}%"
	final_string = output_string.format(gc_content)
	print(final_string)

####creating a function
gc_content(dna)
