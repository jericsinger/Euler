def getPrimes(n):
	import math
	primes = []
	for i in range(0, n):
		primes.append(True)
	
	results = []
	i = 2
	
	while i < math.sqrt(n) + 1:
		if primes[i] == True:
			j = i * i
			while j < n:
				primes[j] = False
				j += i
		i += 1	
	
	for i in range(0, n):
		if i > 1 and primes[i] == True:
			results.append(i)
	
	return results


def isPrime(num, primes):
	i = 0
	while primes[i] <= num:
		if primes[i] == num:
			return True
		i += 1
	return False



def checkPrimes(a, b, primelist):
	n = 0
	pMax = primelist[-1]
	while True:
		result = math.fabs(n ** 2 + a * n + b)
		
		if result > pMax:
			print "not enough primes!"
			break
		if result in primelist:
			n += 1
		else:
			return n


def run():
	import math
	primes = getPrimes(1000000)
	print "Created prime list."
	
	bList = []
	i = 0
	while primes[i] < 1000:
		bList.append(primes[i])
		i += 1
	
	
	aMax = 0
	bMax = 0
	nMax = 0
	for a in range(-999, 999, 2):
		for b in bList:
			n = 0
			while isPrime(math.fabs(n ** 2 + a * n + b), primes):
				n += 1
			
			if n > nMax:
				aMax = a
				bMax = b
				nMax = n
	print "RESULTS"
	print "a =", aMax
	print "b =", bMax
	print "n =", nMax
	print "a*b =", aMax * bMax



run()
