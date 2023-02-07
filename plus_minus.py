
def plusMinus(arr):
    positive_values = 0
    negative_values = 0
    zeros = 0
    for i in arr:
        if i > 0:
            positive_values = positive_values + 1
        elif i < 0:
            negative_values = negative_values + 1
        elif i == 0:
            zeros = zeros + 1
        positive_ratio = positive_values / n 
        negative_ratio = negative_values / n
        zeros_ratio = zeros / n
    print(positive_ratio)
    print(negative_ratio)
    print(zeros_ratio)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
