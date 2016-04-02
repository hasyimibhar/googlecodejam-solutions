from sys import stdin

def credit_pair(total, credits, n):
	for i, c in enumerate(credits):
		for j in range(i + 1, n):
			if credits[j] == total - c:
				return sorted([i + 1, j + 1])

count = int(stdin.readline().rstrip('\n'))
for i in range(0, count):
	total = int(stdin.readline().rstrip('\n'))
	n = int(stdin.readline().rstrip('\n'))
	cs = map(int, stdin.readline().rstrip('\n').split(' '))
	print "Case #%d: %s" % (i + 1, str(credit_pair(total, cs, n))[1:-1].replace(',', ''))
