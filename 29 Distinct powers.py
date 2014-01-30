def getIntCombs(aMin, aMax, bMin, bMax):
	combs = []
	for a in range(aMin, aMax + 1):
		for b in range(bMin, bMax + 1):
			combs.append(a ** b)
	nums = list(set(combs))
	nums.sort()
	print "distinct terms:", len(nums)


getIntCombs(2,100,2,100)