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
    for i in range(lenC-1,-1,-1):
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
 # возвращает таблицу со всеми значениями числа сочетаний (C(n,k) -> tableC[n][k])
def tableC(amountKA):
    b = [[0] * (amountKA+1) for i in range(amountKA+1)]
    for i in range(amountKA+1):
        b[i][0]=1
        b[i][i]=1
        for j in range(1, i):
            b[i][j] = b[i-1][j-1] + b[i-1][j]
    return b

def getCombs(nKA, neighborsMatrix, amountLines):
    #nKA = len(positions)
    returnList = []
    comb = [i for i in range(2,nKA+2)]
    #comb = positions
    lastComb = [amountLines-j for j in reversed(range(nKA))]
    pos = 0
    #nn = 0
    while True:
        #if nn == 565192974447466283705621102602844427902249:
        #    nn = 0
        #    print(1/1000)
        #nn += 1
        print(comb)
        if comb == lastComb: break # последняя комбинация не рассматривается в цикле
        contWhile = False
        breakFor =False
        # если есть соседние позиции
        #print(comb)
        for i in range(len(comb[pos:]) - 1):
            for j in range(1,len(comb[i+pos:])):
                if neighborsMatrix[comb[pos+i]-1][comb[i+pos+j]-1] == 1:
                    pos += i
                    while comb[pos+j] == lastComb[pos+j]: # равно макимальному значение
                        j = j-1
                    comb[pos+j] += 1
                    delt = j
                    if j < 0:
                        pos+=j
                        delt = 0
                    for k in range(pos+delt+1, nKA):
                        comb[k] = comb[k-1] + 1
                    contWhile = True
                    breakFor = True
                    break
            if breakFor: break

        if contWhile: continue

        # если нет соседних позиций
        returnList.append(comb.copy())
        #print(comb)
        for i in range(nKA - 1, -1, -1):
            if (comb[i] != lastComb[i]):
                comb[i] += 1
                if i != 0: pos = i-1
                else: pos = i
                for j in range(i + 1, nKA):
                    comb[j] = comb[j - 1] + 1
                break

    # последняя комбинация
    returnList.append(lastComb)

    return returnList