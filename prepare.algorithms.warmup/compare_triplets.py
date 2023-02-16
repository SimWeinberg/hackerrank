def compareTriplets(a, b):
    pointsA = 0
    pointsB = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            pointsA += 1
        elif b[i] > a[i]:
            pointsB += 1
    return(pointsA, pointsB)