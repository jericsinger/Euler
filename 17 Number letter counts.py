def countnumlet():
	hundreds = ['', \
				'onehundred', \
				'twohundred', \
				'threehundred', \
				'fourhundred', \
				'fivehundred', \
				'sixhundred', \
				'sevenhundred', \
				'eighthundred', \
				'ninehundred']
	tens = ['', \
			'', \
			'twenty', \
			'thirty', \
			'forty', \
			'fifty', \
			'sixty', \
			'seventy', \
			'eighty', \
			'ninety']
	ones = ['', \
			'one', \
			'two', \
			'three', \
			'four', \
			'five', \
			'six', \
			'seven', \
			'eight', \
			'nine', \
			'ten', \
			'eleven', \
			'twelve', \
			'thirteen', \
			'fourteen', \
			'fifteen', \
			'sixteen', \
			'seventeen', \
			'eighteen', \
			'nineteen']
	
	numString = ''
	
	for hundred in range(10):
		for ten in range(10):
			for one in range(10):  
				if (hundred == 0) or (hundred > 0 and one == 0 and ten == 0):
						middleAnd = ''
				else: middleAnd = 'and'
				if ten == 1: one = one + 10
				numString = numString + \
							hundreds[hundred] + \
							middleAnd + \
							tens[ten] + \
							ones[one]
	return len(numString + 'onethousand')
	
print 'countnumlet() = %s' % countnumlet()