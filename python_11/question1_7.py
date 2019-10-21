#!/usr/bin/env python3


#a custom class is created here
class dna_seq(object):
#here I am using the init command which allows the class to read in user input
#the format shows the order by which the user should input when the user wants to extract specific things from the class. 
	def  __init__(self, sequence, gene_name, organism):
		self.sequence = sequence
		self.gene_name = gene_name
		self.organism = organism
#below a method called length is made, where it takes the length of the sequence attribute defined above, then return the output of the length such that you can print it out later as dna_seq_object.length()
	def length(self):
		length_of_sequence = len(self.sequence) 
		return length_of_sequence
#below a method for finding the nucleotide composition is defined
	def nt_composition(self):
		As = self.sequence.count('A')
		Ts = self.sequence.count('T')
		Gs = self.sequence.count('G')
		Cs = self.sequence.count('C')
		string = "There are {}A's, {}T's, {}G's, {}C's"
		final_string = string.format(As, Ts, Gs, Cs)
		return final_string
	def GC_content(self):
		Gs = int(self.sequence.count('G'))
		Cs = int(self.sequence.count('C'))
		total_length = len(self.sequence)
		GC = (Gs+Cs)/total_length
		return GC
	def fasta_format(self):
		fasta_dict = {}
		header = '>'+self.gene_name
		sequence = self.sequence
		string = "{}\n{}"
		final_string = string.format(header, sequence)
		return final_string


######here we are creating a class with the sequence, gnee_name, and organism attributes
sequence = 'ATGC'
gene_name = 'test_gene'
organism = 'julian'

dna_seq_object = dna_seq(sequence, gene_name, organism)

print(dna_seq_object.fasta_format())

