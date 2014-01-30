from __future__ import division
import math

def cf_exp(limit):
	a = [2, 1, 2]
	n = 4
	while len(a) < limit:
		if a[-1] == 1 and a[-2] == 1:
			a.append(n)
			n += 2
		else:
			a.append(1)
	return a


def convergents(cf_notation):
	a = cf_notation
	h = [a[0], a[1]*a[0] + 1] 
	k = [1, a[1]]
	for n in range(2, len(a)):
		h.append(a[n]*h[n-1] + h[n-2])
		k.append(a[n]*k[n-1] + k[n-2])
	return zip(h, k)


cf = cf_exp(100)
c = convergents(cf)
num = c[-1][0]

print reduce(lambda x, y: int(x) + int(y), list(str(num)))