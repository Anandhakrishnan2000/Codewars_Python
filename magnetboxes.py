def doubles(maxk, maxn):
    # your code
    s = 0.0
    for k in range(1,maxk+1):
        s+=u(k,maxn)
    return s


def u(k,n):
    v=0.0
    for x in range(2,n+2):
        v = v + (1/(k*(x**(2*k))))
    return v


print(doubles(10, 100))