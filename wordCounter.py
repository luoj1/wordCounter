import re

def wordCounter(src, target):
	if not src:
		raise ValueError('input address is null')
		return
	if not target:
		raise ValueError('output address is null')
		return
	wordDictionary = {}
	with open(src, 'r') as file:
		line = file.readline()
		while not line == '':
			line = line[:-1];
			# regex that replace everything that is not letter, number, dash or hyphen by space (' ')
			# split the processed line by space
			line =  re.sub("[^0-9^a-z^A-Z^\-^\_]", " ", line).split() 
			for word in line:
				word = word.lower()
				#check if word is a pure number
				if re.sub("[0-9\-\_]", "", word) == "":
					continue
				if word in wordDictionary:
					wordDictionary[word][0] += 1
				else:
					wordDictionary[word] = [1, word]
			line = file.readline()
	wordPair = [wordDictionary[key] for key in wordDictionary]
	wordPair = sorted(wordPair, key=lambda x: (x[0],ord('a') - ord(x[1][0])), reverse=True)
	with open(target, 'w') as writer:
		for pair in wordPair:
			writer.write(str(pair[0]) + ' ')
			writer.write(pair[1])
			writer.write('\n')


