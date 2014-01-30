def euler53(limit, exceeds):
	import math
	results = []
	for n in range(0, limit + 1):
		for r in range(0, n):
			nCr = math.factorial(n) / (math.factorial(r) * math.factorial(n - r))
			results.append(nCr)
	count = 0
	for i in results:
		if i > exceeds:
			count += 1
	return count


print euler53(100, 1000000)