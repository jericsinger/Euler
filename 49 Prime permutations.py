def getPrimes(limit):
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


primes = getPrimes(10000)
for i in range(1000, len(primes)):
	if primes[i]:
		j = 3330
		if i + 2*j > len(primes):
			break
		if set(list(str(i))) == set(list(str(i + j))):
			if set(list(str(i + j))) == set(list(str(i + 2*j))):
				if primes[i + j] and primes[i + 2*j]:
					print i, i + j, i + 2*j
					print str(i) + str(i + j) + str(i + 2*j)
