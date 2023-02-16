#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    i = 0
    diagonal1 = 0
    diagonal2 = 0
    while i < n:
        diagonal1 = diagonal1 + arr[i][i]
        print(diagonal1)
        i += 1
    i = (n-1)
    print(i)
    j = -1
    while i >= 0:
        j = j + 1
        diagonal2 = diagonal2 + arr[i][j]
        print(j)
        print(diagonal2)
        i -= 1
    solution = diagonal1 - diagonal2
    return(abs(solution))
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()