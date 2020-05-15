import linesAndPower as lap
import graphCherdancevo as gc
# import  getCombinations as comb
# import numpy as np
# import sys
import time

matrixGraph = gc.loadConjMatrix() # матрица сопряженности линий
neighborsMatrix = gc.loadConjMatrix(sheetName='neighbors', cellsInd=('B2', 'EY155'))
#dictProtectLines = lap.protectLines(matrixGraph) # словарь, содержащий для каждой позиции КА количесвто зависимых позиций

#neighMatr = [[0,1,1,0,0,0,0], #1
#             [0,0,0,1,1,0,0], #2
#             [0,0,0,0,0,0,0], #3
#             [0,0,0,0,0,0,0], #4
#             [0,0,0,0,0,1,1], #5
#             [0,0,0,0,0,0,0], #6
#             [0,0,0,0,0,0,0]]
#neighMatr = gc.loadConjMatrix(sheetName='neighbors', cellsInd=('B2', 'EY155'))
#AMOUNT_LINES = 154
#nKA = 3
#print(comb.getCombs(nKA,neighMatr,AMOUNT_LINES)[:20])
# lst = [i*2 for i in range(154)]
# print(len(lst))
# print(sys.getsizeof(lst))

# print(lap.searchIndepPos([154,153,152,151,150,149], matrixGraph))
# print(time.ctime())

dictNM = {}
for rowI in range(1,len(neighborsMatrix)+1):
    dictNM[rowI] = []
    for colJ in range(rowI,len(neighborsMatrix[rowI-1])):
        if neighborsMatrix[rowI-1][colJ]==1: dictNM[rowI].append(colJ+1)
    if len(dictNM[rowI])==0: del dictNM[rowI]
#
# print(dictNM)
AMOUNT_LINES = 154
nKA = 10
positions = [AMOUNT_LINES]
for i in range(nKA-1):
    appPos = positions[i] - 1
    positions.append(appPos)
    while positions[-1] != nKA-i:  # неминимальное значение
        if lap.notIsNeigh(positions, dictNM): break
        positions[-1] -= 1

print(positions)