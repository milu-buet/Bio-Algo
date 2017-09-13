# Phylogenetic tree construction

#-----------------------------------------------------------
# return a list of species and the distance matrix
#-----------------------------------------------------------
def Initialize(distance_file):
	Species = []
	D = {}
	with open(distance_file) as f:
		for line in f:
			items = line.strip().split(" ")
			Species.append(items[0])
			for i, s in enumerate(Species):
				if i<len(Species)-1:
					D[s,items[0]] = D[items[0],s] = float(items[i+1])
	return Species, D

#-----------------------------------------------------------
class Node(object):
	def __init__(self, label, left=None, right=None):
		self.label = label
		self.left = left
		self.right = right
		if left is not None and right is not None:
			self.size = left.size + right.size
		else:
			self.size = 1
		self.dist2parent = 0
		self.h = 0

	def Newick(self):
		if self.left is None and self.right is None:
			print('%s:%.2f' % (self.label,self.dist2parent), end="")
		else:
			print("(", end="")
			self.left.Newick()
			print(",", end="")
			self.right.Newick()
			print('):%.2f' % self.dist2parent, end="")
#-----------------------------------------------------------
'''
1. Initialize trees.
2. Find current closest pair in existing trees.
3. Merge the pair.
'''

