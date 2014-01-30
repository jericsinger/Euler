from math import sqrt
def factorLength(n):
  factors = set()
  for x in range(1, int(sqrt(n)) + 1):
    if n % x == 0:
      factors.add(x)
      factors.add(n//x)
  return len(factors)


factorCount = 0
triNum = 0
n = 0

while True:
	triNum = triNum + n
	if factorLength(triNum) > 500:
		break
	n += 1

print(triNum)