# Given an array of integers and a positive integer k, determine the number of (i,j) pairs where i<j and ar[i] + ar[j] is divisible by k.

def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(len(ar)):
        for j in range(i+1,len(ar)):
            if((ar[i]+ar[j])%k==0):
                count += 1
    return(count)
            
print(divisibleSumPairs(6,3,[1,3,2,6,1,2]))
