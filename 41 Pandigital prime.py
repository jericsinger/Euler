def isPan(num):
	if num > 987654321 or num < 1:
		return False
	digits = set('123456789'[0:len(str(num))])
	num_set = set(list(str(num)))
	return digits == num_set


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
	return primes


def primePans(n):
	import itertools
	perms_iter = itertools.permutations('123456789'[:n])
	perms_list = []
	prime_ends = ['1', '3', '7', '9']
	for i in perms_iter:
		if i[-1] in prime_ends:
			perms_list.append(''.join(i))
	return perms_list


def isProbPrime(n, k = 7):
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


def euler41():
	n = 9
	while n > 1:
		pans = primePans(n)
		prime_pans = []
		for i in reversed(pans):
			if isProbPrime(int(i)):
				return i
		n -= 1
	return False


print euler41()