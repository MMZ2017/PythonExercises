from collections import deque

N = int(raw_input())
d = deque()
for _ in range(N):
    inp = raw_input().split()
    if len(inp) > 1:
        comm = inp[0]
        num = int(inp[1])
    else:
        comm = inp[0]
    if comm == "append":
        d.append(num)
    elif comm == "pop":
        d.pop()
    elif comm == "popleft":
        d.popleft()
    elif comm == "appendleft":
        d.appendleft(num)

d = map(str, d)
print " ".join(d)