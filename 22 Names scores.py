import urllib2, string

response = urllib2.urlopen("http://projecteuler.net/project/names.txt")
names = response.read().split(',')
for i in range(0, len(names)):
	names[i] = names[i][1:-1]

names = list(enumerate(sorted(names), start=1))
scores = {}
score = 1
for letter in string.ascii_uppercase:
	scores[letter] = score
	score += 1

total = 0
for name in names:
	total += reduce(lambda x, y: x + y, [scores[x] for x in list(name[1])]) * name[0]


print total 
