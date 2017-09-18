S = raw_input()
d = dict()

for i in S:
    d[i] = d.get(i, 0) + 1

d = sorted(d.items(), key = lambda x: (-x[1], x), reverse = False)


print d[0][0], d[0][1]
print d[1][0], d[1][1]
print d[2][0], d[2][1]
