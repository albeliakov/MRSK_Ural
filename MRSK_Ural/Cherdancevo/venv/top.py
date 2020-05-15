import inputModule
import calculationModule
import outputModule

inData = inputModule.receivingData()
outData = calculationModule.calculationFrom1ToNka(inData)
#print(outData)
outputModule.transmitData(outData)