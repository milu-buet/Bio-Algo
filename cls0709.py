#Md Lutfar Rahman

import time
#----------------------------
import random
def random_string(n):
	out = [ random.choice('ACGT') for i in range(n)]
	return ''.join(out)
#-----------------------------

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

def edit_distance_ita(x,y):
	table = {(-1,-1):0}
	#table[(i,j)] = edit_disyance(x[0:i+1],y[0:j+1])

	for j in range(0,len(y)):
		table[(-1,j)] = j + 1
	for i in range(0,len(x)):
		table[(i,-1)] = i + 1

	for i in range(0,len(x)):
		for j in range(0,len(y)):
			if x[i] == y[j]:
				table[(i,j)] = table[(i-1,j-1)]
			else:
				a = 1 + table[(i-1,j-1)]
				b = 1 + table[(i,j-1)]
				c = 1 + table[(i-1,j)]
				table[(i,j)] = min(a,b,c)
	return table[(len(x)-1,len(y)-1)]


Table = {}
for i in range(5,100):
	T = {}
	x = random_string(i)
	y = random_string(i)
	start = time.time()
	print(i, edit_distance(x,y))
	print(i, edit_distance_ita(x,y))


