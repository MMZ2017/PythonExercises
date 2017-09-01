if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    max = max2 = None
    for x in arr:
        if x == max:
            max2 = max2
        elif x > max:
            max, max2 = x, max
        elif x > max2:
            max, max2 = max, x
    print max2