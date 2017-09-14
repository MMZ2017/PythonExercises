from collections import OrderedDict

N = int(raw_input())
O = OrderedDict()
for _ in range(N):
    item, price = raw_input().rsplit(" ", 1)
    price = int(price)
    O[item] = O.get(item, 0) + price
for item, price in O.items():
    print item, price