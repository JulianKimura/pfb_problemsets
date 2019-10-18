#!/usr/bin/env python3

#first make a dictionary
test_dict = {}

#open the file and make a for loop where we 
with open('Python_06.seq.txt', 'r') as seq_file:
	for line in seq_file:
		line = line.rstrip()
		seqName,sequence = line.split('\t')
		test_dict[seqName]=sequence

for key in test_dict:
	value = test_dict[key]
	value = value.replace('A','t')
	value = value.replace('T','a')
	value = value.replace('C','g')
	value = value.replace('G','c')
	value = value.upper()
	value = value[::-1]
	print(key, value)


 



