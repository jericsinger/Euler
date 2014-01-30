for n in range(1, 998):
	for m in range (n+1, 999):

		if m**2 + m*n == 500:
			break
		else:
			continue

c = m ** 2 + n ** 2

print "a = %d, b = %d, c = %d, and abc = %d" % (m, n, c, m*n*c)