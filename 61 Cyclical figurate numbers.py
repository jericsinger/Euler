def get_lists():
	formulae = {3 : "x*(x+1)/2",
				4 : "x*x", 
				5 : "x*(3*x-1)/2", 
				6 : "x*(2*x-1)",
				7 : "x*(5*x-3)/2",
				8 : "x*(3*x-2)"}
	
	results = {}
	for index in formulae:
		result_list = []
		result = 0
		x = 1
		while result < 10000:
			result = eval(formulae[index])
			x += 1
			if result >= 1000 and result < 10000:
				result_list.append(str(result))
		results[index] = result_list
	return results




def get_permutations():
	import itertools
	nums = [3, 4, 5, 6, 7, 8]
	permutations = [x for x in itertools.permutations(nums, 6)]
	return permutations
# need to allow for non-sequential ordering

def euler61():
	lists = get_lists()
	permutations = get_permutations()
	longs = []
	for order in permutations:
		print "order:", order
		candidates = lists[order[0]]
		expected_length = 4
		for i in range(1, 6):
			moving_on = []
			next_list = lists[order[i]]
			for xx in candidates:
				for yy in next_list:
					if xx[-2:] == yy[:2]:
						moving_on.append(xx + yy)
			expected_length += 4
			candidates = [x for x in moving_on if len(x) == expected_length]
			if len(candidates) == 0:
				break
		if len(candidates) > 0:
			print candidates
			break
	
	nums = []
	while len(candidates) > 0:
		nums.append(int(candidates[0:4]))
		candidates = candidates[4:]
	
	product = 1
	for i in nums:
		product *= i
	
	print product


euler61()
