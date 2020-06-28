

def valid_parentheses(string):
    countopen = 0
    countclose = 0
    if (isparenthesis(string)):
        for i in string:
            if i=='(':
                countopen+=1
            if i==')':
                countclose+=1
        if countopen == countclose:
            return True
        else:
            return False
    else:
        return False

def isparenthesis(str):
    flagopen = 0
    flagclose = 0
    if str=='':
        return True

    for i in range(len(str)):
        if str[i]=='(':
            openindex=i
            break
        else:
            openindex=-1
    for i in range((len(str)-1),-1,-1):
        if str[i]==')':
            closeindex=i
            break
        else:
            closeindex=-1

    if openindex==-1 or closeindex==-1:
        return True

    for i in range(0,openindex):
        if str[i] == ')':
            flagopen = 1
            return False
        else:
            flagopen=0

    for i in range(len(str)-1,closeindex,-1):
        if str[i] =='(':
            flagclose=1
            return False
        else:
            flagclose=0

    if flagopen==0 and flagclose==0:
        return True







str=''
print(valid_parentheses(str))

