import math

n = 2000000
primes = [True for x in range(0, n + 1)]

primes[0] = False
primes[1] = False

for i in range(2, int(math.sqrt(n)) + 1):
	if primes[i] == True:
		j = i * i
		while j < n + 1:
			primes[j] = False
			j += i
	
prime_sum = 0
for i in list(enumerate(primes)):
	if i[1]:
		prime_sum += i[0]

print prime_sum