def solution(args):
    i=0
    string = ""
    while(i<len(args)):
        curr = args[i]
        try:
            next = args[i+1]
        except IndexError:
            next=curr
        if curr+1 != next:
            string+=str(curr)
            if i == len(args)-1:
                pass
            else:
                string+=","
            i+=1
        else:
            rangestring,index = rangestr(args[i:],i-1)
            string+=rangestring
            i=index
            if i == len(args)-1:
                pass
            else:
                string+=","
            i+=1

    return string





def rangestr(args,index):
    actualindex=index
    span=1
    start = args[0]
    rangestring=""
    for i in range(len(args)):
        index+=1
        try:
            if args[i]+1 != args[i+1]:
                end = args[i]
                break
            else:
                span+=1
                continue
        except IndexError:
            end = args[i]
            break
    rangestring += str(start)+"-"+str(end)
    if span>=3:
        return rangestring,index
    else:
        return str(start),actualindex+1



print(solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))