from __future__ import division

def find_chain(now):
	from math import factorial as f
	
	def sum_factorial_digits(num):
		return reduce(lambda x, y: x+y, [f(int(x)) for x in list(str(num))])
	
	chain = [now]
	while True:
		next = sum_factorial_digits(now)
		try:
		 	chain.index(next)
			return chain
		except ValueError:
			chain.append(next)
			now = next
			if len(chain) > 60:
				return chain




def run(limit):
	from itertools import permutations as p
	count = 0
	result = []
	seeds = [False for x in range(0, limit)]
	for n in range(0, limit):
		if not seeds[n]:
			chain = find_chain(n)
			if len(chain) == 60:
				perms = [int(''.join(x)) for x in p(str(n))]
				result.extend([x for x in perms if len(str(x)) == len(str(n))])
			for x in chain:
				if x < limit:
					if not seeds[x]:
						perms = [int(''.join(x)) for x in p(str(x))]
						for y in perms:
							if y < limit:
								seeds[y] = True
			count += 1
	return set(result)


result = run(1000000)
print len(result)
