def combine(seed):
	result = []
	while len(seed) > 1:
		result.append(seed)
		end_sum = sum(seed[-2:])
		seed = seed[:-2]
		seed.append(end_sum)
	for i in result:
		i.reverse()
	return result	


def run(num):
	import itertools
	
	nums = [1] * num
	seeds = combine(nums)
	results = []
	for i in seeds:
		results.extend(combine(i))
	for i in results:
		i.sort()
	
	results.sort()
	result = list(k for k,_ in itertools.groupby(results))
	return result


print len(run(100))