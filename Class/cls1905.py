import math
import random

#lutfar

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
	s = 0
	for c in range(n):
		f = dict(A=0,C=0,G=0,T=0)
		for seq in L:
			f[seq[c]] += 1.0/len(L)
		p = [f['A'],f['C'],f['G'],f['T']]
		s+=H(p)
		#print(c,p,round(H(p), 2))

	return s/len(L)

#-------------------------


def insert_into(seq, pattern):
	# j = random.randint(0,len(pattern)-1)
	# acgt = ['A','C','G','T']
	# acgt.remove(pattern[j])
	# tmp = list(pattern)
	# tmp[j] = random.choice(acgt)
	# pattern = ''.join(tmp)

	i = random.randint(0,len(seq)-1)
	return seq[0:i] + pattern + seq[i:len(seq)]


#-----------------
def random_dna(n):
	s = [random.choice('ACGT') for i in range(n)]
	return ''.join(s)

#------------------
# return random motif
def initial_solution(sequences,k):
	motif = []
	for s in sequences:
		i = random.randint(0, len(s) - k)
		motif.append(s[i:i+k])
	return motif

#-------------------------

def neighbour_of(m,sequences):
	i = random.randint(0,len(seq)-1)
	m1  = m.copy()
	k = len(m[i])
	r = random.randint(0,len(sequences[i])-k)
	m1[i] = sequences[i]


#-------------------
def hill_climb(sequences,pattern):
	motif = initial_solution(sequences,len(pattern))
	no_inprovement = 0

	T = 10#M*N

	while no_inprovement < T:
		neighbour = neighbour_of(motif,sequences)
		if score(neighbour) < score(motif):
			motif = neighbour
		else:
			no_inprovement +=1


#--------------
# print(random_dna(10))
# print(score(['ACGG','ACGG','TAGA']))
# print(score(['ACGG','ACGG','ACGG']))



N, M = 20, 10
pattern = 'TTTTTTTT'
sequences = [ insert_into(random_dna(N), pattern) for i in range(M)]
m = initial_solution(sequences,len(pattern))

print(m, score(m))

# for s in sequences:
# 		print(s)


