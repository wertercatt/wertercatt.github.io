import requests
import sqlite3
import json

#Fractal.is internal API
fractalAdminProjectManage = "https://fractal-core-grpc-server-rest-2-tmg6xh47ja-uc.a.run.app/admin/v1/project/manage/5679095853613056/collection/manage"
fractalAdminProjectHandle = "https://fractal-core-grpc-server-rest-2-tmg6xh47ja-uc.a.run.app/admin/v1/project/handle/cinder"
fractalAdminHistory = "https://fractal-core-grpc-server-rest-2-tmg6xh47ja-uc.a.run.app/admin/v1/history?limit=1176&projectId=5679095853613056"
fractalAdminHistory2 = "https://fractal-core-grpc-server-rest-2-tmg6xh47ja-uc.a.run.app/admin/v1/history?limit=1176&projectId=5679095853613056&cursor=1176"

fractalAdminProjectHandleCinderTokenManage = "https://fractal-core-grpc-server-rest-2-tmg6xh47ja-uc.a.run.app/admin/v1/project/handle/cinder/token/manage/FvbByV9xZmiCEityxoypKfq3tgTe5ZmnQLVf5uGB95bT/history?cursor=&limit=10"

#CoinGecko Public API https://www.coingecko.com/en/api/documentation
coinGeckoCoinsSolanaMarketChartRange = "https://api.coingecko.com/api/v3/coins/solana/market_chart/range?vs_currency=usd&from=1647711974&to=1647798374"

#Solscan Public API https://public-api.solscan.io/docs/
solscanAccountTransactions = "https://public-api.solscan.io/account/transactions?account=C1NDRXpVKLPksQsjSv5ocPUTjFupBuW4JzGQGRMhaivP&limit=50"

fractalHistoryRaw = requests.get(fractalAdminHistory)
fractalHistory = json.loads(fractalHistoryRaw.text)
#print(json.dumps(fractalHistory["transactions"], sort_keys=True, indent=4))
fractalHistoryRaw2 = requests.get(fractalAdminHistory2)
fractalHistory2 = json.loads(fractalHistoryRaw2.text)
highestTransactionVal = 0
lowestTransactionVal = 1.5
highestTransactionId = ""
lowestTransactionId = ""
i = 0
i2 = 0
#print(fractalHistory["next"]["token"])
while i < len(fractalHistory["transactions"]):
    print("<p>")
    print("There was a " + fractalHistory["transactions"][i]["type"] + " transaction at " + fractalHistory["transactions"][i]["time"] + " on Fractal.is<br>")
    print("It was for " + fractalHistory["transactions"][i]["token"]["metaplex"]["name"] + " with the rarity rank of " + str(fractalHistory["transactions"][i]["token"]["rarity"]["rank"]) + "/4444 making it " + fractalHistory["transactions"][i]["token"]["rarity"]["type"] + "<br>")
    mostRareAttributeVal = 1
    leastRareAttributeVal = 0
    mostRareAttribute = ""
    leastRareAttribute = ""
    mostRareAttributeName = ""
    leastRareAttributeName = ""
    makePercentage = "{:%}"
    for x in fractalHistory["transactions"][i]["token"]["rarity"]["attributes"]:
        if x["rarity"] < mostRareAttributeVal:
            mostRareAttributeVal = x["rarity"]
            mostRareAttribute = x["name"]
        if x["rarity"] > leastRareAttributeVal:
            leastRareAttributeVal = x["rarity"]
            leastRareAttribute = x["name"]
    for y in fractalHistory["transactions"][i]["token"]["metaplex"]["attributes"]:
        if y["traitType"] == mostRareAttribute:
            mostRareAttributeName = y["value"]
        if y["traitType"] == leastRareAttribute:
            leastRareAttributeName = y["value"]
    if fractalHistory["transactions"][i]["amount"] > highestTransactionVal:
        highestTransactionVal = fractalHistory["transactions"][i]["amount"]
        highestTransactionId = fractalHistory["transactions"][i]["transactionId"]
    if fractalHistory["transactions"][i]["amount"] < lowestTransactionVal:
        lowestTransactionVal = fractalHistory["transactions"][i]["amount"]
        lowestTransactionId = fractalHistory["transactions"][i]["transactionId"]
    print(mostRareAttributeName + " " + mostRareAttribute + " is the rarest feature of it, appearing in " + makePercentage.format(mostRareAttributeVal) + " of all Cinder NFTs<br>")
    print(leastRareAttributeName + " " + leastRareAttribute + " is the most common feature of it, appearing in " + makePercentage.format(leastRareAttributeVal) + " of all Cinder NFTs<br>")
    print("The transaction ID is " + fractalHistory["transactions"][i]["transactionId"] + "<br>")
    print(fractalHistory["transactions"][i]["toAddress"] + " paid " + fractalHistory["transactions"][i]["fromAddress"] + " " + str(fractalHistory["transactions"][i]["amount"]) + " SOL<br>")
    print("</p>")
    i = i + 1
while i2 < len(fractalHistory2["transactions"]):
    print("<p>")
    print("There was a " + fractalHistory2["transactions"][i2]["type"] + " transaction at " + fractalHistory2["transactions"][i2]["time"] + " on Fractal.is<br>")
    print("It was for " + fractalHistory2["transactions"][i2]["token"]["metaplex"]["name"] + " with the rarity rank of " + str(fractalHistory2["transactions"][i2]["token"]["rarity"]["rank"]) + "/4444 making it " + fractalHistory2["transactions"][i2]["token"]["rarity"]["type"] + "<br>")
    mostRareAttributeVal = 1
    leastRareAttributeVal = 0
    mostRareAttribute = ""
    leastRareAttribute = ""
    mostRareAttributeName = ""
    leastRareAttributeName = ""
    makePercentage = "{:%}"
    for x2 in fractalHistory2["transactions"][i2]["token"]["rarity"]["attributes"]:
        if x2["rarity"] < mostRareAttributeVal:
            mostRareAttributeVal = x2["rarity"]
            mostRareAttribute = x2["name"]
        if x2["rarity"] > leastRareAttributeVal:
            leastRareAttributeVal = x2["rarity"]
            leastRareAttribute = x2["name"]
    for y2 in fractalHistory["transactions"][i2]["token"]["metaplex"]["attributes"]:
        if y2["traitType"] == mostRareAttribute:
            mostRareAttributeName = y2["value"]
        if y2["traitType"] == leastRareAttribute:
            leastRareAttributeName = y2["value"]
    print(mostRareAttributeName + " " + mostRareAttribute + " is the rarest feature of it, appearing in " + makePercentage.format(mostRareAttributeVal) + " of all Cinder NFTs<br>")
    print(leastRareAttributeName + " " + leastRareAttribute + " is the most common feature of it, appearing in " + makePercentage.format(leastRareAttributeVal) + " of all Cinder NFTs<br>")
    print("The transaction ID is " + fractalHistory2["transactions"][i2]["transactionId"] + "<br>")
    print(fractalHistory2["transactions"][i2]["toAddress"] + " paid " + fractalHistory2["transactions"][i2]["fromAddress"] + " " + str(fractalHistory2["transactions"][i2]["amount"]) + " SOL<br>")
    print("</p>")
    if fractalHistory2["transactions"][i2]["amount"] > highestTransactionVal:
        highestTransactionVal = fractalHistory2["transactions"][i2]["amount"]
        highestTransactionId = fractalHistory2["transactions"][i2]["transactionId"]
    if fractalHistory2["transactions"][i2]["amount"] < lowestTransactionVal:
        lowestTransactionVal = fractalHistory2["transactions"][i2]["amount"]
        lowestTransactionId = fractalHistory2["transactions"][i2]["transactionId"]
    i2 = i2 + 1
print("<p>")
print("The highest amount paid for a Fae is " + str(highestTransactionVal) + " SOL in Transaction " + highestTransactionId + "<br>")
print("The lowest amount paid for a Fae is " + str(lowestTransactionVal) + " SOL in Transaction " + lowestTransactionId + "<br>")
