def sum_digit_squares(num):
	digits = list(str(num))
	sum = 0
	for i in digits:
		sum += int(i) ** 2
	return sum


counts = {89 : 0, 1: 0}

for seed in range(1, 10000000):
	result = seed
	while result != 89 and result != 1:
		result = sum_digit_squares(result)
	counts[result] += 1

print counts