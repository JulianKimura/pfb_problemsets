#!/usr/bin/env python3

with open('Python_06.txt', 'r') as song, open('Python_06.seq.txt', 'w') as new_file:
	for line in song:
		uppercase_song = line.upper()
		new_file.write(str(uppercase_song))



