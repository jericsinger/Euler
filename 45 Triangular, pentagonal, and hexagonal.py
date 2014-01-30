def euler45(n):
	import collections
	
	three = []
	five = []
	six = []
	for n in range(143, n):
		three.append(n * (n + 1) / 2)
		five.append(n * (3 * n - 1) / 2)
		six.append(n * (2 * n - 1))
	three_ms = collections.Counter(three)
	five_ms = collections.Counter(five)
	six_ms = collections.Counter(six)
	three_five = collections.Counter(list((three_ms & five_ms).elements()))
	five_six = collections.Counter(list((five_ms & six_ms).elements()))
	result = list((three_five & five_six).elements())
	print result
	


euler45(100000)
