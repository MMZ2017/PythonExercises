from itertools import combinations

n = int(raw_input())
inp = raw_input().split()
k = int(raw_input())
l = list(combinations(inp, k))
x = 0
for i in l:
    if 'a' in i:
        x = x + 1
p = float(x)/float(len(l))
print p