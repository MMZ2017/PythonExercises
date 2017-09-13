from itertools import combinations

inp = raw_input().split()
S = inp[0]
k = int(inp[1])
S = sorted(list(S))

for i in range(1, k+1):
    l = list(combinations(S, i))
    l = sorted(l)
    for x in l:
        print ''.join(x)