def sumFactorial(num):
	from math import factorial
	facts = []
	for i in range(0, 10):
		facts.append(factorial(int(i)))
		
	digits = list(str(num))
	sum = 0
	for i in digits:
		sum += facts[int(i)]
	return sum

sum = 0
for i in range(3, 100000):
	if i == sumFactorial(i):
		sum += i
		print i
print sum