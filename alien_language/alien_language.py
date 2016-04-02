from sys import stdin

def parse_rule(string):
	parsed = []
	group = []
	is_group = False
	for s in string:
		if s == '(':
			group = []
			is_group = True
		elif s == ')':
			parsed.append(group)
			is_group = False
		elif is_group:
			group.append(s)
		else:
			parsed.append([s])

	return parsed

def match(rule, string):
	for i in range(0, len(string)):
		if not string[i] in rule[i]:
			return False

	return True

count = map(int, stdin.readline().rstrip('\n').split(' '))
d = count[1]
n = count[2]

words = []
for i in range(0, d):
	words.append(stdin.readline().rstrip('\n'))

rules = []
for i in range(0, n):
	rules.append(parse_rule(stdin.readline().rstrip('\n')))

for i, r in enumerate(rules):
	matches = 0
	for w in words:
		if match(r, w):
			matches = matches + 1

	print "Case #%d: %d" % (i + 1, matches)
