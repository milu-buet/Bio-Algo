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

#Species, D  = Initialize('phylo_distance.txt')
#print(Species,D)

#------------------------------------------
class Tree(object):
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

def build_tree(dm):
	Species, D = Initialize(dm)
	#print(Species,D)
	Trees = []

	for s in Species:
		Trees.append(Tree(s))

	
	while len(Trees)>1:
		i,j = find_closest_pair(D, Trees)
		ti,tj = Trees[i], Trees[j]

		new_tree = Tree(ti.label+tj.label,ti,tj)
		new_tree.h = D[ti.label,tj.label]/2
		ti.dist2parent = new_tree.h - ti.h
		tj.dist2parent = new_tree.h - tj.h

		for t in Trees:
			if t!=ti and t!=tj:
				D[new_tree.label,t.label] = D[t.label,new_tree.label] = (D[new_tree.left.label,t.label] + D[new_tree.right.label,t.label])/2

		Trees.pop(i)
		Trees.pop(j-1)
		Trees.append(new_tree)

	Trees[0].Newick()

	

	# print(ti.label)
	# print(tj.label)
	# print(D[ti.label,tj.label])


def find_closest_pair(distances, trees):
	closet_pair = None
	closest_distance = None
	for i in range(len(trees)-1):
		for j in range(i+1,len(trees)):
			t1 = trees[i]
			t2 = trees[j]
			#print(t1.label,t2.label)
			if (closest_distance is None) or (closest_distance > distances[t1.label,t2.label]):
				closet_pair = (i,j)
				closest_distance = distances[t1.label, t2.label]

	return closet_pair


build_tree('phylo_distance.txt')


