
 # для каждой позиции расчитывается количество следующих за ней линий
def protectLines(inMatrix):
    dictProtectLines = {}
    for i in range(len(inMatrix)):
        dictProtectLines[i+1] = sum(inMatrix[i])
    return dictProtectLines


# Функция нахождения зависимых линий. На выходе - зависмые линии для конкретного расположения
def lineDepend(arrayPos, matrixLine):
    lineDependReturn = []
    for posJ in range(len(arrayPos)):
        sliceArray = arrayPos[posJ : len(arrayPos)]
        workArray = []
        if len(sliceArray) > 1:
            for i in range(1, len(sliceArray)):
                row = sliceArray[0] - 1
                col = sliceArray[i] - 1
                if matrixLine[row][col] == 1: # если линии зависимы, то оставляем
                    workArray.append(sliceArray[i])

            if len(workArray) > 1:
                delIt = 1
                array1 = workArray
                array3 = []
                while(delIt < len(array1)):
                    array2 = []
                    array3.append(array1[delIt-1])
                    for j in range(delIt, len(array1)):
                        row = array1[delIt-1]-1
                        col = array1[j] - 1
                        if matrixLine[row][col] == 0:  # если линии независимы, то оставляем
                            array2.append(array1[j])
                    array1 = array3+array2
                    delIt += 1
                workArray = array1
        lineDependReturn.append([sliceArray[0]]+workArray)

    return lineDependReturn


# функция подсчета защищаемых КА линий в зависимости от расположения
def lineProtect(dependLines, dictProtectLines):
    lineProtectReturn = []
    for arrPos in dependLines:
        protectLinesPosit = dictProtectLines[arrPos[0]]
        if len(arrPos) > 1:
            for i in range(1, len(arrPos)):
                protectLinesPosit -= dictProtectLines[arrPos[i]]
        lineProtectReturn.append(protectLinesPosit)

    if len(lineProtectReturn) != len(dependLines):
        print("lineProtect(): Количесвто значений в входном массиве не равно в выходном")
    else: return lineProtectReturn

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
def mathExpect(protectLines, influenceLines, power):
    me = 0
    for i in range(len(protectLines)):
        me += (protectLines[i] / influenceLines[i]) * power[i]
    return me