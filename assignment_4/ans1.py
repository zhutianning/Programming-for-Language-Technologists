import math

def eq1(x):
    n = len(x) # numer of elements in the vector
    result = 0
    for i in range(n):
        if i < n:
            each_calculate = ((x[i]-x[i]**3)**2 * (n-1)) / math.sqrt(x[i])
            result += each_calculate
    return result
