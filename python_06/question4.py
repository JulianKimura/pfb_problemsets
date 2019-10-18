#!/usr/bin/env python3

#when making counters, have to pre-define the variables
total_char = 0
total_lines = 0 
#open the fastq file
with open('Python_06.fastq.txt', 'r') as fastq_file:
	for line in fastq_file:
#for loop where it looks at the length of each line, stores it into the char_line variab;e
		char_line = len(line)
#for every loop, we add in the number found in char_line into the total character counter that was started at 0
		total_char += char_line
#for every loop, we add 1 to the total line counter
		total_lines += 1
#taking the average line length by dividing the values shown above
	average_line_length = total_char/total_lines
	string = '''Total number of characters: {}
Total number of lines: {}
Average line length: {}'''
	char_string = string.format(total_char, total_lines, average_line_length)
	print(char_string)




