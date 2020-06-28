from itertools import permutations

def middle_permutation(string):
    ls = [x for x in string]
    perm = list(permutations(ls))
    permlst = []
    for x in perm:
        str = ('').join(x)
        permlst.append(str)
    permlst.sort()
    n=len(permlst)
    if n%2==0:
        return permlst[(n//2)-1]
    else:
        return permlst[n//2]


print(middle_permutation("abc"))