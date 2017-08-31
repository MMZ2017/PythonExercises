if __name__ == '__main__':
    n = int(raw_input())
    l = list()
    for x in range(n):
        s = raw_input().split()
        if s[0] == "insert":
            l.insert(int(s[1]),int(s[2]))
        if s[0] == "print":
            print l
        if s[0] == "remove":
            l.remove(int(s[1]))
        if s[0] == "append":
            l.append(int(s[1]))
        if s[0] == "sort":
            l.sort()
        if s[0] == "pop":
            l.pop()
        if s[0] == "reverse":
            l.reverse()