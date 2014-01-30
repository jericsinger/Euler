def isPal(string):
	if string == string[::-1]:
		return True
	return False


results = []
sum = 0
for i in range(0, 1000000):
	if isPal(str(i)) == True:
		if isPal(bin(i)[2:]) == True:
			results.append(i)
			sum += i

print results
print sum