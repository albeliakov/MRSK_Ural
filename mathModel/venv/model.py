from itertools import combinations
from queue import deque

AMOUNT_LINES = 18 # количесвто линий, подверженных КЗ

 # получение всевозможных позиций растановки КА в зависимочти от их количесвта
def combinationLines(amount_KA, amountLines = AMOUNT_LINES):
    positKA = [i for i in range(2, amountLines + 1)]  #
    combPosit = list(combinations(positKA, amount_KA))
    combinat_list = [list(item) for item in combPosit]
    return combinat_list

# -------------------- данные для схемы (линии электропередачи) ----------------
 # граф для линий (пока не нужен)
graph = {1: [2, 3],          2: [1],           3: [1, 4, 5],  4: [3],           5: [3, 6, 7],    6: [5],
         7: [5, 8, 11, 14],  8: [7, 9, 10],    9: [8],       10: [8],          11: [7, 12, 13], 12: [11],
        13: [11],            14: [7, 15, 16], 15: [14],      16: [14, 17, 18], 17: [16],        18: [16]}

 # матрица сопряженности линий (1 - если расположения КА на данных позициях
 #  будут влиять на функционирование друг друга
              # 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18
matrixGraph = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 1
               [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 2
               [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 3
               [0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 4
               [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 5
               [0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 6
               [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 7
               [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1],  # 8
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0],  # 9
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0],  # 10
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1],  # 11
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],  # 12
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # 13
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],  # 14
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],  # 15
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],  # 16
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],  # 17
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]  # 18

 # для каждой позиции опаисано количество следующих за ней линий
dictProtectLines = {1: 18, 2: 16, 3: 1, 4: 14, 5: 1, 6: 12,
                    7: 1, 8: 5, 9: 3, 10: 3, 11: 3, 12: 1,
                    13: 1, 14: 1, 15: 1, 16: 1, 17: 1, 18: 1}

# ------------------------------------------------------------------------------


# количесвто защищаемых потребителей для каждой позиции КА
def functProtectConsumer(dictAmountConsumer):
    dictPositConsumer = {1: 0, 2: 0,
                         3: dictAmountConsumer[0], 4: 0,
                         5: dictAmountConsumer[2], 6: 0,
                         7: dictAmountConsumer[1], 8: 0,
                         9: 0, 10: 0,
                         11: 0, 12: dictAmountConsumer[7],
                         13: dictAmountConsumer[6], 14: dictAmountConsumer[5],
                         15: dictAmountConsumer[4], 16: dictAmountConsumer[3],
                         17: dictAmountConsumer[9], 18: dictAmountConsumer[8]
                         }

    arrayProtectConsumer = []
    for posKA1 in range(0, AMOUNT_LINES):
        protectConsumer = 0
        for posKA2 in range(0, AMOUNT_LINES):
            if matrixGraph[posKA1][posKA2] == 1:
                protectConsumer += dictPositConsumer[posKA2 + 1]
        arrayProtectConsumer.append(protectConsumer)
    return arrayProtectConsumer


# Функция нахождения зависимых линий. На выходе - зависмые линии для конкретного расположения
def lineDepend(arrayPos, matrixLine=matrixGraph):
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
def lineInfluence(positions, protectLines, matrixLine=matrixGraph):
    #arrayInfl = []
    #arrayInfl.append(protectLines[0])
    #for i in range(1, len(positions)):
    #    for j in range(i):
    #        row = positions[i-j-1] - 1
    #        col = positions[i] - 1
    #        if matrixLine[row][col] == 1:  # если линии зависимы, то
    #            arrayInfl.append(protectLines[i] + arrayInfl[i-j-1])
    #            break
    #arrayInfl[0] = AMOUNT_LINES
    arrayInfl = [AMOUNT_LINES] * len(positions)
    return arrayInfl


 # рассчитывается количество защищаемых потребителей при установке КА на соответсвующей позиции
def consumerProtect(positions, arrayProtectConsumer):
    returnConsumerProtect = []
    for pos in positions:
        returnConsumerProtect.append(arrayProtectConsumer[pos-1])
    return returnConsumerProtect


 # рассчитывается математическое ожидание
def mathExpect(protectLines, influenceLines, consumers):
    me = 0
    for i in range(len(protectLines)):
        me += (protectLines[i] / influenceLines[i]) * consumers[i]
    return me


 # математическая модель для рассчета при установке N КА
def modelNka(nKA, arrayProtectConsumer, dictProtectLines=dictProtectLines):
     # формирование всевозможных позиций расположения КА (без повторений)
    combinatPositions = combinationLines(nKA)
    meMin = 1000000000
    optimalPositions = []
    for positions in combinatPositions:
        positions.append(1) # для расчета линий, незащищаемых ни одной КА
        positions.sort()    # сортировка по уровням графа линий
        #print(positions)
         # для каждой позиции находятся другие позиции КА, которые будут влиять на количесвто защищаемых ей линий
        dependLines = lineDepend(positions)
         # для каждой позиции рассчитываются соответсвующее количесвто защищаемых линий
        protectLines = lineProtect(dependLines, dictProtectLines)
        #print(protectLines)
         # для каждой позиции рассчитывается количесвто линий, влияющих на работу КА
        influenceLines = lineInfluence(positions, protectLines)
        #print(influenceLines)
         # для каждой позиции рассчитывается соответсвующее количесвто защищаемых потребителей
        consumers = consumerProtect(positions, arrayProtectConsumer)
        #print(consumers)
         # расчет мат ожидания
        me = mathExpect(protectLines, influenceLines, consumers)
        if me < meMin:
            optimalPositions.clear()
            meMin = me
            optimalPositions.append(positions[1:])
        elif me == meMin: optimalPositions.append(positions[1:]) # если оптимальных позиций окажется несколько

    return (meMin, nKA, optimalPositions)


 # рассчет для всех 1:N установленных КА
def calculationFrom1toNka(amountKA, numberCustomersTP):
    arrayCalculatData = []
    for i in range(1, amountKA+1):
        arrayCalculatData.append(modelNka(i, functProtectConsumer(numberCustomersTP)))
    return arrayCalculatData

#print(modelNka(17, functProtectConsumer([30, 20, 10, 5, 15, 40, 10, 30, 5, 10])))