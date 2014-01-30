import math
print reduce(lambda x, y: int(x) + int(y), list(str(math.factorial(100))))