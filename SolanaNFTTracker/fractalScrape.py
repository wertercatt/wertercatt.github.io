import requests
import sqlite3
import json

#Fractal.is internal API
fractalAdminProjectManage = "https://fractal-core-grpc-server-rest-2-tmg6xh47ja-uc.a.run.app/admin/v1/project/manage/5679095853613056/collection/manage"
fractalAdminProjectHandle = "https://fractal-core-grpc-server-rest-2-tmg6xh47ja-uc.a.run.app/admin/v1/project/handle/cinder"
fractalAdminHistory = "https://fractal-core-grpc-server-rest-2-tmg6xh47ja-uc.a.run.app/admin/v1/history?limit=10&projectId=5679095853613056"
fractalAdminProjectHandleCinderTokenManage = "https://fractal-core-grpc-server-rest-2-tmg6xh47ja-uc.a.run.app/admin/v1/project/handle/cinder/token/manage/FvbByV9xZmiCEityxoypKfq3tgTe5ZmnQLVf5uGB95bT/history?cursor=&limit=10"

#CoinGecko Public API https://www.coingecko.com/en/api/documentation
coinGeckoCoinsSolanaMarketChartRange = "https://api.coingecko.com/api/v3/coins/solana/market_chart/range?vs_currency=usd&from=1647711974&to=1647798374"

#Solscan Public API https://public-api.solscan.io/docs/
solscanAccountTransactions = "https://public-api.solscan.io/account/transactions?account=C1NDRXpVKLPksQsjSv5ocPUTjFupBuW4JzGQGRMhaivP&limit=50"

fractalHistoryRaw = requests.get(fractalAdminHistory)
fractalHistory = json.loads(fractalHistoryRaw.text)
#print(json.dumps(fractalHistory["transactions"], sort_keys=True, indent=4))
i = 0
#print(fractalHistory["next"]["token"])
while i < int(fractalHistory["next"]["token"]):
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
    print(mostRareAttributeName + " " + mostRareAttribute + " is the rarest feature of it, appearing in " + makePercentage.format(mostRareAttributeVal) + " of all Cinder NFTs<br>")
    print(leastRareAttributeName + " " + leastRareAttribute + " is the most common feature of it, appearing in " + makePercentage.format(leastRareAttributeVal) + " of all Cinder NFTs<br>")
    print("The transaction ID is " + fractalHistory["transactions"][i]["transactionId"] + "<br>")
    print(fractalHistory["transactions"][i]["toAddress"] + " paid " + fractalHistory["transactions"][i]["fromAddress"] + " " + str(fractalHistory["transactions"][i]["amount"]) + " SOL<br>")
    print("</p>")
    i = i + 1