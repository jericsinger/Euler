def get_primes(limit):
	import math
	primes = []
	for i in range(0, limit):
		primes.append(True);
	primes[0] = False
	primes[1] = False
	
	results = [];
	
	for i in range(2, int(math.sqrt(limit)) + 1):
		if primes[i] == True:
			j = i * i
			while j < limit:
				primes[j] = False
				j += i
	
	return primes

# too slow
def find_runs(limit):
	primes_tf = getPrimes(limit)
	primes = []
	for i in range(0, len(primes_tf)):
		if primes_tf[i] == True:
			primes.append(i)
	
	results = {}
	for i in range(0, len(primes)):
		results[primes[i]] = {'sum' : 0, 'run' : 0}
		sum = 0
		for j in range(i, len(primes)):
			sum += primes[j]
			if sum < limit:
				if primes_tf[sum] == True:
					results[primes[i]]['sum'] = sum
					results[primes[i]]['run'] = j - i + 1
	return results


def find_max_sum(runs):
	max_run = 0
	max_sum = 0
	for i in runs:
		run = runs[i]
		if run['run'] > max_run:
			max_run, max_sum = run['run'], run['sum']
	return {'run' : max_run, 'sum' : max_sum}


###################


def get_prime_sums(limit):
	primes_tf = get_primes(limit)
	primes = []
	for i in range(0, len(primes_tf)):
		if primes_tf[i]:
			primes.append(i)
			
	prime_sums = [{'p' : 0, 'f_p' : 0}]
	sums = 0
	for i in primes:
		sums += i
		prime_sums.append({'p' : i, 'f_p' : sums})
	return prime_sums

def find_max_run_under(limit):
	prime_sums = get_prime_sums(limit)
	prime_tf = get_primes(limit)
	max_run = 0
	max_prime = 0
	for i in range(len(prime_sums) - 1, -1, -1):
		i_p = prime_sums[i]['p']
		if prime_sums[i]['f_p'] < limit:
			for j in range(0, i - 1):
				j_p = prime_sums[j]['p']
				fp_diff = prime_sums[i]['f_p'] - prime_sums[j]['f_p']
				if prime_tf[fp_diff]:
					if i - j > max_run:
						max_run = i - j
						max_prime = fp_diff
						run = []
						for k in range(j + 1, i + 1):
							run.append(prime_sums[k]['p'])
						break
	print "max_prime:", max_prime
	print "max_run:", max_run
	print "run:", run


find_max_run_under(1000000)