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
	return [x for x in range(0, limit) if primes[x]]

primes = get_primes(100)
limit = 1000000
i = 0
result = 1
while result * primes[i] < limit:
	result *= primes[i]
	i += 1
print result