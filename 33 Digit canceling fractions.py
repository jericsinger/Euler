def frac():
	from fractions import Fraction
	results = []
	for n in range(10, 98):
		for d in range (n + 1, 100):
			n1 = n // 10
			n2 = n % 10
			d1 = d // 10
			d2 = d % 10
			if d2 == 0:
				continue
			if n2 == d1 and Fraction(n, d) == Fraction(n1, d2):
				print "%s/%s = %s/%s" % (n, d, n1, d2)
				results.append(Fraction(n, d))
	
	product = 1
	for i in results:
		product *= i
	print Fraction(product)


frac()