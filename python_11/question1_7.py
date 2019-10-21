#!/usr/bin/env python3


#a custom class is created here
class dna_seq(object):
#here I am using the init command which allows the class to read in user input
#the format shows the order by which the user should input when the user wants to extract specific things from the class. 
	def  __init__(self, sequence1, gene_name1, organism1, sequence2, gene_name2, organism2):
		self.sequence1 = sequence1
		self.gene_name1 = gene_name1
		self.organism1 = organism1
		self.sequence2 = sequence2
		self.gene_name2 = gene_name2
		self.organism2 = organism2
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
#below we have a method for finding the gc content of the sequence
	def GC_content(self):
		Gs = int(self.sequence.count('G'))
		Cs = int(self.sequence.count('C'))
		total_length = len(self.sequence)
		GC = (Gs+Cs)/total_length
		return GC
#below we have a method for returning the inputted sequence in a fasta format
	def fasta_format(self):
		header = '>'+self.gene_name
		sequence = self.sequence
		string = "{}\n{}"
		final_string = string.format(header, sequence)
		return final_string
#below we have a method for comparing two different sequence records and returns true if they are the same, false if they are different. sameness is based on name, organism, sequence
	def seq_similarity(self):
		gene_information1 = self.sequence1, self.gene_name1, self.organism1
		gene_information2= self.sequence2, self.gene_name2, self.organism2
		if gene_information1 == gene_information2:
			x = 'true'
		else:
			x = 'false'
		return x
	 
			

######here we are creating a class with the sequence, gnee_name, and organism attributes
sequence1 = 'ATGC'
gene_name1 = 'coolguy'
organism1 = 'julian'
sequence2 = 'ATGC'
gene_name2 = 'coolguy'
organism2 = 'julian'


dna_seq_object = dna_seq(sequence1, gene_name1, organism1, sequence2, gene_name2, organism2)

print(dna_seq_object.seq_similarity())

