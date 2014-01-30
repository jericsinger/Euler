candidates = {}
count = 0
for length in range(1, 25):
	candidates[length] = []
	j = 1
	result = 1
	while len(str(result)) <= length:
		if len(str(result)) == length:
			candidates[length].append("%s = %s^%s" % (result, j, length))
			count += 1
		j += 1
		result = j ** length

for i in candidates:
	for j in candidates[i]:
		print j
print count