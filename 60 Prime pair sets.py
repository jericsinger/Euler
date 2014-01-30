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


def is_prob_prime(n, k = 7):
	# Use Rabin-Miller algorithm to return True (n is probably prime) or False (n is definitely composite)
	# http://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Primality_Testing
	import random, sys
	if n < 6: # assuming n >= 0 in all cases... shortcut small cases here
		return [False, False, True, True, False, True]
	elif n & 1 == 0: # should be faster than n % 2
		return False
	else:
		s, d = 0, n - 1
		while d & 1 == 0:
			s, d = s + 1, d >> 1
		for a in random.sample(xrange(2, min(n - 2, sys.maxint)), min(n - 4, k)):
			x = pow(a, d, n)
			if x != 1 and x + 1 != n:
				for r in xrange(1, s):
					x  = pow(x, 2, n)
					if x == 1:
						return False # composite for sure
					elif x == n - 1:
						a = 0 # so we know loop didn't continue to end
						break # could be strong liar, try another a
				if a:
					return False # composite if we reached end of this loop
		return True # probably prime if reached end of outer loop

def solve():
	import itertools	
	limit = 1000000
	primes_tf = get_primes(limit)
	primes = [x for x in range(0, limit) if primes_tf[x] and x < 30000]
	print "primes retrieved. continuing..."
	
	def test(prime_set):
		concat_set = [int(''.join(x)) for x 
					  in itertools.permutations(prime_set, 2)]
		for i in concat_set:
			if i > limit:
				if not is_prob_prime(i):
					return False
			elif not primes_tf[i]:
				return False
		return True
	
	min_sum = 30000
	min_set = []
	for a in xrange(5, len(primes)):
		for b in xrange(a+1, len(primes)):
			prime_set = [str(primes[x]) for x in [a, b]]
			if sum([int(x) for x in prime_set]) > min_sum:
				break
			elif test(prime_set):
				for c in xrange(b+1, len(primes)):
					prime_set = [str(primes[x]) for x in [a, b, c]]
					if sum([int(x) for x in prime_set]) > min_sum:
						break
					elif test(prime_set):
						for d in xrange(c+1, len(primes)):
							prime_set = [str(primes[x]) for x in [a, b, c, d]]
							if sum([int(x) for x in prime_set]) > min_sum:
								break
							elif test(prime_set):
								print prime_set
								for e in xrange(d+1, len(primes)):
									prime_set = [str(primes[x]) for x in [a, b, c, d, e]]
									if sum([int(x) for x in prime_set]) > min_sum:
										break
									elif test(prime_set):
										print prime_set, sum([int(x) for x in prime_set])


solve()

def test(prime_set):
	import itertools
	primes = get_primes(1000000)
	primes = [x for x in range(0, len(primes)) if primes[x]]
	concat_set = [int(''.join(x)) for x in itertools.permutations(prime_set, 2)]
	print concat_set
	for i in concat_set:
		if i not in primes:
			return False
	return True
