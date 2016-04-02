from sys import stdin

def reverse_words(sentence):
	return map(lambda w: w[::-1], sentence[::-1].split(' '))

count = int(stdin.readline().rstrip('\n'))
for i in range(0, count):
	sentence = stdin.readline().rstrip('\n')
	print "Case #%d: %s" % (i + 1, str(reverse_words(sentence))[1:-1].replace(',', '').replace("'", ''))
