import matrix
import random

#-------------------------------------------------------------
# problem 1
#-------------------------------------------------------------
def random_aa(n):
	aa = 'DEXLWRYKHAZICNTSBVQGPFM'
	r = [ random.choice(aa) for i in range(n) ]
	return ''.join(r)

#-------------------------------------------------------------
# problem 2
#-------------------------------------------------------------
def global_align(M, x, y):
	if (x,y) in Table:
		return Table[x,y]

	if len(x) == 0:
		score = sum([ M['*', y_i] for y_i in y ])
		Table[x,y] = score
		return score

	if len(y) == 0:
		score = sum([ M[x_i, '*'] for x_i in x ])
		Table[x,y] = score
		return score

	s = global_align(M, x[0:-1], y[0:-1]) + M[x[-1], y[-1]]
	d = global_align(M, x[0:-1], y) + M[x[-1], '*']
	i = global_align(M, x, y[0:-1]) + M['*', y[-1]]
	score = max(s,d,i)
	Table[x,y] = score
	return score

#-------------------------------------------------------------
def local_align(M, x, y):
	if (x,y) in Table:
		return Table[x,y]

	if len(x) == 0:
		score = 0
		Table[x,y] = score
		return score

	if len(y) == 0:
		score = 0
		Table[x,y] = score
		return score

	s = local_align(M, x[0:-1], y[0:-1]) + M[x[-1], y[-1]]
	d = local_align(M, x[0:-1], y) + M[x[-1], '*']
	i = local_align(M, x, y[0:-1]) + M['*', y[-1]]
	score = max(s,d,i,0)
	Table[x,y] = score
	return score
#-------------------------------------------------------------
M = matrix.get_matrix('blosum62.txt')
x, y = 'ARLRAR', 'LR'
# Global alignment
# ARRBLRSMARR
# ---TLR-----

# Local alignment
# LR
# LR

# BR
# ST
# print(M['S','B'], M['R','T'], 0, M['R','*'], M['T','*'])
print(x)
print(y)
Table = {}
print( global_align(M, x, y) )
Table = {}
print( local_align(M, x, y) )
print(Table)
print( max(Table.values()) )