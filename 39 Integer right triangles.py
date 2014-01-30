def triangles(perimeter):
	import math
	solutions = []
	maxA = perimeter // 2
	for a in range(1, maxA):
		maxB = (perimeter - a) // 2
		for b in range(a, maxB):
			c = perimeter - a - b
			if c > 0:
				if a ** 2 + b ** 2 == c ** 2:
					solutions.append([a, b, c])
	return solutions


def euler39():
	maxLength = 0
	maxP = 0
	for p in range(0, 1001):
		if len(triangles(p)) > maxLength:
			print "NEW MAX: p = %s; count = %s; sets = %s" % (p, len(triangles(p)), triangles(p))
			maxLength = len(triangles(p))
			maxP = p
	print "RESULT: p = %s; count = %s; sets = %s" % (maxP, maxLength, triangles(maxP))


euler39()