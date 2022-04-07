import json
import requests

#load JSON
fractalSales = open("./fractalSales.json")
fractalData = json.load(fractalSales)
i = 0

#transaction value analysis variables
highestTransactionVal = 0
lowestTransactionVal = 1.5
highestTransactionId = ""
lowestTransactionId = ""

#most sold Fae analysis variables
tokenAddressList = []
mostSoldToken = ""
mostSoldVal = 0

#sales per day analysis variables
datesSoldList = []
bestSalesDay = ""
bestSalesVal = 0
worstSalesDay = ""
worstSalesVal = 4444


while i < len(fractalData):
    if fractalData[i]["amount"] > highestTransactionVal:
        highestTransactionVal = fractalData[i]["amount"]
        highestTransactionId = fractalData[i]["transactionId"]
    if fractalData[i]["amount"] < lowestTransactionVal:
        lowestTransactionVal = fractalData[i]["amount"]
        lowestTransactionId = fractalData[i]["transactionId"]
    tokenAddressList.append(fractalData[i]["tokenAddress"])
    datesSoldList.append(fractalData[i]["time"][:10])
    i = i + 1
print("The highest amount paid for a Cinder NFT is " + str(highestTransactionVal) + " SOL in Transaction " + highestTransactionId)
print("The lowest amount paid for a Cinder NFT is " + str(lowestTransactionVal) + " SOL in Transaction " + lowestTransactionId)
for x in tokenAddressList:
    if tokenAddressList.count(x) > mostSoldVal:
        mostSoldVal = tokenAddressList.count(x)
        mostSoldToken = x
for y in datesSoldList:
    if datesSoldList.count(y) > bestSalesVal:
        bestSalesVal = datesSoldList.count(y)
        bestSalesDay = y
    if datesSoldList.count(y) < worstSalesVal:
        worstSalesVal = datesSoldList.count(y)
        worstSalesDay = y
    #print("There were " + str(datesSoldList.count(y)) + " sales on " + y)
    #datesSoldList = [y1 for y1 in datesSoldList if y1 != y]
print(mostSoldToken + " is the Cinder NFT Token address that has been sold the most, having sold " + str(mostSoldVal) + " times")
print(bestSalesDay + " was the best day for Cinder NFT Sales, with " + str(bestSalesVal) + " Cinder NFTs being Sold.")
print(worstSalesDay + " was the worst day for Cinder NFT Sales, with " + str(worstSalesVal) + " Cinder NFTs being Sold.")