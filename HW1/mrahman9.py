#
# MD LUTFAR RAHMAN 
#
# mrahman9@memphis.edu
#
# COMP 8295 - Assignement 1
#
import random
from blosum_reader import *
import time

#----------------------------------------------------------------
def random_string(n):
	out = [ random.choice('ARNDCQEGHILKMFPSTWYV') for i in range(n) ]
	return ''.join(out)
#----------------------------------------------------------------

# reading matrix
M = get_matrix('matrix.txt')
# for k,v in M.items():
# 	print(k, M[k])

# recursive solution
#-----------------------------------------------
Table = {}
def global_alignment(x,y):
	if (x,y) in Table:
		return Table[(x,y)]

	if len(x) == 0:
		Table[(x,y)] = len(y)*(-9)
		return Table[(x,y)] 
	if len(y) == 0:
		Table[(x,y)] = len(x)*(-9)
		return Table[(x,y)] 

	a = M[x[-1],y[-1]] + global_alignment(x[0:-1], y[0:-1])
	b = (-9) + global_alignment(x, y[0:-1])
	c = (-9) + global_alignment(x[0:-1], y)
	Table[(x,y)] = max(a,b,c)
	return Table[(x,y)]
#----------------------------------------------


# iterative solution
#-----------------------------------------------
def global_alignment_ita(x,y):
	table = {(-1,-1) : 0}

	for j in range(0, len(y)):
		table[-1,j] = (j+1)*(-9)
	for i in range(0, len(x)):
		table[i,-1] = (i+1)*(-9)

	for i in range(0, len(x)):
		for j in range(0, len(y)):
			a = M[x[i],y[j]] + table[i-1,j-1]
			b = (-9) + table[i,j-1]
			c = (-9) + table[i-1,j]
			table[i,j] = max(a,b,c)
	return table[len(x)-1, len(y)-1]
#-----------------------------------------------

# x = 'QWHMBRXQYXVRNPVDSCSEAWVVZPQWHRIWXVINSFPEI'
# y = 'DXCBZYPVDSCSEAW'
# v = global_alignment_ita(x,y)
# print(v)


Table = {}
for i in range(500,1000, 100):
	T = {}
	x = random_string(i)
	y = random_string(i)
	start = time.time()
	print(i)
	u = global_alignment(x,y)
	print('\t', u, time.time() - start)
	v = global_alignment_ita(x,y)
	print('\t', v, time.time() - start)