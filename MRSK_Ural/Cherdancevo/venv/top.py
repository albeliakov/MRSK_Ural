import inputModule
import calculationModule
import outputModule

inData = inputModule.receivingData()
outData = calculationModule.calculationFrom1toNka(inData)
outputModule.transmitData(outData)