# How do quantify the difference between two strings?

#----------------------------------------------------------------
# Edit distance between x and y is the minimum number of
# insertions, deletions and substitutions that convert x into y.
#----------------------------------------------------------------
def edit_distance(x,y):
	if (x,y) in Table:
		return Table[(x,y)]

	if len(x) == 0:
		Table[(x,y)] = len(y)
		return len(y)
	if len(y) == 0:
		Table[(x,y)] = len(x)
		return len(x)
	if x[-1] == y[-1]:
		return edit_distance(x[0:-1], y[0:-1])
	else:
		a = 1 + edit_distance(x[0:-1], y[0:-1])
		b = 1 + edit_distance(x, y[0:-1])
		c = 1 + edit_distance(x[0:-1], y)
		Table[(x,y)] = min(a,b,c)
		return min(a,b,c)

#----------------------------------------------------------------
import random
def random_string(n):
	out = [ random.choice('ACGT') for i in range(n) ]
	return ''.join(out)
#----------------------------------------------------------------
Table = {}
for i in range(5,20):
	T = {}
	x = random_string(i)
	y = random_string(i)
	print(i, edit_distance(x,y))


