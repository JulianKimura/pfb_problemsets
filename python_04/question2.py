#!/usr/bin/env python3
#made a string
taxa = 'sapiens, erectus, neanderthalensis'

print(taxa)

print(taxa[1])

type(taxa)

#splits the string into a list
species = taxa.split(', ')

print(species)

print(species[1])


print(type(species))

#alphabetically sort the species list and print it
alphabetical_species = sorted(species)
print(alphabetical_species)

#sorted the list based on the length of the species
length_speciesname = sorted(species, key=len)
print(length_speciesname)




