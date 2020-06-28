from itertools import permutations as pm

def permutations(string):
    lst = [x for x in string]
    perm = set(pm(lst))
    permlst = []
    for x in perm:
        str = ('').join(x)
        permlst.append(str)
    return permlst



