""" 
    permutation of "abcdefg"
    perm(0)
    perm(0,1)
    add s(3) to every position of perm(2)
    add s(4) to every position of perm(0,3)
"""


def perm(X: str) -> str:
    if len(X) == 1:
        return X

    if len(X) == 2:
        perm = ""

    pass
