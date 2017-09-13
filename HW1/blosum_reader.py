'''
- blosum: read blosum files
- example: get_matrix("blosum50.txt")
'''

import re

def get_items(line, ext):
	if ext == 'csv':
		return line.strip().split(',')
	return [ i for i in re.split('\s', line.strip()) if i!='' ]

def get_matrix(fn):
	lines = open(fn).readlines()
	lines = [ l for l in lines if not l.startswith('#')]
	aa = get_items(lines.pop(0), fn[-3:])
	mat = {}
	for line in lines:
		items = get_items(line, fn[-3:])
		a = items.pop(0)
		for i in range(len(items)):
			mat[(a,aa[i])] = int(items[i])
	return mat

if __name__ == '__main__':
	M = get_matrix('data/blosum50.txt')
	for k,v in M.items():
		print(k, M[k])