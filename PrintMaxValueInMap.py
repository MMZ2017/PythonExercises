d = {'HR':3,"MZ":6,"DR":9}

def printMaxValueInMap(d):
    maxK = None
    maxV = None
    for (x,y) in d.items():
        if maxV is None or maxV < y:
            (maxK, maxV) = (x, y)
    print str(maxK) + ":" + str(maxV)

printMaxValueInMap(d)