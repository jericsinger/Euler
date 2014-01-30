# takes too long
def findPans():
	import itertools
	
	pans_list = []
	pans_iter = itertools.permutations('1234567890')
	
	for i in pans_iter:
		if int(i[3]) % 2 == 0 and i[5] in ['0', '5']:
			print i
			if isDiv(int(''.join(i))):
				pans_list.append(i)
				print i


divisors = [1, 2, 3, 5, 7, 11, 13, 17]

def isDiv(num):
	digits = str(num)
	if len(digits) != 10:
		return False
	for i in range(0, len(divisors)):
		num = int(digits[i + 1 : i + 4])
		if num % divisors[i] > 0:
			return False
	return True


def getDivDict():
	div_dict = {}
	for i in divisors:
		div_dict[i] = []
	
	possibles = []
	for i in range(12, 1000):
		if i < 100:
			i = '0' + str(i)
		else:
			i = str(i)
			
		if len(list(i)) == 3:
			possibles.append(i)
	
	for div in divisors:
		for pos in possibles:
			if int(pos) % div == 0 and len(set(list(pos))) == 3:
				div_dict[div].append(str(pos))
	div_dict[1][:] = [x for x in div_dict[1] if not x[0] == '0']
	
	return div_dict


def findOverlaps():
	# number pattern = abcdefghij
	div_dict = getDivDict()
	possibles = div_dict[1]
	
	for n in xrange(1, len(divisors)):
		key = divisors[n]
		for i in xrange(0, len(possibles)):
			for next in div_dict[key]:
				if possibles[i][-2:] == next[:2]:
					possible = possibles[i] + next[2]
					if len(set(list(possible))) == len(possible):
						possibles.append(possible)
		for i in xrange(len(possibles) - 1, -1, -1):
			if len(possibles[i]) < n + 3:
				del(possibles[i])
	return possibles


def euler43():
	pans = findOverlaps()
	sum = 0
	for i in pans:
		sum += int(i)
	print sum
	
euler43()