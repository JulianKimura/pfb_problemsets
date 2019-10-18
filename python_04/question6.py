#!/usr/bin/env python3

my_list = [101,2,15,22,95,33,2,27,72,15,52]
even_list = []
odd_list = []

for number in my_list:
	if number%2 == 0:
		even_list.append(number)
	else:
		odd_list.append(number)

print(sum(even_list))
print(sum(odd_list))




	
	


