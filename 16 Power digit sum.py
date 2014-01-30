def expsum(base,exp):
	string = str(base ** exp)
	expsum = 0	
	for i in range(len(string)):
		expsum = expsum + int(string[i])
	return expsum

print 'expsum(2,1000) = %s' % expsum(2, 1000)