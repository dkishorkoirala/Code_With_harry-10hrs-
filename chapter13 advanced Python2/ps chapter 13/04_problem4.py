def divisible5(n):
    if (n % 5 == 0):
        return True
    return False

a = [2, 124,3553,234,235, 3453,2345,5435,3454,345]

f = list(filter(divisible5, a))
print(f)