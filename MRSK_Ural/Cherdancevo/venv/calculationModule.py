import graphCherdancevo as gc
import linesAndPower as lap
import getCombinations as comb
import numpy as np
import math
import time

AMOUNT_LINES = gc.AMOUNT_LINES # количесвто линий, подверженных КЗ
matrixGraph = gc.loadConjMatrix() # матрица сопряженности линий
dictProtectLines = lap.protectLines(matrixGraph) # словарь, содержащий для каждой позиции КА количесвто зависимых позиций
dictDataTP = gc.loadDataTP() # словарь, содержащий данные про ТП
arrayProtectPower = lap.functProtectConsumer(dictDataTP, matrixGraph, AMOUNT_LINES) # зщищаемая млщность каждой КА
tableComb = comb.tableC(AMOUNT_LINES-1) # таблица комбинаций4
neighborsMatrix = gc.loadConjMatrix(sheetName='neighbors', cellsInd=('B2', 'EY155'))
SUM_POWER = arrayProtectPower[0] # суммарная мощность на всей линии
MAX_CHANGE_POWER = 0.05 # изменеие отключаемой мощности, при которой прекращаются расчеты (в долях)

dictNM = neighborsMatrix
# dictNM = {} #словарь соседних символов
# for rowI in range(1,len(neighborsMatrix)+1):
#     dictNM[rowI] = []
#     for colJ in range(rowI,len(neighborsMatrix[rowI-1])):
#         if neighborsMatrix[rowI-1][colJ]==1: dictNM[rowI].append(colJ+1)
#     if len(dictNM[rowI]) == 0: del dictNM[rowI] # удалить пустые

 # математическая модель для рассчета при установке N КА
#def modelNka(nKA, arrayProtectPower=arrayProtectPower,
#             dictProtectLines=dictProtectLines, matrixGraph=matrixGraph,
#             tableComb=tableComb):
#    meMin = 1000000000
#    optimalPositions = []
#    #print()
#    #print('Количество уснанавливаемых КА -', nKA)
#    #print(time.ctime())
#     # формирование всевозможных позиций расположения КА (без повторений)
#    c = [i for i in range(2,nKA+2)]
#    nKA = 72
#    amountComb = tableComb[AMOUNT_LINES-1][nKA]
#    oneTenth = amountComb//10
#    print(amountComb, oneTenth)
#    for numbPosit in range(1, amountComb+1):
#     #   if numbPosit%oneTenth==0: print('Прошла 1/10')
#        #positList = [1] + c
#        positions = [1] + c
#        #positions = np.array(positList)
#        #print('positions=', positions)
#         # для каждой позиции находятся другие позиции КА, которые будут влиять на количесвто защищаемых ей линий
#        #dependLines = lap.lineDepend(positions, matrixGraph)
#         # для каждой позиции рассчитываются соответсвующее количесвто защищаемых линий
#        #protectLines = lap.lineProtect(dependLines, dictProtectLines)
#        protectLines = lap.lineProtect(positions, dictProtectLines, matrixGraph)
#        #print(protectLines)
#         # для каждой позиции рассчитывается количесвто линий, влияющих на работу КА
#        #influenceLines = lap.lineInfluence(positions, AMOUNT_LINES)
#        #print(influenceLines)
#         # для каждой позиции рассчитывается соответсвующая защищаемая мощность
#        #powers = lap.powerProtect(positions, arrayProtectPower)
#        #print(consumers)
#         # расчет мат ожидания
#        me = lap.mathExpect(positions, protectLines, arrayProtectPower, AMOUNT_LINES)
#        if me < meMin:
#            optimalPositions.clear()
#            meMin = me
#            optimalPositions.append(positions[1:])
#        if me == meMin: optimalPositions.append(positions[1:]) # если оптимальных позиций окажется несколько
#         # формирование новой комбинации
#        c = comb._newComb(c, nKA, AMOUNT_LINES)
#        #print('c=', c)
#    return (meMin, nKA, optimalPositions)
#
# # рассчет для всех 1:N установленных КА
#def calculationFrom1toNka(amountKA):
#    arrayCalculatData = []
#    for i in range(1, amountKA+1): arrayCalculatData.append(modelNka(i))
#    return arrayCalculatData

#print(dictProtectLines)
# def calculationFrom1toNka(amountKA):
#     arrayCalculatData = []
#     meMin = 100000
#     optimalPositions = []
#     for key in dictProtectLines:
#         if key[0] == 1:
#             continue
#         protectLines = np.array((dictProtectLines[(1,)][0]-dictProtectLines[key][0], dictProtectLines[key][0]))
#         powers = np.array((arrayProtectPower[0], arrayProtectPower[key[0]-1]))
#         me = np.sum(protectLines*powers)/AMOUNT_LINES
#         if me < meMin:
#             optimalPositions.clear()
#             meMin = me
#             optimalPositions.append(key)
#         elif me == meMin: optimalPositions.append(key) # если оптимальных позиций окажется несколько
#     arrayCalculatData.append((meMin, 1, optimalPositions.copy()))
#     #print(arrayCalculatData)
#
#     dictPositAndProtectLine = dictProtectLines.copy()
#     dictPP = {}
#
#     for i in range(2,amountKA+1):
#         meMin = 100000
#         optimalPositions.clear()
#         #print(dictPositAndProtectLine)
#         for key in dictPositAndProtectLine:
#             print(i, key)
#             for pos in range(2,key[0]):
#                 #print(i, pos, key)
#                 positions = [pos] + list(key)
#
#                 tuplePositInd = lap.calcForJ(positions, matrixGraph)
#
#                 arrPositInd = tuplePositInd[0]
#                 #print(pos)
#                 #if i == 3: print(dictProtectLines)
#                 posInd = dictProtectLines[(pos,)][0]
#                 protLineOne = AMOUNT_LINES
#
#                 for ind in arrPositInd:
#                     posInd -= dictPositAndProtectLine[key][ind]
#
#                 #print(tuplePositInd[1])
#                 arrNewProt = [posInd] + dictPositAndProtectLine[key]
#                 if pos != 2: dictPP[tuple(positions)] = arrNewProt
#
#                 for ind in tuplePositInd[1]:
#                     protLineOne -= arrNewProt[ind]
#
#
#
#                 arrNewWithOne = [protLineOne] + arrNewProt
#                 powers = lap.powerProtect([1]+positions, arrayProtectPower)
#                 #me = np.sum(arrNewWithOne * powers) / AMOUNT_LINES
#                 me = 0
#                 for el in range(len(arrNewWithOne)):
#                     me += arrNewWithOne[el] * powers[el]
#                 me /= AMOUNT_LINES
#                 if me < meMin:
#                     optimalPositions.clear()
#                     meMin = me
#                     optimalPositions.append(positions)
#                 elif me == meMin:
#                     optimalPositions.append(positions)  # если оптимальных позиций окажется несколько
#
#         arrayCalculatData.append((meMin, i, optimalPositions.copy()))
#
#         dictPositAndProtectLine.clear()
#         dictPositAndProtectLine = dictPP.copy()
#         #if i==2: print(dictPositAndProtectLine)
#         dictPP.clear()
#     return arrayCalculatData
#
# for cal in calculationFrom1toNka(5):
#     print(cal)

# def calculationFrom1ToNka(amountKA = AMOUNT_LINES):
#     newPosit = 0
#     newPL = 0
#     numbComb = 0
#
#     # Инициализация словаря, в который будут записываться рассчитанные данные в виде
#     # кол-во_КА : ( [позиции], мат.ожид. )
#     dictCalculData = {i: ([], round(2*SUM_POWER, 1)) for i in range(1, amountKA)}
#
#     # Формирование ветки позиций, от с бОльшим номером к меньшому
#     for nKA in reversed(range(2,amountKA+1)):
#         # Инициализация ветки для дальнейшего продвижения по ней
#         lstProtLines = [0 for i in range(nKA-1)] # список, хранящий количесвто защищаемых линий
#         cntPos = 1 # счетчик текущего количесвта позиций
#         positions = [nKA]  # первая позиция ветки
#         lstProtLines[cntPos-1] = dictProtectLines[nKA] # инициализация первой позиции ветки
#         lstIndepPosit = [nKA]
#         print(nKA, 'Начал ', time.ctime())
#         # Цикл проведения расчета для всех комбинаций
#         while True:
#             # Цикл рассчета и движения в глубину
#             while True:
#                 numbComb += 1
#                 #print()
#                 #print(positions)
#                 # print(lstIndepPosit)
#
#                 # Рассчет независимых позиций
#                 #independPosit = lap.searchIndepPos(positions, matrixGraph)
#
#                 # Рассчет кол-ва защишаемых линий позицией 1
#                 oneProtLines = dictProtectLines[1]
#                 #for indPos in independPosit:
#                 for indPos in lstIndepPosit:
#                     oneProtLines -= dictProtectLines[indPos]
#
#                 # Рассчет мат ожидания
#                 me = 0
#                 print()
#                 for nPos in range(cntPos):
#                     #print(lstProtLines[nPos], arrayProtectPower[positions[nPos]-1])
#                     me += lstProtLines[nPos] * arrayProtectPower[positions[nPos]-1]
#                 print(oneProtLines, arrayProtectPower[0])
#                 me = (me + oneProtLines*arrayProtectPower[0]) / amountKA
#                 print(me)
#                 # Сохранение, при минимальности мат ожидания, полученных данных
#                 if me < dictCalculData[cntPos][1]:
#                     #dictCalculData[cntPos][0].clear()
#                     dictCalculData[cntPos] = ([positions.copy()], me)
#                 elif me == dictCalculData[cntPos][1]:
#                     dictCalculData[cntPos][0].append(positions.copy())
#                 #print(dictCalculData)
#                 # Условие конца движения в глубину
#                 #print(positions[cntPos-1], len(positions), cntPos)
#                 if positions[cntPos-1] == 2:
#                     cntPos -= 1
#                     #print(cntPos)
#                     break
#
#                 # ДВИЖЕНИЕ В ГЛУБИНУ
#                 newPosit = positions[-1] - 1 # новая позиция меньше на 1 предыдущей
#                 # Рассчет кол-ва защищаемых линий для новой позиции
#                 #print('newPosi', newPosit)
#                 newPL = dictProtectLines[newPosit] # кол-во защищаемых линий новой позицией
#                 newLstIndepPos = [] # для расчета независимых позиций при добалении новой позиции
#                 for pos in lstIndepPosit:
#                     if matrixGraph[newPosit-1][pos-1] == 1: newPL -= dictProtectLines[pos]
#                     else: newLstIndepPos.append(pos) # если старая позиция не влияет на новую, то остается
#                 newLstIndepPos.append(newPosit) # добаление новой позиции
#                 lstIndepPosit = newLstIndepPos.copy() # обновление списка независимых позиций
#                 lstProtLines[cntPos] = newPL
#                 positions.append(newPosit)
#                 cntPos += 1  # количесвто позиций увеличивается
#
#             # Условие окнчания всех рассчетов
#             if cntPos < 2:
#                 if cntPos < 0: print('Отрицательое значение cntPos')
#                 break
#
#             # Формирование нового элемента (шаг назад)
#             positions[cntPos-1] -= 1
#             del positions[-1]
#
#             # Формирование нового списка независимых позиций
#             lstIndepPosit = lap.searchIndepPos(positions, matrixGraph).copy()
#
#
#     print(numbComb)
#     return dictCalculData

# dictRet = calculationFrom1ToNka(154)
# for el in dictRet:
#     print(el, dictRet[el])

def calculationFrom1ToNka(amountKA = AMOUNT_LINES-1):
    returnCalculData = [[SUM_POWER]]
    #cntIter = 0
    # Поиск оптимальных позиций для количества КА от 1 до amountKA
    for nKA in range(1, amountKA+1):
        txtF = open('outData.txt', 'a')
        print()
        print(nKA, 'начало:', time.ctime())
        meMin = 2*SUM_POWER #
        optimalPositions = []
        numbComb = 0

        # ИНИЦИАЛИЗАЦИЯ ПЕРВОНАЧАЛЬНЫХ ДАННЫХ
        # стартовый список позиций
        # positions = [i for i in range(AMOUNT_LINES, AMOUNT_LINES-nKA, -1)]
        positions = [AMOUNT_LINES]
        for i in range(nKA-1):
            appPos = positions[i] - 1
            positions.append(appPos)
            while positions[-1] != nKA-i:  # неминимальное значение
                if lap.notIsNeigh(positions, dictNM): break
                positions[-1] -= 1

        if nKA > 1:
            # кортеж, содержащиq независмые позиции, исключая последнюю позицию (для расчета для 1 и новой позиций)
            tplIndPosWithoutLast = lap.searchIndepPos(positions[:-1], matrixGraph)
            #print('tpl', tplIndPosWithoutLast)
            # список, содержащий кол-во защищаемых линий, исключая для последней позиции
            lstProtLinesWithoutLast = lap.calculProtLines(positions[:-1], matrixGraph, dictProtectLines)
            #print(lstProtLinesWithoutLast)
        else:
            tplIndPosWithoutLast = []
            lstProtLinesWithoutLast = []

        # ЦИКЛ ФОРМИРОВАНИЯ КОМБИНАЦИЙ И ИХ ПРОСЧЕТА
        while True:
            #print(positions)
            numbComb += 1
            if numbComb%100000000==0: print('Кол-во просчитанных комбинаций: ', numbComb)
            lastPosit = positions[-1] # последняя в списке позиция
            #if nKA==amountKA:
            #     print()
                #print(positions)
            # ФОрмирование списка независимых позиций и списка с кол-вом защищаемых линий для каждой позиции
            lstIndPos = []
            lstProtLines = lstProtLinesWithoutLast.copy()
            #if nKA == amountKA and positions[1] > 151: print('lstProtLinesWithoutLast', lstProtLinesWithoutLast)
            lastProtLines = dictProtectLines[lastPosit]
            for indPos in tplIndPosWithoutLast:
                if matrixGraph[lastPosit-1][indPos-1] == 0:
                    lstIndPos.append(indPos)
                else:
                    lastProtLines -= dictProtectLines[indPos]
            lstIndPos.append(lastPosit)
            lstProtLines.append(lastProtLines)
            # if nKA == amountKA:
            #     print(lstProtLines)
            #     print(lstIndPos)

            # Рассчет кол-ва защишаемых линий позицией 1
            oneProtLines = dictProtectLines[1]
            for indPos in lstIndPos:
                oneProtLines -= dictProtectLines[indPos]

            # Рассчет мат ожидания
            me = 0
            for nPos in range(nKA):
                me += lstProtLines[nPos] * arrayProtectPower[positions[nPos] - 1]
            me = (me + oneProtLines * arrayProtectPower[0]) / AMOUNT_LINES
            if me < meMin:
                optimalPositions.clear()
                meMin = me
                optimalPositions.append(positions.copy())
            elif me == meMin:
                optimalPositions.append(positions.copy())  # если оптимальных позиций окажется несколько

            # Условие оканчание расчетов для соответсвующего nKA
            if positions[0] == nKA + 1: break

            # ФОрмирование нового списка позиций
            # if lastPosit != 2 :
            #     positions[-1] = lastPosit-1
            #
            # else:
            #     for i in range(-2, -(nKA+1), -1):
            #         if positions[i] != -i + 1:
            #             positions[i] = positions[i] - 1
            #             for ind in range(i+1, 0, 1):
            #                 positions[ind] = positions[ind-1] - 1
            #             break
            #
            #     # формирование новых списков независимых позиций и кол-ва защищаемых линий
            #     tplIndPosWithoutLast = lap.searchIndepPos(positions[:-1], matrixGraph)
            #     lstProtLinesWithoutLast = lap.calculProtLines(positions[:-1], matrixGraph, dictProtectLines)
            #
            indBreak = 0
            for i in range(-1, -(nKA + 1), -1):
                #print('pos1', positions)
                if positions[i] != -i + 1:
                    positions[i] = positions[i] - 1
                    while positions[i] != -i + 1: # неминимальное значение
                        #print('pos2', positions)
                        if lap.notIsNeigh(positions[:len(positions)+i+1], dictNM): break
                        positions[i] = positions[i] - 1

                    for ind in range(i+1, 0, 1):
                        #print('hui')
                        positions[ind] = positions[ind - 1] - 1
                        #print('pos3', positions)
                        while positions[ind] != -ind + 1:
                            #print('pos444', positions[:len(positions)+ind+1])
                            #print(lap.notIsNeigh(positions[:len(positions)+ind+1], dictNM))
                            if lap.notIsNeigh(positions[:len(positions)+ind+1], dictNM): break
                            #print(positions[ind])
                            positions[ind] = positions[ind] - 1
                            #print(positions[ind])
                    indBreak = i
                    break
            if indBreak < -1:
                # формирование новых списков независимых позиций и кол-ва защищаемых линий
                tplIndPosWithoutLast = lap.searchIndepPos(positions[:-1], matrixGraph)
                lstProtLinesWithoutLast = lap.calculProtLines(positions[:-1], matrixGraph, dictProtectLines)


        # Для проверки количесва сгененрированных комбинаций позиций
        # combNK = tableComb[AMOUNT_LINES - 1][nKA]
        # if numbComb != combNK:
        #     print('ОШИБКА: Несоответсвие количесвта кобюинаций:')
        #     print('        кол-во сгенерированных ({}) != кол-ву истинных ({})'.format(numbComb, combNK))
        # -----------------------------------------------------------

        # Приостановка рассчетов при достижения изменения отключаемой мощности не болле, чем на 2%
        if 1 - (meMin / returnCalculData[-1][0]) <= MAX_CHANGE_POWER:
            returnCalculData.append((round(meMin, 1), nKA, optimalPositions.copy()))
            print('ВНИМАНИЕ: Достигли изменения отключаемой мощности не более, чем на {:.1%}'.format(MAX_CHANGE_POWER))
            print('          при количестве установленных КА = {}'.format(nKA))
            break

        txtF.write(str((round(meMin, 1), nKA, optimalPositions.copy())) + '\n')
        txtF.close()
        returnCalculData.append((round(meMin, 1), nKA, optimalPositions.copy()))
    print('\nКонец рассчетов:', time.ctime())

    return returnCalculData[1:]

# for i in calculationFrom1ToNka(5):
#     print(i)