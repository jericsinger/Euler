# http://www.blackpawn.com/texts/pointinpoly/

def same_side(p1,p2, a,b):
	import numpy as np
	
	def vec(a, b):
		return [x[1]-x[0] for x in zip(a, b)]
	
	p1, p2 = np.array(p1), np.array(p2)
	a, b = np.array(a), np.array(b)
		
	b_a = vec(a, b)
	p1_a, p2_a = vec(a, p1), vec(a, p2)
	
	cp1 = np.cross(b_a, p1_a)
	cp2 = np.cross(b_a, p2_a)
	if np.dot(cp1, cp2) >= 0:
		return True
	return False


def point_in_tri(p, abc):
	a, b, c = abc[0], abc[1], abc[2]
	if same_side(p,a, b,c) and same_side(p,b, a,c) and same_side(p,c, a,b):
		return True
	return False


def get_tris():
	import urllib2
	response = urllib2.urlopen("http://projecteuler.net/project/triangles.txt")
	raw_tris = [x.split(',') for x in response.read().split('\n')]
	tris = []
	for string in raw_tris[:-1]:
		i = [int(x) for x in string]
		tris.append([[i[0],i[1]], [i[2],i[3]], [i[4],i[5]]])
	return tris

p = [0, 0]

tris = get_tris()
results = [point_in_tri(p, abc) for abc in tris]
print results.count(True)