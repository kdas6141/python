#initialize the movie_titles list
movie_titles = ["Love Actually", "STAR WARS", "From Russia With love",\
                "Dr. Strange love", "Borne Ultimatum", "The fault in our stars",\
                "Borne supremacy", "A star is born", "Star sky and Hutch",\
                "Star Trek", "Lover's Paradise", "A Christmas Star",\
                "Ernest Saves Christmas","A CHRISTMAS CAROL",\
                "The Muppet Christmas Carol", "White Christmas"]

srch_str = ''
srch_str = input("Enter your search words, seperated by spaces: ")
if srch_str.strip() == '':
	print('No words were entered...exiting the program.')
	exit(0)


'''
Convert the string of words into a list of words
for each word in the list,
   change its case to Title case
   record its length in word_lent_list
Notes:
- We do the above processing in preparation for getting the format of the output correct
'''

srch_list = srch_str.split()
word_len_list = []
for i in range(len(srch_list)):
	srch_list[i] = srch_list[i].title()
	word_len_list = word_len_list + [ len(srch_list[i]) ]
max_len = max(word_len_list)

freq = {}
for title in movie_titles:
	words_in_title = title.split()
	for word in words_in_title:
		title_case = word.title()
		if title_case in freq.keys():
			freq[title_case] += 1
		else:
			freq[title_case] = 1


for key in sorted(freq.keys()):
	print("{0} {1}".format(key.ljust(max_len), '*'*freq[key]))