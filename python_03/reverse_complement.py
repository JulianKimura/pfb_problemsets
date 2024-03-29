#!/usr/bin/env python3

dna = 'ATGCAGGGGAAACATGATTCAGGAC'
#these steps below will replace letters with lower case complements, this allows me to maintain existing leters when I take the complement of others later
dna = dna.replace('A','t')

dna = dna.replace('T','a')

dna = dna.replace('C','g')

complement = dna.replace('G','c')

#this is making the entire new sequence all upper case
complement = complement.upper()

#this is taking the reverse sequence of the generated sequence above
reverse_complement = complement[::-1]

string = '''Original Sequence 5' ATGCAGGGGAAACATGATTCAGGAC 3'
Complement 3' {} 5'
Reverse Complement 5' {} 3'
'''
final_string = string.format(complement, reverse_complement)
print(final_string)

 
