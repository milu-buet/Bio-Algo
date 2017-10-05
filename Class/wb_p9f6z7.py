class BWT():
	def __init__(self, t):
		self.bwt = self.build_bwt(t)
		self.Occ = self.build_occ(t)
		self.Count = self.build_count(t)
		self.largest = sorted(list(set(t)))

	#----------------------------------------------------------
	# return the left rotation of t
	def rotate(self, t):
		first = t[0]
		everything_but_first = t[1:]
		return everything_but_first + first

	#----------------------------------------------------------
	# construct the Burrows-Wheeler transform of T
	def build_bwt(self, T):
		rotations = [T]
		# Get all rotations of T and store them to rotations.
		for i in range(1,len(T)):
			s = self.rotate(rotations[-1])
			rotations.append( s )
		rotations.sort()
		# construct a list containing last characters of sorted rotations.
		t = [ x[-1] for x in rotations ]
		return ''.join(t)

	#----------------------------------------------------------
	def build_occ(self, t):
		occ = { c : [0]*len(t) for c in set(t) }
		for i in range(len(self.bwt)):
			c = self.bwt[i]
			for char in occ:
				occ[char][i] = occ[char][i-1]
			occ[c][i] += 1
		return occ

	#----------------------------------------------------------
	def build_count(self, t):
		characters = list(set(t))
		characters.sort()
		count = {'$' : 0}
		for i in range(1, len(characters)):
			count[characters[i]] = count[characters[i-1]] + t.count(characters[i-1])
		return count

	#----------------------------------------------------------
	def reconstruct(self):
		c, i = '$', 0
		t = [c]
		for j in range(len(self.bwt)-1):
			c = self.bwt[i]
			i = self.Count[c] + self.Occ[c][i] - 1
			t = [c] + t
		return ''.join(t)

#----------------------------------------------------------
# return the number of occurances

	def query(self,pattern):
		pass


#--------------------------------------------------------
import random

def random_string(n):
	return ''.join([ random.choice('actg') for i in range(n)])
# text = 'abaaba$'
text = random_string(50) + '$'
b = BWT(text)
print(text)
print(b.bwt)
print(b.reconstruct())
