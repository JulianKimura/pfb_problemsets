#!/usr/bin/env python3

from Bio import SeqIO

n = 0
nt_count = 0
seq_length = 0
for seq_record in SeqIO.parse("test.fa", "fasta"):
	n += 1
	for nt in seq_record.seq:
		nt_count +=1
	seq_length += int(len(seq_record.seq))
	avg_length = seq_length/n
sequence_count = "Sequence count: {}".format(n)
total_nucleotides = "Total number of nucleotides: {}".format(nt_count)
Average_seq_length = "Average length of Sequence : {}".format(avg_length)
print(sequence_count)
print(total_nucleotides)
print(Average_seq_length)

