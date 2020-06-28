from itertools import permutations, combinations
def listPosition(word):
    """Return the anagram list position of the word"""
    perm = set(permutations(word,len(word)))
    wordlst = []
    for x in perm:
        string = ("").join(x)
        wordlst.append(string)
    wordlst.sort()
    print(wordlst)
    i = wordlst.index(word)
    return i+1




print(listPosition('ABAB'))