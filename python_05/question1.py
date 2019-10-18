#!/usr/bin/env python3



key_list = ['book', 'song', 'tree']
favorite_list = ['1984', 'bohemian rhapsody', 'oak']

fav_dict = {}

for value in range(3):
	fav_dict[key_list[value]] = favorite_list[value]

fav_dict['organism'] = 'pangolin'

#here, the command input is making the script give you a choice, and once you select one, it will feed it into the print command at the botton where it prints the dictionary entry
str = input('type in new organism')
fav_dict['organism'] = str

key_list = ['book', 'song', 'tree', 'organism']
favorite_list = ['1984', 'bohemian rhapsody', 'oak', 'pangolin']
 
for x in key_list:
	print('values:', fav_dict[x])
	print('keys:', x)

  


 

