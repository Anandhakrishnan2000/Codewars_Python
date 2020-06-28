def pig_it(text):
    #your code here
    txtlst = text.split(" ")
    conlst = []
    for x in txtlst:
        str = ""
        if x.isalpha():
            str += x[1:]+x[0]+"ay"
        else:
            str = x
        conlst.append(str)
    convertstr = (" ").join(conlst)
    return convertstr



pig_it('This is my string')