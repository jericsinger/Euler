def get_matrix():
	import urllib2
	response = urllib2.urlopen('http://projecteuler.net/project/matrix.txt')
	lines = response.readlines()
	stripped_lines = []
	for line in lines:
		stripped_lines.append(line.rstrip('\n'))
	matrix = []
	for line in stripped_lines:
		matrix.append(line.split(','))
	for y in range(0, len(matrix)):
		for x in range(0, len(matrix[y])):
			matrix[y][x] = int(matrix[y][x])
	return matrix


matrix = get_matrix()
n = len(matrix) - 1
path_sum = 0
seed = 1


for i in range(seed, -1, -1):
	for j in range(n, -1, -1):
		if i == n and j == n:
			continue
		if j == n:
			min_x = matrix[i+1][j]
		elif i == n:
			min_x = matrix[i][j+1]
		else:
			min_x = min(matrix[i+1][j], matrix[i][j+1])
		matrix[i][j] += min_x
print matrix[0][0]