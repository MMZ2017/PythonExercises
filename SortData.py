N, M = map(int, raw_input().split())
l = list()
li = list()
for _ in range(N):
    li = map(int, raw_input().split())
    l.append(li)
K = int(raw_input())
l = sorted(l, key = lambda x: x[K])
for i in l:
    i = map(str, i)
    print " ".join(i)