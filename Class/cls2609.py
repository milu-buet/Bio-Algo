# Lutfar

#print("test")

S = 'adasasfadsfa'
p = 'hello'

def substring(S,p):
	for i in range(len(S)):
		j = len(p) + i
		if p == S[i:j]:
			return i
	return False

print(substring(S,p))

