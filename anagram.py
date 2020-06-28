def anagrams(word, words):
    # your code here
    anagram = []
    for i in words:
        if check(word, i):
            anagram.append(i)
    return anagram

def check(word, element):
    flag = 0
    if len(word) == len(element):
        for i in word:
            if count(i, word) == count(i, element):
                flag = 1
            else:
                return False
        if flag == 1:
            return True
        else:
            return False
    else:
        return False


def count(i, word):
    count = 0
    for x in word:
        if x == i:
            count += 1
    return count

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))

