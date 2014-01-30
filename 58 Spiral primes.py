from __future__ import division

def is_prob_prime(n, k = 7):
	# http://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Primality_Testing
	import random, sys
	if n < 6:
		return [False, False, True, True, False, True]
	elif n & 1 == 0:
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
						return False
					elif x == n - 1:
						a = 0
						break
				if a:
					return False
		return True


# Too constrained
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

def get_diags(lim):
	prime_diags = [False]
	diags = [1, 3, 5, 7, 9]
	width = 3
	n = 9
	a, b = 3, len(diags)
	ratio = a / b
	
	while ratio >= lim:
		width += 2
		interval = width - 1
		limit = width ** 2
		while n < limit:
			n += interval
			if is_prob_prime(n):
				a += 1
			b += 1
		ratio = a / b
	print "ratio = %s / %s = %s" % (a, b, a / b)
	return width



print get_diags(0.1)