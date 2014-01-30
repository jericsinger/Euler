import math

def isPrime(q):	# test if q is prime
	"""Test if q is prime. Returns True/False"""
	
	prime = False	
	
	for i in range(2, int(math.sqrt(q))):
		if q % i == 0:
			break
	else:
		prime = True
	return prime


count = 0
num = 1

while count != 10001:
	num += 1
	if isPrime(num):
		count += 1

		
print num
	