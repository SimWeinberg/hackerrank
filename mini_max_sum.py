import math
import os
import random
import re
import sys

# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers

# The function accepts INTEGER_ARRAY arr as parameter.

def miniMaxSum(arr):
    sums = []
    for i in arr:
        sumN = sum(arr) - i
        sums.append(sumN)
    minSum = min(sums)
    maxSum = max(sums)
    print(minSum, maxSum)
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
