n = 2
for i in range(7830456):
    n = (2 * n) % 10000000000
 
n *= 28433
n += 1

print n