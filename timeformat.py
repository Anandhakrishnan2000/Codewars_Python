def format_duration(seconds):
    years = 0
    days = 0
    hours = 0
    min = 0
    sec = 0
    years = year(seconds)
    if years>0:
        seconds = seconds % 31536000
    days = day(seconds)
    if days>0:
        seconds = seconds % 86400
    hours = hour(seconds)
    if hours>0:
        seconds = seconds % 3600
    min = minute(seconds)
    if min>0:
        seconds = seconds % 60
    sec = seconds
    lst = []
    if years>0:
        if years==1:
            lst.append("1 year")
        else:
            lst.append(str(years)+" years")
    if days>0:
        if days==1:
            lst.append("1 day")
        else:
            lst.append(str(days)+" days")
    if hours>0:
        if hours==1:
            lst.append("1 hour")
        else:
            lst.append(str(hours)+" hours")
    if min>0:
        if min==1:
            lst.append("1 minute")
        else:
            lst.append(str(min)+" minutes")
    if sec>0:
        if sec==1:
            lst.append("1 second")
        else:
            lst.append(str(sec)+" seconds")

    if len(lst) == 0:
        return "now"
    else:
        string = ""
        for i in range(len(lst)):
            string+=lst[i]
            if i<len(lst)-2:
                string+=", "
            elif i==len(lst)-2:
                string+=" and "
            else:
                pass
        return string


def year(sec):
    y = sec//31536000
    return y
def day(sec):
    d = sec//86400
    return d
def hour(sec):
    h = sec//3600
    return h
def minute(sec):
    m = sec//60
    return m


print(format_duration(36654151))