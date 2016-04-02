from sys import stdin
from sys import maxint

def permutate(v):
	if len(v) == 1:
		return [v]
	elif len(v) == 2:
		return [v, (v[1], v[0])]
	else:
		perms = []
		for i in range(0, len(v)):
			head = v[i]
			tail = v[:i] + v[i+1:]
			for p in permutate(tail):
				perms.append((head,) + p)

		return perms

def scalar_product(a, b):
	c = 0
	for i in range(0, len(a)):
		c += a[i] * b[i]
	return c

count = int(stdin.readline().rstrip('\n'))

for i in range(0, count):
	size = int(stdin.readline().rstrip('\n'))
	v1 = tuple(map(int, stdin.readline().rstrip('\n').split(' ')))
	v2 = tuple(map(int, stdin.readline().rstrip('\n').split(' ')))
	perms_v1 = permutate(v1)
	perms_v2 = permutate(v2)

	min_c = maxint
	for vi in perms_v1:
		for vj in perms_v2:
			min_c = min(min_c, scalar_product(vi, vj))

	print "Case #%d: %d" % (i + 1, min_c)
