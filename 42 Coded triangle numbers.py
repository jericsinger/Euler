def getTriangles(limit):
	triangles = []
	for i in xrange(0, limit + 1):
		triangles.append(False)
	t = 0
	n = 0
	while True:
		t = (n ** 2 + n) / 2
		if t > limit:
			break
		else:
			triangles[t] = True
			n += 1
	return triangles


def getValues():
	letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	value = 1
	values = {}
	for letter in letters:
		values[letter] = value
		value += 1
	return values


def getValue(word, values):
	value = 0
	for char in word:
		value += values[char]
	return value


def euler42():
	# find longest word --> max required triangle numbers
	import urllib2
	response = urllib2.urlopen('http://projecteuler.net/project/words.txt')
	words = response.read().split(',')
	max_len = 0
	for i in xrange(0, len(words)):
		words[i] = words[i].replace('"', '')
		max_len = max(max_len, len(words[i]))
	max_value = max_len * 26
	
	# get list of triangle numbers and letter values
	triangles = getTriangles(max_value)
	values = getValues()
	
	# iterate through words, counting those that are triangle
	count = 0
	for word in words:
		if triangles[getValue(word, values)]:
			count += 1
	print "Triangle words in words.txt:", count


euler42()