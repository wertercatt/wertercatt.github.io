import requests
import json

magicEdenCollectionsCinderActivities = "https://api-mainnet.magiceden.dev/v2/collections/cinder/activities?offset=0&limit=500"
magicEdenHistoryRaw = requests.get(magicEdenCollectionsCinderActivities)
magicEdenHistory = json.loads(magicEdenHistoryRaw.text)

i = 500
while (len(json.loads(magicEdenHistoryRaw.text))) == 500:
    magicEdenCollectionsCinderActivities = "https://api-mainnet.magiceden.dev/v2/collections/cinder/activities?limit=500&offset=" + str(i)
    magicEdenHistoryRaw = requests.get(magicEdenCollectionsCinderActivities)
    magicEdenHistory.extend(json.loads(magicEdenHistoryRaw.text))
    i = i + 500
print(json.dumps(magicEdenHistory, sort_keys=True, indent=4))