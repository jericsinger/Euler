def getPrimes(n):
	import math
	primes = []
	for i in range(0, n + 1):
		primes.append(True);
	primes[0] = False
	primes[1] = False
	
	results = [];
	
	for i in range(2, int(math.sqrt(n)) + 1):
		if primes[i] == True:
			j = i * i
			while j < n + 1:
				primes[j] = False
				j += i
	
	for i in range(2, len(primes)):
		if primes[i] == True:
			results.append(i)
	
	return primes



def run37(limit):
	def getTruncs(num):
		truncs = [num]
		num = str(num)
		for i in range(len(num) - 1, 0, -1):
			truncs.append(int(num[:i]))
			truncs.append(int(num[i:]))
		return truncs
	
	def testTruncs(num):
		truncs = getTruncs(num)
		for truncation in truncs:
			if primes[truncation] == False:
				return False
		return True
	
	
	primes = getPrimes(limit)
	prime_truncs = []
	sum = 0
	
	for i in range(10, len(primes)):
		if primes[i] == True and testTruncs(i) == True:
			sum += i
			prime_truncs.append(i)
			print prime_truncs
			if len(prime_truncs) >= 11:
				print sum
				return
	print "Truncatable primes found within limit of n<%s: %s" % (limit, len(prime_truncs))
	print "Sum:", sum


run37(1000000)