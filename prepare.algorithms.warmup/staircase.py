import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    i = 1
    spaces = n-1
    multiplier = 1
    while i < n:
        print(" "*spaces + "#"*multiplier)
        spaces = spaces - 1
        multiplier = multiplier + 1
        i += 1
    print("#"*n)

def staircase(n):
    for stairs in range(1, n + 1):
        print(' ' * (n - stairs) + '#' * stairs)
    
    
if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
