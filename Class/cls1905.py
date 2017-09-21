import math


#--------------
#shannon entropy
def H(p):
	h = 0
	for p_i in p:
		if p_i >0:
			h += -p_i * math.log2(p_i) 
	return h
#-------------

def score(L):
	n = len(L[0])
	for c in range(n):
		f = dict(A=0,C=0,G=0,T=0)
		for seq in L:
			f[seq[c]] += 1.0/n
		p = [f['A'],f['C'],f['G'],f['T']]
		print(c,p)


b = [1,0,0,0]
a = H(b)
print(a)