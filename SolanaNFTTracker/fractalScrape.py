import requests
import sqlite3

fractalManage = "https://fractal-core-grpc-server-rest-2-tmg6xh47ja-uc.a.run.app/admin/v1/project/manage/5679095853613056/collection/manage"

response = requests.get(fractalManage)
print(response.json())