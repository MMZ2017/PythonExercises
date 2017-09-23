import re

l = re.split('[,.]', raw_input())
for i in l:
    if len(i) > 0:
        print i