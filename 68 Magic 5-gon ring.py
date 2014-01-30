def sum_check(list_of_lists):
	for i in range(0, len(list_of_lists)):
		if sum(list_of_lists[i]) != sum(list_of_lists[0]):
			return False
	return True


def use_check(list_of_lists, n):
	all_items = set([item for sublist in list_of_lists for item in sublist])
	return all_items == set(range(1, n + 1))


def gon_check(list_of_lists):
	for i in range(0, len(list_of_lists)):
		j = i + 1 if i < len(list_of_lists) - 1 else 0
		if list_of_lists[i][2] != list_of_lists[j][1]:
			return False
	return True


def ring_sums(n):
	nums = range(1, n+1)
	size = n / 2
	return range(sum(nums[:size]), sum(nums[size:]) + 1, size)

def gons(solution_set):
	items = [i for sub in solution_set for i in sub]
	counts = {}
	for key in items:
		if key in counts:
			counts[key] += 1
		else:
			counts[key] = 1
	return counts

def is_solution(solution_set, n):
	inners = []
	outers = [x[0] for x in solution_set]
	for i in range(0, len(solution_set)):
		inners.extend(solution_set[i][1:])
		j = i + 1 if i < len(solution_set) - 1 else 0
		if solution_set[i][2] != solution_set[j][1]:
			return False
	if set(outers).intersection(set(inners)) == set([]):
		if set(outers).union(set(inners)) == set(range(1, n+1)):
			return True
	return False


def rings(n):
	import itertools
	nums = range(1, n+1)
	d, l, r = {}, {}, {}
	sets = itertools.permutations(nums, 3)
	for subset in sets:
		key = sum(subset)
		if key in d:
			d[key].append(subset)
		else:
			d[key] = [subset]
	for key in d:
		if set([i for sub in d[key] for i in sub]) == set(nums):
			l[key] = d[key]
	for key in l:
		trial_set = l[key]
		trials = [x for x in itertools.combinations(trial_set, n / 2) if set([i for sub in x for i in sub]) == set(nums) and is_solution(x, n)]
		print trials




def rings_new(n):
	import itertools, collections
	nums = range(1, n+1)
	sets = sorted([x for x in itertools.permutations(nums, 3)])
	d, o = {}, {}
	for s in sets:
		k = sum(s)
		if k in d:
			d[k].append(s)
		else:
			d[k] = [s]
	for k in d:
		o[k] = [x for x in itertools.permutations(d[k], n/2) if is_solution(x, n)]
		o[k] = sorted(o[k])[:n/2 - 1]
		print k
		print o[k]
		print '-----'


rings_new(10)
