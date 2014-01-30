import urllib2
response = urllib2.urlopen("http://projecteuler.net/project/keylog.txt")
lines = response.readlines()
entries = [x[:-1] for x in lines]

digits = {x: {'ante' : [], 'post' : []} for x in '0123456789'}

for entry in entries:
	a, b, c = entry[0], entry[1], entry[2]
	digits[a]['post'].extend([b, c])
	digits[b]['ante'].append(a)
	digits[b]['post'].append(c)
	digits[c]['ante'].extend([a, b])

for digit in digits:
	for time in ['post', 'ante']:
		digits[digit][time] = set(digits[digit][time])
		

for digit in digits:
	if len(digits[digit]['post']) - len(digits[digit]['ante']) != 0:
		digits[digit]['order'] = len(digits[digit]['ante'])

code = []
for digit in sorted(digits.keys()):
	if 'order' in digits[digit].keys():
		code.append([digits[digit]['order'], digit])

access = ''
code.sort(key=lambda x: x[0])
for i in code:
	access += i[1]

print access