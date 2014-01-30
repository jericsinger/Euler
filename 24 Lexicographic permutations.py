import itertools

string = '0123456789'
permutations = list(itertools.permutations(string, len(string)))
print ''.join(permutations[999999])