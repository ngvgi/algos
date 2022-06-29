import math


def getX(a, b, c):
    try:
        root = math.sqrt(b**2 - (4*a*c))
        denom = 2*a
        neg_b = b * - 1
        x1 = (neg_b + root) / denom
        x2 = (neg_b - root) / denom
        smaller_X = x1 if x1 < x2 else x2
        return smaller_X
    except ValueError:
        return 'Cannot get the root of a negative number'


a, b, c = 9, 2, 6
sol = getX(a, b, c)
print(sol)
