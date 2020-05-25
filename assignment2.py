#!/usr/bin/env python3
# Kaushik Das
import sys
list_movies = ["Love Actually", "STAR WARS", "From Russia With love",
"Dr. Strangelove", "Bourne Ultimatum", "The fault in our stars",
"Bourne supremacy", "A star is born", "Starsky and Hutch",
"Star Trek", "Lover's Paradise", "A Christmas Star",
"Ernest Saves Christmas","A CHRISTMAS CAROL",
"The Muppet Christmas Carol", "White Christmas"]

word_dict = {}

for movie in list_movies:
	word_list = movie.split()
	for word in word_list:
		if word.lower() in word_dict.keys():
			word_dict[word.lower()] += 1
		else :
			word_dict[word.lower()] = 1

while True:
	sprompt = input("Enter a your serch word: ")
	if sprompt.isspace() or len(sprompt)==0: 
		sys.exit()

	input_list = sprompt.lower().split()
	input_list.sort()
	for input_word in input_list:
		if input_word.lower() in word_dict.keys() :
			print("{0} {1}".format(input_word.lower()[0:1].upper()+input_word.lower()[1:].ljust(10, " "), 
				'*' * word_dict[input_word.lower()]))
