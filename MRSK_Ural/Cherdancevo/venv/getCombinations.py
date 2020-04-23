 # eckjdbt
def _loopCondition(c, nKA, amountLines):
    deltaN = amountLines-nKA
    loopCondition = 0
    for i in range(len(c)):
        if (c[i] != deltaN+(i+1)):
            loopCondition = 1
            break
    return loopCondition

 # формирование новой комбинации
def _newComb(c, nKA, amountLines):
    deltaN = amountLines-nKA
    lenC = len(c)
    for i in reversed(range(lenC)):
        if (c[i] != deltaN+(i+1)):
            c[i] += 1
            for j in range(i+1, lenC):
                c[j] = c[j-1]+1
            break
    return c

def C(n, k):
    if k == 0:
        return 1
    elif k > n:
        return 0
    else:
        return C(n - 1, k) + C(n - 1, k - 1)

#print(_loopCondition([2,5,6], 3, 5))
#print(_newComb([2,4,6], 3, 5))
