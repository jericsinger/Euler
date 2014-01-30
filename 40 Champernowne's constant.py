def euler40(lim):
	i = 0
	digits = []
	while len(digits) <= lim:
		i_list = list(str(i))
		digits.extend(i_list)
		i += 1
	
	find = 1
	found = []
	product = 1
	while find <= lim:
		product *= int(digits[find])
		found.append(int(digits[find]))
		find *= 10
	print found
	print product

euler40(1000000)
