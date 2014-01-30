def trianglePathFile():
	
	raw = open('/Users/justinsinger/Desktop/Dropbox/Code/Programming/Euler/euler67.txt','r')
	triangle = raw.readlines()
	raw.close()	
	for i in range(len(triangle)):
		triangle[i] = triangle[i].strip()
		triangle[i] = triangle[i].split(' ')
	
	for i in range(len(triangle)):
		for j in range(len(triangle[i])):
			triangle[i][j] = int(triangle[i][j])
	
	triangle.reverse()
	sums = []
	sums.append(triangle[0])
	
	for i in range(1, len(triangle)):
		line = []
		for j in range(0, len(triangle[i])):
			line.append(triangle[i][j] + max(sums[i-1][j], sums[i-1][j+1]))
		sums.append(line)
	sums.reverse()
	return sums[0][0]
	

print trianglePathFile()
