#!/usr/bin/env python3

import re

#open the file
with open('Python_07_ApoI.fasta.txt', 'r') as fasta:
#for loop through each line in the fasta
	for line in fasta:
#eliminate all new line characters
		line = line.rstrip()
#in this regex, we are iterating through the line, looking for the particular variable matches that is defined by
#the regex. here, the brackets isolates a specific and/or statement from the rest of the string.
		for matches in re.findall(r"[A|G]AATT[C|T]",line): 
#having print nested within the for loop makes the matches variable print everytime the for loop rins on each line
			print(matches) 	
