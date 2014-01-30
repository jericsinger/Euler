# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

def e19():
	import calendar
	
	counter = 0
	
	for y in range(1901, 2001):
		for m in range(1, 13):
			if calendar.weekday(y,m,1) == 6: counter += 1
			
	return counter

print e19()