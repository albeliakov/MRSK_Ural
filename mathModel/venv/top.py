import inputModule
import model
import outputModule

inData = inputModule.receivingData()
outData = model.calculationFrom1toNka(inData[0], inData[1])
outputModule.transmitData(outData)