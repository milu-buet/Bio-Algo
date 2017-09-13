# Md Lutfar Rahman

#print('hello')


#recursive decomposition
def length(L):
	if L == []:
		return 0
	tail_of_L = L[1:-1]
	return 1 + length(tail_of_L)


def reverse(L):
	if len(L) == 0:
		return []

	tail_of_L = L[1:]
	#print(tail_of_L)
	return reverse(tail_of_L) + [L[0]]

print(reverse('abc'))


#Edit distance between x and y is the minimum of insertion, deletions and substitutions that convert x into y.
def edit_distance(x,y):
	return 0


X = 'THISISACAT'
Y = 'THATSACAT'

print(edit_distance(X,Y))