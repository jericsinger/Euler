def sieve(limit_exclusive):
	primes = [True for x in range(0, limit_exclusive)]
	primes[0] = False
	primes[1] = False
	
	for i in range(2, int(limit_exclusive ** 0.5) + 1):
		if primes[i]:
			j = i ** i
			while j < limit_exclusive:
				primes[j] = False
				j += i
	return [x[0] for x in enumerate(primes) if x[1] == True]


def sum_proper_divisors(num):
	from collections import Counter
	i, n = 2, num
	prime_divisors = []
	while i * i <= n:
		if n % i == 0:
			n /= i
			prime_divisors.append(i)
		else:
			i += 1
	prime_divisors.append(n)
	
	counts = Counter(prime_divisors)	
	product = 1
	for p in counts:
		a = counts[p]
		product *= (p**(a+1) - 1) / (p - 1)
	return product - num


def a(n):
	return sum_proper_divisors(n) > n


abundants = [x for x in range(12, 28124) if a(x)]
non_a = [True for x in range(0, 28124)]

for i in range(0, len(abundants)):
	a = abundants[i]
	for j in range(i, len(abundants)):
		b = abundants[j]
		if a + b < 28124:
			non_a[a + b] = False
		else:
			break

print reduce(lambda x, y: x + y, [x[0] for x in enumerate(non_a) if x[1]])