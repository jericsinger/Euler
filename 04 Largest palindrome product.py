max = max_a = max_b = 0

# build a list of palindromic products of 3-digit numbers
for a in range(999, 99, -1):
	for b in range(990, 99, -1):
		if a * b > max:
			string = str(a * b)
			if string == string[::-1]:
				max = a * b
				max_a = a
				max_b = b

print "%d * %d = %d" % (max_a, max_b, max)
	
