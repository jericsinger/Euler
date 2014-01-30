def sumDigitPowers(num, exp):
	sum = 0
	for i in list(str(num)):
		sum += int(i) ** exp
	return sum


def run(exp):
	maxDigitValue = 9 ** exp
	
	num = 1000000
	sum = 0
	while num > 1:
		if num == sumDigitPowers(num, exp):
			print num
			sum += num
		num -= 1
	print "sum:", sum
	return


run(5)