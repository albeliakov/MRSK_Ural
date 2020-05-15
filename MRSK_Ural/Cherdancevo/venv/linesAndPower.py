import numpy as np

 # для каждой позиции расчитывается количество следующих за ней линий
def protectLines(inMatrix):
    dictProtectLines = {}
    for i in range(len(inMatrix)):
        dictProtectLines[i+1] = sum(inMatrix[i]) #np.array(sum(inMatrix[i]))
    return dictProtectLines

 # расчет количесвта защищаемых линий для соответсвующей позиции КА
def lineProtect(arrayPos, dictProtectLines, matrixLine):
    newDictProtLines = {}
    additProtLines = []
    reversArrayPos = arrayPos[::-1]
    newDictProtLines[reversArrayPos[0]] = dictProtectLines[reversArrayPos[0]]
    additProtLines.append(reversArrayPos[0])
    for pos in reversArrayPos[1:]:
        i = 0
        posLines = dictProtectLines[pos]
        while i < len(additProtLines):
            if matrixLine[pos-1][additProtLines[i]-1] == 1:
                posLines -= dictProtectLines[additProtLines[i]]
                del additProtLines[i]
            else: i+= 1
        newDictProtLines[pos] = posLines
        additProtLines.append(pos)

    return newDictProtLines


# рассчитывается количество линий, влияющих на функционирование КА на соответсвующей позиции
def lineInfluence(positions, amountLines):
    arrayInfl = [amountLines] * len(positions)
    return arrayInfl

# защищаемая мощность для каждой позиции КА
def functProtectConsumer(dictProtectPower, matrixGraph, amountLines):
    arrayProtectPower = []
    for posKA1 in range(0, amountLines):
        protectPower = 0
        for posKA2 in range(0, amountLines):
            if matrixGraph[posKA1][posKA2] == 1:
                listPower = dictProtectPower[posKA2 + 1]
                protectPower += listPower[1] * listPower[2]
        arrayProtectPower.append(protectPower)
    return arrayProtectPower

 # рассчитывается защищаемая мощность при установке КА на соответсвующей позиции
def powerProtect(positions, arrayProtectPower):
    returnPowerProtect = []
    for pos in positions:
        returnPowerProtect.append(arrayProtectPower[pos-1])
    return returnPowerProtect


 # рассчитывается математическое ожидание
def mathExpect(positions, protectLines, arrayProtectPower, amountLines):
    me = 0
    for pos in positions:
        me += protectLines[pos] * arrayProtectPower[pos-1]

    return me/amountLines

def calcForJ(posit, matrixGraph):
    positIsProt = []
    positIndOne = []
    for j in range(-1, -len(posit), -1):
        isBreak = False
        for k in range(-2, -len(posit), -1):
            if matrixGraph[posit[j]-1][posit[k]-1] == 1:
                break
                isBreak = True
        if isBreak:
            continue
        else:
            #print(posit)
            #print(j)
            #print(posit[-len(posit)], posit[j])
            if matrixGraph[posit[-len(posit)]-1][posit[j]-1] == 1: positIsProt.append(j)
            else: positIndOne.append(j)
    positIndOne.append(-len(posit))

    return (positIsProt, positIndOne)

# поиск независимых позиций
def searchIndepPos(positions, matrixGraph):
    lstIndependPositions = []
    lenPos = len(positions)
    for posI in range(lenPos-1):
        isBreak = False
        for posJ in range(posI+1,lenPos):
            if matrixGraph[positions[posJ]-1][positions[posI]-1] == 1:
                isBreak = True
                break
        if isBreak: continue
        lstIndependPositions.append(positions[posI])
    lstIndependPositions.append(positions[-1])
    return tuple(lstIndependPositions)

# расчет кол-ва защищаемых линий
def calculProtLines(positions, matrixGraph, dictProtLines):
    lstProtLines = []
    dictPosAndPrL = {}
    for iPos in positions:
        positProtLines = dictProtLines[iPos]
        #j = 0
        #lstIndPL = []
        for jPos in list(dictPosAndPrL.keys()):
        #for jPos in dictPosAndPrL:
            if matrixGraph[iPos - 1][jPos - 1] == 1:
                positProtLines -= dictPosAndPrL[jPos]
                #lstIndPL.append(jPos)
                del dictPosAndPrL[jPos]
        lstProtLines.append(positProtLines)
        # for pos in lstIndPL:
        #     del dictPosAndPrL[pos]
        dictPosAndPrL[iPos] = positProtLines
    return lstProtLines

# проверка на наличие соседних позиций.
def notIsNeigh(listPos, dictNeigh):
    breakGenPos = True
    # if listPos[-1] in dictNeigh:
    #     for neigh in dictNeigh[listPos[-1]]:
    #         if neigh in listPos[:-1]:
    #             breakGenPos = False
    #             break
    rowEl = listPos[-1]-1
    for el in reversed(listPos[:-1]):
        if dictNeigh[rowEl][el-1] == 1:
            breakGenPos = False
            break
    return breakGenPos