def getPrimes(n):
	primes = []
	for i in range(0, n):
		primes.append(True)
	
	results = []
	
	for i in range(2, math.sqrt(n) + 1):
		if primes[i] == True:
			j = i * i
			while j < n + 1:
				primes[j] = False
				j += i
	
	for i in primes:
		if i > 1 and primes[i] == true:
			results.append(i)
	
	return results


print getPrimes(50)
