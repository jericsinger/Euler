def getPrimes(n):
	import math
	primes = []
	for i in range(0, n + 1):
		primes.append(True);
	
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



def getCircs(num):
	from collections import deque
	
	digits = deque(list(str(num)))
	results = []
	for i in range(0, len(digits)):
		results.append(int(''.join(digits)))
		digits.appendleft(digits.pop())
	return results



def checkCircs(circs, primes):
	for i in circs:
		if primes[i] == True:
			continue
		else:
			return False
	return True


def run(n):
	circ_primes = []
	for i in range(0, n + 1):
		circ_primes.append(False)
	
	primes = getPrimes(n)
	print "Got primes. Checking circs..."
	
	for i in range(0, n + 1):
		if circ_primes[i] == True:
			continue
		if primes[i] == True:
			circs = getCircs(i)
			check = checkCircs(circs, primes)
			if check == True:
				for num in circs:
					circ_primes[int(num)] = True
	
	results = []
	for i in range(2, n + 1):
		if circ_primes[i] == True:
			results.append(i)
	print "There are %s circular primes below %s" % (len(results), n)
	print results


run(1000000)