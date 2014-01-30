def euler56():
	import math
	max_sum = 0
	for a in range(0, 100):
		for b in range(0, 100):
			result = sumDigits(str(a ** b))
			if int(result) > max_sum:
				max_sum = int(result)
	return max_sum



def sumDigits(string):
	string_sum = 0
	for digit in string:
		string_sum += int(digit)
	return string_sum



print euler56()