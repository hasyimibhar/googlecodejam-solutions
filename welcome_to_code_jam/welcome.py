from sys import stdin
from collections import namedtuple

welcome = "welcome to code jam"

def count_subseq(string, exact):
	reduced_string = ""
	for s in string:
		if s in exact:
			reduced_string = reduced_string + s
	string = reduced_string

	perms = []
	for i, s in enumerate(string):
		if s == exact[0]:
			perms.append((i, 1))

	for c in range(1, len(exact)):
		new_perms = []

		for i, s in enumerate(string):
			if s == exact[c]:
				j = 0
				count = 0
				while j < len(perms) and i >= perms[j][0]:
					count = count + perms[j][1]
					j = j + 1

				if j > 0:
					new_perms.append((i, count))
		perms = sorted(new_perms)

	return reduce(lambda x, p: x+p[1], perms, 0)

count = int(stdin.readline().rstrip('\n'))
for i in range(0, count):
	string = stdin.readline().rstrip('\n')
	result = count_subseq(string, welcome)
	print "Case #%d: %s" % (i + 1, str(result)[-4:].zfill(4))
