def self_powers(limit):
	result = 0
	for i in range(1, limit + 1):
		result += i ** i
	return str(result)


result = self_powers(1000)
print result[-10:]