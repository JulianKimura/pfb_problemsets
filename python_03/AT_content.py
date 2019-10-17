#!/usr/bin/env python3

dna = 'AATTGGCCA'

dna_length = float(len(dna))

As = float(dna.count('A'))
Ts = float(dna.count('T'))
Gs = float(dna.count('G'))
Cs = float(dna.count('C'))

AT_content = (As + Ts)/dna_length
GC_content = (Gs + Cs)/dna_length

string = 'The AT content is {} and the GC content is {}'
final_string = string.format(AT_content, GC_content)

print(final_string)


