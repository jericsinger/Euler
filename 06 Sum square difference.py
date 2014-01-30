def squares(a, b):
	"""Adds square of b to a."""
	return a + b ** 2

def sumSquare(*args):
	"""Return sum of squares of args."""
	return reduce(squares, args)


print (101 * 50) ** 2 - sumSquare(*range(1,101))