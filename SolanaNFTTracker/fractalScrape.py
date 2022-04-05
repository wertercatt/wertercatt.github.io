import requests
import sqlite3
import json

#Fractal.is internal API
fractalAdminProjectManage = "https://fractal-core-grpc-server-rest-2-tmg6xh47ja-uc.a.run.app/admin/v1/project/manage/5679095853613056/collection/manage"
fractalAdminProjectHandle = "https://fractal-core-grpc-server-rest-2-tmg6xh47ja-uc.a.run.app/admin/v1/project/handle/cinder"
fractalAdminHistory = "https://fractal-core-grpc-server-rest-2-tmg6xh47ja-uc.a.run.app/admin/v1/history?cursor=&limit=10&projectId=5679095853613056"
fractalAdminProjectHandleCinderTokenManage = "https://fractal-core-grpc-server-rest-2-tmg6xh47ja-uc.a.run.app/admin/v1/project/handle/cinder/token/manage/FvbByV9xZmiCEityxoypKfq3tgTe5ZmnQLVf5uGB95bT/history?cursor=&limit=10"

#CoinGecko Public API https://www.coingecko.com/en/api/documentation
coinGeckoCoinsSolanaMarketChartRange = "https://api.coingecko.com/api/v3/coins/solana/market_chart/range?vs_currency=usd&from=1647711974&to=1647798374"

#Solscan Public API https://public-api.solscan.io/docs/
solscanAccountTransactions = "https://public-api.solscan.io/account/transactions?account=C1NDRXpVKLPksQsjSv5ocPUTjFupBuW4JzGQGRMhaivP&limit=50"

fractalHistoryRaw = requests.get(fractalAdminHistory)
fractalHistory = json.loads(fractalHistoryRaw.text)
print(json.dumps(fractalHistory["transactions"][0], sort_keys=True, indent=4))
print("There was a " + fractalHistory["transactions"][0]["type"] + " transaction at " + fractalHistory["transactions"][0]["time"] + " on Fractal.is")
print("It was for " + fractalHistory["transactions"][0]["token"]["metaplex"]["name"] + " which has the rarity rank of " + str(fractalHistory["transactions"][0]["token"]["rarity"]["rank"]) + " which makes it a " + fractalHistory["transactions"][0]["token"]["rarity"]["type"] + " NFT")
print("The transaction ID is " + fractalHistory["transactions"][0]["transactionId"])
print(fractalHistory["transactions"][0]["toAddress"] + " paid " + fractalHistory["transactions"][0]["fromAddress"] + " " + str(fractalHistory["transactions"][0]["amount"]) + " SOL")