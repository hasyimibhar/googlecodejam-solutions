from sys import stdin
from sys import maxint
from multiprocessing.pool import ThreadPool

def scalar_product(a, b):
	c = 0
	for i in range(0, len(a)):
		c += a[i] * b[i]
	return c

count = int(stdin.readline().rstrip('\n'))

for i in range(0, count):
	size = int(stdin.readline().rstrip('\n'))
	a = tuple(sorted(map(int, stdin.readline().rstrip('\n').split(' '))))
	b = tuple(sorted(map(int, stdin.readline().rstrip('\n').split(' ')), reverse=True))

	min_c = scalar_product(a, b)
	print "Case #%d: %d" % (i + 1, min_c)
