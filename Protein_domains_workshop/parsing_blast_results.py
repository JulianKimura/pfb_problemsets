#!/usr/bin/env python3

import sys

fields = "qseqid sseqid percid alen mismat gaps q_start q_end s_start s_end evalue bits"
#here you are splitting the fields based on spaces, and turning the whole thing into a list. this will be fed into the dictionary
fields = fields.split(' ')


line_list = []
file_dict = {}
hits_list =[]
outputstring = ''

#if you want to have a script take in multiple files at once, you can create a for loop with the sys.argv statement, and make the sys.argv statement more vague by placing this: [1:] this will pull in every file you specify right next to the script on the command line
for hitfile in sys.argv[1:]:
#for every file that you input, do the following:
#open the file as an input file
	with open(hitfile, 'r') as input_file:
#for every line you open eliminate all line break characters
		for line in input_file:
			line = line.rstrip()
#if there isnt a # in the line do the following
			if '#' not in line:
#this line will zip together all of the field names you specified before as a key, and split the lines based on \t 
				hit_data = dict(zip(fields,line.split('\t')))
#this will create a dictionary entry called file that will have the name of the input file as the key terms
				hit_data['file'] = hitfile
#this will append the hit_data dictionary onto the master list that will contain all of the files materias ont it
				hits_list.append(hit_data)
				break

#this prints out the output from above into a clean and table format
for hit in hits_list:
	print('\t'.join([hit[x] for x in ('file', 'percid','alen','evalue')]))


