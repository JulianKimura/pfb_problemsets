#!/usr/bin/env python3

import re

with open('bowtie2.sam', 'r') as samfile:
	gene_name_list = []
	gene_count_dict = {}
	for line in samfile:
		line = line.rstrip()
		line_list = line.split('\t')
		gene_name = re.sub(r"\^.+","",line_list[2])
		if gene_name not in gene_count_dict:
			gene_count_dict[gene_name] = set()
#use the .add method for sets. this appends a new item to the set. but because it is a set, if it is a duplicate, it wont be a new entry.
		gene_count_dict[gene_name].add(line_list[0])
	genes = gene_count_dict.keys()






'''BRIAN HAAS SOLUTION
sam_file = sys.argv[1]
	with open(sam_file) as fh:
		for line in fh:
			fields = line.split("\t")
			read_name = fields[0]
			gene_trans = fields[2]
			gene, trans = gene_trans.split("^")
			if gene not in gene_to_reads_dict:
				gene_to_reads_dict[gene] = set()
			gene_to_reads_dict[gene].add(read_name)
	print(gene_to_reads_dict)
	genes = list(gene_to_reads_dict.keys()
	genes = sorted(genes, key = lambda x : len(gene_to_reads_dict[x]), reverse = True)
	for gene in genes:
		read_set = gene_to_reads_dict[gene]
		print("{}\t{}".format(gene,len(read_set)))
'''
'''
		gene_name_list.append(line_list[2])
	gene_name_set = set(gene_name_list)
	gene_name_uniq = list(gene_name_set)
	print(gene_name_uniq)
'''


'''
	for gene in gene_name_list:
		if gene in gene_count_dict:
			gene_count_dict[gene] +=1
		else:
			gene_count_dict[gene] = 1
print(gene_count_dict)	
'''
