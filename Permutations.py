from itertools import permutations

inp = raw_input().split()
S = inp[0]
n = int(inp[1])
l = list(permutations(S, n))
l.sort()
for i in l:
    print "".join(i)