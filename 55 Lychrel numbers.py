def euler55():
	count = 0
	for i in range(0, 10000):
		if not findPal(i):
			count += 1
	return count



def findPal(num):
	i = 1
	now = str(num)
	now_r = str(num)[::-1]
	while i < 50:
		next = str(int(now) + int(now_r))
		if next == str(next)[::-1]:
			return True
		now = next
		now_r = str(next)[::-1]
		i += 1
	return False


print euler55()