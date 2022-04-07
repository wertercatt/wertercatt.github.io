import requests
import json

fractalAdminHistory = "https://fractal-core-grpc-server-rest-2-tmg6xh47ja-uc.a.run.app/admin/v1/history?limit=1176&projectId=5679095853613056"
fractalAdminHistoryRaw = requests.get(fractalAdminHistory)
fractalHistory = json.loads(fractalAdminHistoryRaw.text)
fractalHistoryOut = []
fractalHistoryOut.extend(fractalHistory["transactions"])
i = 1176
while (len(json.loads(fractalAdminHistoryRaw.text)["transactions"])) == 1176:
    fractalAdminHistory = "https://fractal-core-grpc-server-rest-2-tmg6xh47ja-uc.a.run.app/admin/v1/history?limit=1176&projectId=5679095853613056&cursor=" + str(i)
    fractalAdminHistoryRaw = requests.get(fractalAdminHistory)
    fractalHistory = json.loads(fractalAdminHistoryRaw.text)
    fractalHistoryOut.extend(fractalHistory["transactions"])
    i = i + 1176
print(json.dumps(fractalHistoryOut, sort_keys=True, indent=4))