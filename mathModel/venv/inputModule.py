defaultNumberConsumers = [30, 20, 10, 5, 15, 40, 10, 30, 5, 10] # количесвто потребителей на ТП по умолчанию

 # получение внешених данных
def receivingData(defaultNumberConsumers=defaultNumberConsumers):
    amountKA = int(input('Введите максимальное количесвто КА для расчета (от 1 до 17): '))
    newDataTP = int(input('Для изменения количества потребителей на ТП введите 1 (иначе - любую цифру): '))
    if newDataTP == 1:
        numberConsumersOnTP = []
        for i in range(1, 11):
            tpI = int(input('Кол-во потребителей на ТП №'+str(i)+': '))
            numberConsumersOnTP.append(tpI)
    else: numberConsumersOnTP = defaultNumberConsumers
    return  (amountKA, numberConsumersOnTP)