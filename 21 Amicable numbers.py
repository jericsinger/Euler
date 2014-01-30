def d(n):
	if n < 2: return False
	
	divisors = [x for x in range(1, n // 2 + 1) if n % x == 0]
	return reduce(lambda x, y: x + y, divisors)


amicables = []
for i in range(2, 10000):
	if d(d(i)) == i and d(i) != i:
			amicables.append(i)

print reduce(lambda x, y: x + y, amicables)
