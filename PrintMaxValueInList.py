l = [8,2,3,4,5,6,7]

def printMaxInList(l):
	max = l[0]
	for i in range(len(l)):
		if l[i] > max:
			max = l[i]
	print max

printMaxInList(l)