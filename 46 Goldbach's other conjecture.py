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


def euler46(limit):
	import math
	
	primes_tf = getPrimes(limit)
	primes_list = []	
	odd_composites_tf = []
	odd_composites_list = []
	
	for i in primes_tf:
		odd_composites_tf.append(False)
	
	for i in range(0, len(primes_tf)):
		if primes_tf[i] == False and i % 2 > 0 and i > 1:
			odd_composites_tf[i] = True
			odd_composites_list.append(i)
	
	for i in range(0, len(primes_tf)):
		if primes_tf[i] == True:
			primes_list.append(i)
	
	audit = []
	for num in odd_composites_list:
		found = False
		for prime in primes_list:
			square = (num - prime) / 2
			if square < 1:
				break
			sqrt = square ** 0.5
			if sqrt == int(sqrt):
				found = True
				audit.append("%s = %s + 2x%s^2" % (num, prime, int(sqrt)))
				break
		if found == False:
			return num


print euler46(10000)