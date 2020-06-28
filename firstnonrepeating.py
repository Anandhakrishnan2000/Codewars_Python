def first_non_repeating_letter(string):
    #your code here
    i=0
    for x in string:
        if string.lower().count(x.lower()) > 1:
            i+=1
            continue
        else:
            return x
    else:
        return ''






print(first_non_repeating_letter('sTreSS'))