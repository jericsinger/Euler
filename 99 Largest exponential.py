import math, urllib2
response = urllib2.urlopen('http://projecteuler.net/project/base_exp.txt')
pairs = [x.rstrip('\n').split(',') for x in response.readlines()]
max_result, max_line = 0, 0
line = 1

for pair in pairs:
	x, y = int(pair[0]), int(pair[1])
	result = y * math.log(x)
	if result > max_result:
		max_result, max_line = result, line
	line += 1

print max_line