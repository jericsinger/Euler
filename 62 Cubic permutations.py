from __future__ import division
import itertools
i = 1
count = 0
while True:
	print i
	cube = i ** 3
	permutations = itertools.permutations(str(cube), len(str(cube)))
	count = 0
	for trial in permutations:
		num = ''.join(trial)
		root = int(num) ** (1 / 3)
		if int(root) == root:
			print root
			count += 1
		if count >= 2:
			break
	i += 1

print i
