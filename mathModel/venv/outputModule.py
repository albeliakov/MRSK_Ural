from prettytable import PrettyTable
from tabulate import tabulate
import matplotlib.pyplot as plt

def xy2XandY(inArr):
    xArr = []
    yArr = []
    for arr in inArr:
        xArr.append(arr[0])
        yArr.append(arr[1])
    return (xArr, yArr)

 # сортировка по мат ожиданию (по возрастанию)
def sortByME(outData):
    return sorted(outData, key=lambda data: data[0])


 # извлечение позиций из массивов и представление в строков формате
def viewPositions(arrayPosit):
    strOr = ''
    posit = ''
    for arr1 in arrayPosit:
        posit += strOr
        for el in arr1:
            posit += str(el)+', '
        posit = posit[:len(posit)-2]
        strOr = '\nили\n'
    return posit


 # вывод результатов в виде таблицы
def transmitData(outData):
    columnNames = ['Среднее количество\nотключаемых потребителей',
                   'Количество\nустанавливаемых КА',
                   'Места для установки']

    arrayOutData = []
    for nKA in sortByME(outData):
        arrayOutData.append((round(nKA[0], 2), nKA[1], viewPositions(nKA[2])))

    xyOD = xy2XandY(arrayOutData)
    plt.plot(xyOD[1], xyOD[0])
    plt.ylabel('Среднее количество отключаемых потребителей')
    plt.xlabel('Количество устанавливаемых КА')
    plt.grid()

    plt.show()

    print()
    print(tabulate(arrayOutData, headers=columnNames,tablefmt='grid',colalign=("center", "center", "center")))