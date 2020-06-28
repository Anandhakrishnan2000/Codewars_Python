snaillst = []
def snail(snail_map):
    maxlen = len(snail_map)

    ival=0
    jval=0

    if(maxlen==1):
        snaillst.append(snail_map[0][0])
        return snaillst
    elif maxlen>1:
        for j in range(maxlen):
            jval=j
            snaillst.append(snail_map[0][j])
        for i in range(ival+1,maxlen):
            ival=i
            snaillst.append(snail_map[i][jval])
        for j in range(jval-1,-1,-1):
            jval=j
            snaillst.append(snail_map[ival][j])
        for i in range(ival-1,0,-1):
            ival=i
            snaillst.append(snail_map[i][jval])
        newmap = newmatrix(snail_map)
        return snail(newmap)
    else:
        return snaillst


def newmatrix(snail_map):
    maxlen = len(snail_map)
    jval=0
    ival=0
    newlst = []
    for j in range(maxlen):
        jval = j
        snail_map[0][j]='x'
    for i in range(ival + 1, maxlen):
        ival = i
        snail_map[i][jval]='x'
    for j in range(jval - 1, -1, -1):
        jval = j
        snail_map[ival][j]='x'
    for i in range(ival - 1, 0, -1):
        ival = i
        snail_map[i][jval]='x'
    for x in snail_map:
        item = []
        for i in x:
            if i!='x':
                item.append(i)
        newlst.append(item)
    finallst = removex(newlst)
    return finallst

def removex(lst):
    finlst = []
    for x in lst:
        if len(x)!=0:
            finlst.append(x)
    return finlst



array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
#expected = [1,2,3,4,5,6,7,8,9]
print(snail(array))
