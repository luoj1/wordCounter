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
			line =  re.sub("[^0-9&^a-z&^A-Z&^\-&^\_]", " ", line).split() 
			for word in line:
				if word in wordDictionary:
					wordDictionary[word] = wordDictionary[word] + 1
				else:
					wordDictionary[word] = 1
			line = file.readline()

	with open(target, 'w') as writer:
		for word in wordDictionary:
			writer.write(word + ' ')
			writer.write(str(wordDictionary[word]))
			writer.write('\n')


