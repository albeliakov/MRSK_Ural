import xlwt
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


  # Псстрочная запись в эксель-файл
def writeExcel(book, sheetName, cols, colNames, rows):
     # именование столбцов
    rowNames = sheetName.row(0)
    for index, col in enumerate(cols):
        rowNames.write(index, colNames[index])

     # заполнение значений
    for ind in range(len(rows)):
        row = sheetName.row(ind+1)
        for index, col in enumerate(cols):
            value = rows[ind][index]
            row.write(index, value)

    # Save the result
    book.save("Выходные_данные.xls")


 # вывод результатов в виде таблицы
def transmitData(outData):
    # Initialize a workbook
    book = xlwt.Workbook(encoding="utf-8")
    # Add a sheet to the workbook
    sheet1 = book.add_sheet("Выходные данные")

    cols = ['A', 'B', 'C']
    colNames = ['Среднее количество отключаемых потребителей',
                   'Количество устанавливаемых КА',
                   'Места для установки']

    # формирование данных, для записи в эксель-файле
    arrayOutData = []
    for nKA in sortByME(outData):
        arrayOutData.append((round(nKA[0], 2), nKA[1], viewPositions(nKA[2])))

     # запись в excel-файл
    writeExcel(book, sheet1, cols, colNames, arrayOutData)

     # построение графика
    xyOD = xy2XandY(arrayOutData)
    plt.plot(xyOD[1], xyOD[0])
    plt.ylabel('Среднее количество отключаемых потребителей')
    plt.xlabel('Количество устанавливаемых КА')
    plt.grid()
    plt.show()
