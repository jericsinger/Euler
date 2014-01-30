index = 2
a = 1
b = 1
c = 2
while len(str(c)) < 1000:
	c = a + b
	a = b
	b = c
	index += 1
print index