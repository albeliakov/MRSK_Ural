from graphCherdancevo import AMOUNT_LINES

 # получение внешених данных
def receivingData():
    print('Возможное количесвто устанавливаемых КА - [1:'+str(AMOUNT_LINES-1)+']')
    amountKA = int(input('Введите максимальное количесвто КА для расчета: '))
    if amountKA not in range(1, AMOUNT_LINES):
        while amountKA not in range(1, AMOUNT_LINES):
            print('Введено некорректное значение количества КА')
            amountKA = int(input('Введите еще раз: '))
    return (amountKA)
