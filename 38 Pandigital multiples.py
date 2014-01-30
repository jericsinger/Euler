#### FAIL: too slow

def findPans(digits):
	if digits > 9 or digits < 1:
		digits = 9
	nums = '123456789'[0:digits]
	nums_set = set(list(nums))
	print nums_set
	
	pans = []
	for i in range(int(nums), int(nums[::-1]) + 1):
		new_nums_set = set(list(str(i)))
		if new_nums_set == nums_set:
			pans.append(i)
	print pans



def test():
	result = []
	for i in range(123456789, 987654322):
		result.append(i)
	print "done"


######################
def isPan(numStr):
	if len(numStr) == 9:
		nums = '123456789'
		nums_set = set(list(nums))
		numStr_set = set(list(numStr))
		if nums_set == numStr_set:
			return True
	return False

def available(used):
	#takes string
	nums = '123456789'
	used = list(str(used))
	for i in used:
		nums = nums.replace(i, '')
	return nums
	# returns as string

def unique(n):
	#takes int
	num_list = list(str(n))
	num_set = set(num_list)
	if len(num_list) == len(num_set):
		return True
	return False

def panCheck(num):
	pans = []
	result = ''
	i = 1
	while True:
		result += str(num * i)
		if len(result) < 9:
			i += 1
			continue
		if len(result) == 9:
			if isPan(result):
				return result
		else:
			return False

def euler38():
	max_i = 192
	for i in range(100000	, 0, -1):
		if unique(i):
			if panCheck(i) is not False:
				break
	print panCheck(i)


euler38()