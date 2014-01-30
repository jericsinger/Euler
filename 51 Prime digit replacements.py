def get_primes(limit):
	import math
	primes = []
	for i in range(0, limit):
		primes.append(True);
	primes[0] = False
	primes[1] = False
	
	results = [];	
	for i in range(2, int(math.sqrt(limit)) + 1):
		if primes[i] == True:
			j = i * i
			while j < limit:
				primes[j] = False
				j += i
	return primes


def wildcards(n, primes):
	from collections import Counter as c
	import string
	n = list(str(n))
	digits = set(n)
	
	def count_primes(variants):
		count = 0
		for v in variants:
			count += 1 if primes[int(v)] else 0
		return count
	
	max_count = 0
	for d in digits:
		variants = []
		for i in string.digits:
			variants.append(''.join([i if x==d else x for x in n]))
			variants = [x for x in variants if x[0] != '0']
			count = count_primes(variants)
			if count > max_count:
				max_count = count
	return max_count

limit = 1000000
primes_tf = get_primes(limit)
print "primes retrieved. continuing..."
primes = [x for x in range(0, limit) if primes_tf[x]]
count = 0
i = 0
while count != 8:
	if i < len(primes):
		n = primes[i]
		count = wildcards(n, primes_tf)
		i += 1
	else:
		print "no solution. increase prime limit"
print n, count