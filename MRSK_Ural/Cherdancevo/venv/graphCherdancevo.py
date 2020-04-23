from openpyxl import load_workbook

AMOUNT_LINES = 154
wbName = 'матрица.xlsx'
sheetConjMatrix = 'conjMatrix'
cellConjMatrix = ('C3', 'EZ156')
sheetDataTP = 'TP'
cellDataTP = ('B3', 'E156')

# Загрузка матрицы сопряженности линий из excel-файла
def loadConjMatrix(wbName=wbName, sheetName=sheetConjMatrix, cellsInd=cellConjMatrix):
    # Load in the workbook
    wb = load_workbook('./'+wbName)
    # Get a sheet by name
    sheet = wb.get_sheet_by_name(sheetName)

    conjMatrix = []
    arrayRowLine = []
    for cellObj in sheet[cellsInd[0]:cellsInd[1]]:
        for cells in cellObj:
            arrayRowLine.append(cells.value)
        conjMatrix.append(arrayRowLine.copy())
        arrayRowLine.clear()
    return conjMatrix

 # Загрузка данных по ТП в словарь из excel-файла в виде:
  # №_линии: (№_ТП, номин_мощн, загрузка)
def loadDataTP(wbName=wbName, sheetName=sheetDataTP, cellsInd=cellDataTP):
    wb = load_workbook('./'+wbName)
    sheet = wb.get_sheet_by_name(sheetName)

    dictPowerLine = {}
    for cellObj in sheet[cellsInd[0]:cellsInd[1]]:
        dictPowerLine[int(cellObj[0].value)] = (str(cellObj[1].value),
                                                int(cellObj[2].value),
                                                float(cellObj[3].value))
    return dictPowerLine



