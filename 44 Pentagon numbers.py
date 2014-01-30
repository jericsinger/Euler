def isPent(num):
	import math
	result = (math.sqrt(1 + 24 * num) + 1) / 6
	return result == int(result)


def euler44():
	result = 0
	found = False
	j = 1
	
	while not found:
		p_j = j * (3 * j - 1) / 2
		
		for k in range(j - 1, 0, -1):
			p_k = k * (3 * k - 1) / 2
			if isPent(p_k - p_j) and isPent(p_j + p_k):
				result = p_k - p_j
				found = True
				break


print euler44()