#!/usr/bin/env python3

total_char = 0
total_lines = 0 
with open('Python_06.fastq.txt', 'r') as fastq_file:
	for line in fastq_file:
		char_line = len(line)
		total_char += char_line
		total_lines += 1
	average_line_length = total_char/total_lines
	string = '''Total number of characters: {}
Total number of lines: {}
Average line length: {}'''
	char_string = string.format(total_char, total_lines, average_line_length)
	print(char_string)




