N, X = map(int, raw_input().split())
l = list()
lall = list()
for _ in range(X):
    l = map(float, raw_input().split())
    lall.append(l)
for i in zip(*lall):
    print sum(i)/len(i)