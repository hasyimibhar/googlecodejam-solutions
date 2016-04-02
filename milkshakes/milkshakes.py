from sys import stdin

def parse_customer(n, line):
	prefs = [-1] * n
	tokens = map(int, line.split(' '))
	count = tokens[0]

	ti = 1
	for i in range(0, count):
		pi = tokens[ti]
		ti += 1

		pt = tokens[ti]
		ti += 1

		prefs[pi - 1] = pt 

	return prefs

def is_valid(n, customers):
	empty = [-1] * n
	for cust in customers:
		if cust == empty:
			return False

	return True

def is_solved(n, solution):
	for i in range(0, n):
		if solution[i] == -1:
			return False

	return True

def check_possibility(n, customers):
	# Look for a column with all unmalted.
	# If found, then the solution is to
	# prepare all unmalted.
	for i in range(0, n):
		all_unmalted = True
		for cust in customers:
			if cust[i] != 0:
				all_unmalted = False
				break

		if all_unmalted:
			return (True, [0] * n)

	solution = [-1] * n

	while is_valid(n, customers):
		has_single = False
		solved_customers = []

		for i in range(0, len(customers)):
			# Look for customers with only one possible choice.
			cust = customers[i]
			single_choice = True
			choice = -1
			choice_idx = -1
			for j in range(0, n):
				c = cust[j]
				if c != -1:
					if choice == -1:
						choice = c
						choice_idx = j
					else:
						single_choice = False

			if single_choice:
				# If customer only has one possible choice,
				# set the solution i to his choice.
				has_single = True
				solution[choice_idx] = choice
				solved_customers.append(i)

				for j in range(0, len(customers)):
					if j != i:
						if customers[j][choice_idx] == choice:
							solved_customers.append(j)
						else:
							customers[j][choice_idx] = -1

				break

		for si in sorted(solved_customers, reverse=True):
			del customers[si]

		if is_valid(n, customers) and is_solved(n, solution):
			return (True, solution)

		# No more single choice
		elif not has_single:
			break

	if not is_valid(n, customers):
		return (False, solution)
	else:
		for i in range(0, n):
			if solution[i] == -1:
				solution[i] = 0

		return (True, solution)

count = int(stdin.readline().rstrip('\n'))
for i in range(0, count):
	n = int(stdin.readline().rstrip('\n'))
	m = int(stdin.readline().rstrip('\n'))

	customers = []
	for j in range(0, m):
		c = parse_customer(n, stdin.readline().rstrip('\n'))
		customers.append(c)

	result = check_possibility(n, customers)

	if result[0]:
		print "Case #%d: %s" % (i + 1, str(result[1])[1:-1].replace(',', ''))
	else:
		print "Case #%d: IMPOSSIBLE" % (i + 1)
