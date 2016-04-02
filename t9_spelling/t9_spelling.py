from sys import stdin

keypad = {
	'a': "2",
	'b': "22",
	'c': "222",
	'd': "3",
	'e': "33",
	'f': "333",
	'g': "4",
	'h': "44",
	'i': "444",
	'j': "5",
	'k': "55",
	'l': "555",
	'm': "6",
	'n': "66",
	'o': "666",
	'p': "7",
	'q': "77",
	'r': "777",
	's': "7777",
	't': "8",
	'u': "88",
	'v': "888",
	'w': "9",
	'x': "99",
	'y': "999",
	'z': "9999",
	' ': "0"
}

def t9_spelling(string):
	spelling = ""
	last_key = None
	for s in string:
		if last_key == keypad[s][0]:
			spelling = spelling + ' '
		spelling = spelling + keypad[s]
		last_key = keypad[s][0]
	return spelling

count = int(stdin.readline().rstrip('\n'))
for i in range(0, count):
	string = stdin.readline().rstrip('\n')
	print "Case #%d: %s" % (i + 1, t9_spelling(string))
