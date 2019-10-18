#!/usr/bin/env python3

my_list = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

lengths = [(len(x),x) for x in my_list]

print(lengths)
