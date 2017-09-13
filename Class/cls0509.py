#Md Lutfar Rahman

def edit_distance(x,y):
	if len(x) == 0:
		return len(y)
	if len(y) == 0:
		return len(x)

	if x[-1] == y[-1]:
		return edit_distance(x[0:-1],y[0:-1])

	s_delete = 	1 + edit_distance(x[0:-1],y)
	s_insert = 	1 + edit_distance(x,y[0:-1])
	s_sub = 	1 + edit_distance(x[0:-1],y[0:-1])	

	return min(s_delete,s_insert,s_sub)

table = {}
def edit_distance_cache(x,y):
	if (x,y) in table:
		return table[x,y]
	
	if len(x) == 0:
		table[x,y] = len(y)
		return table[(x,y)]
	if len(y) == 0:
		table[x,y] = len(x)
		return table[(x,y)]

	if x[-1] == y[-1]:
		table[(x,y)] =  edit_distance_cache(x[0:-1],y[0:-1])
	
	else:
		s_delete = 	1 + edit_distance_cache(x[0:-1],y)
		s_insert = 	1 + edit_distance_cache(x,y[0:-1])
		s_sub = 	1 + edit_distance_cache(x[0:-1],y[0:-1])

		table[(x,y)] = 	min(s_delete,s_insert,s_sub)

	return table[(x,y)]


X = 'THISISACAT'
Y = 'THATSACAT'

#----------------------------
import random
def random_string(n):
	out = [ random.choice('ACGT') for i in range(n)]
	return ''.join(out)
#-----------------------------

for i in range(5,14):

	X = random_string(i)
	Y = random_string(i)

	print(i,"slow=",edit_distance(X,Y),"fast=",edit_distance_cache(X,Y))