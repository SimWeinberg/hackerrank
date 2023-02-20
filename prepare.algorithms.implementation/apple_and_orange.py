# Sam's house has an apple tree and an orange tree that yield an abundance of fruit. Using the information given below, determine the number of apples and oranges that land on Sam's house.

# When a fruit falls from its tree, it lands x units of distance from its tree of origin along the -axis. *A negative value of  means the fruit fell x units to the tree's left, and a positive value of x means it falls x units to the tree's right. *

# Given the value of  for  apples and  oranges, determine how many apples and oranges will fall on Sam's house (i.e., in the inclusive range )?

def countApplesAndOranges(s, t, a, b, apples, oranges):
    fallenApples = []
    fallenOranges = []
    applesOnHouse = 0
    orangesOnHouse = 0 
    for i in apples:
        fA = i + a
        fallenApples.append(fA)
    for i in  oranges:
        fO = i + b
        fallenOranges.append(fO)
    for i in fallenApples:
        if i >=s and i <=t:
            applesOnHouse = applesOnHouse + 1
    for i in fallenOranges:
        if i >=s and i <=t:
            orangesOnHouse = orangesOnHouse + 1
    print(applesOnHouse)
    print(orangesOnHouse)