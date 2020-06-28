
def primeFactors(n):
    if isprime(n):
        strg = str("("+str(n)+")")
        return strg
    else:
        fact = factlist(n)
        factlst = []
        for x in factors:
            factlst.append(x)
        factstr = factstring(factlst)
        return factstr


def factlist(n,iternum=2):
    global factors
    if iternum<=n:
        if n%iternum == 0:
            factors.append(iternum)
            productfact = n/iternum
            if isprime(productfact):
                factors.append(productfact)
                return factors
            else:
                factlist(productfact)
        else:
            iternum+=1
            factlist(n,iternum)
    else:
        factlst = list(factors)
        return factlst

def factstring(fact):
    factset = list(set(fact))
    factset.sort()
    factstr = ""
    for x in factset:
        power = fact.count(x)
        if power==1:
            factstr = factstr + "(" + str(x) + ")"
        else:
            factstr = factstr + "(" + str(x) + "**" + str(power) + ")"
    return factstr


def isprime(n):
    num = n
    if num==4:
        return True

    if num > 1:
        for i in range(2, num // 2):

            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                return False
                break
        else:
            return True

    else:
        return False


factors = []
print(primeFactors(933555431))