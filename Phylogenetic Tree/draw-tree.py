from Bio import Phylo
tree = Phylo.read('tree1.dnd', 'newick')
print(tree)
Phylo.draw_ascii(tree)
Phylo.draw(tree)