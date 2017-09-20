n = int(raw_input())
for _ in range(n):
    a, b = map(int, raw_input().split())
    try:
        print a/b
    except ZeroDivisionError as e:
        print "Error Code:", e
    except ValueError as f:
        print "Error Code:", f