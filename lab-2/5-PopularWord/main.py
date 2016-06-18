def get_words(lines):
	words = {}
	lines = "".join([i for i in lines if not i in '!,.?;:"!@#$%^&*()_-+=<>/}{[]|'])
	for word in lines.replace('\n',' ').split(' '):
		words[word] = words[word]+1 if word in words else 1
	return [[i,words[i]] for i in sorted(words, key=words.get, reverse = True)]
def get_popular(words):
	return "---" if (len(words)>1) and (words[0][1] == words[1][1]) else words[0][0]
with open('input5.txt','r') as f:
	print(get_popular(get_words(f.read())))
