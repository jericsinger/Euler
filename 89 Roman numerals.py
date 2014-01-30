def roman_to_int(numerals):
	roman = {	'I' : 1,
				'V' : 5,
				'X' : 10,
				'L' : 50,
				'C' : 100,
				'D' : 500,
				'M' : 1000	}
	numerals = list(numerals)
	replacement = [roman[x] for x in numerals]
	reduced = 0	
	while len(replacement) > 1:
		if replacement[0] < replacement[1]:
			reduced += replacement[1] - replacement[0]
			replacement = replacement[2:]
		else:
			reduced += replacement[0]
			replacement = replacement[1:]
	reduced += replacement[0] if len(replacement) == 1 else 0	
	return reduced


def int_to_roman(integer):
	remaining = integer
	roman = {	1: 'I',
				5: 'V',
				10 : 'X',
				50 : 'L',
				100 : 'C',
				500 : 'D',
				1000 : 'M'	}
	vals = sorted(roman)
	expanded = ''	
	i = len(vals) - 1
	while remaining > 0:
		if remaining % vals[i] == remaining:
			i -= 1
		else:
			expanded += roman[vals[i]]
			remaining -= vals[i]	
	replacements = (('DCCCC', 'CM'),
					('CCCC', 'CD'),
					('LXXXX', 'XC'),
					('XXXX', 'XL'), 
					('VIIII', 'IX'),
					('IIII', 'IV'))
	for replacement in replacements:
		expanded = expanded.replace(replacement[0], replacement[1])	
	return expanded


def shrink(numerals):
	return int_to_roman(roman_to_int(numerals))

def control():
	import urllib2
	response = urllib2.urlopen('http://projecteuler.net/project/roman.txt')
	raw_data = response.readlines()
	data = [each.replace('\n', '') for each in raw_data]
	
	savings = 0
	for i in data:
		savings += len(i) - len(shrink(i))
		
	print savings


control()