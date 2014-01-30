def euler52():
	x = 1
	while True:
		results = [sorted(list(str(x)))]
		for n in range(2, 7):
			next = sorted(list(str(n * x)))
			if next == results[-1]:
				results.append(sorted(list(str(n * x))))
			else:
				break
		if len(results) == 6:
			return x
		x += 1


print euler52()
