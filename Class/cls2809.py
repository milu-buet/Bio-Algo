# Lutfar

#print("test")

class BWT():

	def __init__(self, T):
		self.T = T + '$'
		self.bwt = self.build_bwt(T)
		self.occ = self.build_occ(T)
		self.count = self.build_count(T)

	def rotate(self,t):
		return t[len(t)-1] + t[0:len(t)-1] 


	# construct the burrow-wheeler transform of T
	def build_bwt(self, T):
		rotations = []
		rotations.append(T)
		for i in range(len(T)-1):
			tt = self.rotate(rotations[-1])
			rotations.append(tt)
		
		rotations.sort()
		#print(rotations)
		last_col = []
		for s in rotations:
			last_col.append(s[-1])
		#print(last_col)
		return ''.join(last_col)

	def build_occ(self,t):
		occ = {c : [0]*len(t) for c in set(t)}
		for i in range(len(self.bwt)):
			c = self.bwt[i]
			for char in occ:
				occ[char][i] = occ[char][i-1]
			occ[c][i] += 1

		return occ

	def build_count(self,t):
		characters = list(set(t)).sort()
		count = {'$' : 0}

		for i in range(1, len(characters)):
			count[characters[i]] = count[characters[i-1]] + t.count[characters[i-1]]

		return count


	def reconstruct(self):
		c = '$'
		i = 0
		t = [c]
		for j in range(len(self.bwt)-1):
			c = self.bwt[i]
			i = self.count[c] + self.occ[c][i] - 1
			t = [c] + t

		return ''.join(t)



text = 'abaaba'

#print(rotate(text))
print(BWT(text).bwt)
