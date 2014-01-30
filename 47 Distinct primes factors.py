# http://stackoverflow.com/questions/23287/prime-factors
def prime_factors_set(n):
    """Returns all the prime factors of a positive integer"""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1: factors.append(n)
            break
    return list(set(factors))


def find_consecutives(n):
	i = 4
	count = 0
	while count < n:
		if len(prime_factors_set(i)) == n:
			count += 1
		if len(prime_factors_set(i)) != n and count > 0:
			count = 0
		i += 1
	nums = []
	for r in range(i - n, i):
		nums.append(r)
	return nums


print find_consecutives(4)