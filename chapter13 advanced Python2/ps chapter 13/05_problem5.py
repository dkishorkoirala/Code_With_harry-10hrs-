from functools import reduce
l = [2, 124, 53, 234, 235, 3453, 2345, 5435, 3454, 345]

def greater(a,b):
    if a > b:
        return a
    return b

print(reduce(greater, l))