# Phylogenetic tree construction

#-----------------------------------------------------------
tree_string = ''
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
		global tree_string
		if self.left is None and self.right is None:
			#print('%s:%.2f' % (self.label,self.dist2parent), end="")
			tree_string = tree_string + '%s:%.2f' % (self.label,self.dist2parent)

		else:
			tree_string = tree_string + "("
			#print("(", end="")
			self.left.Newick()

			tree_string = tree_string + ","
			#print(",", end="")
			self.right.Newick()

			tree_string = tree_string + '):%.2f' % self.dist2parent
			#print('):%.2f' % self.dist2parent, end="")
#-----------------------------------------------------------
'''
1. Initialize trees.
2. Find current closest pair in existing trees.
3. Merge the pair.
'''
#-----------------------------------------------------------
def build_tree(Species, D):
	global tree_string
	tree_string = ''
	Trees = []
	for s in Species:			#1. build initial trees
		Trees.append( Tree(s) )

	while len(Trees) > 1:
		i, j = find_closest_pair(D, Trees)
		ti, tj = Trees[i], Trees[j]
		new_tree = Tree(ti.label + tj.label, ti, tj)
		new_tree.h = D[ti.label, tj.label] * 0.5
		ti.dist2parent = new_tree.h - ti.h
		tj.dist2parent = new_tree.h - tj.h
		Trees.pop(j)
		Trees.pop(i)
		for t in Trees:
			d = D[ti.label, t.label]*ti.size + D[tj.label,t.label]*tj.size
			d = d / (ti.size + tj.size)
			D[new_tree.label, t.label] = d
			D[t.label, new_tree.label] = d
		Trees.append(new_tree)

	Trees[0].Newick()
	return tree_string

#-----------------------------------------------------------
def find_closest_pair(distance, trees):
	closest_pair = None
	closest_distance = None
	for i in range(0, len(trees)):
		for j in range(i+1, len(trees)):
			t1, t2 = trees[i], trees[j]
			if (closest_pair is None) or (closest_distance > distance[t1.label, t2.label]):
				closest_pair = (i, j)
				closest_distance = distance[t1.label, t2.label]
	return closest_pair

#-----------------------------------------------------------




