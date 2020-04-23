import graphCherdancevo as gc
import linesAndPower as lap
import getCombinations as comb
import math
import time

AMOUNT_LINES = gc.AMOUNT_LINES # количесвто линий, подверженных КЗ
matrixGraph = gc.loadConjMatrix() # матрица сопряженности линий
dictProtectLines = lap.protectLines(matrixGraph) # словарь, содержащий для каждой позиции КА количесвто зависимых позиций
dictDataTP = gc.loadDataTP() # словарь, содержащий данные про ТП
arrayProtectPower = lap.functProtectConsumer(dictDataTP, matrixGraph, AMOUNT_LINES) # зщищаемая млщность каждой КА

 # математическая модель для рассчета при установке N КА
def modelNka(nKA, arrayProtectPower=arrayProtectPower, dictProtectLines=dictProtectLines, matrixGraph=matrixGraph):
    meMin = 1000000000
    optimalPositions = []
    print()
    print('Устанавлимый КА №', nKA)
    print(time.ctime())
     # формирование всевозможных позиций расположения КА (без повторений)
    c = [i for i in range(2,nKA+2)]
    amountComb = comb.C(AMOUNT_LINES-1, nKA)
    oneTenth = amountComb//10
    for numbPosit in range(1, amountComb+1):
        if numbPosit%oneTenth==0: print('Прошла 1/10')

        positions = [1] + c
        #print('positions=', positions)

         # для каждой позиции находятся другие позиции КА, которые будут влиять на количесвто защищаемых ей линий
        dependLines = lap.lineDepend(positions, matrixGraph)

         # для каждой позиции рассчитываются соответсвующее количесвто защищаемых линий
        protectLines = lap.lineProtect(dependLines, dictProtectLines)

        #print(protectLines)
         # для каждой позиции рассчитывается количесвто линий, влияющих на работу КА
        influenceLines = lap.lineInfluence(positions, AMOUNT_LINES)
        #print(influenceLines)

         # для каждой позиции рассчитывается соответсвующая защищаемая мощность
        powers = lap.powerProtect(positions, arrayProtectPower)
        #print(consumers)

         # расчет мат ожидания
        me = lap.mathExpect(protectLines, influenceLines, powers)
        if me < meMin:
            optimalPositions.clear()
            meMin = me
            optimalPositions.append(positions[1:])
        elif me == meMin: optimalPositions.append(positions[1:]) # если оптимальных позиций окажется несколько

         # формирование новой комбинации
        c = comb._newComb(c, nKA, AMOUNT_LINES)
        #print('c=', c)
    return (meMin, nKA, optimalPositions)

 # рассчет для всех 1:N установленных КА
def calculationFrom1toNka(amountKA):
    arrayCalculatData = []
    for i in range(1, amountKA+1): arrayCalculatData.append(modelNka(i))
    return arrayCalculatData
