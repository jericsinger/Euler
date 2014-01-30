from sys import argv
import math

script, to_factor = argv
to_factor = int(to_factor)

def isPrime(q):	# test if q is prime
	"""Test if q is prime. Returns True/False"""
	
	prime = False	
	
	for i in range(2, int(math.sqrt(q))):
		if q % i == 0:
			break
	else:
		prime = True
	return prime


def isFactor(q, x): # test if q is a factor of x
	"""Test if q is a factor of x. Returns True/False"""
	
	factor = False
	
	if x % q == 0:
		factor = True
		
	return factor


primes = []
i = 2

while i <= to_factor:

	if isFactor(i, to_factor) and isPrime(i):
		primes.append(i)
		to_factor = to_factor / i
		i = 2
	else:
		i += 1

print primes