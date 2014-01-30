def getPerms(str, num=None):
	import itertools
	perms = itertools.permutations(str, num)
	result = []
	for i in perms:
		result.append(i)
	return compileNums(result)
	#returns as list of ints


def compileNums(permlist):
	compiled = []
	for i in permlist:
		compiled.append(int(''.join(i)))
	return compiled
	#concats lists within a list of lists 
	#returns the result as a list of ints


def available(used):
	#takes string
	nums = '123456789'
	used = list(used)
	for i in used:
		nums = nums.replace(i, '')
	return nums
	# returns as string



def run():
	products = []
	nums = '123456789'
	two_digit_perms = getPerms(nums, 2)
	for i in two_digit_perms:
		remaining = available(str(i))
		three_digit_perms = getPerms(remaining, 3)
		for j in three_digit_perms:			
			remaining = available(str(i) + str(j))
			rSort = ''.join(sorted(remaining))
			
			product = int(i) * int(j)
			pSort = ''.join(sorted(str(product)))
			
			if rSort == pSort:
				print "%s x %s = %s" % (i, j, product)
				products.append(product)
	result = set(products)
	return list(result)


def run2():
	products = []
	nums = '123456789'
	four_digit_perms = getPerms(nums, 4)
	for i in four_digit_perms:
		remaining = available(str(i))
		one_digit_perms = getPerms(remaining, 1)
		for j in one_digit_perms:			
			remaining = available(str(i) + str(j))
			rSort = ''.join(sorted(remaining))
			
			product = int(i) * int(j)
			pSort = ''.join(sorted(str(product)))
			
			if rSort == pSort:
				print "%s x %s = %s" % (i, j, product)
				products.append(product)
	result = set(products)
	return list(result)




result = run() + run2()
print sorted(result)
sum = 0
for i in result:
	sum += i
print sum