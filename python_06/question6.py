#!/usr/bin/env python3

cat_line_list = []
with open('alpaca_all_genes.tsv', 'r') as all_genes:
	for line in all_genes:
		line = line.rstrip()
		line_list = line.split('\t')
		cat_line_list.extend(line_list)
	print(cat_line_list)
#at this step we have made the list for one of the files. make this list into a set, and then do it for the rest of the files that you have downloaded


