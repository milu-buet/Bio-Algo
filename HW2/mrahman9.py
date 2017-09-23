#
# MD LUTFAR RAHMAN 
#
# mrahman9@memphis.edu
#
# COMP 8295 - Assignement 2
#

from Tree import *
from Bio import Phylo

#Question_1-------------------------------------------------------
#input: data file location
#output: A dictionary whose keys are gene names and values are DNA sequences
def getGeneDataset(data_file):
	gene_dataset = {}
	species = []
	lines = open(data_file).readlines()

	for i in range(len(lines)-1):
		if lines[i][0] == '>':
			species_name = '-'.join(lines[i].split('|')[1].strip().split(' '))
			gene_dataset[species_name] = lines[i+1].strip()
			species.append(species_name)

	return gene_dataset, species
#-------------------------------------------------------

def edit_distance_ita(x,y):
	table = {(-1,-1):0}

	for j in range(0,len(y)):
		table[(-1,j)] = j + 1
	for i in range(0,len(x)):
		table[(i,-1)] = i + 1

	for i in range(0,len(x)):
		for j in range(0,len(y)):
			if x[i] == y[j]:
				table[(i,j)] = table[(i-1,j-1)]
			else:
				a = 1 + table[(i-1,j-1)]
				b = 1 + table[(i,j-1)]
				c = 1 + table[(i-1,j)]
				table[(i,j)] = min(a,b,c)
	return table[(len(x)-1,len(y)-1)]


#Question_2---------------------------------------------
#input: gene dictionary produced by getGeneDataset
#output: distance matrix D. Edit distance of each pair of genes
def getEditDistances(gene_dict):
	D = {}  #Edit distances
	for gene1 in gene_dict:
		for gene2 in gene_dict:
			if gene1 != gene2 and (gene1,gene2) not in D:
				#print(gene1,gene2)
				edit_distance = edit_distance_ita(gene1,gene2)
				D[gene1,gene2] = D[gene2,gene1] = edit_distance
	return D
#---------------------------------------------
#---------------------------------------------
def build_phylogenetic_tree(data_file):
	gene_dict, species = getGeneDataset(data_file)
	D = getEditDistances(gene_dict)
	tree_string = build_tree(species, D)
	return tree_string
#---------------------------------------------

def create_file(content):
	fn = 'tree' 
	file = open(fn, 'w')
	file.write(content + '\n')
	file.close()
	return fn

def create_phylo_tree(tree_string):
	tree_file = create_file(tree_string)
	tree = Phylo.read(tree_file, 'newick')
	return tree

def draw_tree_ascii(tree_string):
	tree = create_phylo_tree(tree_string)
	Phylo.draw_ascii(tree)

def draw_tree_image(tree_string):
	tree = create_phylo_tree(tree_string)
	Phylo.draw(tree)

#Question_3 --------------------------------------------
#input: gene data file
#output: drawing phylogenetic tree in ascii
def phylogenetic_tree_ascii(data_file):
	tree_string = build_phylogenetic_tree(data_file)
	draw_tree_ascii(tree_string)


#Question_4 --------------------------------------------
#input: gene data file
#output: drawing phylogenetic tree in an image
def phylogenetic_tree_image(data_file):
	tree_string = build_phylogenetic_tree(data_file)
	draw_tree_image(tree_string)



#-------------------------------------------------------
#Three gene dataset
gene_data_files = ['a2_dataset/ds1.fasta','a2_dataset/ds2.fasta','a2_dataset/ds3.fasta']

#-------------------------------------------------------
for data_file in gene_data_files:
	phylogenetic_tree_ascii(data_file)

for data_file in gene_data_files:
	phylogenetic_tree_image(data_file)
