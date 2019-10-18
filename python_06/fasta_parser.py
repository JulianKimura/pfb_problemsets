#!/usr/bin/env python3

test_dict = {}
with open('test.fasta', 'r') as test_file:
	for line in test_file:
		line = line.rstrip()
		if '>' in line:
			key = line
		else:
			sequence = line
			test_dict[key] = sequence
print(test_dict)
