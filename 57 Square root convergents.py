from __future__ import division
from decimal import *
from fractions import *


def get_equations():
	
	now = "1 + 1/2"
	expansions = [0, eval(now)]
	for i in range(2, 100):
		next = now[:-1] + "(2 + 1/2"
		getcontext().prec = 300
		expansions.append(Decimal(eval(next + (i-1) * ")")))
		now = next
	
	print expansions


def euler57():
	import fractions
	equations = get_equations()

############


def better():
	count = 0
	last_num = 3
	last_den = 2
	results = [(0, 0)]
	for i in range(1, 1000):
		this_num = last_num + 2 * last_den
		this_den = last_num + last_den
		results.append((this_num, this_den))
		if len(str(this_num)) > len(str(this_den)):
			count += 1
		last_num = this_num
		last_den = this_den
	print count


better()