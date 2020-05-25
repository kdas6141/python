import re
search_ptrn = "Rob"
#search_ptrn = "^Rob"
search_ptrn = "Rob$"
regex = re.compile(search_ptrn, re.IGNORECASE)
f = open('names.txt')

for ln in f.readlines():
	#match = regex.search(ln)
	match = re.findall(regex, ln)
	if match:
		#print(ln[:-1])
		#print(match.group(), match.start(), match.end(), match.span())
		print(match)
f.close()

#f = open('names.txt')
#all_matches = re.findall(regex, f.read())
#f.close()
#print(all_matches)

