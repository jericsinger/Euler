def getDiags(diameter):
	widths = range(3, diameter + 1, 2)
	diags = [1]
	n = 1
	
	for width in widths:
		interval = width - 1
		limit = width ** 2
		while n < limit:
			n += interval
			diags.append(n)
	return diags


def sumList(list):
	sum = 0
	for i in list:
		sum += i
	return sum

print sumList(getDiags(1001))