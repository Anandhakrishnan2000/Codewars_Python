

def same_structure_as(original,other):
    if original == other:
        return True
    else:
        if type(original) == type(other):
            orig = convert(original)
            oth = convert(other)
            if orig == oth:
                return True
            else:
                return False
        else:
            return False



def v(x):
   return 1

def convert(l):
    z = []
    for x in l:
        if isinstance(x, list):
            z.append(convert(x))
        else:
            z.append(v(x))
    return z




print(same_structure_as([1, [1, 1]], [2, [2, 2]]))
