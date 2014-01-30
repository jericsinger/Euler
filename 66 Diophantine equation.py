
Ds = [d for d in range(1, 1000) if d ** 0.5 != int(d ** 0.5)]
answer = {'D' : 0, 'x' : 0}

def pell(d):
	import math
	p, k, x1, y, sd = 1, 1, 1, 0, d ** 0.5
	
	while k != 1 or y == 0:
		p = k * (p / k + 1) - p
		p = p - int((p - sd) / k) * k
		
		x = (p * x1 + d * y) / abs(k)
		y = (p * y + x1) / abs(k)
		k = (p * p - d) / k
		
		x1 = x
	
	return x
	


for d in Ds:
	x = pell(d)
	if x > answer['x']:
		answer = {'D' : d, 'x' : x}

print answer


# http://blog.dreamshire.com/2011/01/22/project-euler-problem-66-solution/