from sys import stdin
from collections import namedtuple
from operator import itemgetter

cell = namedtuple('cell', ['x', 'y'])

def search_basin(elv_map, w, h, c):
	current = c
	basin_found = False
	while not basin_found:
		f = flow_to(elv_map, w, h, current)
		if f is None:
			basin_found = True
		else:
			current = f

	return current

def flow_to(elv_map, w, h, c):
	flows = []

	if c.y > 0 and elv_map[c.y-1][c.x] < elv_map[c.y][c.x]: # North
		flows.append((1, cell(c.x, c.y-1), elv_map[c.y-1][c.x]))
	if c.x > 0 and elv_map[c.y][c.x-1] < elv_map[c.y][c.x]: # West
		flows.append((2, cell(c.x-1, c.y), elv_map[c.y][c.x-1]))
	if c.x < w - 1 and elv_map[c.y][c.x+1] < elv_map[c.y][c.x]: # East
		flows.append((3, cell(c.x+1, c.y), elv_map[c.y][c.x+1]))
	if c.y < h - 1 and elv_map[c.y+1][c.x] < elv_map[c.y][c.x]: # South
		flows.append((4, cell(c.x, c.y+1), elv_map[c.y+1][c.x]))

	if len(flows) == 0:
		return None

	flows = sorted(flows, key=itemgetter(2)) # Sort according to altitude
	flows = filter(lambda x: x[2] == flows[0][2], flows) # Only keep lowest altitudes
	flows = sorted(flows, key=itemgetter(0)) # Sort according to direction
	return flows[0][1]

count = int(stdin.readline().rstrip('\n'))
for i in range(0, count):
	mi = map(int, stdin.readline().rstrip('\n').split(' '))
	w = mi[1]
	h = mi[0]
	elv_map = []
	for y in range(0, h):
		row = map(int, stdin.readline().rstrip('\n').split(' '))
		elv_map.append(row)

	basins = []
	basin_labels = {}
	label = 'a'
	for y in range(0, h):
		row = []
		for x in range(0, w):
			b = search_basin(elv_map, w, h, cell(x, y))
			if not b in basin_labels:
				basin_labels[b] = label
				label = chr(ord(label)+1)
			row.append(basin_labels[b])
		basins.append(row)

	print "Case #%d:" % (i + 1)
	for y in range(0, h):
		print str(basins[y])[1:-1].replace(',', '').replace("'", '')
